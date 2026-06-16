# Phase 11 — Build One Model with Sensitivity Tables

**Contents**: Step 0 method-selection gate (forward multiple default / DCF / SOTP) · Step 0.5 fresh derivation (mandatory) · Currency convention (FPIs) · Why one model · Architecture (Sheets 1–4: assumptions, historicals, valuation build, sensitivity) · Tornado construction · Methodology choices to ask the user · Process (Steps 1–7: reuse skills + formatting standard, assumptions, valuation, sensitivity mechanics, bull/base/bear envelope, model summary, valuation_outputs.yaml single source of truth + xlsx-vs-md audit)

**Goal**: Translate the surviving pillars from Phase 10 into a working financial model. ONE model, not three. Bull/base/bear comparison happens at the **assumption-flex level** via sensitivity tables and a tornado chart, not as three parallel theses.

**Output**: `~/Claude Projects/Equity Research/[TICKER]/deliverables/[ticker]_model.xlsx`

## Step 0 — Method-selection gate (pick the valuation approach FIRST)

Before deriving a single assumption, **choose the valuation method that fits the business.** This is the first decision of Phase 11 — it determines what the model is and what Appendix A looks like. **The default is a forward-multiple valuation, not a DCF.** DCF is no longer automatic; it is selected only when the business genuinely fits, or run as a secondary cross-check.

| Method | Use when | Default? |
|---|---|---|
| **Forward multiple** (FY+2 EBITDA/EPS × triangulated multiple) | Cyclical, mature, comparable-rich, lumpy or charge-prone cash flows — i.e. most names | **YES — default** |
| **SOTP** (segment-level multiples + non-core stakes) | Multi-segment or hidden-asset names (e.g. core E&C + a separate listed stake + net cash) | When segments deserve different multiples |
| **DCF (FCFF)** | Steady-state, predictable FCF, terminal value not dominant — or as a cross-check | Opt-in only |

**Why the default flipped to multiples.** For cyclical, charge-prone, lumpy-cash-flow businesses a DCF's terminal value dominates the answer while its inputs (mid-cycle margin, terminal growth, WACC) are unknowable — so the output is an artifact of the assumptions, not the business. The market prices these names on a forward multiple, and the sell-side overwhelmingly does too. (In the FLR consensus map, six of seven analysts valued the name on a forward multiple — UBS 7.7× FY27 EBITDA, Citi 18× FY27 EPS, Barclays 10.7× FY26 EBITDA, Baird 6.0× FTM EBITDA — and the two DCFs swung entirely on an unverifiable mid-cycle-margin × WACC pair.) Anchoring to a defensible multiple is *more* interview-defensible, not less.

**Selecting DCF or SOTP is a positive, stated choice.** If you pick DCF, write one line in `working/valuation_outputs.yaml` justifying why this business is steady-state enough that terminal value isn't doing unjustifiable work (use the Gordon-suitability test under "If DCF selected" below). If you pick SOTP, list the segments and the non-core assets valued separately.

### Which forward metric — EV/EBITDA vs P/E (for the default path)

Which metric you apply the multiple to is company-dependent, so the gate prescribes a rule, not a single metric:

- **Default: compute BOTH, lead with EV/EBITDA, cross-check with P/E, and reconcile the gap.** When the two implied targets diverge materially, that gap is *signal* (usually balance sheet, tax, or buyback) and the memo must explain it.
- **Lead with EV/EBITDA when:** capital structures vary across the peer set (EBITDA is pre-leverage), D&A / capital intensity distorts net income, the story is enterprise-level with a separate equity bridge (net cash, minorities, non-core stakes), or earnings are negative / noisy.
- **Lead with P/E when:** capital structures are homogeneous AND the market quotes the sector on earnings (financials, staples, quality compounders), or below-the-line items (tax, interest, buyback-driven share-count shrinkage) are central to the equity story.
- **Single-metric edge cases:** EV/EBITDA-only when earnings are negative / meaningless; P/E-only for financials where EBITDA is meaningless.
- **FLR application:** lead EV/EBITDA (net cash + NuScale stake live outside operating EBITDA → handled in the bridge; EPS distorted by buybacks and volatile tax), cross-check Citi's 18× P/E, reconcile.

### What "multiple-based" means concretely (default mechanics)

Standard sell-side mechanics:

- **Estimate forward EBITDA and EPS for FY+1 and FY+2** off the Phase 4 driver model. Value primarily off **FY+2** (a full cycle out, what bulls and bears anchor to); show FY+1 as the nearer checkpoint.
- **Pick the target multiple** (EV/EBITDA and/or P/E) and **justify where in the triangulated range it sits.** The applied multiple is anchored against three pillars — gathered already in the Phase 5 consensus map (all available from CapIQ data, so triangulation holds even without research notes):
  1. **Peer-set forward multiples** (where comparable names trade today — CapIQ comps tab)
  2. **The company's own ~5-year trading range** (own-history premium / discount — CapIQ multiple history)
  3. **The consensus PT-implied multiple** — under `research_notes_available: false`, computed from the **aggregate consensus PT mean ÷ CapIQ forward EBITDA/EPS** (Phase 5 records this); under `research_notes_available: true`, the richer **reverse-engineered per-bank PT-implied multiples**.
