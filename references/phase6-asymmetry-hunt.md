# Phase 6 — Asymmetry Hunt

**Goal**: Surface 5–8 candidate places where the Street might be wrong, with verbatim evidence. These are the **raw material** for thesis pillars in Phase 8.

**Output**: `working/asymmetries.md`

## Why this matters

A pillar with no asymmetry is just consensus repackaged — no edge. Every defensible thesis pillar starts with an asymmetry: a place where you can identify a probable gap between Street's view and reality. This phase systematically hunts for those gaps.

## The 4 asymmetry types

### Type 1 — Disclosure-thin / variance-wide

**What it is**: A driver that meaningfully moves the price target, but the company doesn't disclose enough about it for the Street to converge on an estimate. Different analysts plug different numbers because they're guessing.

**How to spot**: Look at the consensus map (Phase 5). Drivers flagged as "Wide" dispersion are the candidates. Then check: is the dispersion driven by (a) genuine uncertainty / weak disclosure, or (b) analysts haven't bothered? The former is opportunity; the latter is just noise.

**Evidence to gather**:
- The dispersion range itself (e.g., FY26 NRR estimates range 105% to 122%, 17pp spread)
- Mgmt's framing of the driver (any quotes that hint at direction)
- Third-party data that could resolve the uncertainty (web traffic, product usage data, hiring data)
- Why the company isn't disclosing (regulatory? competitive? not yet established?)

**Example (Snowflake-style)**:
> *Driver: Net Revenue Retention. Y1 estimates range 117% (bull) to 105% (bear), spread 12pp. Co only discloses one annual NRR; cohort decay is unmodeled. CFO commentary in Q2 FY25 call ("optimization is intensifying") didn't quantify. Asymmetry: NRR is the swing variable for FY26 ARR; whoever is right wins.*

### Type 2 — Recent inflection not yet in Street numbers

**What it is**: Something just changed — a guidance shift, a product launch, a management comment, a contract win, a regulatory ruling — but Street models are stale because revisions take 2–8 weeks.

**How to spot**: Read the **most recent transcript** (and the press releases of the last 30 days) carefully. Look for things mgmt is hammering that prior transcripts didn't mention. Compare to the dates of the sell-side notes in `sell-side/` — are any pre-inflection?

**Evidence to gather**:
- The verbatim mgmt quote or press release
- Date of the inflection
- Date of the most recent sell-side note (was it before the inflection?)
- The driver impact: if this signal is real, what driver moves and by how much?

**Example (META FY24 capex cut)**:
> *Q1 FY24 transcript: CFO reduced capex guidance from $35B–$40B to $33B–$37B citing "more efficient AI compute." 6 of 11 sell-side notes pulled were pre-cut. Asymmetry: capex assumption is mostly stale in models; FCF Y2 likely under-estimated by ~$2-3B.*

### Type 3 — Framework miss (Street's mental model is wrong)

**What it is**: The Street's mental model of how the business works is becoming wrong, but everyone's still using the old framework. The most powerful (and rarest) asymmetry type.

**How to spot**: Compare how the **Street** describes the business to how mgmt is describing it on recent calls. The Street's framing comes from sell-side notes when `research_notes_available: true`; otherwise from the **earnings-call analyst Q&A + financial press** (`working/street_view.md`; full Mode-A fallback ladder in Phase 1 Step 9) — the questions analysts ask reveal the mental model they're using, which is exactly what you're testing for staleness. Is there a divergence? Is mgmt re-defining its own narrative? Common cases:
- Street values on ARR multiples; company has shifted to consumption pricing → multiple is wrong
- Street uses backward-looking comp set; the company has moved into a new TAM
- Street treats company as cyclical; secular shift is making it non-cyclical (or vice versa)
- Street prices on EBITDA; capex profile has changed making FCF the right metric

