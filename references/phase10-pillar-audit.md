# Phase 10 — Pillar Audit

**Goal**: Run each finalized pillar through 3 quality checks. Skill drafts candidate killing conditions; user verifies. Skill computes materiality mechanically. Skill counts evidence sources. Output is the surviving pillar set + the killing conditions list (used in Phase 13 pitch and post-publication monitoring).

**Output**: `working/pillars_audited.md` and `working/killing_conditions.md`

## The 3 checks

| Check | Type | Mechanic |
|---|---|---|
| **Falsifiable** | Hard gate | Skill drafts 2–3 candidate killing conditions per pillar; user reviews/edits/accepts. Pillars with no defensible killing conditions get killed. |
| **Material** | Hard gate | Skill runs the pillar's claim through the model architecture and computes target price impact. Pillars with <10% impact get flagged. |
| **Defensible** | Soft gate | Skill counts independent supporting data points. <3 = flag. Override-able for nascent / uncovered theses. |

**Differentiation check is dropped** — judgment-laden, not mechanical. The user knows when a pillar is consensus-aligned because they wrote it.

## Check 1 — Falsifiable (skill drafts, user verifies)

### What killing conditions are

A killing condition is a specific event or number that would prove the pillar wrong. It's **forward-looking** and **observable** — a tripwire that, if triggered by future data, kills the pillar.

Killing conditions serve two roles:
1. **Discipline at thesis formation**: forcing yourself to specify what would falsify the pillar means you've thought about it clearly. Vague pillars can't have killing conditions.
2. **Live monitoring after publication**: when next earnings prints, you check the list. If a condition triggered, the pillar is dead — you must update the thesis or change the rating.

### How skill drafts them

For each pillar, skill drafts 2–3 candidate killing conditions based on:
- The **mechanism** (Phase 8 element 3) — what would break the causal chain?
- The **driver** (Phase 8 element 2) — what reading on this driver would invalidate?
- The **timeframe** (Phase 8 element 5) — what would have to be observed by what date?

### Example

**Pillar**: *"Gross margin will expand to 48% by FY27 (+400bps vs Street) because mix shift to software-only deployments — currently 38% of new ACV — will reach 50%+ by FY27."*

**Skill-drafted killing conditions:**

1. *"Software-only mix drops below 30% of new ACV in either of the next 2 quarterly disclosures."*
2. *"Reported gross margin declines QoQ for 2 consecutive quarters without a one-time charge explanation."*
3. *"Management removes software-only SKU from product roadmap or de-emphasizes it in IR communications."*

Each is:
- **Specific** (a number or event)
- **Observable** (in earnings releases, transcripts, or product collateral)
- **Forward-looking** (will be tested by future data)
- **Tied to mechanism** (mix shift, GM trend, product strategy)

### User verification

Skill presents the candidate killing conditions and asks user to:
- **Accept** as-is
- **Edit** for accuracy or specificity
- **Reject and request alternatives** if poorly drafted
- **Drop the pillar** if no good killing conditions can be written (means pillar is too vague)

If the user **can't accept** any killing conditions for a pillar, kill the pillar. A pillar without falsifiable conditions is unfalsifiable — i.e., not a defensible analytical claim.

## Check 2 — Material (two sub-checks: edge + thesis)

Materiality has two distinct questions. A pillar can be material under one and not the other. Both should be computed.

### 2A — Edge materiality

**Question**: does the pillar's *edge over Street* move PT by enough to matter?

**Mechanic**:
1. Take the pillar's magnitude **vs Street** (the differential, not the absolute level)
2. Flow through model: GP delta → OI delta (apply flow-through %) → NI (after tax) → EPS (÷ shares) → price/share (× multiple) → convert FX if needed
3. **Divide by spot price** to get % impact

**Threshold**: ≥10% of spot price.

**What this tests**: differentiated insight. If all pillars fail this, the thesis is **directionally Street-aligned** with no contrarian edge. That's a valid posture for quality compounders but should be acknowledged — it changes how the trade is pitched (alignment + setup, not edge + asymmetry).

### 2B — Thesis materiality

**Question**: is the pillar *load-bearing* — would removing it (assuming a bear case for this driver) collapse the trade?