- **Equity bridge:**
  - EV/EBITDA path: `EV = FY+2 EBITDA × target EV/EBITDA` → `equity = EV − net debt (+ net cash) − minorities + non-core investments (e.g. a listed-stake residual)` → `÷ diluted shares = per-share`.
  - P/E path: `per-share = FY+2 EPS × target P/E` directly (already equity-level). **Reconcile the two paths** and explain any material gap.
- **Optional discount-back** to a 12-month price target at cost of equity (state if applied).
- **Bull / base / bear envelope** = flex BOTH the forward estimate (via driver assumptions) AND the applied multiple (re-rate / de-rate). This is cleaner and more honest than DCF's WACC / terminal-g flex.

The four methodology questions to surface at Phase 11 start are under "[Methodology choices](#methodology-choices--ask-user-explicitly-at-phase-11-start)" below — the default-path set, with the DCF set nested under "if DCF selected."

## Step 0.5 — Fresh derivation (mandatory before any assumption is entered)

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

1. Compute equity value in the reporting currency natively — forward multiple applied to reporting-currency EBITDA/EPS for the default path, or (if DCF) reporting-currency cash flows discounted at a reporting-currency WACC that uses the local risk-free rate, not US 10y
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

The canonical layout is **Cover → Assumptions → Income Statement (history + forecast) → Scenarios → Multiples → Sensitivity** (six tabs). This is the same shape as a clean sell-side model: a reader should be able to open it cold and audit it tab-by-tab without a legend. (Older spec versions described "4 sheets" and treated the earnings build as optional; that under-served P/E-led names — see Sheet 3.) The DCF build replaces the Scenarios/Multiples valuation mechanics only when DCF was selected in Step 0; everything else is method-agnostic.

### Sheet 0 — Cover

A one-glance summary tab: ticker + listing(s), committed direction, valuation date, spot price, the bull/base/bear PT grid with %s, the applied multiple per scenario, working/output currency + FX rate and date, and the headline one-line thesis. This is the model's own front page — it should match `working/valuation_outputs.yaml` exactly.

### Sheet 1 — Assumptions (every input + a Notes column)

The driver tree from Phase 4, populated with:
- **Historical actuals — 4–5 fiscal years, not 3** (pull the prior-year filing for the 4th/5th year). Show them *in this sheet*, with a **computed growth / margin row beside each driver**, so every forward assumption sits directly next to the trend it is extrapolating. Historicals are the visible anchor, not a passive reference tab.
- Forecast inputs (your view, expressing the surviving pillars)
- Side-by-side: a column showing **Street consensus** for the same drivers (from Phase 5 consensus map) for comparison
- **A mandatory `Notes` column** — one line per hardcoded input stating *why this number*, with a `[source]` tag (e.g. *"+14% accom: vs +21% FY25 actual; tapers as base scales — [Q4 letter] + [May-Day room-night data]"*). This is the sheet-level twin of the cell-comment rule, but visible without hovering. **A forecast input with a blank Notes cell is an incomplete model** — it means the number was picked, not derived. This column is the single highest-value model-quality feature; do not skip it.

This sheet is the visible "thesis as numbers" — every pillar's claim should be findable here, and every input should carry its justification beside it.

### Sheet 2 — Income Statement (history + forecast)

A single P&L tab carrying **4–5 historical years (verbatim from filings) and the forecast years side by side**, built down to the headline metric the multiple is applied to (EBITDA and/or clean EPS). History and forecast living in the same tab is what makes the forecast auditable — a reader sees each forward line as a continuation of its own actual series. (Pull the audited BS / CFS for the same years onto a reference tab for tie-outs and trend validation; a *full forward 3-statement* projection is required only when the user asks, when non-operating volatility distorts the headline metric, or when a balance-sheet walk is itself load-bearing — e.g. a buyback or deleveraging thesis.)

**Model the cost side off margins, not a built-up COGS line, and trend the margins — never hold them constant.**
- For a forward-multiple model you need EBITDA/EPS to land cleanly, not a bottoms-up cost stack. **Drive cost of revenue and opex off ratio assumptions** (gross margin %, S&M / R&D / G&A as % of revenue) applied to the revenue build — not a separately forecast COGS line that can drift out of sync with revenue.
- **A flat ratio held across the whole forecast is a red flag, not a neutral default.** Margins and opex ratios move — with scale (operating leverage), mix, pricing, and the pillars themselves. Each ratio should **trend** across the forecast years, and each step of the trend gets a Notes-cell justification (e.g. *"S&M 24.0%→23.5%: international cohort matures, P1 leverage"*). A constant ratio almost always means the line wasn't actually modeled.

