# Phase 8 — Auto-Draft Pillars

**Goal**: Translate the asymmetries from Phase 6 into 2–4 finalized thesis pillars *for the chosen direction* from Phase 7. Skill drafts; user critiques, kills, sharpens; iterate until pillars feel right.

**Output**: `working/pillars.md` with 2–4 surviving pillars.

## What a pillar is

A pillar is one **specific, testable argument** supporting the direction. Every pillar must have **all 5 elements**:

| Element | What it captures |
|---|---|
| **Claim** | The differentiated view in one sentence |
| **Driver** | Which line of the P&L (or balance sheet) this affects, from Phase 4 driver tree |
| **Mechanism** | The causal story — *why* this happens |
| **Magnitude** | The financial impact, quantified, in the right unit |
| **Timeframe** | When this plays out (specific year or window) |

## The template

> *"[Driver] will [direction] [magnitude] by [date] because [mechanism], driving [P&L impact vs. consensus]."*

### Example (well-formed pillar — bull case for hypothetical SaaS company)

> **Pillar 1: Margin expansion ahead of consensus**
>
> *"Gross margin will expand to 48% by FY27 (vs. Street consensus 44%) because mix shift to software-only deployments — disclosed at 38% of new ACV in Q3 FY25 vs. 22% a year earlier — carries 92% incremental GM vs. hardware-attached at 65%, driving ~$0.45 incremental FY27 EPS not yet in Street numbers."*
>
> - **Driver**: Gross margin %
> - **Magnitude**: +400bps gap to Street (48% vs 44%)
> - **Mechanism**: Software-only mix shift (38% → projected 50%+ by FY27)
> - **Timeframe**: by FY27
> - **Evidence**: Q3 FY25 transcript p.7 (CFO mix disclosure); FY24 10-K Item 7 (margin profile by product type); Investor Day 2024 slide 23 (LT GM target 47–49%)

Notice: every element is filled. Numbers are specific. The driver is from the Phase 4 tree. The mechanism cites real evidence. Timeframe is concrete.

### Example (bad pillar — what NOT to write)

> *"Strong management team will execute well in the AI tailwind, leading to upside."*

This fails everything:
- No driver
- No magnitude
- No mechanism (just buzzwords)
- No timeframe
- Not falsifiable

If your draft looks like this, **drop it or rewrite from scratch**.

## Process

### Step 1 — Pull from Phase 6

Each Phase 6 asymmetry already has a "pillar candidate" field. Start there. Some asymmetries map cleanly to one pillar; some need to be combined; some don't make the cut.

### Step 2 — Match asymmetries to direction

Phase 7 chose long, short, or pass. Filter Phase 6 asymmetries:
- **If LONG**: use bullish-leaning + either-direction asymmetries that resolve bullishly
- **If SHORT**: use bearish-leaning + either-direction asymmetries that resolve bearishly
- **If PASS**: shouldn't be in Phase 8 (skip to Phase 13 pass note)

Asymmetries that lean against the chosen direction become **Phase 9 risk material**, not pillars. Don't draft pillars on the wrong side.

### Step 3 — Draft 4–6 candidate pillars

More than the final 2–4 — overdraft and let user kill. Each candidate must have all 5 elements. If a candidate is missing magnitude or timeframe, fill them in by computing from the driver tree and consensus map; if you can't, drop it.

### Step 4 — Rank by importance

Rank candidates by:
- **Driver leverage**: how much does this driver actually move the price target? (You'll get a quantitative answer in Phase 10 materiality test, but you can pre-rank by intuition: revenue growth > GM > tax rate > working capital.)
- **Evidence strength**: how many independent supporting data points?
- **Timeframe definitiveness**: pillars with clear near-term resolution > vague long-term

Top 4–6 stay. Lower-ranked move to a "considered, dropped" appendix.

### Step 5 — Present to user

```markdown
# [TICKER] Candidate Pillars (Phase 8 Auto-Draft)
Direction: [LONG / SHORT]

## Candidate 1 — [short title]
**Pillar statement**: "[full 5-element sentence]"

| Element | Value |
|---|---|
| Driver | [from tree] |
| Magnitude | [vs. Street consensus] |
| Mechanism | [causal story] |
| Timeframe | [date / window] |
| Evidence | [list of sources with paths/pages] |

**Anchored to asymmetry**: [Phase 6 asymmetry #N]

---

## Candidate 2 — [short title]
[same format]

---

[etc.]
```

### Step 6 — Q&A interlude (HEAVY)

Prompt:

> "Phase 8: [N] candidate pillars drafted. Each has all 5 elements. Review, kill, sharpen, or request alternatives. Common moves: 'kill #2' (drop a weak pillar), 'sharpen #3' (request a tighter version), 'draft alternatives for #1' (request 2–3 different angles), 'merge #1 and #4' (combine related pillars). When you're satisfied with 2–4 surviving pillars, say 'finalize.'"

Common iterations:
- *"Pillar [N] feels weak — alternatives?"* — draft 2 alternative versions of the same underlying claim with different mechanisms or timeframes
- *"Sharpen the magnitude on [N]"* — provide more granular numbers, narrower range
- *"What's the strongest version of this argument?"* — try the most aggressive defensible framing
- *"Is there a pillar I'm missing?"* — re-scan Phase 6 for skipped candidates
- *"This pillar overlaps with [M]"* — restructure to remove overlap, possibly merge

Iterate freely. The user's critiques are the value-add — don't rush.

### Step 7 — Finalize

When user says "finalize":
- Lock 2–4 pillars
- Save to `working/pillars.md` with the same format as the candidate list
- Confirm: *"[N] pillars finalized. Proceeding to Phase 9 (steel-man counter-arguments)."*

## What this is NOT

- NOT model assumptions yet (Phase 11 translates them)
- NOT vetted for falsifiability or materiality yet (Phase 10 audit)
- NOT the published thesis (still subject to audit + iteration)

## Common failure modes

- **Vague pillars**: catch this at the 5-element check. If any element is missing, the pillar isn't ready.
- **Pillars without evidence**: every pillar must cite. If you can't cite, you're guessing.
- **Pillars on the wrong side**: don't draft a bullish pillar when the direction is short. The other side becomes risks (Phase 9), not pillars.
- **Overlapping pillars**: 4 pillars that all say "AI is good" with different framings is really one pillar. Distinct pillars hit distinct drivers.
- **Too many pillars**: more than 4 is hard to defend in a pitch. If you can't pick 2–4, you don't have a thesis yet.
