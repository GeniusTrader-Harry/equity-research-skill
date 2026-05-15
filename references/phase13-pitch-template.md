# Phase 13 — Write the Pitch (Investment Memo)

**Goal**: Synthesize Phases 1–12 into a 5–8 page investment memo. The memo is the deliverable — used for interview pitches, PM hand-offs, and self-reference. Page 1 is the verbal-pitchable summary; pages 2–8 carry the depth.

**Output**: `~/Claude Projects/Equity Research/[TICKER]/deliverables/[ticker]_pitch.md`

## Why 5–8 pages, not 1, not 50

- **1-page** is too tight to demonstrate analytical depth interviewers probe for (*"what's your evidence on pillar 2?"*). Forces compression that hides the work.
- **30–50 pages** (sell-side initiation format) is for institutional publication, not for a student building understanding or pitching in an interview. ~80% would be boilerplate.
- **5–8 pages** matches buy-side associate / PM internal memo format. Enough room for 3–4 pillars at ~½–1 page each plus risks, valuation, and killing conditions. Tight enough to force discipline.

## Two-layer principle

| Layer | Content | Purpose |
|---|---|---|
| **Memo** (5–8 pages, `deliverables/[ticker]_pitch.md`) | Synthesized argument with evidence + model output + killing conditions | Interview artifact; self-test of integration |
| **Working archive** (`working/`) | Phase 1 raw filings + briefs, Phase 2–3 understanding, Phase 6 asymmetries, Phase 8–10 pillar dev, Phase 11 model | Drill-down reference; not handed to anyone |

The memo references the archive but does not reproduce it.

## Two pitch formats

### Standard Investment Memo (LONG or SHORT direction)
Used when Phase 7 committed to a direction and Phase 12 converged. 5–8 pages. See section "Standard Memo Structure" below.

### Pass Note
Used when Phase 7 committed to PASS, or when Phase 12 failed to converge after 2 iterations. 1–2 pages. See "Pass Note Format" below.

---

## STANDARD MEMO STRUCTURE — 7 sections

### Section 1 — Pitch summary (½–1 page)

The verbal-pitchable top. If someone reads only page 1, they have the call.

```markdown
# [TICKER] — [Rating] — Target $[X], [+/-Y%]
Date: [YYYY-MM-DD] | Current: $[Z] | Author: [name]

**Rating**: [BUY / HOLD / SELL]
**Target price**: $[X] ([+/-Y%] vs. current $[Z])
**Conviction**: [Low / Medium / High]
**Time horizon**: [6mo / 12mo / 18mo]

## Risk/reward (asymmetric payoff around the base case)

| Scenario | Target | vs Spot | Trigger |
|---|---|---|---|
| Bull (pillars-fire) | $[C] | +[D]% | [1-line linking to specific pillars overshooting] |
| **Base (committed view)** | **$[X]** | **+[Y]%** | [the thesis as committed] |
| Bear (pillars-fail) | $[A] | -[B]% | [1-line linking to specific counter-pillars materializing] |

**Skew** = (Bull − Spot) / (Spot − Bear) = **[ratio]:1**

## In one paragraph
[1–2 sentence framing of setup + thesis in plain English. The 60-second verbal pitch.]

## Pillars (one line each)
1. **[Pillar 1 title]** — [one-sentence claim with key number]
2. **[Pillar 2 title]** — [one-sentence claim with key number]
3. **[Pillar 3 title]** — [one-sentence claim with key number]

## Key risks (one line each)
1. **[Risk 1]** — [one-sentence counter-pillar]
2. **[Risk 2]** — [one-sentence counter-pillar]
3. **[Risk 3]** — [one-sentence counter-pillar]

## Catalysts
- [Date] — [event] — [why it matters / which pillar it tests]
- [Date] — [event] — [why it matters]

## What would change my mind (teaser)
See Section 7. [N] killing conditions; the most important: [1 example].
```

### Section 2 — Business in 5 minutes (½–¾ page)

Compressed from Phase 2 `company_brief.md`. Not a re-derivation — a synthesis pointing at what matters for the thesis.