**Mechanic**:
1. Take the pillar's magnitude **vs a defensible bear-case alternative** for this driver (not vs Street — vs the no-growth or flatline case)
2. Flow through the model the same way
3. **Divide by spot price** (or by the analyst's own PT — pick one and be consistent)

**Threshold**: ≥10% of spot price.

**What this tests**: structural necessity. If a pillar fails 2B, it's a "free" upside — not load-bearing — and shouldn't be a pillar at all (it's a catalyst or sub-driver).

### When each matters

| Edge (2A) | Thesis (2B) | Pillar type |
|---|---|---|
| High | High | High-conviction differentiated — rare; treat as the headline pillar |
| Low | High | **Defensive load-bearing** — Street-aligned but structurally necessary. Common for quality compounders. Keep but flag as defensive |
| High | Low | Differentiated but doesn't move PT enough — probably a catalyst, not a pillar |
| Low | Low | Drop — neither edge nor load-bearing |

### Example (single pillar, both sub-checks)

**Pillar claim**: GM expands +400bps to 48% in FY27 vs Street 44%.

**2A — Edge materiality (vs Street 44%)**:
- 400bps × $12B FY27 revenue = $480M GP delta vs Street
- ~$400M OI → ~$300M NI → $0.25 EPS → × 25x = $6.25/share
- ÷ $145 spot = **+4.3% → ⚠ Sub-threshold edge**

**2B — Thesis materiality (vs bear-case: GM stays at current 42% with no expansion)**:
- 600bps × $12B = $720M GP delta vs bear
- ~$600M OI → ~$450M NI → $0.38 EPS → × 25x = $9.4/share
- ÷ $145 = **+6.5% → ⚠ Borderline thesis**

**Verdict**: pillar is **neither edge nor strongly load-bearing**. Sharpen or drop.

### Output

Materiality scorecard with both columns:

| Pillar | Edge vs Street (2A) | Thesis vs bear (2B) | Type |
|---|---|---|---|
| 1. GM expansion | +4.3% ⚠ | +6.5% ⚠ | Marginal — sharpen or drop |
| 2. Software ARR | +18.9% ✓ | +24.2% ✓ | High-conviction differentiated |
| 3. Op leverage | +3.1% ⚠ | +12.4% ✓ | Defensive load-bearing |

### Action rules

- **Both fail**: drop the pillar
- **Only 2A passes**: pillar is a catalyst, not load-bearing — reframe or drop
- **Only 2B passes**: defensive load-bearing — keep, flag as defensive in Phase 13 pitch (this is normal for quality compounders aligned with Street direction)
- **Both pass**: differentiated pillar — headline material in pitch

### Why both checks matter

Phase 9 + Phase 10 catch different failure modes:
- **2A failing across all pillars** → thesis is Street-aligned. Not a flaw; just means the pitch should emphasize setup (drawdown / catalysts) over edge.
- **2B failing on any pillar** → that pillar isn't structurally needed. It can be deleted without changing the rating.

Both findings are useful. Don't average them into a single materiality score — keep them separate so the user sees the actual structure of the thesis.

## Check 3 — Defensible (skill counts evidence)

### What defensibility means

How many independent supporting data points back this pillar? Pillars resting on a single mgmt comment can die in one earnings call. Pillars with multiple independent signals (mgmt commentary + product data + competitor signal + channel checks) are robust.

### Mechanic

For each pillar, skill scans the evidence already gathered and counts independent sources:

| Source type | Examples |
|---|---|
| Mgmt commentary | Earnings call quotes, investor day statements, IR calls |
| Reported data | 10-K / 10-Q metrics, segment-level disclosures |
| Third-party data | Industry reports (Gartner, IDC), web traffic, hiring data |
| Competitor signals | Competitor commentary on related dynamics |
| Channel checks | Customer / partner / distributor primary research |
| Sell-side validation | Multiple analysts converging on similar views |

**Threshold**: 3+ independent sources = robust. 1–2 = fragile. 0 = drop.

**Independence matters**: 3 quotes from the same earnings call = 1 source (the call). Mgmt + 1 sell-side note repeating mgmt = 1 source (the company's framing). Real independence = different observation channels.

### Output

| Pillar | Sources | Verdict |
|---|---|---|
| 1. GM expansion | (1) Q3 transcript p.7, (2) IDay 2024 slide 23, (3) Q2 transcript p.9, (4) FY24 10-K Item 7 | ✓ Robust (4 sources) |
| 2. Software ARR | (1) Q3 transcript only | ⚠ Fragile (1 source) |
| 3. Op leverage | (1) Mgmt LT model, (2) sell-side consensus | ⚠ Fragile-medium (2 sources) |

Soft gate: user can override "fragile" for genuinely **uncovered alpha** — pillars where the whole point is that data is scarce. But the override should be conscious.

## Mechanical integrity gates (run AFTER the 3 quality checks, BEFORE writing outputs)

These are yes/no machine-checkable gates that catch silent-error classes. None of them are judgement-laden — they either pass or fail, and a failure must be fixed (not waived) before Phase 10 outputs are written.

### Gate A — External anchor existence check

**Question**: every external anchor cited as evidence in any pillar must be traceable to the actual source file with the data point quoted.

**Mechanic**:
1. List every external anchor cited in pillar evidence (sell-side estimate, consensus median, regulatory threshold, industry-report figure, peer benchmark).
2. For each anchor, confirm:
   - The source file exists at the claimed path (`sell-side/[firm].pdf`, `working/consensus_map.md`, etc.)
   - The cited data point actually appears in the source — with the exact metric, year, and value
   - The forecast horizon claimed is within the source's actual coverage (e.g., does the sell-side note actually cover FY+3? Does CapIQ Median actually have estimates for FY+3 / FY+5?)
3. Flag any anchor that fails. **Fix the citation or drop the claim — do not waive.**

**Why this exists**: anchors get fabricated mid-workflow when working from memory. Example failure mode: citing "[Vendor] Median FY+3 GM at 35.0%" when [Vendor]'s coverage actually ends at FY+2. The error is invisible to the user unless they re-pull the source.

### Gate B — Decomposition bridge math check

**Question**: any bridge or decomposition cited as evidence (margin bridge, revenue-growth decomposition, balance-sheet walk, EPS bridge) must mechanically sum to the disclosed headline.

**Mechanic**:
1. For each cited bridge, list every component contribution with its sign (positive / negative) and magnitude.
2. Sum the components.
3. Compare the sum to the disclosed headline; difference must be ≤ ±5 units (bps, %, $M — whichever the bridge uses) OR explicitly noted as "residual / rounding."
4. Flag any bridge where the sum does not reconcile. **Re-verify signs of each component before using the bridge as evidence.**

**Why this exists**: sign convention on bridge components (which way each contribution moves the headline) is easy to get wrong when reading a third-party note quickly. Example failure mode: listing a "Music royalty −200bps" headwind and an "Audiobook −70bps" drag both as positive contributions, producing a bridge that sums to a number meaningfully different from the disclosed headline. The error is invisible until checked mechanically.

### Gate C — Joint killing-condition dependency check

**Question**: for each killing condition, does triggering it invalidate more than one pillar?

**Mechanic**:
1. For each KC, trace which pillar it falsifies directly.
2. Then check: would the triggering condition also break the assumption-base of any *other* pillar? (E.g., a KC tied to "no Q3 27 price hike" — does the missing hike also reduce the margin pillar's forward magnitude through its pricing-flow-through lever?)
3. If yes, document the joint dependency in the KC text itself: *"JOINT Pillar [X] + Pillar [Y] trigger — also breaks ... base PT haircut to ~$..."*

**Why this exists**: joint triggers carry more weight at monitoring time — when one fires, multiple pillars die simultaneously, not just the one named. Surfacing the dependency at Phase 10 prevents the user from learning about it during post-publication monitoring.

### Gate D — KC base-case calibration check

**Question**: under the base-case model projection, would any KC mechanically fire?

**Mechanic**:
1. For each KC threshold (e.g., "ratio <X%," "metric below Y," "Y/Y delta exceeds Z bps"), look up the base-case projected value for the relevant metric and period.
2. If the base-case projected value already crosses the KC threshold, the KC is mis-calibrated — it would fire under the thesis's own base case, falsely signaling pillar death.
3. Recalibrate the threshold OR change the metric: typical fix is to base the KC on Y/Y delta or vs-projection delta rather than absolute level, with the threshold set materially beyond the modeled drift.

**Why this exists**: a KC like *"Sub/MAU stock ratio < 38.5%"* mechanically fires under a base case where the ratio drifts to ~38.2% from mix effects even with the thesis intact. The KC must be calibrated above the modeled drift — e.g., *"Y/Y decline > 150bps"* — to actually represent a thesis-breaking signal.

### Gate output

Run all four gates as a checklist before writing `pillars_audited.md` and `killing_conditions.md`:

| Gate | Status | Notes |
|---|---|---|
| A — Anchor existence | ✓ / ✗ | [If ✗: which anchor failed and how it was fixed] |
| B — Bridge math | ✓ / ✗ | [If ✗: which bridge failed and resolution] |
| C — Joint KC dependencies | ✓ / ✗ | [If ✗: which KCs were updated to flag joint triggers] |
| D — KC base-case calibration | ✓ / ✗ | [If ✗: which KCs were recalibrated and how] |

All four must be ✓ before Phase 10 finalises.

## Final output of Phase 10

After running all 3 checks and applying user judgment:

### `working/pillars_audited.md`

```markdown
# [TICKER] Audited Pillars
Direction: [LONG / SHORT]

## Pillar 1 — [title] [STATUS: surviving / dropped / sharpened]
[Full 5-element pillar statement]

### Audit results
| Check | Result |
|---|---|
| Falsifiable | ✓ (3 killing conditions) |
| Material | ✓ (+18.9% target impact) |
| Defensible | ✓ (4 independent sources) |

### Killing conditions
1. [verbatim from approved list]
2. [verbatim]
3. [verbatim]

### Evidence sources
- [list with paths/pages]

---
[repeat for each pillar]
```

### `working/killing_conditions.md` — structured format

Every KC carries a **stable ID** (KC1, KC2, KC3, …), an explicit verbatim **trigger**, the **pillar it kills** (with joint dependencies if any), the **monitoring cadence**, and the **source to check** during monitoring. The ID stays stable across this file, Phase 13's "What would change my mind" section, and the `equity-research-update` companion skill's three-test.

The structured format is mandatory — it's what the companion update skill reads to run Test B (KC test) mechanically. Free-prose KCs from older runs need to be re-formatted before any update event.

```markdown
# [TICKER] Killing Conditions (What Would Change My Mind)

Pillar references (from `pillars_audited.md`):
- **P1**: [pillar 1 short title]
- **P2**: [pillar 2 short title]
- **P3**: [pillar 3 short title]

---

## KC1 — [short label] (Pillar P[N])

- **Trigger**: [verbatim condition with a specific number or event — must be checkable from a public source]
- **What it kills**: P[N] [pillar title]; JOINT P[M] if applicable (and how)
- **Cadence**: every earnings · monthly · when [specific event happens] · continuous
- **Source for monitoring**: [where the data point lands — e.g. earnings release headline metric / transcript Q&A search / specific 10-K item / regulatory docket]
- **Why this falsifies the pillar**: [≤30 words tying the trigger back to the pillar's mechanism]

## KC2 — [short label] (Pillar P[N])

- **Trigger**: …
- **What it kills**: …
- **Cadence**: …
- **Source for monitoring**: …
- **Why this falsifies the pillar**: …

## KC3 — [short label] (Pillar P[N])

…
```

**ID stability rules:**
- KC IDs (KC1, KC2, …) are assigned at Phase 10 finalisation and never renumbered. If a KC is dropped during a later HEAVY refinement, its ID is retired (don't reuse it); subsequent KCs continue from the highest used ID + 1.
- Pillar IDs (P1, P2, P3) match `pillars_audited.md` exactly. If a pillar is dropped, its ID retires too.

**Format-validation checklist** (before declaring Phase 10 finalised):
- Every KC has all five bullet fields (Trigger / What it kills / Cadence / Source / Why)
- Trigger is testable from a public source (no "if mgmt seems concerned")
- Pillar reference in heading matches an actual pillar from `pillars_audited.md`
- Cadence is specific (not just "ongoing")

## Q&A interlude (HEAVY)

Prompt:

> "Phase 10 audit complete. [N] pillars surviving (originally [M]). Killing conditions drafted — review for each surviving pillar. Common asks: 'kill #X' (drop a sub-threshold pillar), 'sharpen killing condition #Y' (more specific), 'add a killing condition' (skill missed one), 'override fragile flag on #Z' (for uncovered theses), 'recompute materiality on #W' (sanity-check the math). When satisfied, say 'finalize.'"

Common iterations:
- *"This killing condition isn't specific enough"* — sharpen with a number or date
- *"Recompute materiality assuming X"* — re-run with different assumptions, show the math
- *"What's the worst-case if all 3 killing conditions trigger simultaneously?"* — answer honestly; this is the thesis collapse scenario

When user says "finalize":
- Save outputs
- Confirm: *"Phase 10 finalized. [N] pillars surviving with [M] killing conditions. Proceeding to Phase 11 (model + sensitivity)."*

## What this is NOT

- NOT the model itself (Phase 11)
- NOT the sensitivity analysis (Phase 11)
- NOT the pitch (Phase 13)

It's the **quality gate**. Pillars that survive Phase 10 are the ones that actually go into the model and the pitch.

## Critical: killing conditions are sacred

The killing conditions written here go **verbatim** into:
- The Phase 13 pitch's "What would change my mind" section
- The post-publication monitoring checklist (every earnings, every news event)

Don't paraphrase between phases. Sharpen them now so future-you (and the PM, and the interviewer) can hold present-you accountable.
