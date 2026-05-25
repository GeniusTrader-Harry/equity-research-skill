# Phase 13 — Write the Pitch (Investment Memo)

**Goal**: Synthesize Phases 1-12 into an interview-grade investment memo. The memo is the deliverable — used for interview pitches, PM hand-offs, and self-reference. The cover page is the verbal-pitchable summary; the body sections carry the depth.

**Output**:
- `~/Claude Projects/Equity Research/[TICKER]/deliverables/[ticker]_pitch.md` — source markdown
- `~/Claude Projects/Equity Research/[TICKER]/deliverables/[ticker]_pitch.docx` — Word output
- `~/Claude Projects/Equity Research/[TICKER]/deliverables/[ticker]_pitch.pdf` — PDF output (sell-side styled)

## Why 10-18 pages, not 5-8, not 50

- **5-8 pages** is too tight to include a defensible DCF appendix. Without one, the memo loses interview defensibility — interviewers probe valuation mechanics, not just the headline PT.
- **30-50 pages** (sell-side initiation format) is for institutional publication. ~80% boilerplate.
- **10-18 pages** matches buy-side associate / PM memo format with appendices. Body sections carry the thesis depth, appendices carry the model mechanics.

## Two-layer principle

| Layer | Content | Purpose |
|---|---|---|
| **Memo** (10-18 pages, body + 2 appendices, `deliverables/[ticker]_pitch.*`) | Synthesized argument with evidence + model output + killing conditions + DCF mechanics | Interview artifact; self-test of integration |
| **Working archive** (`working/`) | Phase 1 raw filings + briefs, Phase 2-3 understanding, Phase 6 asymmetries, Phase 8-10 pillar dev, Phase 11 model | Drill-down reference; not handed to anyone |

The memo references the archive but does not reproduce it.

## Two pitch formats

### Standard Investment Memo (LONG or SHORT direction)
Used when Phase 7 committed to a direction and Phase 12 converged. 10-18 pages. See section "Standard Memo Structure" below.

### Pass Note
Used when Phase 7 committed to PASS, or when Phase 12 failed to converge after 2 iterations. 1-2 pages. See "Pass Note Format" below.

---

## Vocabulary at the memo boundary

The working files use **"Pillar"** (analytical vocabulary). The deliverable memo uses **"Thesis"** (pitch vocabulary). Rename at the memo boundary:

- "Pillar 1 / Pillar 2 / Pillar 3" → "Thesis 1 / Thesis 2 / Thesis 3"
- Killing condition labels: "P1.2" → "T1.2"
- "Counter-pillar" → "Risk" (in memo Section 5)

Working files stay as-is.

---

## STANDARD MEMO STRUCTURE

### Cover page (1 page)

YAML frontmatter renders into a clean sell-side cover via pandoc + the shipped CSS. **Do NOT add a `# TICKER` h1 heading** — it would duplicate the YAML title block. Body content starts at section 1.

```markdown
---
title: "[Company name] ([Exchange]: [TICKER])"
subtitle: "[LONG/SHORT] | Price target $[PT] ([+/-X%]) | YYYY-MM-DD"
author: "[Your name]"
---

| | |
|---|---|
| **Rating** | **[LONG / SHORT]** |
| **Price target (12-month)** | **$[PT]** |
| **Current price** ([YYYY-MM-DD]) | $[spot] |
| **Upside to target** | **+/-[X]%** |
| **Market cap** | ~$[Mkt cap] |
| **Reporting currency** | [USD / EUR / GBP / etc. + FX rate to USD if non-USD] |

## Five-year financial estimates ([currency] M)

| | **FY[N]A** | **FY[N+1]E** | **FY[N+2]E** | **FY[N+3]E** | **FY[N+5]E** |
|---|---|---|---|---|---|
| Revenue | | | | | |
| Y/Y growth | | | | | |
| [Key margin — GM or EBITDA] | | | | | |
| Operating income | | | | | |
| EBIT margin | | | | | |
| FCFF | | | | | |
| [Key driver — subs, units, ASP] | | | | | |

*FY[N]A audited per [filing] filed [date]. Forwards from internal model; full schedule in Appendix A.*
```