```markdown
# Business

**What & how**: [2–3 sentences on what the company does and how it makes money]

**Revenue mix** (FY[year]):
- [Segment 1]: [%] — [1-line description]
- [Segment 2]: [%] — [1-line description]
- [Segment 3]: [%] — [1-line description]

**Scale**: [revenue, EBITDA margin, FCF, employees, geographic split — 3 lines]

**Management**: [CEO + CFO names, tenure, 1-line track record, insider ownership %]
```

### Section 3 — Industry & competitive position (½–¾ page)

Compressed from Phase 3 `industry_brief.md`. Focused on what matters for the thesis.

```markdown
# Industry

**Market structure**: [TAM with source; growth rate; concentrated vs. fragmented; key secular trend — 2–3 lines]

**Competitive set** (top 3–5):
| Company | Position | Comment |
|---|---|---|
| [Comp 1] | [#X] | [1-line] |
| [Comp 2] | [#X] | [1-line] |
| [Comp 3] | [#X] | [1-line] |

**Where [TICKER] sits**: [2–3 sentences — market share, defensibility, moat type with evidence]
```

### Section 4 — Thesis pillars in depth (1.5–3 pages) — LOAD-BEARING

This is the meat. Each pillar gets a structured write-up of ~300–500 words:

```markdown
## Pillar [N] — [short title]

**Claim**: *"[5-element pillar statement verbatim from Phase 10 audited list]"*

**Mechanism** (~80–120 words). [Causal story. Why does this happen? What's the underlying business / industry / accounting / behavioral driver?]

**Evidence** (~120–180 words):
- [Source 1, with file path or page #]: [verbatim quote or specific data point]
- [Source 2, with citation]: [data point]
- [Source 3, with citation]: [data point]
- [Source 4]: [if applicable — independence matters; aim for 3+ independent sources from Phase 10 Check 3]

**Magnitude** (~60–100 words). [Walk through the math from driver delta to EPS to target price impact. Mirror Phase 10 Check 2 computation. Example: "+400bps GM × $12B revenue = $480M incremental gross profit, ~85% flow-through = $400M EBIT, after 25% tax = $300M NI, ÷1.2B shares = $0.25 EPS, × 25x multiple = $6.25/share = +4.3% to target."]

**Asymmetry mapping**: Phase 6 asymmetry #[N] ([title]). Why Street has it wrong: [1 sentence].

**Model linkage**: Cell `Assumptions!_[ref]` = [value] vs. Street consensus [value].

---
[repeat for each surviving pillar from Phase 10]
```

**Quality check**: if a pillar's write-up can't fill ~300 words honestly, the pillar is too thin to defend in an interview. Sharpen, drop, or kick back to Phase 10.

### Section 5 — Risks (steel-manned) (¾–1 page)

Verbatim from Phase 9 `risks.md` with light formatting. Each counter-pillar + rejection reasoning.

```markdown
# Risks (steel-manned counter-arguments)

These are the strongest arguments for the opposite direction. We've considered them and reject them, but they remain real risks.

## Counter-pillar 1 — [title]
**Bear case**: *"[5-element counter-pillar statement from Phase 9]"*

**Why we still hold the call**: [paragraph from Phase 9 rejection reasoning — specific evidence, not vibes]

**Severity if it plays out**: [estimated target impact, e.g., "would push target to $[X] (-Y%)"]

---
[repeat for each Phase 9 counter-pillar, typically 2–3 total]
```

### Section 6 — Valuation (½–1 page)

Compressed Phase 11 model output. Don't reproduce the model — summarize it.