**Evidence to gather**:
- The modal Street framing (paraphrase — from sell-side notes if available, else from the analyst Q&A on recent calls / press)
- Mgmt's current framing (verbatim quotes)
- The framework gap and why it matters
- What multiple or model would the new framework imply?

**Example (early Snowflake 2021)**:
> *Sell-side framed SNOW as SaaS at 20–25x ARR (subscription multiples). But pricing is consumption — usage can drop 20%+ in customer optimization without churn. Framework: subscription multiples overstate value of consumption revenue. If consumption businesses trade at 15–18x ARR (closer to transactional comps), multiple compression of 25–35% is implied even if estimates are right. Asymmetry: framework, not estimates.*

### Type 4 — Behavioral mistake

Three sub-types — each is a known, documented analyst bias.

#### 4a. Extrapolation
Street takes the last 4 quarters and projects them forward indefinitely. After 4 strong quarters, models pencil in 5+ years of strength. After 4 weak quarters, models pencil in indefinite weakness. Cycles mean-revert; models don't.

**How to spot**: Look at the most recent 4 quarters. Are they meaningfully above or below long-term trend? Is the Street straight-lining recent performance, or modeling reversion?

**Example**: After 4 quarters of 35% revenue growth, Street models 25% next year, 22% the year after. But the comparable historical pattern for this kind of inflection-to-mean shows reversion to ~15% within 6 quarters of peak.

#### 4b. Anchoring
Street anchors on the prior cycle's peak or trough. If a semis company's peak revenue was $50B in 2021, the Street treats $50B as a ceiling — even when TAM has grown 50% since.

**How to spot**: Compare current Street estimates to the prior cycle peak (or trough). Is there an arbitrary cap or floor that's not justified by current fundamentals?

**Example**: NVDA datacenter peak revenue 2018 was ~$3B; analysts in early 2023 capped FY26 estimates at $30B (10x prior peak) even though TAM had grown 30x. The cap was anchoring, not analysis.

#### 4c. Narrative dominance
A name becomes "the AI play" or "the EV play" and gets priced on narrative rather than fundamentals. When narrative shifts (often abruptly), fundamentals didn't actually change much but multiples reset hard.

**How to spot**: Is the multiple anomalously high or low vs. peers / history given the fundamentals? What narrative is the multiple pricing? Is that narrative durable or showing cracks?

**Example**: 2024 EV multiple compression — Tesla / Rivian / Lucid all multiple-compressed by 50%+ on narrative shift even as unit volumes were close to flat. Fundamentals barely changed; multiples did.

## Process

### Step 1 — For each of the 4 types, scan systematically

Don't free-associate. Go through each type, look for candidates:
- Type 1: scan Phase 5 dispersion flags
- Type 2: scan most recent transcripts (last 90 days) for new mgmt commentary
- Type 3: compare the modal Street framing (sell-side notes if available, else analyst Q&A + press) to mgmt framing
- Type 4: compare Street estimates to fundamentals + historical patterns

### Step 2 — For each candidate, write an entry

```markdown
## ASYMMETRY [N]: [short title]

**Type**: [1 / 2 / 3 / 4a / 4b / 4c]
**Driver impacted**: [from driver tree]
**Lean direction**: bullish / bearish / either (depending on which way the asymmetry resolves)

### Evidence
[Verbatim quotes / data / source paths. Be specific.]

### Why this matters
[1–2 sentences on the financial impact if the asymmetry is real.]

### What would prove it real / wrong
[The data point or event that would resolve uncertainty.]

### Pillar candidate (Phase 8 input)
[Phrase the asymmetry as a candidate pillar in the 5-element format.]
```

### Step 3 — Aim for 5–8 candidates

Quality over quantity. 5 strong candidates with verbatim evidence beats 12 vague ones. If you can only find 3, that's fine — say so. If you find 12, prioritize the ones with the largest driver impact.

### Step 3b — Two structural checks before finalizing (MANDATORY)

Run both checks and write the result into the closing section of `working/asymmetries.md`:

