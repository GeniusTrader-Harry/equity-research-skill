# Phase 5 — Consensus Map

**Goal**: For every driver in the Phase 4 tree, document what the Street currently expects, where estimates are tightly clustered vs. widely dispersed, and where the Street has no view at all. This is the **map of priced-in expectations** — without it, you can't have edge.

**Output**: `working/consensus_map.md` with a driver-by-driver table.

## Why this matters

Edge = your view minus the Street's view. To know if you have edge, you must first know what the Street believes. Phase 5 makes the Street's view explicit so Phases 6–8 can hunt for gaps.

## What to record per driver

For each node in the driver tree, fill in:

| Field | What it captures |
|---|---|
| **Driver name** | From Phase 4 tree |
| **Unit** | %, $, bps, ratio, count |
| **Y1 consensus** | Street's median estimate for current FY |
| **Y2 consensus** | Median for FY+1 |
| **Y3 consensus** | Median for FY+2 |
| **Estimate dispersion** | Tight / wide. Tight = top quintile to bottom quintile <15% spread. Wide = >30% spread. |
| **Mgmt guidance** | Most recent guidance for this driver. Quote verbatim with source. |
| **Coverage flag** | "Tracked" / "Implicit" / "No Street view" |

### Coverage flags

- **Tracked**: Sell-side analysts explicitly model this driver. Found in their tables.
- **Implicit**: Not directly modeled, but implied by other estimates. E.g., NRR isn't always disclosed but is implied by ARR growth + new logo growth.
- **No Street view**: Street has not formed an estimate. This is itself a flag — these drivers are candidates for "uncovered alpha" asymmetries in Phase 6.

## Where to find consensus

**Two-tier source rule** — different data needs different sources. This aligns with the canonical source-hierarchy table in `phase1-context-load.md`.

### Tier A — Headline-level forward consensus (Revenue, OI, EBITDA, EPS, GM, FCF at total-company level)