```markdown
# Valuation

## Central case
**Methodology**: DCF primary, comps cross-check.
**Target**: $[X] (= $[Y] DCF, $[Z] comps-implied; weighted [%/%])
**Upside / downside**: [+/-Y%] vs. current $[current]
**Implied forward [P/E or EV/EBITDA]**: [Xx] (vs. comp set median [Yx])

## Key DCF assumptions
| Driver | FY[Y1] | FY[Y3] | FY[Y5] | Terminal |
|---|---|---|---|---|
| Revenue growth | [%] | [%] | [%] | [%] |
| Gross margin | [%] | [%] | [%] | [%] |
| Operating margin | [%] | [%] | [%] | [%] |
| WACC | — | — | — | [%] |
| Terminal growth | — | — | — | [%] |

## Sensitivity (bull/base/bear envelope around the committed base)
- Bull case (top 2-3 swing assumptions flexed favorable + pillars overshoot): $[C] ([+D%])
- **Base (committed)**: $[X] ([+/-Y%])
- Bear case (top 2-3 swing assumptions flexed unfavorable + counter-pillars partially realize): $[A] ([-B%])
- Risk/reward skew: (Bull − Spot) / (Spot − Bear) = [ratio]:1

Note: bull and bear are not alternative theses — they're the payoff envelope around the single committed direction. Triggers link to specific pillars/counter-pillars from Phases 8–9.

## Tornado — top 5 assumptions by target leverage
1. [Assumption] — ±[%] target impact
2. [Assumption] — ±[%]
3. [Assumption] — ±[%]
4. [Assumption] — ±[%]
5. [Assumption] — ±[%]

## Comps cross-check
| Peer | Fwd P/E | Fwd EV/EBITDA |
|---|---|---|
| [TICKER] | [X] | [X] |
| [Comp 1] | [X] | [X] |
| [Comp 2] | [X] | [X] |
| Median (n=[N]) | [X] | [X] |

[1–2 sentences: where TICKER trades vs. peers and why the gap is justified or temporary]

Full model: `deliverables/[ticker]_model.xlsx`
```

### Section 7 — What would change my mind (¼–½ page)

**Verbatim from Phase 10 `killing_conditions.md`. No paraphrasing.**

```markdown
# What Would Change My Mind

These are the pre-specified conditions that would invalidate the thesis. If any trigger, the pillar dies and the rating must be revisited.

## For Pillar 1 — [title]
- [killing condition 1 verbatim from `working/killing_conditions.md`]
- [killing condition 2 verbatim]
- [killing condition 3 verbatim]

## For Pillar 2 — [title]
- [verbatim]
- [verbatim]

## For Pillar 3 — [title]
- [verbatim]
- [verbatim]

## Catalyst calendar (when to check)
| Date | Event | Conditions to monitor |
|---|---|---|
| [date] | [earnings / IR day / industry data] | [which conditions are testable] |
| [date] | [event] | [conditions] |
```

This section is the **defensibility lock**. At interviews when asked *"what would change your view?"*, you read this section.

---

## PASS NOTE FORMAT