**Structural-input vs realised-output margin — show the bridge.** When a *revenue-only* adjustment sits between your input margin and the reported margin — a take-rate cut, a rebate/give-back, a gross-to-net reclass, a promotional credit — the **realised** margin that falls out of the IS will differ from the **structural** margin you input (because the adjustment cuts revenue but not cost, or vice versa). This is not an error, but it *looks* like one to a reviewer. Make it explicit: keep the structural input as a memo row, show the revenue-only adjustment as its own **bridge line**, and let the realised margin compute below it. Generalises to any business with a meaningful gross-to-net wedge (marketplaces/take-rate, gross-vs-net revenue, rebate-heavy distribution).

What the forward forecast must produce depends on the method chosen in Step 0:
- **Forward multiple (default)**: forecast **forward EBITDA and clean EPS** for FY+1 and FY+2 (and through FY+3 if useful) off the Phase 4 drivers — enough of the P&L to land both metrics cleanly. See "Sheet 3 → the earnings/EPS build" for the clean-EPS discipline.
- **DCF (if selected)**: forecast **FCFF** (EBIT × (1−t) + D&A − Capex − ΔWC) per year FY+1 through FY+5.

### Sheet 3 — Valuation build (forward multiple by default; FCFF if DCF selected)

#### Default path — forward-multiple build

Forecast forward EBITDA and EPS for FY+1 and FY+2 off the Phase 4 drivers, then value primarily off **FY+2**:

```
Per-share value (EV/EBITDA path — lead)
  EV          = FY+2 EBITDA × target EV/EBITDA
  − Net debt  (+ Net cash)
  − Minority interest
  + Non-core investments        ← e.g. a separately listed stake, valued at market/haircut
  = Equity value
  ÷ Diluted shares outstanding  (incl. SBC dilution + convertible if-converted)
  = Per-share value (working currency)
  × FX rate                     = Per-share value (output currency)

Per-share value (P/E path — lead OR cross-check)
  = FY+2 clean EPS × target P/E  ← already equity-level (see "the earnings/EPS build" below)
```

**Which path leads is not fixed — P/E is a first-class lead, not a permanent cross-check.** For sectors quoted and pitched on earnings (consumer, internet, financials, quality compounders, many ADRs) the **P/E × clean-EPS path is the headline and the EV/EBITDA bridge is the cross-check** — the reverse of the default. Use the EV/EBITDA-vs-P/E rule in Step 0 to decide which leads; whichever leads, build the other and reconcile.

##### The earnings / EPS build (required whenever P/E is the lead or the cross-check)

EPS is not a net-margin shortcut and not an afterthought. When a P/E is being applied, the EPS it multiplies must be built and defined with the same care as the multiple:

- **Define "clean / adjusted EPS" explicitly, and strike it on the SAME basis as the comps.** Write a labelled clean-EPS row stating exactly what is excluded and *why* — e.g. SBC (only if the peer set quotes ex-SBC), one-off investment / fair-value gains and losses, impairments, restructuring, FX remeasurement, discrete tax items. **The exclusions must match how the peer multiples are struck**: applying a clean-EPS to a comp set that trades on GAAP EPS (or vice versa) is a silent apples-to-oranges error that mis-prices the target. State the basis in `valuation_outputs.yaml` and in the Notes column.
- **Build EPS through the full below-the-line, not off a net margin.** Operating income → net interest / investment income → associates / JV income → pre-tax → tax at a justified effective rate → minority interest → net income to common → ÷ **diluted** share count (incl. SBC dilution + convertible if-converted, net of buyback) → EPS. Each of these below-the-line lines is its own assumption with a Notes justification — they are exactly where naïve models hide a constant ratio.
- **Trend the below-the-line ratios** (tax rate, NII yield, minority share) with justification — same discipline as the operating margins; a flat tax or NII line is the same red flag.

The **target multiple is triangulated** against (a) peer-set forward multiples, (b) the company's own ~5-year trading range, and (c) the consensus PT-implied multiple — per-bank PT bridges if `research_notes_available`, else the aggregate consensus PT ÷ CapIQ forward metric (all gathered in the Phase 5 consensus map; all available from CapIQ data). State where in that range the applied multiple sits and which pillar justifies any premium / discount. Optionally discount the forward fair value back to a 12-month PT at cost of equity (state if applied).

For **SOTP** names, run the same bridge per segment (each segment EBITDA × its own multiple), then add net cash and non-core stakes — the equity bridge above is already SOTP-shaped via the non-core-investments line.

#### If DCF selected (or run as a cross-check) — FCFF build

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

### Choosing the terminal method (DCF path only)

When DCF is the selected method, the terminal value method still matters:

**Default within DCF: exit EV/EBITDA multiple.** Anchor to (a) closest peer comp current forward multiple, (b) the consensus PT-implied exit multiple (per-bank if `research_notes_available`, else aggregate consensus PT ÷ forward metric), (c) target company's own historical trading range. Build base/bull/bear at three multiples reflecting different terminal business-state assumptions (e.g., "mid-cycle consumer subs," "premium platform," "mature DSP").

