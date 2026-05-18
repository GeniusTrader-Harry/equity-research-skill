# Phase 11 — Build One Model with Sensitivity Tables

**Goal**: Translate the surviving pillars from Phase 10 into a working financial model. ONE model, not three. Bull/base/bear comparison happens at the **assumption-flex level** via sensitivity tables and a tornado chart, not as three parallel theses.

**Output**: `~/Claude Projects/Equity Research/[TICKER]/deliverables/[ticker]_model.xlsx`

## Step 0 — Fresh derivation (mandatory before any assumption is entered)

Phase 11 is the first phase that produces **auditable numbers**. Every assumption used here must be derived from **primary sources** — 20-F / 10-K line items, shareholder letter actuals, sell-side consensus xlsx, `extractions/headline_anchors.md`. Back-of-envelope numbers from Phases 7–10 (share count approximations like "~205M," tax rate assumptions like "~25%," multiple choices like "~25x P/E," GP→OI flow-through estimates like "~75%," and any PT-impact / materiality math) are **NOT** carried over into the model.

The rule:
- **Pillar STRUCTURE** (which drivers matter, what direction, what magnitudes vs Street) → carried over from Phases 8/10.
- **Pillar NUMBERS** (specific bps deltas, $ magnitudes, EPS impacts) → re-derived independently in the model.

Specifically re-derive from primary sources:
- **Shares outstanding** — 20-F FDSO + SBC schedule + buyback program (not "~205M" placeholder)
- **Tax rate** — 20-F effective rate footnote + jurisdictional mix (not "~25%" placeholder)
- **Capex intensity** — 20-F historical capex / revenue (not "asset-light, de minimis" handwave)
- **Working capital** — 20-F NWC components, days-based driver build (not zero)
- **Cost of debt** — actual interest expense / average debt balance from 20-F (not assumed)
- **Beta** — derived from 2-3yr weekly returns vs market index (not handed down)
- **Capital structure weights** — actual debt + equity from BS (not "all equity" simplification)

**Why**: back-of-envelope numbers built up in Phases 7–10 are approximations for *qualitative structuring* (which pillars are defensive vs offensive, which counters matter). Phase 11 is *quantitative precision*. Carrying approximations through compounds error. The track record across previous runs has been: every back-of-envelope chain caught at least one error when surfaced for review. Fresh derivation forces the model to stand on its own.

**Reconciliation, not suppression**: after the model produces base/bull/bear PT and tornado, compare the model output to the pillar magnitudes asserted in `working/pillars_audited.md`. If the model disagrees with a Phase 8/10 pillar magnitude, that's a **Phase 12 surprise trigger** — not an error to silently align away. Flag the surprise honestly; that's exactly what Phase 12 exists to handle.

## Currency convention (FPIs and multi-currency reporters)

**Two separate decisions** that previous spec versions conflated:

| Decision | Rule |
|---|---|
| **Working currency** (Phases 2–11 analysis and model) | **Reporting currency** (what the company files its 20-F/10-K in) |
| **Output currency** (target price in memo + pitch summary) | **Listing currency** (primary market where the stock trades) |
| **Conversion timing** | At the END of Phase 11, after equity value per share is computed in reporting currency |

Examples:

| Ticker | Reports in | Lists primary on | Working currency | Output currency |
|---|---|---|---|---|
| SPOT | EUR | NYSE | **EUR** | **USD** |
| BABA | CNY/USD (dual presentation) | NYSE | **USD** (their dual-reporting) | **USD** |
| ASML | EUR | Euronext Amsterdam | **EUR** | **EUR** (same) |
| TSM | TWD | TWSE / NYSE ADR | **TWD** | **USD** (if testing US ADR) |
| NVDA | USD | NASDAQ | **USD** | **USD** (no FX issue) |

### Why analysis must be in reporting currency

- Mgmt guidance is given in reporting currency (€660M OI guide for SPOT, etc.)
- European/Asian sell-side banks build models in reporting currency natively
- YoY growth rates and margins are unaffected by FX translation noise
- Consensus comparison is clean (EUR to EUR, not EUR-via-USD-translation)
- Beat/miss judgments don't get distorted by FX-assumption gaps between consensus-time and actual-time