**Do NOT include on the cover:**
- "Conviction" line (belongs in PM cover note, not public memo)
- "Time horizon" line (implicit from PT period)
- Three-line thesis bullets (the body delivers thesis depth)
- 52-week range (not material to call)
- Probability-weighted target (single-point base PT + envelope is the convention)

### Section 1 — Business overview (1 page)

Compressed from Phase 2 `company_brief.md`. Not a re-derivation — a synthesis pointing at what matters for the thesis.

```markdown
# 1. Business Overview

## What [Company] does and how it makes money

[2-3 paragraph framing: what the business does, how revenue is generated, and the segment mix.]

[Insert revenue mix table:]

| Segment | FY[N] revenue ([currency] M) | % total | Segment GM / margin | FY[N] growth |
|---|---|---|---|---|

[Optional 1-paragraph deeper economics framing — royalty waterfall, unit economics, etc.]

## Product portfolio

[Insert product table — rows = product lines:]

| Product | What it is | Pricing | Role |
|---|---|---|---|

[1-paragraph notes on GTM model, customer mix, geographic distribution.]

## Operating economics — [profitability inflection / margin trajectory]

[Insert historical table showing the operating trajectory:]

| | FY[N-3] | FY[N-2] | FY[N-1] | FY[N] |
|---|---|---|---|---|
| Operating margin | | | | |
| Operating income | | | | |
| [Key segment margins as applicable] | | | | |

[2-3 paragraphs explaining the operating-economics drivers and what the trajectory means for the thesis.]
```

**Do NOT include in Section 1:**
- Management subsection (demoted; lives in `working/company_brief.md`). Include only if management is itself part of the thesis (activist call, new-CEO turnaround, etc.).

### Section 2 — Industry & competitive position (1-2 pages)

Compressed from Phase 3 `industry_brief.md`.

```markdown
# 2. Industry & Competitive Position

## Market structure
[Bullets: TAM, growth rate, secular drivers, concentration]

## [Unit economics framing if applicable — e.g., royalty waterfall, take rate, etc.]
[Industry-specific economic constraint that frames the thesis]

## Competitive set

| Player | Owner | [Size metric] | Share | Position |
|---|---|---|---|---|

[1-paragraph framing: where TICKER sits and the structural read.]

## Moats

[Insert moat table:]

| Moat type | Rating | Evidence (≤1 sentence each) |
|---|---|---|

## [Optional] Long-duration competitive threat: [named threat]

[Include this sub-section ONLY when one competitor poses an asymmetric multi-year share-shift risk that needs substantive (>150w) treatment. Explain (i) the mechanism by which they could take share, (ii) the asymmetry vs current pricing (e.g., ad-funded vs subscription-funded economics), (iii) the data showing whether/where share is currently shifting, (iv) the metric to monitor going forward. If competition is symmetric or already accounted for in the competitive-set table, skip this sub-section.]
```

### Section 3 — Investment Thesis (3-5 pages) — LOAD-BEARING

The meat of the memo. Each thesis gets a **balanced** structure — neither pure-prose nor pure-bullet, both have failure modes.

**Per-thesis structure:**

```markdown
## Thesis [N] — [headline with key number]

**Claim.** [1-2 sentences with the central testable assertion + headline magnitude.]

**Mechanism.**
[Paragraph 1 — the structural argument in prose. Why does this work at the business-model level? What is the causal story? Not data points — the underlying mechanic.]

[Supporting bullets when appropriate — particularly for distinct sub-mechanisms or supporting points:]
- **[Sub-mechanism / supporting point name].** [Explanation.]
- ...

[Optional Paragraph 2 — tying the mechanism to model output or to the broader thesis architecture.]

**Evidence.**
- [Specific data point with source citation]
- [Source quote, with file path or page #]
- [...]
```

**Word budget per thesis:** ~600-900 words for supporting theses, ~1,000-1,500 words for the **load-bearing thesis** (the one carrying the bull edge).

### Load-bearing thesis — deeper structure

