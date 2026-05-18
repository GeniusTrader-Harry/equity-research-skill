# Example Deliverable — Reference Memo

This directory contains a fully-worked example deliverable from a real end-to-end run of the equity-research-customised-process skill.

## Files

- **`SPOT_pitch.md`** — Source markdown (matches the pitch_template.md scaffold; 6,802 words, 19 pages rendered)
- **`SPOT_pitch.pdf`** — Sell-side styled PDF output (built via `bash build_memo.sh SPOT` against the `memo_style.css` shipped in this skill)

## Why this example exists

Templates alone under-specify the integration. The shipped `pitch_template.md` shows the scaffold; this example shows how a real deliverable populates that scaffold across a coherent thesis.

The example demonstrates:

- **Cover page conventions**: YAML title block + rec table + 5-year financial estimates (no duplicate `# h1`)
- **Section 1 (Business)**: product → revenue structure → product portfolio table → operating economics — in that order, with no Management subsection
- **Section 2 (Industry)**: market structure + waterfall framing + competitive set + 7-row moat table + named long-duration competitive threat
- **Section 3 (Investment Thesis)**: balanced prose + bullets per thesis; load-bearing thesis (Thesis 2 here) carries a six-lever sub-section build (~150w per lever)
- **Section 4 (Risks)**: just "Risks" as section title (no "Steel-manned Counter-Pillars"); 2-3 risks with bear claim / why I still hold / severity
- **Section 5 (Valuation)**: envelope table with bull mechanics folded INSIDE the Trigger column; no body methodology paragraph; no body WACC build; tornado; headline equity bridge
- **Section 6 (Catalysts + KCs)**: catalyst calendar + KCs verbatim from working files (with Pillar → Thesis rename)
- **Appendix A (DCF)**: methodology + explicit FCFF schedule + discount factors + terminal value + WACC build + equity bridge + sensitivity
- **Appendix B (Assumptions)**: load-bearing schedules (GM bridge, segment trajectory, OpEx, tax, share count)

## Important caveat — example, not template

This is a **specific thesis on a specific company at a specific point in time** (LONG SPOT, $510 PT, May 2026). Future runs will have:

- Different direction (could be SHORT)
- Different load-bearing pillar (could be capital return, sub growth, regulatory, anything)
- Different structural framing (no royalty waterfall if not in music industry)
- Different appendix B content (no GM bridge if margins aren't the thesis)
- Different page count, word count, lever count

**Do not copy the content** — only the structure, conventions, and section discipline. The `pitch_template.md` scaffold is the structural reference; this example is the integration reference.

## How to use this example

When drafting a new memo:

1. Start from `pitch_template.md` (the scaffold)
2. Refer to this example to see how a real memo populates that scaffold
3. Adapt structure to your thesis content — don't force SPOT-shaped framing onto a different stock

The cover page, section ordering, balanced-prose-plus-bullets pattern inside theses, valuation envelope structure, and appendix layout are content-agnostic. The lever names, sector framings, named threats, and Appendix B schedules are entirely content-specific.