The Phase 2 brief revealed why this matters: USD-translated Revenue showed a "-0.4% miss" on Q1 26 vs CapIQ Median consensus, while the same data in EUR or constant-currency growth showed a small beat / acceleration. Working in reporting currency avoids this class of error.

### Conversion mechanic at end of Phase 11

1. Compute EUR equity value (or whichever reporting currency) using EUR cash flows discounted at EUR WACC (uses the eurozone risk-free rate, not US 10y)
2. Divide by total shares outstanding → per-share equity value in reporting currency
3. Convert to listing currency at chosen FX rate (typically current spot at memo date)
4. Express the target in listing currency
5. **State the implied FX assumption explicitly** in the memo (e.g., *"Target $X assumes 1.10 USD/EUR; under 1.05 USD/EUR target would be $Y; under 1.15 USD/EUR target would be $Z"*) so a reader can recompute under different FX

### Conventions for historical/forecast translation

For historical periods where you ARE working in listing currency (e.g., for charting a USD revenue trend even though primary model is EUR):
- **Historical P&L items**: average period exchange rate (sourced from filings — most FPIs disclose this in their MD&A or footnotes)
- **Historical balance-sheet items**: period-end exchange rate
- **Projections**: current spot for base case

### Memo Section 6 must include

- Working currency stated explicitly
- Output currency stated explicitly
- FX assumption used for conversion (and its date / rationale)
- FX sensitivity to listing-currency target if EUR/USD moves ±5% / ±10%

### FX as a sensitivity — only when there's real economic exposure

The reporting → listing translation above is **mechanical bookkeeping** and is not itself a thesis driver. Don't put translation-only mismatches in the tornado.

Include FX in the tornado **only** when there's a real economic mismatch:
- **Revenue currency mix differs meaningfully from cost currency mix** (e.g., USD revenue with EUR opex)
- **OR**: a material slice of revenue is in a currency other than the modeling currency (e.g., a USD-modeled firm with 40%+ EUR revenue)

If revenue is concentrated in one currency that matches the cost base — even if the firm reports in a different currency for corporate-domicile reasons — there's no economic FX exposure. Skip FX as a sensitivity.

**How to assess**: read the segment/geographic disclosure in the annual filing (10-K Item 1 or 20-F Item 4/5). Look for revenue-by-geography breakdown and cost-of-revenue currency commentary. If they disclose ~one currency for both, skip. If there's a real mix, include FX with typical ±10% flex.

**Examples**:

| Ticker | Reports in | Lists in | Revenue currency | Cost currency | FX in tornado? |
|---|---|---|---|---|---|
| NVDA | USD | USD | USD globally | USD globally | **No** — no exposure |
| AAPL | USD | USD | ~55% non-USD | mixed | **Yes** — material EUR/CNY/JPY revenue |
| SPOT | EUR | USD | ~40% USD, mix elsewhere | USD-heavy royalties + global opex | **Yes** — real revenue/cost FX mix |
| Cayman-domiciled biotech with 100% US ops | USD | USD | USD | USD | **No** — translation-only |

Pull these from `working/context.md` (Step 7 populates `Reporting currency` and `Model currency`).

## Why one model, not three

The earlier (rejected) approach was three full scenarios with a selector cell. Final design is simpler: one model expressing your direction's view, plus sensitivity flexes around the swing assumptions. This:
- Reflects how analysts actually work (you have one view, you stress-test it)
- Matches the steel-man approach (counter-arguments are risks, not parallel theses)
- Surfaces fragility (tornado chart shows where the thesis is vulnerable)
- Stays disciplined (no false precision from parallel scenarios)

## Architecture

The model has 4 sheets:

### Sheet 1 — Assumptions

The driver tree from Phase 4, populated with:
- Historical actuals (last 3 fiscal years from filings)
- Forecast inputs (your view, expressing the surviving pillars)
- Side-by-side: a column showing **Street consensus** for the same drivers (from Phase 5 consensus map) for comparison

This sheet is the visible "thesis as numbers" — every pillar's claim should be findable here.

### Sheet 2 — Historical reference (audited 3-statement, no forward projection)

Audited IS / BS / CFS for the last 3–5 fiscal years from filings — pulled verbatim, used only as historical reference and trend validation. **No forward 3-statement projection is required**: the goal of Phase 11 is a defensible target price via DCF, not a full earnings model. EPS forecasting is downstream of DCF and adds little value if the thesis is FCF-based.

