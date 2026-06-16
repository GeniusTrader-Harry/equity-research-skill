#!/usr/bin/env python3
"""CapIQ .xls export parser — turn the standard sell-side/ data exports into
one readable summary so each run doesn't hand-roll xlrd parsing.

Usage: python3 parse_capiq_exports.py <sell-side-dir> [-o <output.md>]
       (default output: ../working/capiq_summary.md relative to sell-side dir)

Handles the three standard CapIQ export types (auto-detected by sheet names):
  1. Estimates report  — sheets: Consensus, Revisions, Surprise, Guidance, ...
  2. Comp set          — sheets: Trading Multiples, Operating Statistics, ...
  3. Company financials — sheets: Key Stats, Multiples (own history), ...

Graceful degradation: any file/sheet whose layout isn't recognized is reported
as a sheet inventory + "parse manually" flag — never a crash, never silent
wrong numbers. The analyst extracts unrecognized figures ad-hoc as before.
Requires: xlrd (legacy .xls OLE format).
"""
import os
import re
import sys
import warnings

warnings.filterwarnings("ignore")

try:
    import xlrd
except ImportError:
    print("xlrd not installed — pip install xlrd. Falling back: parse manually.")
    sys.exit(1)


def cell(sh, r, c):
    try:
        v = sh.cell_value(r, c)
    except IndexError:
        return ""
    return v


def fmt(v):
    if isinstance(v, float):
        if v == int(v) and abs(v) < 1e15:
            return f"{int(v):,}"
        return f"{v:,.2f}"
    return str(v).strip()


def xldate(v, book):
    try:
        import datetime
        return xlrd.xldate.xldate_as_datetime(v, book.datemode).strftime("%Y-%m")
    except Exception:
        return fmt(v)


# ---------------------------------------------------------------- estimates
def parse_estimates(book, out):
    sh = book.sheet_by_name("Consensus")
    # --- target price / ratings blocks: rows where col0 == 'Target Price'
    out.append("### Target price & ratings")
    header_listing = None
    for r in range(sh.nrows):
        c0 = str(cell(sh, r, 0)).strip()
        if re.match(r".*(NasdaqGS|SEHK|NYSE|LSE|DB):", c0) and "Mean" in str(cell(sh, r, 1)):
            header_listing = c0.split("(")[0].strip()
        if c0 == "Target Price" and header_listing:
            mean, med, hl, n = cell(sh, r, 1), cell(sh, r, 2), cell(sh, r, 3), cell(sh, r, 5)
            out.append(f"- **{header_listing}** — PT mean {fmt(mean)} / median {fmt(med)} / high-low {fmt(hl)} / analysts {fmt(n)}")
        if str(cell(sh, r, 7)).strip().startswith("1 - Buy"):
            counts = []
            for rr in range(r, min(r + 6, sh.nrows)):
                lbl = str(cell(sh, rr, 7)).strip()
                if lbl and cell(sh, rr, 8) != "":
                    counts.append(f"{lbl}: {fmt(cell(sh, rr, 8))}")
            if counts and header_listing:
                out.append(f"  - ratings — " + " · ".join(counts))
    # --- company-level annual consensus block
    out.append("\n### Company-level annual consensus (median)")
    metrics = ["Revenue", "EBITDA", "EBIT", "Net Income (GAAP)", "Free Cash Flow",
               "Gross Margin %", "Capital Expenditure", "Cash From Operations"]
    blk = None
    for r in range(sh.nrows):
        if str(cell(sh, r, 0)).strip().startswith("Company Level"):
            blk = r
            break
    if blk is None:
        out.append("- [layout not recognized — parse Consensus sheet manually]")
        return
    years = {}
    for c in range(1, sh.ncols):
        v = cell(sh, blk, c)
        if isinstance(v, float) and 2000 < v < 2040:
            years[c] = int(v)
    rows = {}
    r = blk + 1
    while r < sh.nrows:
        label = str(cell(sh, r, 0)).strip()
        if label.startswith("Company Level") or (label and "(" in label and ":" in label):
            break
        if label in metrics:
            med_r = None
            for rr in range(r + 1, min(r + 8, sh.nrows)):
                if str(cell(sh, rr, 0)).strip() == "Median":
                    med_r = rr
                    break
            if med_r:
                rows[label] = {yr: cell(sh, med_r, c) for c, yr in years.items()}
        r += 1
    if not rows:
        out.append("- [no metric rows recognized — parse manually]")
        return
    import datetime
    cur = datetime.date.today().year
    keep = sorted({yr for vals in rows.values() for yr, v in vals.items()
                   if v not in ("", "-")})
    keep = [y for y in keep if cur - 2 <= y <= cur + 4]
    out.append("| Metric | " + " | ".join(str(y) for y in keep) + " |")
    out.append("|---|" + "---|" * len(keep))
    for m in metrics:
        if m in rows:
            cells = [fmt(rows[m].get(y, "")) if rows[m].get(y, "") not in ("", "-") else "—" for y in keep]
            out.append(f"| {m} | " + " | ".join(cells) + " |")
    out.append("\n(units/currency per export header; verify against the file before citing)")