Whichever thesis is the load-bearing one (the offensive pillar from Phase 10 — could be margin expansion, unit growth, capital return, ARPU, anything) warrants **deeper sub-structure** than a single Mechanism paragraph:

- If the load-bearing thesis has a **multi-lever build** (a margin bridge, a revenue-build, a balance-sheet walk), break the Mechanism into labelled sub-sections — one per lever:

```markdown
### Lever (a) — [name]: [magnitude FY+1 / FY+2 / FY+3]

[~150 words explaining: what the lever IS, why it has the directional sign in the forecast period, where the magnitude comes from, what disclosure or analog supports it.]
```

Six levers × ~150 words = ~900w mechanism block, which is appropriate for an offensive pillar carrying the upside edge.

### What NOT to include in each thesis

- **"Magnitude vs Street" sub-blocks.** Edge-vs-sell-side materiality math (e.g., "+170bps above CJ at 34.1%") belongs in `working/pillars_audited.md` as the analytical record showing where the edge is sized. The memo should describe **mechanism + evidence + sizing in absolute terms** (e.g., "+€247M of gross profit per 100bps × $16-20/share"), not analyst-materiality comparisons against named anchors.
- **Editorialising closes.** Lines like "this is the defensive thesis" or "this matches Wolfe-mid" are repetitive. The structure of evidence carries the offensive/defensive distinction without explicit labels.
- **Model-output decompositions in parentheses.** Lines like "(model output: Premium segment GM 37.3% × 90.7% of revenue)" add noise. Keep headline numbers; suppress the decomposition arithmetic unless it's the central point.

### Section 4 — Risks (1 page)

Steel-manned counter-theses from Phase 9. **Section title: just "Risks"** (no "Steel-Manned Counter-Pillars" subtitle).

```markdown
# 4. Risks

[1-paragraph framing: which counter-theses survived steel-manning and which were dropped, with a sentence on why each dropped one was rejected.]

## Risk 1 — [title]

**Bear claim.** [Paragraph stating the strongest version of the counter-argument with specific numbers.]

**Why I still hold the call:**
- [Reason 1 with specific evidence]
- [Reason 2]
- [Reason 3]

**Severity if it plays out.** [Bear PT impact + which killing condition catches it.]

---

[Repeat for Risk 2, 3 as applicable. Typically 2-3 risks survive.]
```

### Section 5 — Valuation (1-2 pages)

Compressed Phase 11 model output. Don't reproduce the model — summarise it. **Body keeps: envelope → tornado → headline equity bridge. Methodology + WACC build move to Appendix A.**

```markdown
# 5. Valuation

## Bull / Base / Bear envelope

| Scenario | PT | vs Spot | Trigger |
|---|---|---|---|
| **Bear** | **$[A]** | **−[B]%** | <ul><li>[Bear mechanic 1]</li><li>[Bear mechanic 2]</li><li>[Bear mechanic 3]</li></ul> |
| **Base** | **$[X]** | **+[Y]%** | <ul><li>[Base mechanic 1 — anchored to specific thesis]</li><li>[Base mechanic 2]</li><li>[Base mechanic 3]</li></ul> |
| **Bull** | **$[C]** | **+[D]%** | <ul><li>[Bull mechanic 1 — Thesis stack at upper end]</li><li>[Bull mechanic 2]</li><li>[Bull mechanic 3]</li><li>[Bull mechanic 4 — multiple expansion / WACC compression if applicable]</li></ul> |

[Note: bull mechanics live INSIDE the Trigger column, not as a standalone block below. A standalone bull-case-mechanics block reads as an orphan.]

## Tornado — top 5 assumptions by target leverage

| Rank | Assumption | ± PT impact | Linked thesis |
|---|---|---|---|

[1-2 sentence read on diversification: are top assumptions clustered or diffuse? Is the thesis one-pillar fragile or multi-pillar?]

## Headline equity bridge

[2-3 line summary: EV + net cash = equity / shares = per-share USD. Pointer to Appendix A for full mechanics.]

Full DCF mechanics, WACC build, and sensitivity in Appendix A.
```