Forward periods are built FCFF-only (Sheet 3). Skip a forward 3-statement unless one of:
- The user explicitly asks for forward EPS / NI guidance for a per-EPS-multiple cross-check
- The business has material non-operating volatility (large derivative gains, tax volatility, FX-translated below-the-line) that distorts FCFF and requires a full NI walk
- The pitch will be quoted at a P/E multiple rather than DCF (rare for the thesis-first workflow)

Otherwise: forecasted P&L lives in the FCFF build on Sheet 3 (EBIT × (1−t) + D&A − Capex − ΔWC) — no need to extend NI / EPS forward.

### Sheet 3 — DCF (FCFF-based)

Forward forecast is FCFF-only. Build per year FY+1 through FY+5 (5yr explicit):

```
FCFF (Unlevered Free Cash Flow)
  = EBIT × (1 − tax rate)        ← NOPAT
  + D&A                          ← non-cash add-back (incl. IFRS-16 lease depreciation)
  − ΔWorking Capital             ← cash absorbed/released by growth
  − Capex                        ← maintenance + growth capex
```

Then:
- Discount each year's FCFF at WACC (CAPM-based; sensitivity to risk-free rate, beta, ERP)
- Terminal value: **exit EV/EBITDA multiple primary** (TV = FY+5 EBITDA × exit multiple). Gordon perpetuity (TV = FCFF_n+1 / (WACC − g)) is an **optional cross-check** for businesses already in steady-state. See "Choosing the terminal method" below.
- PV(explicit) + PV(terminal) = Enterprise Value
- EV − Net Debt − Minority Interest + Investments = Equity Value
- ÷ Diluted shares outstanding (including SBC dilution + convertible if-converted) = Per-share value (in working currency)
- × FX rate = Per-share value (output currency)

Why FCFF (not FCFE / not NI-based DCF): FCFF discounted at WACC gives Enterprise Value cleanly. Net Income depends on capital structure (interest costs, tax shield) and obscures the operating economics. For a thesis-first DCF, you want the operating-cash-flow-to-value link clean.

### Choosing the terminal method

**Default: exit EV/EBITDA multiple.** Anchor to (a) closest peer comp current forward multiple, (b) sell-side PT-implied exit multiples reverse-engineered from published PTs, (c) target company's own historical trading range. Build base/bull/bear at three multiples reflecting different terminal business-state assumptions (e.g., "mid-cycle consumer subs," "premium platform," "mature DSP").

**Gordon perpetuity is appropriate ONLY when** the forecast endpoint genuinely represents steady-state: stable margin profile, growth converging to nominal GDP, no remaining re-rating optionality. For mid-transition platforms (consumer subs ramping toward platform economics, hardware mid-product-cycle, energy-transition names, mid-rollout SaaS), Gordon imposes a perpetual-growth ceiling that structurally underprices market-implied terminal optionality and produces an austere implied terminal multiple (often <10x EBITDA when peer-set trades 15-22x). That's a methodology artifact, not the business.

**Test for Gordon-suitability**: at the forecast endpoint, would you expect revenue growth to stay within ±200bps of terminal g indefinitely, and EBIT margin to be ±100bps of the endpoint? If yes, Gordon is defensible. If no, exit-multiple is the only honest method.

If both methods are computed, triangulate by stating each separately — do not average them silently into a single number.

### Sheet 4 — Sensitivity & Tornado

This is where the bull/base/bear comparison lives.

**Two-way data tables**: pick the 2 most important swing assumptions (usually revenue growth + margin, or growth + multiple). Show target price across a 3×3 or 5×5 grid of assumption flexes.

**Tornado chart**: for each input assumption, flex it ±X% (X varies by metric — see below) and measure target price impact. Sort longest-to-shortest. The result visualizes which assumptions are doing the heavy lifting.

## Tornado chart construction

For each input assumption, define a "reasonable" flex range (this isn't a worst-case stress — it's a ±sensitivity to small variations):

| Assumption type | Typical flex |
|---|---|
| Revenue growth rate | ±200bps |
| Gross margin | ±200bps |
| Operating margin / OpEx ratios | ±100bps |
| Terminal growth rate | ±50bps |
| Exit multiple | ±2x |
| WACC | ±50bps |
| Tax rate | ±100bps |