**Gordon perpetuity is appropriate ONLY when** the forecast endpoint genuinely represents steady-state: stable margin profile, growth converging to nominal GDP, no remaining re-rating optionality. For mid-transition platforms (consumer subs ramping toward platform economics, hardware mid-product-cycle, energy-transition names, mid-rollout SaaS), Gordon imposes a perpetual-growth ceiling that structurally underprices market-implied terminal optionality and produces an austere implied terminal multiple (often <10x EBITDA when peer-set trades 15-22x). That's a methodology artifact, not the business.

**Test for Gordon-suitability**: at the forecast endpoint, would you expect revenue growth to stay within ±200bps of terminal g indefinitely, and EBIT margin to be ±100bps of the endpoint? If yes, Gordon is defensible. If no, exit-multiple is the only honest method.

If both methods are computed, triangulate by stating each separately — do not average them silently into a single number.

### Sheet 4 — Sensitivity & Tornado

This is where the bull/base/bear comparison lives.

**Two-way data tables**: pick the 2 most important swing assumptions (usually revenue growth + margin, or growth + multiple). Show target price across a 3×3 or 5×5 grid of assumption flexes.

**Tornado chart**: for each input assumption, flex it ±X% (X varies by metric — see below) and measure target price impact. Sort longest-to-shortest. The result visualizes which assumptions are doing the heavy lifting.

## Tornado chart construction

For each input assumption, define a "reasonable" flex range (this isn't a worst-case stress — it's a ±sensitivity to small variations). **On the default path, the load-bearing swing variables are the forward-estimate drivers (revenue growth, margin) and the applied multiple itself** — not WACC / terminal-g, which only appear under the DCF path.

| Assumption type | Typical flex | Default path | DCF path |
|---|---|---|---|
| Revenue growth rate | ±200bps | ✓ | ✓ |
| Gross margin | ±200bps | ✓ | ✓ |
| Operating margin / OpEx ratios | ±100bps | ✓ | ✓ |
| **Applied valuation multiple** (EV/EBITDA or P/E) | **±2x EV/EBITDA or ±20%** | **✓ — usually a top bar** | — |
| Tax rate | ±100bps | ✓ | ✓ |
| Terminal growth rate | ±50bps | — | ✓ (terminal flex) |
| Exit multiple | ±2x | — | ✓ (terminal flex) |
| WACC | ±50bps | — (only if discount-back applied) | ✓ |

For each:
1. Hold all other assumptions at central case
2. Flex the one assumption ±range
3. Recompute target price
4. Bar length = max - min target price (% of central)
5. Sort all bars by length, longest at top

Resulting visual (default / forward-multiple path):

```
Revenue growth Y2  ±200bps      [████████████████]  ±35%
Applied multiple   ±2x          [██████████]        ±18%
Gross margin Y3    ±200bps      [███████]           ±12%
Operating leverage ±100bps      [████]              ±7%
Tax rate           ±100bps      [██]                ±3%
SG&A growth        ±100bps      [█]                 ±2%
```

(Under the DCF path the bars are the same operating drivers plus WACC ±50bps and terminal-g ±50bps in place of the applied multiple.)