**Do NOT include in Section 5:**
- Standalone "Methodology" subsection in body (1-2 sentences inline is enough; full methodology in App A)
- WACC build in body (moves to App A)
- Risk/reward skew prose explanation (let the envelope table speak)
- Comps cross-check (demoted to optional; belongs in working files unless comparables analysis is part of the thesis)
- Sell-side reconciliation (demoted to optional; same logic)

### Section 6 — Catalysts and Killing Conditions (1 page)

**Killing conditions VERBATIM from Phase 10** (with Pillar → Thesis rename only).

```markdown
# 6. Catalysts and Killing Conditions

[1-paragraph framing: KCs are the defensibility lock; each is pre-specified, observable, thesis-linked.]

## Catalyst calendar

| Date | Event | KC tested |
|---|---|---|

## Killing conditions (verbatim, thesis-linked)

### Thesis 1 — [title]
1. [verbatim from working/killing_conditions.md, with Pillar → Thesis rename]
2. [verbatim]
3. [verbatim]

[Repeat for Thesis 2, Thesis 3.]

### Counter-thesis triggers (bear monitoring)
- **C1.1** ([title]): [verbatim]
- **C2.1** ([title]): [verbatim]
```

### Appendix A — Discounted Cash Flow (1-2 pages)

Full DCF mechanics — what got compressed out of Section 5. Includes WACC build (moved from body).

```markdown
# Appendix A — Discounted Cash Flow

## Methodology

[1 paragraph: FCFF or DCF-of-equity? Terminal method (exit multiple / Gordon / both)? Mid-year vs end-of-year discounting? SBC add-back yes/no? Working currency and FX convention. These four choices should mirror what was committed in Phase 11.]

## Explicit FCFF schedule

| FY | EBIT | Tax rate | NOPAT | + D&A | + ΔWC | − Capex | **FCFF** |
|---|---|---|---|---|---|---|---|

[Brief notes on tax curve, working capital assumptions.]

## Discount factors and present value

| FY | t (years) | Disc factor | FCFF | **PV** |
|---|---|---|---|---|

## Terminal value

[Method + math.]

| Scenario | Multiple | FY[N+5] [terminal driver] | Terminal value | PV |
|---|---|---|---|---|

## WACC build

| Component | Value | Source |
|---|---|---|
| Risk-free rate | | |
| Equity risk premium | | |
| Beta | | |
| **Cost of equity (CAPM)** | | |
| Pre-tax cost of debt | | |
| After-tax cost of debt | | |
| Equity / debt weights | | |
| **WACC** | | |

[1-paragraph WACC sensitivity note — alternative beta or peer-median check.]

## Equity bridge

| Component | Value |
|---|---|
| PV of explicit FCFF | |
| PV of terminal value | |
| **Enterprise Value** | |
| + Net cash | |
| **Equity Value** | |
| ÷ Diluted shares | |
| Per share (local currency) | |
| × FX | |
| **Per share (USD)** | |
| Spot price | |
| **Implied return** | |

## Sensitivity (WACC × Exit multiple)

[Table showing PT range across the meaningful sensitivity envelope.]
```

### Appendix B — Key Model Assumptions (½-1 page)

Drill-down on the most important forward assumptions. Content varies by thesis type — pick the schedules that are load-bearing:

- **For margin theses**: GM bridge table by lever, Ad-Supp / segment GM trajectory, OpEx schedule by line item
- **For volume theses**: Subscriber / unit roll, conversion / penetration assumptions, retention / churn schedule
- **For capital-return theses**: Buyback schedule, dividend schedule, share-count walk, leverage trajectory
- **For all theses**: Tax curve, share count walk

```markdown
# Appendix B — Key Model Assumptions

## [Schedule 1 — the most load-bearing forward assumption]
[Table.]

## [Schedule 2]
[Table.]

## OpEx schedule (% of revenue)
| FY | [Lines as applicable] | **Total OpEx** |
|---|---|---|

## Tax curve (forward effective rate)
| FY | Effective tax rate | Rationale |
|---|---|---|

## Share count schedule
| FY | Diluted shares | Detail |
|---|---|---|

*Working archive in `working/`. Live model: `deliverables/[ticker]_model.xlsx`.*
```

