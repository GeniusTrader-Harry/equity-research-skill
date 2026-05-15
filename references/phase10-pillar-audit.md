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

## Check 2 — Material (skill computes mechanically)

### What materiality means

Does the pillar's claim, if true, move the target price by enough to matter? **Threshold: ≥10% target price impact.** Pillars below this threshold are not worth being thesis pillars — they may be true but they don't drive the rating.

### Mechanic

Skill runs the pillar's quantitative claim through a simplified model approximation:

1. **Identify the driver** the pillar moves (from Phase 4 tree)
2. **Compute the dollar impact** of the pillar's magnitude on the relevant P&L line
3. **Translate to EPS** (or FCF, depending on what drives the model)
4. **Apply the relevant multiple** (forward P/E from comps, or DCF terminal multiple)
5. **Compare to current price** to get % target move

### Example

**Pillar claim**: GM expands +400bps to 48% in FY27 vs Street 44%.
**Computation**:
- 400bps × FY27 revenue $12B = $480M incremental gross profit
- Assume passes through to operating profit (modulo OpEx ratio holding): ~$400M operating profit
- After 25% tax: ~$300M net income
- ÷ 1.2B shares = $0.25 EPS uplift
- × 25x P/E (current multiple) = $6.25 / share
- Current price $145 → +4.3%

**Verdict**: 4.3% < 10% threshold. **Marginal/sub-threshold pillar.**

### Output

Skill produces a materiality scorecard:

| Pillar | Driver | Magnitude vs Street | EPS impact | Target impact | Verdict |
|---|---|---|---|---|---|
| 1. GM expansion | GM% | +400bps | +$0.25 | +4.3% | ⚠ Sub-threshold |
| 2. Software ARR | Revenue | +$1.5B | +$1.10 | +18.9% | ✓ Material |
| 3. Op leverage | OpEx% | -200bps | +$0.50 | +8.6% | ⚠ Marginal |

User decides what to do with sub-threshold or marginal pillars:
- **Drop**: most common response
- **Sharpen**: if there's a more aggressive defensible version of the magnitude
- **Stack**: combine 2 marginal pillars into one if they hit related drivers
- **Keep with caveat**: rare; only if the pillar is unusually strong on other tests

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

### `working/killing_conditions.md`

A flat list of all killing conditions across all surviving pillars. This is what appears in the Phase 13 pitch under "What would change my mind" — used verbatim, no paraphrasing.

```markdown
# [TICKER] Killing Conditions (What Would Change My Mind)

## For Pillar 1 — [title]
- [condition 1]
- [condition 2]
- [condition 3]

## For Pillar 2 — [title]
- ...
```

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