**Primary source: CapIQ Consensus xlsx** (already pulled in Phase 1 / Step 8).
- The xlsx aggregates dozens of analyst models into a Median (and Mean, High, Low, # analysts) for each metric, by fiscal year, going out to FY+2 or FY+3.
- This is the cleanest single source for the headline forward consensus — use the **Median** row.
- Cross-check: confirm the # of analysts in the xlsx is reasonable (typically 15-30 for a covered name); if very few (<5), the median is noisy.

**Backup (if CapIQ not available)**:
- Bloomberg / FactSet consensus tab (same aggregation, different vendor)
- Yahoo Finance (free, but only top-line revenue and EPS)
- Median of available sell-side notes in `sell-side/`

### Tier B — Driver-level disaggregated consensus (segment growth, ARPU, NRR, sub-KPIs, GM by segment, etc.)

**Primary source: sell-side notes in `sell-side/`.**
- CapIQ does not model these granularly — its xlsx stops at headline metrics.
- Each sell-side note typically has a multi-year forecast table that decomposes the top line into driver-level assumptions (segment growth rates, sub-driver ARPU, KPI counts, etc.)
- Take the **median across notes** for each driver. Note the date of each note (older = staler).
- Where notes diverge, the dispersion itself is signal for Phase 6 asymmetry hunt.

**Backup**: if no sell-side notes are in `sell-side/`, mark the driver "No Street view" — this is itself a candidate "uncovered alpha" asymmetry for Phase 6.

### Why two tiers and not one ranking

Headline metrics → CapIQ is best because it's aggregated across many models cleanly.
Driver-level metrics → Sell-side notes are required because CapIQ doesn't have them.

Both are needed in this phase. They answer different questions.

## Process

### Step 1 — Build the table skeleton from the driver tree

Copy each driver from `working/driver_tree.md` into a new table.

### Step 2 — Fill in for each driver

Follow the two-tier rule above:
- **Headline metrics** (revenue, OI, EBITDA, EPS, GM, FCF) → **CapIQ Consensus xlsx Median** (extract with the label-based pattern from Phase 2 § "Extracting CapIQ Consensus xlsx — robust pattern"). Backup: median of sell-side notes if CapIQ unavailable.
- **Driver-level / segment / sub-KPIs** (segment growth, ARPU, NRR, customer count, etc.) → median of sell-side notes in `sell-side/`. Mark "No Street view" if no analyst tracks the driver — this is a candidate Phase 6 asymmetry.

### Step 3 — Flag dispersion

For each driver where you have ≥3 estimates:
- Compute (max − min) / median
- <15% = Tight
- 15–30% = Medium
- \>30% = Wide

Wide dispersion = the Street disagrees about this driver = potential asymmetry candidate.

### Step 4 — Quote management guidance

For each driver mgmt has guided on, quote the most recent guidance verbatim from the latest earnings call or investor day. Include speaker, date, and source.

Example:
> *"GM expansion: 'We expect gross margin to expand 100–150bps in FY26.' — CFO, Q3 FY25 earnings call, Oct 28 2025."*

### Step 5 — Cross-reference and flag inconsistencies

If Street consensus is meaningfully different from mgmt guidance, flag it. Either:
- Mgmt is sandbagging → Street has updated for the upside
- Street disbelieves guidance → potential asymmetry in either direction
- Information asymmetry → who's right?

## Output format

```markdown
# [TICKER] Consensus Map
Date: [YYYY-MM-DD]
Sources: [list — e.g., GS initiation 2024-09, JPM update 2025-10, Yahoo Finance aggregate]

## Top-line drivers

| Driver | Unit | Y1 | Y2 | Y3 | Dispersion | Mgmt guidance | Coverage |
|---|---|---|---|---|---|---|---|
| Revenue total | $M | ... | ... | ... | Tight | "double-digit growth" Q3 call | Tracked |
| EPS | $ | ... | ... | ... | Wide | none | Tracked |
| GM% | % | ... | ... | ... | Medium | "47-49% LT target" 2024 IDay | Tracked |

## Segment / KPI drivers

| Driver | Unit | Y1 | Y2 | Y3 | Dispersion | Mgmt guidance | Coverage |
|---|---|---|---|---|---|---|---|
| Software revenue | $M | ... | ... | ... | Wide | Q3: "ramping faster than expected" | Tracked |
| Net Revenue Retention | % | ... | ... | ... | Wide | not disclosed | Implicit |
| Customer count >$1M ARR | # | — | — | — | — | not disclosed | No Street view |

## Notable observations
- [Where dispersion is widest — flag for Phase 6 asymmetry hunt]
- [Where consensus diverges from mgmt guidance — flag]
- [Drivers with no Street view — these are uncovered alpha candidates]

## Anchor existence matrix — which sources cover which metric × year

This is a separate table that explicitly records **what each source covers** — used by Phase 8 (drafting pillars) and Phase 10 (Gate A — anchor existence check) so no pillar cites a forecast horizon that the source does not actually publish.

| Source | Note date | Revenue FY+1 | Revenue FY+2 | Revenue FY+3 | GM FY+1 | GM FY+2 | GM FY+3 | OI FY+1 | OI FY+2 | OI FY+3 | [Key driver] FY+3 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| CapIQ Median | [date pulled] | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✗ |
| [Sell-side firm 1] | [date] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (quantified bridge) | ✓ | ✓ | ✓ | ✓ |
| [Sell-side firm 2] | [date] | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ (narrative only) | ✓ | ✓ | ✓ | — |
| [Sell-side firm 3] | [date] | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ (stops FY+2) | ✓ | ✓ | ✗ | — |

Fill in:
- ✓ = source publishes a forecast for that cell
- ✗ = source explicitly does NOT cover that cell (e.g., CapIQ Median for FY+3 forecasts)
- (qualifier) = note if the forecast is narrative-only vs quantified-bridge, audited vs estimate, etc.
- — = unknown / not checked

**Rule for Phases 8 + 10**: never cite a source for a cell marked ✗. If FY+3 GM is needed and CapIQ doesn't cover it, the only valid anchors are the sell-side firms that DO publish FY+3 GM — and the pillar evidence must name them, not generic "Street consensus."
```

## Q&A interlude (LIGHT–MEDIUM)

After producing:

> "Phase 5 complete. Consensus map at `working/consensus_map.md`. Notable: [3 most interesting observations]. Continue to Phase 6 (asymmetry hunt) or ask first."

Common questions:
- *"Why is dispersion wide on [driver X]?"* — usually means weak disclosure. Confirm with the source.
- *"What does NRR mean?"* — yes, define jargon when asked.
- *"Why does Street disagree with mgmt on [Y]?"* — usually means analysts have applied a discount to mgmt guidance based on history of misses, or analysts have factored in something mgmt isn't acknowledging.

When user says continue, advance to Phase 6.

## What this is NOT

- NOT your view (that's Phase 6 onwards)
- NOT a forecast you're committing to
- NOT a critique of consensus — just a description of it

Just the map. The hunt is next.