### Appendix C — Update history (mandatory scaffold)

Every memo carries `## Appendix C — Update history` as the final appendix. At initiation, the table has only the first row (the initiation). All subsequent updates — produced by the `equity-research-update` companion skill — append rows chronologically.

```markdown
# Appendix C — Update history

| Date | Event | Decision | Key change |
|---|---|---|---|
| [YYYY-MM-DD initiation date] | Initiation | [DIRECTION], PT $[XXX] | — |
```

**Class values for the "Decision" column** (all subsequent rows):
- `No change` — Class 1 log-only update (no body edits)
- `Refined` — Class 2 in-place refinement (thesis text or model lightly touched; PT may have moved <5%)
- `Heavy refinement` — Class 3 (pillar restated or KC fired but direction retained)
- `LONG → [direction]` / `Closed` — Class 4 direction reversal

**Key change column rules:**
- ≤30 words
- MUST mention any pillar invalidated, any KC fired, any PT change with old → new
- For the initiation row: `—`

The memo's git log carries the full diff; this appendix is the human-readable audit trail visible inside the PDF itself.

---

## PASS NOTE FORMAT

When Phase 7 committed to PASS or Phase 12 didn't converge. Same file path (`deliverables/[ticker]_pitch.md`), shorter (1-2 pages):

```markdown
# [TICKER] — PASS
Date: [YYYY-MM-DD] | Current price: $[Z]

**Rating**: PASS
**Reason**: [paragraph synthesis of why no defensible thesis emerged]

## What was tested
- Direction(s) considered: [LONG / SHORT / both]
- Pillars considered: [list with reason each was dropped]
- Strongest counter: [what made the steel-man too credible to overcome]

## Where the case is interesting
[1-2 strongest reasons someone might be long or short. Don't dismiss — acknowledge legitimate arguments.]

## Why we don't take them
[Specific reasons: insufficient evidence, asymmetry already priced, multiple-expansion risk. Cite Phase 6 / Phase 9.]

## Conditions for revisiting
- [Event 1, e.g., "If mgmt discloses cohort retention at next investor day"]
- [Event 2, e.g., "If price drops to $[X] (-15% from current) without fundamental deterioration"]
- [Event 3]

## Reference materials retained
[paths to working/ files]
```

---

## Build pipeline — DOCX + PDF

### One-time tooling setup (macOS)

```bash
brew install pandoc pango
pip install weasyprint
# macOS pango binding requires DYLD_LIBRARY_PATH at runtime (handled in build_memo.sh)
```

### Per-project setup at Phase 13 start

```bash
cd "~/Claude Projects/Equity Research/[TICKER]"
cp ~/.claude/skills/equity-research-customised-process/assets/build_memo.sh working/
cp ~/.claude/skills/equity-research-customised-process/assets/memo_style.css working/
# Edit working/memo_style.css @bottom-left footer with actual ticker/rating/PT/author/date
```

### YAML frontmatter conventions

Pandoc renders the YAML title/subtitle/author block as `<header class="title">` in HTML5 — the shipped CSS styles this as a sell-side cover. **Do not also include a `# TICKER` h1 heading in the body** — that produces a duplicate cover title.

```yaml
---
title: "[Company name] ([Exchange]: [TICKER])"
subtitle: "[LONG/SHORT] | Price target $[PT] ([+/-X%]) | YYYY-MM-DD"
author: "[Your name]"
---
```

### TOC convention

- **Memos ≤10 pages**: no TOC. Pandoc inserts TOC between title block and body, which collides with the cover layout (rec box + financials end up after the TOC instead of right under the title).
- **Memos >10 pages**: include `--toc --toc-depth=1` if desired. Each h1 then appears in TOC; h2/h3 are excluded.

The shipped `build_memo.sh` defaults to **no TOC**. Add `--toc --toc-depth=1` to both pandoc invocations if you want one.

### Build command

```bash
cd "~/Claude Projects/Equity Research/[TICKER]"
bash working/build_memo.sh [TICKER]
```