For each:
1. Hold all other assumptions at central case
2. Flex the one assumption ±range
3. Recompute target price
4. Bar length = max - min target price (% of central)
5. Sort all bars by length, longest at top

Resulting visual:

```
Revenue growth Y2  ±200bps      [████████████████]  ±35%
Terminal multiple  ±2x          [██████████]        ±18%
Gross margin Y3    ±200bps      [███████]           ±12%
Operating leverage ±100bps      [████]              ±7%
WACC               ±50bps       [███]               ±5%
Tax rate           ±100bps      [██]                ±3%
SG&A growth        ±100bps      [█]                 ±2%
```

**Interpretation**:
- The **top 2–3 bars** are your load-bearing assumptions. Your strongest pillars should sit on these.
- If a pillar is about an assumption near the bottom (e.g., tax rate), it's not a real thesis pillar — it can't move the target enough.
- If **one bar is dramatically longer than the others** (e.g., one assumption explains 75%+ of variance), the thesis is one-pillar fragile (Phase 12 surprise mode #3).

## Methodology choices — ask user explicitly at Phase 11 start

Four choices materially affect the PT and downstream documents. The skill must SURFACE these as explicit questions at Phase 11 start rather than silently default — defaults vary by sector, and a buried choice causes silent drift if user discovers it later.

| # | Question | Default | Why surface |
|---|---|---|---|
| 1 | **FCFF — SBC add-back or not?** | No (more honest — SBC is a real economic cost; dilution captured in share count instead) | If user comes from a school that historically adds SBC back to FCF (sell-side convention pre-2020), they'll expect the higher FCF. Surfacing the choice prevents disagreement at memo review |
| 2 | **Terminal method — exit EV/EBITDA, Gordon perpetuity, or both?** | Exit multiple for platform / mid-transition; Gordon for steady-state financials / utilities | Different sector conventions; Gordon imposes a methodology ceiling that may not reflect economic reality (see "Choosing the terminal method" above) |
| 3 | **Discount timing — mid-year or end-of-year?** | Mid-year (more accurate; cash flows occur throughout year not at year-end) | Both defensible; choice affects PT by 3-5%. User should commit upfront |
| 4 | **Output FX rate — current spot at memo date, year-end forward, or both?** | Current spot at memo date | For multi-currency reporters; the spot date should be stamped in valuation_outputs.yaml |

Ask all four at Phase 11 start. Document the answers in `working/valuation_outputs.yaml` (see Step 7) — these are the inputs every other doc reads from.

## Process

### Step 1 — Reuse existing skill infrastructure

Don't rebuild from scratch. Invoke:
- `financial-analysis:dcf-model` for the DCF mechanics
- `financial-analysis:3-statement-model` for the IS/BS/CFS templates
- `financial-analysis:xlsx-author` if running headless (e.g., not driving live Excel)

These skills handle the standard mechanics — formulas, formatting, integrity checks — so we can focus on *which* assumptions express the pillars.

### Step 2 — Populate assumptions

For each pillar from Phase 10:
- Identify the corresponding driver in Phase 4 tree
- Set the forecast input to the pillar's claimed magnitude
- Document the link: comment cell with *"Pillar #N — [claim]"*

For non-pillar drivers: use Street consensus or a neutral benchmark.

### Step 3 — Build 3-statement + DCF

Standard mechanics. Verify:
- BS balances every period
- Cash flow ties to BS cash change
- DCF discounts to today's date
- Equity value reconciles to enterprise value bridge

If anything fails, run `financial-analysis:audit-xls` to catch errors.

### Step 4 — Build sensitivity sheet

- Two-way data tables on top 2 swing assumptions
- Tornado chart with the flex ranges above
- Probability-weighted target (optional): assign rough probability to a +1σ / -1σ scenario, compute weighted target

### Step 5 — Compute the Bull / Base / Bear envelope (asymmetric payoff)

**Important framing**: this is *not* three parallel theses. The committed direction (Phase 7) IS the **base case**. Bull and Bear are the **payoff envelope around that single committed view** — what does the same thesis look like if it overshoots vs under-delivers? This is what buy-side / interview audiences mean when they ask "what's your risk/reward."

From the same model, flex the **top 2-3 tornado swing assumptions** (the load-bearing ones) in each direction:

- **Bull case (pillars-fire)**: flex top swing assumptions to +1σ / favorable end. What does the target look like if your pillars deliver more / faster than your central expectation? (E.g., GM expansion accelerates to 200bps/yr vs 130bps in base; Marketplace adoption faster; etc.)
- **Base case (your committed view)**: the central target from the model as built. This is your committed direction's target.
- **Bear case (pillars-fail / steel-man-realizes)**: flex top swing assumptions to -1σ / unfavorable end, AND let the Phase 9 steel-man counter-pillars partially materialize. (E.g., AI capex extends another year; ad-supp segment GM resolves bearish; tax normalizes to top of range; etc.)

The bull and bear are anchored to the **pillars and counter-pillars** you've already built — not invented scenarios. Each bull/bear should have a 1-line trigger linking it to specific pillars/risks.

**Compute risk/reward skew** (diagnostic, not gating):

```
Skew = (Bull target − Spot) / (Spot − Bear target)
```

- Skew > 2: favorable asymmetric payoff — small downside, larger upside
- Skew ~1: symmetric payoff — no asymmetry edge from valuation
- Skew < 1: unfavorable — more downside than upside

**Note**: skew is diagnostic, not a hard gate. A Low-conviction long with skew 1.5 may still be a defensible call if the thesis is sound; the skew just tells you the valuation isn't itself doing the work. A High-conviction long with skew 0.8 is a yellow flag worth interrogating — why commit if the math says the asymmetry isn't there?

### Step 6 — Document the central target + envelope

```markdown
# [TICKER] Model Output Summary
Date: [YYYY-MM-DD]
Committed direction: [LONG / SHORT] (from Phase 7)

## Base case (your committed view)
- Implied share price: $[X]
- Current price: $[Y]
- Implied upside/downside: [Z]%

## Bull / Base / Bear envelope

| Scenario | Target | vs Spot | Trigger (1 line linking to pillars/risks) |
|---|---|---|---|
| Bull (pillars-fire) | $[C] | +[D]% | [e.g., "GM expansion to 200bps/yr + Marketplace contribution + Ad-Supp segment GM resolves bullish"] |
| **Base (committed)** | **$[X]** | **+[Z]%** | [Phase 7 thesis as committed] |
| Bear (pillars-fail) | $[A] | -[B]% | [e.g., "AI capex extends + ad-supp segment GM resolves bearish + tax normalizes to top of range"] |

**Risk/reward skew**: (Bull − Spot) / (Spot − Bear) = **[ratio]:1**

## Tornado: top 5 assumptions by leverage
1. [Assumption] — ±[%]
2. [Assumption] — ±[%]
[...]

## Pillar-to-assumption mapping
- Pillar 1: drives [Assumption X], contributing [%] to the +/- vs current price
- Pillar 2: drives [Assumption Y], contributing [%]
- Pillar 3: drives [Assumption Z], contributing [%]
```

Save to `working/model_summary.md` for reference in Phase 12.

### Step 7 — Finalise: single source of truth + xlsx-vs-md audit

Phase 11 must produce a **single source of truth** for all valuation outputs that every downstream document (Phase 12 iteration log, Phase 13 memo, killing conditions check) reads from. Manual transcription of PT / bull / bear / WACC across multiple markdown files causes silent drift.

#### Step 7a — Produce `working/valuation_outputs.yaml`

```yaml
# Single source of truth for valuation outputs.
# Every downstream doc (pillars_audited.md, killing_conditions.md, phase12 iteration log,
# phase13 memo) reads from this file. Do NOT manually transcribe these values elsewhere.

ticker: "[TICKER]"
valuation_date: "YYYY-MM-DD"
spot_price:
  value: 422.11
  currency: "USD"
  source: "[exchange + timestamp]"

methodology:
  fcff_sbc_addback: false           # Step-0.5 question 1
  terminal_method: "exit_multiple"  # Step-0.5 question 2 — exit_multiple | gordon | both
  discount_timing: "mid_year"       # Step-0.5 question 3 — mid_year | end_of_year
  fx_basis: "spot_at_valuation_date" # Step-0.5 question 4

working_currency: "EUR"
output_currency: "USD"
fx_rate:
  pair: "USD_per_EUR"
  value: 1.17
  date_pulled: "YYYY-MM-DD"
  source: "[Bloomberg / FX vendor / ECB reference]"

wacc:
  risk_free_rate: 3.07
  equity_risk_premium: 5.00
  beta: 1.55
  cost_of_equity: 10.82
  pre_tax_cost_of_debt: 5.50
  after_tax_cost_of_debt: 4.24
  equity_weight: 0.95
  debt_weight: 0.05
  wacc: 10.8

scenarios:
  base:
    pt_listing_ccy: 510.50
    pt_local_ccy: 436.30
    upside_pct: 20.9
    fy30_ebitda_local: 6254
    exit_multiple: 18
    enterprise_value_local: 84566
    net_cash_local: 7500
    equity_value_local: 92066
    diluted_shares_m: 211
  bull:
    pt_listing_ccy: 692
    upside_pct: 64
    fy30_ebitda_local: 7200
    exit_multiple: 22
  bear:
    pt_listing_ccy: 279
    upside_pct: -34
    fy30_ebitda_local: 3900
    exit_multiple: 14

skew:
  formula: "(bull - spot) / (spot - bear)"
  value: 1.88

tornado_top5:
  - rank: 1
    assumption: "Exit EV/EBITDA multiple"
    flex_unit: "4x"
    pt_impact: 56
    pt_impact_pct: 11
    linked_thesis: 2
  - rank: 2
    assumption: "FY28E Consolidated GM"
    flex_unit: "200bps"
    pt_impact: 48
    pt_impact_pct: 9
    linked_thesis: 2
  # ...
```

#### Step 7b — Run xlsx-vs-md consistency audit

Mechanical check before declaring Phase 11 complete:

1. **PT base, bull, bear**: read from xlsx Summary tab or named cells; confirm match to `valuation_outputs.yaml`.
2. **WACC + components**: read from xlsx WACC tab; confirm match.
3. **FY[N+5] EBITDA base / bull / bear**: read from xlsx DCF tab; confirm match.
4. **Exit multiples base / bull / bear**: read from xlsx Sensitivity tab; confirm match.
5. **Net cash / equity bridge components**: read from xlsx; confirm match.
6. **Skew calculation**: recompute from yaml scenarios; confirm matches the value stored.

Any mismatch is a fail. Resolve by editing the yaml to match the xlsx (xlsx is source of truth for outputs) OR by editing the xlsx if a typo introduced the divergence.

#### Step 7c — Sweep working/ for orphaned valuation numbers

Phase 11 finalise step also greps the existing working/ files (`pillars.md`, `pillars_audited.md`, `risks.md`, `killing_conditions.md`, `dcf_build.md`, `model_summary.md`) for hard-coded valuation numbers — PT, bull, bear, skew, WACC. Any orphaned value must either:
- Be replaced with a reference to `valuation_outputs.yaml` (e.g., a comment "base PT $510 per valuation_outputs.yaml" rather than the bare number)
- OR be updated to match the yaml

This prevents the "skew 1.69 vs 1.88" class of cross-doc drift.

## Q&A interlude (LIGHT)

This phase is mostly mechanical. Common asks:

- *"Walk me through how you got from Pillar [N] to the assumption"* — show the driver mapping
- *"What's the central target?"* — pull from the summary
- *"Why is [assumption] dominating the tornado?"* — explain mechanically (high leverage, high uncertainty range, or both)
- *"Can you show me the model?"* — file path; user can open in Excel

When user says continue, advance to Phase 12.

## Critical: pillars must show up as assumptions

Every Phase 10 surviving pillar must be findable as a specific cell or set of cells in the assumptions sheet. If a pillar isn't translatable to a model input, the pillar wasn't tight enough — flag back to Phase 10 for sharpening.

## What this is NOT

- NOT three parallel scenario models — one model, three sensitivities
- NOT a comps-only valuation (we use DCF as the primary; comps are a sanity check)
- NOT the final pitch (Phase 13)

## Common failure modes

- **Model doesn't balance**: run audit-xls. Fix BS first, then cash tie-out.
- **DCF terminal value > 80% of total**: usually means explicit forecast period is too short or growth assumptions too aggressive. Extend forecast or temper.
- **Tornado has one massive bar**: see Phase 12 surprise mode #3.
- **Implied multiple is unreasonable** (e.g., 50x P/E for a slow-grower): see Phase 12 surprise mode #2.
- **Pillar can't be expressed as an assumption**: pillar was too vague. Kick back to Phase 10.