# ---------------------------------------------------------------- comp set
def parse_compset(book, out):
    for sheet, title in [("Trading Multiples", "Peer trading multiples"),
                         ("Operating Statistics", "Peer operating statistics")]:
        try:
            sh = book.sheet_by_name(sheet)
        except Exception:
            continue
        out.append(f"### {title}")
        hdr_r = None
        for r in range(sh.nrows):
            if str(cell(sh, r, 0)).strip() == "Company Name":
                hdr_r = r
                break
        if hdr_r is None:
            out.append("- [layout not recognized — parse manually]")
            continue
        hdrs = [str(cell(sh, hdr_r, c)).strip()[:24] for c in range(sh.ncols)]
        out.append("| " + " | ".join(h or " " for h in hdrs) + " |")
        out.append("|---" * len(hdrs) + "|")
        r = hdr_r + 1
        while r < sh.nrows:
            c0 = str(cell(sh, r, 0)).strip()
            if not c0 or c0.startswith(("Summary", "Displaying")):
                if c0.startswith("Summary"):
                    out.append("")
                r += 1
                if c0.startswith("Displaying"):
                    break
                continue
            vals = [fmt(cell(sh, r, c)) for c in range(sh.ncols)]
            out.append("| " + " | ".join(v or "—" for v in vals) + " |")
            r += 1
        out.append("")


# ------------------------------------------------------------- own history
def parse_financials(book, out):
    try:
        sh = book.sheet_by_name("Multiples")
    except Exception:
        return
    out.append("### Own multiple history (quarterly)")
    date_r = None
    for r in range(min(20, sh.nrows)):
        vals = [cell(sh, r, c) for c in range(2, min(8, sh.ncols))]
        if sum(1 for v in vals if isinstance(v, float) and 40000 < v < 50000) >= 3:
            date_r = r
            break
    if date_r is None:
        out.append("- [layout not recognized — parse Multiples sheet manually]")
        return
    dates = {c: xldate(cell(sh, date_r, c), book) for c in range(2, sh.ncols)
             if isinstance(cell(sh, date_r, c), float)}
    cols = sorted(dates)[-12:]
    wanted = ["TEV/NTM Total Revenues", "TEV/NTM EBITDA", "P/NTM EPS"]
    out.append("| Metric (avg per quarter) | " + " | ".join(dates[c] for c in cols) + " |")
    out.append("|---|" + "---|" * len(cols))
    for r in range(sh.nrows):
        label = str(cell(sh, r, 0)).strip()
        if label in wanted and str(cell(sh, r, 1)).strip() == "Average":
            vals = []
            for c in cols:
                v = cell(sh, r, c)
                vals.append(f"{v:.1f}" if isinstance(v, float) else "—")
            out.append(f"| {label} | " + " | ".join(vals) + " |")


# ------------------------------------------------------------------- main
def classify(book):
    names = set(book.sheet_names())
    if "Consensus" in names:
        return "estimates"
    if "Trading Multiples" in names and "Business Description" in names:
        return "compset"
    if "Key Stats" in names or ("Multiples" in names and "Income Statement" in names):
        return "financials"
    return "unknown"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    d = os.path.expanduser(argv[1])
    outpath = None
    if "-o" in argv:
        outpath = argv[argv.index("-o") + 1]
    if not outpath:
        outpath = os.path.join(os.path.dirname(os.path.abspath(d)), "working", "capiq_summary.md")
    files = [f for f in sorted(os.listdir(d)) if f.lower().endswith((".xls", ".xlsx"))]
    if not files:
        print(f"No .xls/.xlsx files in {d}")
        return 1
    import datetime
    out = [f"# CapIQ export summary", f"Source dir: `{d}` — generated by parse_capiq_exports.py",
           "All figures [CapIQ export] — verify against the file before citing in outputs.", ""]
    for fn in files:
        path = os.path.join(d, fn)
        out.append(f"\n## {fn}")
        try:
            book = xlrd.open_workbook(path)
        except Exception as e:
            out.append(f"- could not open ({type(e).__name__}) — **parse manually**")
            continue
        kind = classify(book)
        inv = ", ".join(f"{s.name}({s.nrows}x{s.ncols})" for s in book.sheets())
        out.append(f"Sheets: {inv}")
        try:
            if kind == "estimates":
                parse_estimates(book, out)
            elif kind == "compset":
                parse_compset(book, out)
            elif kind == "financials":
                parse_financials(book, out)
            else:
                out.append("- unknown export type — **parse manually** (sheet inventory above)")
        except Exception as e:
            out.append(f"- extractor failed ({type(e).__name__}: {e}) — **parse manually**")
    os.makedirs(os.path.dirname(outpath), exist_ok=True)
    with open(outpath, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"Wrote {outpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