Outputs:
- `deliverables/[ticker]_pitch.docx`
- `deliverables/[ticker]_pitch.pdf`

### Page break behaviour

The shipped CSS sets `h1 { page-break-before: always }` — each `# Section` heading triggers a new page. Cover (no h1) → page 1. Section 1 → page 2. And so on. Sub-headings (h2, h3) do NOT break pages.

---

## Process

### Step 1 — Pre-Phase-13 internal-consistency audit (DO THIS FIRST)

Before drafting, run the consistency audit per [SKILL.md "Pre-Phase-13 audit checklist"](../SKILL.md):

1. Every pillar magnitude reconciles to the model output within tolerance (or the difference is documented)
2. Every killing condition links to a pillar claim and to a model assumption
3. All valuation numbers (PT, bull/base/bear, skew, WACC) trace back to `working/valuation_outputs.yaml` — no manual transcription drift
4. Every external anchor cited in pillars is traceable to the source file with the data point quoted

If any check fails, fix the working files BEFORE drafting the memo. The memo is a synthesis layer — if the inputs disagree, no amount of memo iteration will fix it.

### Step 2 — Assemble from working files

The skill draws content from:
- `working/direction.md` → rating
- `working/company_brief.md` → Section 1 (Business)
- `working/industry_brief.md` → Section 2 (Industry)
- `working/pillars_audited.md` → Section 3 (Thesis 1-3)
- `working/risks.md` → Section 4 (Risks)
- `working/valuation_outputs.yaml` + `working/model_summary.md` → Section 5 + Appendix A
- `working/model_assumptions.md` → Appendix B
- `working/killing_conditions.md` → Section 6 (VERBATIM, with Pillar → Thesis rename)

Use the template at `assets/pitch_template.md` as the scaffold.

### Step 3 — Identify catalysts

From Phases 5-12, extract 3-5 specific events that will move the stock and date them.

### Step 4 — Draft full memo

Write to `deliverables/[ticker]_pitch.md`. Target **5,000-8,000 words, 10-18 pages rendered**.

### Step 5 — Build DOCX + PDF

```bash
bash working/build_memo.sh [TICKER]
```

Verify both outputs open cleanly and the page count is in the 10-18 range.

### Step 6 — Length and discipline check

After draft, verify:
- Word count 5,000-8,000?
- Page count 10-18?
- Each thesis 600-900w (load-bearing thesis 1,000-1,500w)?
- Killing conditions verbatim from Phase 10 (with Pillar → Thesis rename)?
- Every quantitative claim → source file + page/section?
- Cover page alone contains: rating, PT, current, upside, 5-yr financials?
- No "Conviction" / "Time Horizon" / 52-week / probability-weighted lines on cover?
- No "Pillar" anywhere in body (all renamed to "Thesis")?
- No "Magnitude vs Street" comparisons inside theses (sized in absolute terms instead)?
- No editorialising thesis closes ("this is defensive...")?
- "Mechanism" used as the section label inside each thesis (not "Why the call is correct")?
- Valuation Section: no body methodology paragraph, no body WACC build, bull mechanics inside envelope-table Trigger column?
- Appendix A present with full DCF + WACC build + sensitivity?
- Appendix B present with thesis-relevant model assumptions?

### Step 7 — Present to user

```markdown
# [TICKER] Pitch Drafted

- Word count: [X]
- Page count (PDF): [Y]
- Theses: [list with word counts each, load-bearing thesis flagged]
- Killing conditions: [N total]
- Model output: $[target] ([+/-%])

Saved to:
- `deliverables/[ticker]_pitch.md`
- `deliverables/[ticker]_pitch.docx`
- `deliverables/[ticker]_pitch.pdf`

Review for tone, sharpness, accuracy. Common asks: 'tighten thesis [N],' 'expand evidence on [N],' 'rewrite section 1,' 'fix [specific section].' When satisfied, say 'finalize.'
```

### Step 8 — Iterate

Expect 2-4 iteration rounds. Common edit patterns:

- **Structural reshuffles** — section ordering, what goes in body vs appendix
- **Depth changes** — "expand thesis 2," "compress section 6," "tighten the risks section"
- **Content cuts** — entire sections may be dropped per user preference ("remove the comps cross-check")
- **Terminology preferences** — user may rename things ("call them Mechanism not Driver")
- **Format preferences** — bullets vs prose balance, table layouts

These are iteration discovery, not failures. Capture stylistic preferences in `~/.claude/projects/-Users-[user]/memory/` (auto-memory) if they look settled across multiple memos — the next first-draft should match the established convention rather than re-iterating from defaults.

After each iteration, rerun `bash working/build_memo.sh [TICKER]` to regenerate outputs.

### Step 9 — Finalize

When user says "finalize":

```markdown
✅ [TICKER] research complete.

Rating: [X] | Target: $[Y] ([Z]% upside/downside)

Theses: [N] surviving
Killing conditions to monitor: [M]
Next catalyst: [event] on [date]

Deliverables:
  - Pitch memo (md + docx + pdf): deliverables/[ticker]_pitch.{md,docx,pdf}
  - Model: deliverables/[ticker]_model.xlsx

Research archive (working files retained):
  - Phase 1 sources: filings/, transcripts/, ir-materials/, sell-side/
  - Phase 2-10 working files: working/
  - Phase 11 model + valuation_outputs.yaml
  - Phase 12 iteration log

Live monitoring: after each earnings event or material news, check `working/killing_conditions.md`. If a condition triggers, the thesis dies and rating must be revisited.

Workflow ended.
```

## Style notes

- **Plain English over jargon.** Audience is a PM or interviewer — sharp but not pretentious.
- **Quantify everything.** Theses without numbers are vibes.
- **Cite religiously.** Every quantitative claim → source (file + page).
- **Lead with the answer.** Each section opens with the conclusion, then evidence.
- **Tables for comparisons.** Prose for arguments. **Balanced bullets + prose** inside each thesis.
- **Confident, not hedged.** Avoid "world-class," "best-in-class," "compelling growth." Use neutral descriptive language with quantified claims.
- **No first-person plural marketing voice.** Use "I" (it's your view) or impersonal ("the data shows").
- **Killing conditions VERBATIM from Phase 10** (with Pillar → Thesis rename only).

## What this is NOT

- NOT a 30-page institutional initiation report (use `equity-research:initiating-coverage` for that)
- NOT a 1-page tear-sheet (use `equity-research:thesis` for that)
- NOT a re-derivation of the working files — it's a synthesis on top of them
- NOT a marketing document — risks and falsifiability are first-class, not buried

## Common failure modes

- **Paraphrasing killing conditions**: kills the discipline. Section 6 must be verbatim from Phase 10.
- **Pure-bullet thesis sections**: sparse, reads as a list of claims. Use balanced prose + bullets.
- **Pure-prose thesis sections**: hard to scan, claims merge. Same fix.
- **"Magnitude vs Street" math inside thesis body**: belongs in working files. Memo describes mechanism + evidence + absolute-terms sizing.
- **Editorialising thesis closes**: "this is the defensive thesis" / "this matches Wolfe-mid." Drop — structure carries the role.
- **Bull case mechanics outside envelope table**: orphan block. Fold into Trigger column.
- **Methodology paragraph in Section 5 body**: redundant. 1-2 sentences inline + full method in Appendix A.
- **WACC build in body**: moves to Appendix A.
- **Missing DCF appendix**: undermines interview defensibility.
- **No cover page**: just opening at `# 1` is sell-side malpractice. Use YAML title block + rec table + 5-yr financials.
- **`# TICKER` h1 duplicating YAML title**: drop the h1; let YAML render the cover.
- **TOC sandwich**: pandoc default puts TOC between title and body. For memos ≤10 pages, omit TOC.
- **First-person plural marketing voice**: "we believe," "we see compelling opportunity" — analyst writing, not equity-marketing writing.

## Critical: the memo as accountability mechanism

The killing conditions section makes the pitch defensible 6 months from now. When earnings prints and a condition triggers, the rating must change. You don't get to wiggle. That's the deal you make with yourself at publication — the analytical version of writing trading rules down in advance.