**Interpretation**:
- The **top 2–3 bars** are your load-bearing assumptions. Your strongest pillars should sit on these.
- If a pillar is about an assumption near the bottom (e.g., tax rate), it's not a real thesis pillar — it can't move the target enough.
- If **one bar is dramatically longer than the others** (e.g., one assumption explains 75%+ of variance), the thesis is one-pillar fragile (Phase 12 surprise mode #3).

## Methodology choices — ask user explicitly at Phase 11 start

These choices materially affect the PT and downstream documents. The skill must SURFACE them as explicit questions at Phase 11 start rather than silently default — defaults vary by sector, and a buried choice causes silent drift if user discovers it later. **Which set of questions applies depends on the Step 0 method gate.**

### Default path (forward multiple) — ask these four

| # | Question | Default | Why surface |
|---|---|---|---|
| 1 | **Which multiple — EV/EBITDA, P/E, or both (reconciled)?** | Both — lead EV/EBITDA, cross-check P/E (see the EV/EBITDA-vs-P/E rule in Step 0) | The lead metric depends on capital-structure homogeneity and what the sector is quoted on; reconciling the two surfaces balance-sheet / tax / buyback effects |
| 2 | **Which forward year drives the headline?** | FY+2 (a full cycle out); FY+1 shown as the nearer checkpoint | Anchoring to the wrong year over- or under-states the cyclical position |
| 3 | **Where in the triangulated range does the applied multiple sit, and why?** | At peer median unless a pillar justifies a premium / discount | The applied multiple is the second-biggest tornado bar; its justification (quality/growth differential vs peers; own-history premium/discount) must be explicit, not assumed |
| 4 | **Discount the forward fair value back to a 12-month PT?** (+ FX convention) | No discount-back (state the FY+2-based fair value as the 12-month target); current spot at memo date for FX | Both defensible; if applied, the cost-of-equity discount affects PT by a few %. FX spot date stamped in valuation_outputs.yaml |

### If DCF selected — ask these four instead

| # | Question | Default | Why surface |
|---|---|---|---|
| 1 | **FCFF — SBC add-back or not?** | No (more honest — SBC is a real economic cost; dilution captured in share count instead) | If user comes from a school that historically adds SBC back to FCF (sell-side convention pre-2020), they'll expect the higher FCF. Surfacing the choice prevents disagreement at memo review |
| 2 | **Terminal method — exit EV/EBITDA, Gordon perpetuity, or both?** | Exit multiple for platform / mid-transition; Gordon for steady-state financials / utilities | Different sector conventions; Gordon imposes a methodology ceiling that may not reflect economic reality (see "Choosing the terminal method (DCF path only)" above) |
| 3 | **Discount timing — mid-year or end-of-year?** | Mid-year (more accurate; cash flows occur throughout year not at year-end) | Both defensible; choice affects PT by 3-5%. User should commit upfront |
| 4 | **Output FX rate — current spot at memo date, year-end forward, or both?** | Current spot at memo date | For multi-currency reporters; the spot date should be stamped in valuation_outputs.yaml |

Ask the applicable set at Phase 11 start. Document the answers in `working/valuation_outputs.yaml` (see Step 7) — these are the inputs every other doc reads from.

## Process

### Step 1 — Reuse existing skill infrastructure

Don't rebuild from scratch. Invoke:
- `financial-analysis:comps-analysis` for the forward-multiple build and the peer triangulation table (default path)
- `financial-analysis:dcf-model` for the DCF mechanics — **only if DCF was selected in Step 0** (or as a cross-check)
- `financial-analysis:3-statement-model` for the IS/BS/CFS templates
- `financial-analysis:xlsx-author` if running headless (e.g., not driving live Excel)

These skills handle the standard mechanics — formulas, formatting, integrity checks — so we can focus on *which* assumptions express the pillars.

**Model formatting standard** (applies whether the xlsx is built via those skills or a custom script):
- **Font colors**: blue = hardcoded input, black = formula, green = cross-sheet link. This is the audit-at-a-glance convention every benchmark model skill enforces.
- **Cell comments on every hardcoded input**: `Source: [document], [date], [reference]` — added as the value is entered, not retrofitted. This is the cell-level version of the citation discipline.
- **Borders**: thick borders around major sections, thin around data tables — the model should read in sections without a legend.

### Step 2 — Populate assumptions

For each pillar from Phase 10:
- Identify the corresponding driver in Phase 4 tree
- Set the forecast input to the pillar's claimed magnitude
- Document the link: comment cell with *"Pillar #N — [claim]"*

For non-pillar drivers: use Street consensus or a neutral benchmark.

#### Every forward GROWTH driver must be evidence-grounded

A growth assumption with no contemporaneous evidence behind it is the soft underbelly of the model — it is the first thing a sharp reader attacks ("why do you assume growth *slows* — what in the data says so?"). For each forward growth driver, the Notes cell must carry:
1. **its own trailing trend** (the last 2–3 actuals it is extrapolating from), and
2. **≥1 contemporaneous leading indicator** — the most recent real-world read on that driver (latest-quarter KPI, a high-frequency proxy, peer prints, channel/industry data, mgmt guide), and
3. **the next hard data point** that will confirm or break it (the next earnings print / KPI release / regulatory milestone), named with its date — this becomes a natural catalyst and a candidate killing-condition tripwire.

A forecast that decelerates or inflects with nothing in (2) to support it is an assertion, not an estimate — temper it to the trend or find the evidence.

#### Size the EXPOSED base of any lever — a driver rarely acts on 100% of a reported line

When a pillar or risk acts on only a *portion* of a reported segment (a regulatory cap that hits one product/geography, a price change on one cohort, a mix shift within a line), do not apply it to the whole reported line — **size the exposed sub-portion first**, as its own assumption:
- If the company discloses the split, use it.
- **If it does not, build the exposed share two ways and reconcile them** — a top-down decomposition (geography / product mix off disclosures) *and* a bottom-up market-sizing (e.g. addressable GMV × take-rate ÷ segment revenue). Independent methods that agree give a defensible number; methods that diverge tell you the decomposition is fragile.
- **Any assumed sub-split is flagged `[est]`** in the Notes cell and must reconcile against the independent method *before* it becomes load-bearing. An exposed-base figure built on a single unverified decomposition is exactly the kind of number that collapses under "is this real, or did you make it up?"

### Step 3 — Build the valuation

Standard mechanics. Verify, by method:

**Default (forward multiple):**
- Forward EBITDA and EPS tie to the assumption-sheet drivers
- Equity bridge reconciles (EV from multiple → net cash/debt, minorities, non-core stakes → equity → per share)
- EV/EBITDA and P/E paths reconciled, with any gap explained
- Applied multiple sits inside (or is explicitly justified outside) the triangulated peer / own-history / consensus-implied range

**If DCF selected:**
- BS balances every period
- Cash flow ties to BS cash change
- DCF discounts to today's date
- Equity value reconciles to enterprise value bridge

**Mandatory post-build audit**: once the xlsx is complete, run `financial-analysis:audit-xls` (scope: full model — BS balance, tie-outs, hardcode scan, hockey-stick check) regardless of whether anything visibly failed, and resolve critical findings before declaring Phase 11 done. A model that was never audited and a model that passed look identical otherwise.

**When `audit-xls` is unavailable** (e.g. the model was built via a custom script rather than the financial-analysis skills), run a minimal integrity self-check before declaring Phase 11 done — these are the checks that catch the silent-error class:
- **No unsubstituted placeholders**: scan the written workbook for literal `{...}` / template tokens that didn't get filled (a build-script defect that ships a broken formula looking like a value).
- **Tie-outs**: the sum of any decomposed components (segment splits, geography, cost lines) **reconciles to the disclosed total** for every historical year. A historical split that doesn't sum to the filed total is fabricated or mis-keyed — this check catches it instantly.
- **Scenario wiring**: bear/base/bull scenario cells actually **reference the lever cells** (not hardcoded copies that silently detach when the lever changes).
- **Independent recompute**: re-derive the headline metric (EBITDA / clean EPS / PT) for the base case in a separate calculation (a few lines of Python, or a checking block on a scratch tab) and **diff it against the workbook's output**. Any non-trivial gap is a formula error to find before the number leaves the model.

### Review gate before scenarios — show the assumptions + pillar→driver map, then pause

Phase 11 is a HEAVY phase (SKILL.md Principle 2). The single most common failure mode in practice is wiring up scenarios and sensitivities on top of assumptions the user has not yet seen — and then discovering, three rounds later, that a base assumption was wrong or that a pillar "can't be seen in the model." Pre-empt it:

Once Step 2 (assumptions) and Step 3 (base valuation) are done — **before building the sensitivity / bull-base-bear machinery** — render the **populated assumptions sheet (with its Notes column) and the pillar→driver map**, and explicitly pause for review ("here are the drivers and where each pillar feeds in — review before I wire scenarios"). Do not present a finished six-scenario model as a fait accompli when the base inputs were never inspected. This is the in-phase application of the "show me before you edit" discipline.

### Step 4 — Build sensitivity sheet

- Two-way data tables on top 2 swing assumptions
- **Table mechanics** (benchmark convention): odd dimensions (5×5 standard) so the **center cell is the base case** — bold it; every cell recalculates from its row/column headers as a live formula (no linear interpolation, no hand-typed values). Applies equally on the default forward-multiple path (multiple × driver flex).
- Tornado chart with the flex ranges above
- Probability-weighted target (optional): assign rough probability to a +1σ / -1σ scenario, compute weighted target

### Step 5 — Compute the Bull / Base / Bear envelope (asymmetric payoff)

**Important framing**: this is *not* three parallel theses. The committed direction (Phase 7) IS the **base case**. Bull and Bear are the **payoff envelope around that single committed view** — what does the same thesis look like if it overshoots vs under-delivers? This is what buy-side / interview audiences mean when they ask "what's your risk/reward."

From the same model, flex the **top 2-3 tornado swing assumptions** (the load-bearing ones) in each direction:

- **Bull case (pillars-fire)**: flex top swing assumptions to +1σ / favorable end. What does the target look like if your pillars deliver more / faster than your central expectation? (E.g., GM expansion accelerates to 200bps/yr vs 130bps in base; Marketplace adoption faster; etc.)
- **Base case (your committed view)**: the central target from the model as built. This is your committed direction's target.
- **Bear case (pillars-fail / steel-man-realizes)**: flex top swing assumptions to -1σ / unfavorable end, AND let the Phase 9 steel-man counter-pillars partially materialize. (E.g., AI capex extends another year; ad-supp segment GM resolves bearish; tax normalizes to top of range; etc.)

The bull and bear are anchored to the **pillars and counter-pillars** you've already built — not invented scenarios. Each bull/bear should have a 1-line trigger linking it to specific pillars/risks.

#### When the central driver is a discrete / phased event, build scenarios from the real outcome distribution — not a symmetric ±1σ flex

The mechanical "flex the top assumptions ±1σ" works for *continuous* drivers (growth, margin). It is the **wrong construction when the thesis turns on a discrete or phased event** — a regulatory ruling, a litigation outcome, a contract renewal, a capacity ramp, a binary launch. For those, σ is meaningless; what matters is the *distribution of real-world outcomes*, which is usually **asymmetric** and often **phased in over the forecast horizon**:

- **Set scenario values from the outcome distribution, not symmetry.** If the adverse outcome is *known to happen* and the only question is severity (e.g. a penalty that will land), the **base must price the expected outcome**, the **bull is "no worse than today" not "better than today,"** and the bear is the severe version. Do not reflexively centre the bull and bear symmetrically around base — ask "what does each tail actually look like?"
- **Phase the driver in if the event is mid-flight.** A driver tied to an event already in motion does not step instantly to steady state at FY+1 — it **glides** (e.g. a half-elapsed year gets a partial hit; steady state arrives a year later). Model the glide path across the forecast years explicitly; an instant step over-states the near-year impact and mis-times the catalyst.
- **Name the transmission mechanism** for the lever (how the event actually reaches the P&L line — which cap, which rate, which volume), as a Notes row. A scenario value with no stated mechanism is a guess.

#### The bear must reflect the bear *narrative* — including the multiple

- **Let the bear multiple go where the bear story goes.** A bear that only modestly de-rates the multiple manufactures a falsely favorable skew. If the bear narrative is *structural* (the franchise is impaired, the re-rate never comes), the bear multiple can sit **below the historical trough**, toward distressed-peer levels — not pinned at the 5-year low. The multiple is part of the scenario, not a constant.
- **Two-tier bear.** Distinguish the **modeled bear** (the in-model scenario: the load-bearing pillars fail / the event resolves adverse) from a **tail / combined bear** (several independent risks hit together — e.g. the regulatory outcome *and* competitive share loss *and* FX). Carry both; decide deliberately which to headline. The honest headline bear is usually the **combined** one, because a reader's real question is "how bad if more than one thing goes wrong," not "how bad if exactly one does."

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

Phase 11 must produce a **single source of truth** for all valuation outputs that every downstream document (Phase 12 iteration log, Phase 13 memo, killing conditions check) reads from. Manual transcription of PT / bull / bear / applied multiple (or WACC, on the DCF path) across multiple markdown files causes silent drift.

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
  method: "forward_multiple"          # Step-0 gate — forward_multiple | sotp | dcf
  # --- default-path fields (present when method is forward_multiple or sotp) ---
  multiple_type: "ev_ebitda"          # ev_ebitda | pe | both — default-path Q1
  forward_year: "FY+2"                # default-path Q2 — headline forward year (FY+1 shown as checkpoint)
  discount_back_to_12m_pt: false      # default-path Q4 — if true, discount fair value at cost of equity
  # --- DCF-path fields (present ONLY when method is dcf) ---
  fcff_sbc_addback: false             # DCF Q1
  terminal_method: "exit_multiple"    # DCF Q2 — exit_multiple | gordon | both
  discount_timing: "mid_year"         # DCF Q3 — mid_year | end_of_year
  fx_basis: "spot_at_valuation_date"  # asked on both paths

# --- Earnings basis: required whenever a P/E is applied (lead OR cross-check). ---
# The EPS the multiple multiplies must be defined, and struck on the SAME basis as the comps.
earnings_basis:
  metric: "clean_eps"                  # clean_eps | gaap_eps | adjusted_eps
  excludes: ["one_off_investment_gains", "fv_remeasurement", "impairments"]  # what's stripped out
  sbc_treatment: "expensed"            # expensed | added_back — MUST match how peer multiples are struck
  comps_basis_match: "peers quoted on non-GAAP ex-one-offs; clean EPS aligns"  # the apples-to-apples check
  fy2_clean_eps_local: 27.74

working_currency: "EUR"
output_currency: "USD"
fx_rate:
  pair: "USD_per_EUR"
  value: 1.17
  date_pulled: "YYYY-MM-DD"
  source: "[Bloomberg / FX vendor / ECB reference]"

# --- Default path (forward_multiple / sotp): applied multiple + triangulation anchors + equity bridge ---
# Present when method is forward_multiple or sotp. Omit the `wacc:` block below unless method is dcf.
applied_multiple:
  type: "ev_ebitda"                   # ev_ebitda | pe
  value: 8.5                          # the base-case applied multiple
  peer_anchor: "7.5-10.5x FY+2 EV/EBITDA (peer set, Phase 5 consensus map)"
  own_history_anchor: "5yr range 6-12x; median ~8x"
  consensus_implied_anchor: "consensus PT mean $50.7 ÷ FY+2 EBITDA ⇒ ~8.4x (notes-off); or per-bank 7.7x (UBS) to 10.7x (Barclays) if research_notes_available"
  position_rationale: "base at 8.5x ≈ peer median + slight own-history premium for backlog quality"
equity_bridge:                        # base-case bridge (EV/EBITDA path; mirror for P/E cross-check)
  forward_ebitda_local: 3100          # FY+2 EBITDA in working currency
  forward_eps_local: 4.20             # FY+2 EPS (for the P/E cross-check)
  enterprise_value_local: 26350       # forward_ebitda × applied_multiple
  net_debt_local: -2500               # negative = net cash
  minorities_local: 0
  non_core_investments_local: 900     # e.g. residual listed-stake value
  equity_value_local: 29750
  diluted_shares_m: 170
  per_share_local: 175.0
  per_share_output_ccy: 175.0         # × fx_rate if working ≠ output currency
  pe_crosscheck_per_share: 168.0      # FY+2 EPS × target P/E — reconcile to per_share above
  reconciliation_note: "EV/EBITDA $175 vs P/E $168; ~4% gap from net cash + buyback share-count shrink"

# --- DCF path only: include this block when method == dcf; otherwise omit entirely ---
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
  # Default path: flex BOTH the forward estimate AND the applied multiple.
  # (DCF path: swap applied_multiple → exit_multiple, forward_estimate → terminal EBITDA, and add wacc per scenario.)
  base:
    pt_listing_ccy: 175.0
    pt_local_ccy: 175.0
    upside_pct: 20.9
    forward_estimate_local: 3100      # FY+2 EBITDA (or EPS if P/E-led)
    applied_multiple: 8.5
    enterprise_value_local: 26350
    net_cash_local: 2500
    equity_value_local: 29750
    diluted_shares_m: 170
  bull:
    pt_listing_ccy: 238.0
    upside_pct: 64
    forward_estimate_local: 3450      # estimate beats
    applied_multiple: 9.5             # re-rate
  bear:
    pt_listing_ccy: 96.0
    upside_pct: -34
    forward_estimate_local: 2650      # estimate misses
    applied_multiple: 7.0             # de-rate

skew:
  formula: "(bull - spot) / (spot - bear)"
  value: 1.88

# --- Base vs Street: tells you whether your base is differentiated or consensus-hugging. ---
# Under Mode A (research_notes_available: false) cite ONLY the headline consensus revenue / OI / EPS
# and headline consensus PT — never a more granular "the Street models X" claim.
vs_consensus:
  forward_year: "FY+2"
  base_rev_pct: -0.036                  # base revenue vs consensus revenue
  base_oi_pct: -0.057
  base_eps_pct: -0.099
  consensus_source: "CapIQ headline consensus, [date]"
  note: "base prices the expected remedy → ~4-10% below Street by design; bull ~= at/above consensus"

tornado_top5:
  - rank: 1
    assumption: "FY+2 revenue growth"
    flex_unit: "200bps"
    pt_impact: 31
    pt_impact_pct: 18
    linked_thesis: 1
  - rank: 2
    assumption: "Applied EV/EBITDA multiple"   # DCF path: "Exit EV/EBITDA multiple"
    flex_unit: "2x"
    pt_impact: 28
    pt_impact_pct: 16
    linked_thesis: 2
  # ...
```

**Method-conditionality of the schema:**
- `method: forward_multiple | sotp` → include `applied_multiple` and `equity_bridge`; **omit the `wacc:` block**; scenarios carry `applied_multiple` + `forward_estimate_local`.
- `method: dcf` → include the `wacc:` block; scenarios carry `exit_multiple` + terminal EBITDA; `applied_multiple`/`equity_bridge` may be omitted (or kept if the multiple is run as a cross-check).

#### Step 7b — Run xlsx-vs-md consistency audit

Mechanical check before declaring Phase 11 complete:

1. **PT base, bull, bear**: read from xlsx Summary tab or named cells; confirm match to `valuation_outputs.yaml`.
2. **Forward estimate base / bull / bear** (FY+2 EBITDA or EPS — or terminal EBITDA on the DCF path): read from xlsx; confirm match.
3. **Applied multiple base / bull / bear** (or exit multiple on the DCF path): read from xlsx Sensitivity tab; confirm match.
4. **Net cash / equity bridge components** (incl. non-core investments): read from xlsx; confirm match.
5. **WACC + components** — *DCF path only*: read from xlsx WACC tab; confirm match. Skip when method is forward_multiple / sotp.
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

## Critical: pillars must show up as assumptions — in the workbook, not just the summary

Every Phase 10 surviving pillar must be findable as a specific cell or set of cells in the assumptions sheet. If a pillar isn't translatable to a model input, the pillar wasn't tight enough — flag back to Phase 10 for sharpening.

**This must be a visible in-workbook artifact, not only a markdown table in `model_summary.md`.** Put a **pillar→driver block on the Scenarios sheet**: one row per surviving pillar, with columns *[Pillar · driver line it controls · bear / base / bull value · transmission note]*. "I can't see how Pillar 1 is reflected in the model" is a real and recurring reviewer reaction — the cure is that the mapping lives *in the model the reviewer is looking at*, with the bear/base/bull driver values sitting right beside the pillar they express. The `model_summary.md` version (Step 6) is a copy of this block, not its only home.

## What this is NOT

- NOT three parallel scenario models — one model, three sensitivities
- NOT a forced DCF — the default is a forward multiple; DCF is selected only when the business genuinely fits (Step 0). When DCF *is* run on a multiple-default name, the multiple is the primary and DCF the cross-check, not the reverse
- NOT the final pitch (Phase 13)

## Common failure modes

- **Equity bridge doesn't reconcile** (default path): EV/EBITDA and P/E paths land far apart with no explanation — find the balance-sheet / tax / buyback driver of the gap, or fix a bridge-component sign.
- **Applied multiple unsupported**: the base multiple sits outside the triangulated peer / own-history / consensus-implied range with no pillar justifying the premium / discount — see Phase 12 surprise mode #2.
- **Model doesn't balance** (DCF path): run audit-xls. Fix BS first, then cash tie-out.
- **DCF terminal value > 80% of total** (DCF path): usually means explicit forecast period is too short or growth assumptions too aggressive — a strong signal the name should have been valued on a forward multiple instead. Extend forecast, temper, or revisit the Step 0 method choice.
- **Tornado has one massive bar**: see Phase 12 surprise mode #3.
- **Pillar can't be expressed as an assumption**: pillar was too vague. Kick back to Phase 10.