When Phase 7 committed to PASS or Phase 12 didn't converge. Same file path (`deliverables/[ticker]_pitch.md`), shorter (1–2 pages):

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
[1–2 strongest reasons someone might be long or short. Don't dismiss — acknowledge legitimate arguments.]

## Why we don't take them
[Specific reasons: insufficient evidence, asymmetry already priced, multiple-expansion risk, etc. Cite Phase 6 / Phase 9 work.]

## Conditions for revisiting
- [Event 1, e.g., "If mgmt discloses cohort retention at next investor day"]
- [Event 2, e.g., "If price drops to $[X] (-15% from current) without fundamental deterioration"]
- [Event 3]

## Coverage status
Re-evaluate after [event / quarter / event window].

## Reference materials retained
[paths to working/ files in case future revisit needs the prior work]
```

Pass notes are valuable — they document disciplined non-action.

---

## Process

### Step 1 — Assemble from working files

The skill draws content from:
- `working/direction.md` → rating, conviction
- `working/company_brief.md` → Section 2
- `working/industry_brief.md` → Section 3
- `working/pillars_audited.md` → Section 4 (pillar statements + evidence)
- `working/risks.md` → Section 5 (counter-pillars + rejection reasoning)
- `deliverables/[ticker]_model.xlsx` + `working/model_summary.md` → Section 6
- `working/killing_conditions.md` → Section 7 (verbatim)
- `working/phase12_final.md` (or `iterations.md`) → final pillar set + target post-iteration

Use the template at `assets/pitch_template.md` as the scaffold.

### Step 2 — Identify catalysts

From the analysis, extract 3–5 specific events that will move the stock and date them. Sources:
- Earnings dates (next 2–3 quarters)
- Investor days / conferences (from IR calendar)
- Product launches / FDA decisions / regulatory rulings (from press, transcripts)
- Macro / industry events relevant to the thesis

### Step 3 — Compose the headline

Most-tightened version of:
> *"[LONG/SHORT] [TICKER]. Target $[X] ([Y]% [upside/downside]) on [central thesis in ~12–18 words]."*

Example:
> *"LONG NVDA. Target $1,600 (+22%) on sustained hyperscaler capex + sovereign AI uncovered TAM driving FY27 datacenter revenue 25% above Street."*

### Step 4 — Draft full memo

Write to `deliverables/[ticker]_pitch.md`. Target ~2,500–4,000 words, 5–8 pages rendered.

### Step 5 — Length and discipline check

After draft, verify:
- Word count 2,500–4,000?
- Each pillar 300–500 words? If much less, pillar may be thin. If much more, pillar may be padded.
- Killing conditions verbatim from Phase 10?
- Every quantitative claim → source file + page/section?
- Page 1 alone has the full call (rating, target, pillars one-liners, risks one-liners, catalysts)?

### Step 6 — Present to user

```markdown
# [TICKER] Pitch Drafted

- Word count: [X]
- Estimated pages: [Y]
- Pillars: [list with word counts each]
- Killing conditions: [N total]
- Model output: $[target] ([+/-%])

Saved to: `deliverables/[ticker]_pitch.md`

Review for tone, sharpness, accuracy. Common asks: 'tighten pillar [N],' 'expand evidence on [N],' 'rewrite section 1,' 'fix [specific section].' When satisfied, say 'finalize.'
```

### Step 7 — Iterate

User will likely request tone edits, sharpening, expansion. Iterate freely. Section 1 (Pitch Summary) often takes 2–3 passes because it's the verbal-pitch scaffold.

### Step 8 — Finalize

When user says "finalize":

```markdown
✅ [TICKER] research complete.

Rating: [X] | Target: $[Y] ([Z]% upside/downside) | Conviction: [Level]

Pillars: [N] surviving
Killing conditions to monitor: [M]
Next catalyst: [event] on [date]

Deliverables:
  - Pitch memo: deliverables/[ticker]_pitch.md
  - Model: deliverables/[ticker]_model.xlsx

Research archive (working files retained):
  - Phase 1 sources: filings/, transcripts/, ir-materials/, sell-side/
  - Phase 2–10 working files: working/
  - Phase 11 model summary + Phase 12 iteration log

Live monitoring: after each earnings event or material news, check `working/killing_conditions.md`. If a condition triggers, the pillar dies and rating must be revisited.

Workflow ended.
```

## Style notes

- **Plain English over jargon.** Audience is a PM or interviewer — sharp but not pretentious.
- **Quantify everything.** Pillars without numbers are vibes.
- **Cite religiously.** Every quantitative claim → source (file + page).
- **Lead with the answer.** Each section opens with the conclusion, then evidence.
- **Tables for comparisons.** Prose for arguments.
- **Confident, not hedged.** Avoid "world-class," "best-in-class," "compelling growth." Use neutral descriptive language with quantified claims. Confident analysts don't need superlatives.
- **No first-person plural marketing voice.** Use "I" (it's your view) or impersonal ("the data shows").
- **Killing conditions VERBATIM from Phase 10.** Never paraphrase between phases.

## What this is NOT

- NOT a 30-page institutional initiation report (use `equity-research:initiating-coverage` for that)
- NOT a 1-page tear-sheet (use `equity-research:thesis` for that)
- NOT a re-derivation of the working files — it's a synthesis on top of them
- NOT a marketing document — risks and falsifiability are first-class, not buried

## Common failure modes

- **Paraphrasing killing conditions**: kills the discipline. Section 7 must be verbatim from Phase 10.
- **Padding pillars to fill space**: if a pillar can't honestly fill 300 words, it's thin. Better 2 strong pillars than 4 padded.
- **Burying the lede**: page 1 must be pitchable in 60 seconds. If a reader has to dig to page 3 for the rating, structure failed.
- **Missing citations**: every claim with a number needs a source. Otherwise it's an assertion, not analysis.
- **Confusing memo and working archive**: the memo references but doesn't reproduce briefs. Copy-pasting 1,000 words from `company_brief.md` = padding.
- **First-person plural marketing voice**: "we believe," "we see compelling opportunity" — analyst writing, not equity-marketing writing.

## Critical: the memo as accountability mechanism

The killing conditions section makes the pitch defensible 6 months from now. When earnings prints and a condition triggers, the rating must change. You don't get to wiggle. That's the deal you make with yourself at publication — the analytical version of writing trading rules down in advance.
