#!/usr/bin/env python3
"""Citation validator — the skill's no-orphan-numbers rule as a REVIEW LIST.

Usage: python3 validate_citations.py <file.md> [<file2.md> ...]

Flags numeric claims (%, bps, currency, M/bn, multiples) on prose lines with
no citation. Accepted as citations: bracket markers ([source, p.N] / [source] /
[computed ...] / [est, not disclosed]) AND prose attribution ("per Wolfe Exh 35",
"(IFPI 2024)", "source:", "disclosed ..."), including in the 2 preceding lines.

IMPORTANT — exit 1 means "lines to review", not "broken". The regex cannot
distinguish a factual claim about the world (MUST be cited) from the analyst's
own model output or killing-condition threshold (IS the source — no citation
needed). At review: every flagged line must be either (a) cited, or (b)
confirmed as own-model output / forward threshold. Table rows are reported as
warnings only — confirm each table carries a table-level source note.
"""
import re
import sys

# numeric-claim patterns (any one on a line makes it a "claim line")
CLAIM_PATTERNS = [
    re.compile(r"\d+(?:\.\d+)?\s*%"),                       # 17%
    re.compile(r"\d+(?:\.\d+)?\s*bps\b", re.I),             # 130bps
    re.compile(r"\d+(?:\.\d+)?\s*pp\b"),                    # 1.3pp
    re.compile(r"[$€£¥]\s?\d"),                              # $47.11, €17,186
    re.compile(r"\b(?:US|HK|RMB|CNY|EUR|GBP|JPY)\$?\s?\d"),  # RMB62.4, US$8.9
    re.compile(r"\d(?:[\d,\.]*)\s*(?:M|bn|B)\b"),            # 698.4M, 62.4bn
    re.compile(r"\d(?:[\d,\.]*)\s*(?:million|billion)\b", re.I),
    re.compile(r"\b\d+(?:\.\d+)?x\b"),                       # 18x
]

# a citation marker = bracketed token containing at least one letter,
# that is NOT a markdown link label followed by ( — links don't cite.
MARKER = re.compile(r"\[[^\]]*[A-Za-z][^\]]*\](?!\()")

# prose-style attribution (memo style): "per Wolfe Exh 35", "(IFPI 2024)",
# "(Bernstein industry analysis)", "disclosed in the Q4 25 letter", "source:".
# Working files should use brackets; the Phase 13 memo cites in prose — both count.
ATTRIB = [
    re.compile(r"\b[Pp]er\s+[A-Z]"),
    re.compile(r"\b[Aa]ccording to\s+\S"),
    re.compile(r"\bsource[s]?\s*:", re.I),
    re.compile(r"\bdisclosed\b", re.I),
    re.compile(r"\(([^)]*\b(19|20)\d{2}\b[^)]*|[^)]*\b(Exh|p\.\s?\d|10-K|20-F|6-K|MD&A|letter|transcript|deck|init\w*|consensus|CapIQ|guidance|filing\w*|estimate\w*|analysis)\b[^)]*)\)", re.I),
]


def attributed(line: str) -> bool:
    return any(p.search(line) for p in ATTRIB)

# lines to skip entirely
SKIP = [
    re.compile(r"^\s*#"),          # headings
    re.compile(r"^\s*\|[\s\-:|]+\|\s*$"),  # table separator rows
    re.compile(r"^\s*[-*_]{3,}\s*$"),       # hr
    re.compile(r"^\s*(?:date|fetched|updated)\b", re.I),
]

# claim-pattern matches to ignore (false-positive guards)
FALSE_POS = [
    re.compile(r"\bFY\s?\d{2,4}"),     # FY25 — period label, not a claim by itself
    re.compile(r"\bQ[1-4]\b"),
    re.compile(r"\b(19|20)\d{2}\b"),   # years
    re.compile(r"\bp\.\s?\d+"),        # page refs
]


def strip_false_positives(line: str) -> str:
    out = line
    for pat in FALSE_POS:
        out = pat.sub(" ", out)
    return out


def check_file(path: str):
    """Returns (hard_findings, table_warnings).

    Prose lines with uncited numeric claims = hard findings (fail).
    Table data rows with uncited numbers = warnings only — tables typically
    carry one table-level source note rather than per-cell citations; the
    analyst confirms the note exists.
    """
    findings, warnings_ = [], []
    in_fence = False
    in_yaml = False
    try:
        lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
    except OSError as e:
        return [(0, f"cannot read file: {e}")], []
    for i, raw in enumerate(lines, 1):
        if i == 1 and raw.strip() == "---":
            in_yaml = True
            continue
        if in_yaml:
            if raw.strip() == "---":
                in_yaml = False
            continue
        if raw.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if any(p.search(raw) for p in SKIP):
            continue
        stripped = strip_false_positives(raw)
        if not any(p.search(stripped) for p in CLAIM_PATTERNS):
            continue
        if MARKER.search(raw) or attributed(raw):
            continue
        # 2-line lookback: list items under an attribution lead-in
        # ("Per Wolfe Exh 35, of every $1: ...") count as covered.
        ctx = " ".join(lines[max(0, i - 3):i - 1])
        if MARKER.search(ctx) or attributed(ctx):
            continue
        if raw.lstrip().startswith("|"):
            warnings_.append((i, raw.strip()[:140]))
        else:
            findings.append((i, raw.strip()[:140]))
    return findings, warnings_


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    total = 0
    for path in argv[1:]:
        findings, warns = check_file(path)
        if findings:
            print(f"\n== {path}: {len(findings)} uncited numeric claim(s) in prose ==")
            for ln, text in findings:
                print(f"  L{ln}: {text}")
            total += len(findings)
        else:
            print(f"OK  {path}: prose clean")
        if warns:
            print(f"  note: {len(warns)} table row(s) with uncited numbers "
                  f"(e.g. L{warns[0][0]}) — confirm each table carries a source note.")
    if total:
        print(f"\nFAIL: {total} orphan number(s) in prose. Cite ([source], [computed ...]) "
              f"or flag ([est, not disclosed]) before saving.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