1. **Setup-bias check** (when the Phase 1 setup flag shows a significant drawdown or run-up): report the bull-vs-bear candidate count and justify the imbalance with evidence in one paragraph. A big drawdown invites rebound narratives; a big run-up invites momentum narratives — the skew must be driven by the evidence, not the price chart. (Real case: SPOT 2026-05 first cut was 5 bull / 0 bear on a stock 46% off highs; the user's pushback re-cut it to 1 bull / 2 bear, changing the thesis framing.)

2. **Conviction-ceiling check**: count how many *independent* drivers (per the Phase 4 driver tree) the surviving asymmetries route through. If they all pivot on one driver, flag explicitly: "one-driver thesis — conviction cap Medium; Phase 7 must acknowledge this before committing." (Real case: FLR 2026-06 — all three asymmetries reduced to the segment-margin ramp; the cap only surfaced organically in the file's closing paragraph.)

These are flags for the user's Phase 7 judgment, not auto-decisions.

### Step 4 — Save to `working/asymmetries.md`

## Q&A interlude (MEDIUM)

After producing:

> "Phase 6 complete. [N] candidate asymmetries surfaced at `working/asymmetries.md`. Bullish lean: [N]. Bearish lean: [N]. Either: [N]. [Setup-bias check: …] [Independent drivers: N — conviction ceiling flag if 1]. Continue to Phase 7 (direction commit) or ask about specific candidates."

Common questions:
- *"What's the evidence behind asymmetry [N]?"* — pull more verbatim quotes, more transcript context
- *"Could asymmetry [N] go the other way?"* — yes, often, and you should articulate both
- *"Are there any asymmetries you didn't include?"* — there may be candidates you ranked too low; show your work
- *"How confident are you in [N]?"* — be honest. Some candidates are strong; some are speculative.

When user says continue, advance to Phase 7.

## Common failure modes

- **Vague asymmetries**: "AI tailwind for the company" is not an asymmetry. "Sovereign AI deployments will add $50B incremental TAM by 2027 and Street has zero in their numbers" is.
- **Asymmetries without evidence**: every entry must cite. Quotes, data, source files. No conjecture without support.
- **Confirmation bias**: don't bias toward bullish or bearish based on the user's mood. The hunt is symmetric. If most candidates lean bearish, surface that.
- **Ignoring uncovered drivers**: drivers flagged "No Street view" in Phase 5 are often the highest-edge asymmetries (uncovered alpha) and easy to miss.
- **Majority-vs-outlier mistaken for asymmetry**: if one sell-side note (e.g., a single initiation) disagrees with the majority of analysts AND with mgmt commentary, **disagreeing with the outlier is not an asymmetry vs Street consensus** — it's just agreeing with the majority. Real asymmetry requires you to disagree with the *Street MAJORITY* (or with the cluster the consensus xlsx aggregates), not with one lone analyst. Test: if you find yourself "leaning bear because Bernstein + JPM + Wolfe + mgmt all say X and only Citizens JMP says Y," you have **no edge** — you're consensus. Drop the entry. (Real case from SPOT 2026-05: audiobook segment GM trajectory; demoted after this test.)
- **Fake precision in bps decomposition**: when citing margin-bridge contributions or driver-decomposition values that come from sell-side waterfall charts, verify whether the sell-side actually published bottoms-up math (rare) or just labeled the bars (common). Most published "bridges" are analyst opinion with chart labels, not auditable builds. Cite the chart but note the magnitudes are analyst estimates without verifiable methodology.
- **Promoting an asymmetry without primary-data backing**: a real asymmetry needs at least one primary-source data point (mgmt commentary, 20-F disclosure, KPI trajectory) — not just two sell-side analysts disagreeing. If the only support is "Analyst A says X, Analyst B says Y," that's sell-side dispersion, not edge. Run a light-touch primary-data scan (transcripts, filings) before promoting.

The user picks the direction in Phase 7. Phase 6's job is to lay out the candidates honestly.
