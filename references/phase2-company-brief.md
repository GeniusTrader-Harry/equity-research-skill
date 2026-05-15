# Phase 2 — Company Brief

**Goal**: Produce a readable ~1,500–2,000 word synthesis that gives the user genuine understanding of the business. This is NOT a copy of the 10-K business description — it's a thoughtful condensation with citations.

**Output**:
- `extractions/20F_extraction.md` (or `10K_extraction.md` for US issuers) — produced in Step 0 below
- `extractions/headline_anchors.md` — produced in Step 0 below
- `working/company_brief.md` — the main synthesis output

---

## Step 0 — Structured multi-source read + produce extractions (MANDATORY, HARD GATE)

**Before drafting `working/company_brief.md`, the analyst must perform a structured multi-source read of the company's primary disclosures and produce two extraction files**:
- `extractions/20F_extraction.md` — qualitative + granular reference (3,000-5,000 words)
- `extractions/headline_anchors.md` — quantitative anchor table (the numeric backbone for Phases 4, 5, 11)

The skill orchestrator must refuse to advance past Phase 2 without both files on disk.

**Why this step exists**: in earlier iterations the analyst drafted Company Brief from memory or keyword-grep, leading to year-shifted anchors, missing segment GM, missing OpEx splits, and fabricated citations. Reading primary sources properly here prevents the entire failure mode.

### Methodology — borrow from `equity-research:initiating-coverage` Task 1

The reading methodology is taken from the **`equity-research:initiating-coverage` skill's Task 1 (Company Research)** at `~/.claude/plugins/cache/claude-for-financial-services/equity-research/0.1.0/skills/initiating-coverage/references/task1-company-research.md`. **Borrow the methodology; do NOT borrow the output structure.**

| Element of initiating-coverage Task 1 | Borrow? | Notes |
|---|---|---|
| **Sequential structured read by 10-K / 20-F section** (Item 1 → 1A → 7 → 8 → notes) | ✅ Borrow | Reading top-down catches signals keyword-grep misses |
| **Multi-source triangulation** (10-K + 10-Q + DEF 14A + 8-Ks + transcripts + IR deck + competitor filings + LinkedIn for mgmt + Gartner/IDC/industry research) | ✅ Borrow | One filing isn't enough |
| **Multi-year reading** (read FY[N] AND FY[N-1] annual filings minimum; FY[N-2] if pre-profitability or major narrative shift) | ✅ Borrow | The current-year 20-F has 3-year P&L but only 1-year MD&A narrative |
| **Structured risk taxonomy** — 4 categories (Company / Industry / Financial / Macro), 8-12 total risks, 50-100 word descriptions | ✅ Borrow | More disciplined than ad-hoc "top N" |
| **Dedicated management research step** — 300-400 word bios for CEO + CFO + 2 other key execs from DEF 14A / equivalent + LinkedIn + press interviews | ✅ Borrow | Mgmt depth otherwise gets skimmed |
| **Output structure: 9 sections × 6,000-8,000 words** | ❌ Do NOT borrow | That's the heavy initiation-report use case; this skill is thesis-first, 5-8 page memo |
| **Output format: DOCX report** | ❌ Do NOT borrow | This skill outputs markdown |
| **Linear deliverable pipeline (Task 1 → Task 2 → Task 3)** | ❌ Do NOT borrow | This skill is thesis-first: brief feeds Phase 4 + Phase 6, not a linear report |

**In one sentence**: Read with initiating-coverage Task 1's depth and breadth, but produce this skill's lean outputs (extraction reference files + 1,500-2,000 word Company Brief).

### Sub-step 0a — Sources to gather + multi-year read

**Primary (company-issued)**:
- **Latest 20-F / 10-K** (must read in full)
- **Prior-year 20-F / 10-K** (must read MD&A + Risk Factors + segment disclosures — captures narrative drift)
- **FY[N-2] 20-F / 10-K** (optional; read only if there's a major narrative inflection — pre-profitability transition, acquisition, divestiture, accounting change)
- **Last 4 quarterly filings** (10-Qs for US; 6-K shareholder letters for FPIs)
- **Latest DEF 14A** (US issuers; for FPIs there is no equivalent — use AGM convening notice, latest investor day deck, or LinkedIn for governance / mgmt comp)
- **Last 4 earnings call transcripts**
- **Most recent investor day deck** if held within 2 years

**Secondary (third-party)**:
- 2-3 key competitors' latest 10-K Item 1 / 20-F Item 4 — for competitive framing cross-check (full competitive landscape lives in Phase 3 Industry Brief; here just enough to triangulate)
- LinkedIn profiles for CEO + CFO + 2 other key execs
- Industry research firm headlines (Gartner / Forrester / IDC / IFPI / etc.) — TAM cross-check only; full industry sizing is Phase 3

**Recommended reading order**:
1. Latest 20-F Item 1 / 4 (Business overview)
2. Latest 20-F Item 1A / 3.D (Risk Factors)
3. Latest 20-F Item 7 / 5 (MD&A) — this is where the narrative lives
4. Latest 20-F Item 8 / 18 (Audited financials + footnotes) — segment note, share count, tax, leases, debt
5. **Prior-year 20-F MD&A + Risk Factors** — narrative drift check
6. Latest 4 quarterly filings (skim KPI tables; deep-read the most recent CFO commentary)
7. Latest DEF 14A (US) or equivalent — mgmt comp + insider ownership + board
8. Latest investor day deck (if recent) — mgmt's own framing of strategy & targets
9. Last 2-3 earnings call transcripts — Q&A captures Street pushback patterns

### Sub-step 0b — `extractions/20F_extraction.md` (qualitative + granular reference)

Read each section sequentially and extract both **verbatim quotes** for high-value language and **paraphrased synthesis** for context. Cite with section name + page anchor.

Internal structure of the file (borrowed from initiating-coverage Task 1's 9-section template, condensed):

| Section in extraction file | What to capture | Source |
|---|---|---|
| **1. Business overview** | Segments, products, geographic mix, customer concentration, key suppliers, IP, regulatory regime, employee count | 20-F Item 4 / 10-K Item 1 |
| **2. Risk factors** (structured 4-category taxonomy) | Company-specific risks (4-6), industry risks (3-4), financial risks (2-3), macro risks (2-3); 50-100 word body for each; flag risks added/removed/rephrased vs. prior year | 20-F Item 3.D / 10-K Item 1A; FY[N-1] 20-F for diff |
| **3. MD&A narrative** | YoY commentary on revenue, COGS, OpEx (R&D / S&M / G&A separately), margin movement, FX, capex, liquidity. **Read both FY[N] AND FY[N-1] MD&A for trajectory.** | 20-F Item 5 / 10-K Item 7 |
| **4. Audited P&L (3 years)** | Revenue, COGS, GP, R&D, S&M, G&A, OI, financial items, tax, NI, EPS basic + diluted, weighted avg shares | F-pages / Item 8 |
| **5. Segment note** | Segment revenue, segment COGS, segment GP, segment GM, segment OpEx if disclosed | F-pages segment footnote |
| **6. Share count + equity activity** | Basic shares, diluted shares, SBC charges (3 years), convertibles/warrants/options outstanding, treasury shares (buyback signal), equity changes | F-pages equity statement + relevant notes |
| **7. Tax footnote** | Effective rate, jurisdictional split, deferred tax assets/liabilities, any tax-driven one-time items | Tax note |
| **8. Lease + debt schedule** | Maturity ladders, fixed vs floating, weighted average rates, covenants | Notes |
| **9. Management** (4 bios × 300-400 words) | CEO + CFO + 2 other key execs; current role, prior roles, education, tenure, key accomplishments | DEF 14A (US) / AGM notice + LinkedIn + press interviews |
| **10. Board + governance** | Board composition, independence, insider ownership %, exec comp structure | DEF 14A / mgmt comp note |
| **11. Related party transactions** | Counterparties, $ value, nature | Related party note |
| **12. Subsequent events** | Material disclosures post fiscal year-end | Notes |
| **13. Prior-year narrative drift** | What changed in MD&A / risk factors between FY[N-1] and FY[N]? Captures management's evolving framing | Diff between FY[N-1] and FY[N] 20-Fs |

If a section is "Not applicable" or absent for this issuer, write `[N/A — not disclosed in filing]` for that row.

**Target length: 3,000-5,000 words.** This is a *reference* file, not a synthesis — density and citation discipline matter more than narrative flow.

### Sub-step 0c — `extractions/headline_anchors.md` (quantitative anchor table)

Open the **most recent Q4 shareholder letter** (or equivalent annual earnings press release for US issuers) for the 5-year history table. Combine with audited P&L line items from the 20-F. Save as a dense reference file with every line cited.

Template:

```markdown
# [TICKER] — Headline Anchors

Last updated: YYYY-MM-DD
Reporting currency: [EUR / USD / ...]
Sources:
- Q4 [YYYY] shareholder letter: `transcripts/shareholder_letter_Q4_FY[YY].htm`
- 20-F FY[YY]: `filings/20F_FY[YY].htm`
- Q[N] [YYYY] press release: `transcripts/...`

## Annual P&L history (5 years, reporting currency [€/$])

| Line (€M) | FY[N-4] | FY[N-3] | FY[N-2] | FY[N-1] | FY[N] | Source |
| (Revenue, OI, NI, EPS basic, EPS diluted, FCF, GM%, OpMargin%) |

## Segment split (latest year, with prior-year for context)

| Segment | Revenue | % of total | YoY growth | Segment GM | Source |

## KPI history (5 years)

| KPI | FY[N-4] | FY[N-3] | FY[N-2] | FY[N-1] | FY[N] | Source |
| (subs, MAU, ARPU, comp sales, NRR, RPO, etc.) |

## Last 6 quarters

| Quarter | Revenue | OI | NI | EPS | Key KPI | Source |

## Detailed FY[N] P&L from 20-F (audited)

(Lines NOT in the shareholder letter — R&D / S&M / G&A separated, plus tax, finance items)

| Line | FY[N] | % of rev | Source |

## Cash flow + capital structure

(CFO, capex, FCF, share count, SBC, debt, treasury, dividends, buybacks)
```

**Phase 4 (driver tree) opens this file first. Phase 5 (consensus map) compares Street estimates to anchor history. Phase 11 (model build) imports the 3-year history straight from this file.**

### Sub-step 0d — Hard gate check

Before proceeding to Step 1 (writing the Company Brief), verify both extraction files exist and are non-trivial:

```bash
test -f extractions/20F_extraction.md && test -f extractions/headline_anchors.md \
  && [ "$(wc -w < extractions/20F_extraction.md)" -gt 1000 ] \
  && echo "OK to proceed" || echo "MISSING or INSUFFICIENT extractions — cannot proceed"
```

If either file is missing or under 1,000 words, stop and complete Step 0 first.

---

## Structure of the Company Brief

Four sections, target word counts in parens. Cite every quantitative claim with file path and section.

### Section 1 — What & how (~400 words)

- **Plain English description**: What does the company actually do? Avoid corporate jargon. If your friend asked "what does this company do?", how would you answer in 2 sentences?
- **How they make money**: Revenue model (subscription, transaction, licensing, services, mix). Key revenue lines and what drives each.
- **Revenue mix**: by segment, geography, customer type. Use a table.
- **Scale**: revenue (current FY + 3yr CAGR), employees, customers, key operational metrics
- **Cite**: 10-K Item 1 (Business), latest 10-Q, latest earnings deck

### Section 1b — Latest quarter actuals vs consensus (mandatory)

Every Phase 2 brief MUST include a comparison table for the most recent reported quarter (actual vs pre-print consensus) AND a comparison for the next-quarter guide vs current consensus.

### Standard metrics — STRICT list (only these six; in this order)

1. **Revenue**
2. **EPS Normalized** (preferred to GAAP — Normalized strips one-time items like social charges, FX gains/losses on derivatives; only fall back to GAAP if Normalized isn't disclosed)
3. **Operating Income** (include whenever the firm reports it as a line item — most do; banks and certain financials use NII/PPNR instead)
4. **Net Income Normalized** (preferred to GAAP, same reasoning as EPS)
5. **Gross Margin**
6. **Special indicator(s) for the firm** — the operational KPIs central to the thesis. **Can be multiple — include all KPIs that matter, not just one.** Examples:
   - SPOT: Premium Subscribers EOP, MAU EOP, ARPU
   - Consumer SaaS: ARR, NRR, Net Adds, ARPU
   - Enterprise SaaS: RPO, Bookings, NRR
   - Retail: Comp sales / SSSG, Store count, AUR
   - Banks: Net Interest Income, NIM, CIR, Loan Growth, NPL ratio
   - Biotech: Pipeline milestones, R&D spend, regulatory milestones
   - Advertising: Ad revenue, impressions, eCPM
   - Semis: Wafer shipments, ASP, Utilization
   - Note: not all of these will have CapIQ consensus. For KPIs where consensus isn't separately reported (e.g., MAU for SPOT), show actual + company guidance and flag "consensus not separately reported in CapIQ."

**Do NOT include in the comparison table**:
- **EBITDA** — derivative of Operating Income; usually redundant
- **Free Cash Flow** — definitions vary widely between company-reported and CapIQ-standardized (lease treatment, working capital, capex). The consensus comparison is unreliable. **Never use CapIQ FCF for beat/miss comparison.** If management reports FCF, include the company-reported figure in the surrounding narrative as informational color, but do NOT line it up against a CapIQ Median.
- Cash EPS, Book Value, Dividend per share, etc. — not core to operational beat/miss
- Any other metrics — keep the table to exactly 6 lines for readability and discipline

### Source rules (final)

| Comparison | Source |
|---|---|
| **Past-quarter actuals vs consensus** | **CapIQ Consensus xlsx** (Median column for the relevant past quarter). Use only this. |
| **Next-quarter guide vs consensus** | **Web search**, in this tool hierarchy: (1) WebFetch / WebSearch on free press sites — Yahoo Finance, MarketWatch, MarketBeat, Investing.com, CNBC, Seeking Alpha cached, 24/7 Wall St — these typically quote pre-guide consensus in plain text; (2) Curl-based fetch (with DuckDuckGo HTML search) if WebFetch fails; (3) Chrome MCP only when paywalled/authenticated content is needed (FT, WSJ, Bloomberg.com subscriptions) or anti-bot 403s block the simpler paths. Don't default to Chrome MCP — it's the heavy hammer reserved for sites that need it. |
| **Forward (FY+1 / FY+2 / FY+3) consensus** | **CapIQ Consensus xlsx** (used in Phase 5 driver-level map). |

### Currency

Always use **reporting currency** (e.g., EUR for SPOT, EUR for ASML, CNY for many Asian FPIs). The CapIQ xlsx must be exported with **Currency = Reporting**, NOT USD. USD-translated comparisons introduce FX-translation noise that can flip the sign of a beat/miss. See Phase 11 spec for full currency convention.

### Extracting CapIQ Consensus xlsx — robust pattern (DO NOT hardcode row offsets)

CapIQ exports a multi-row block per metric with sub-statistics ("Actuals/Estimates", "Final Est." (mean), "Median", "High", "Low", "Std. Dev.", "Number of Analysts", "Accounting Standard"). The **row order within a block is not guaranteed** to be the same across exports — it depends on metric selection, version, and the export config. **Hardcoding offsets like "Median = r+3" WILL break.**

**Use label-based lookup instead**:

1. **Quarter columns**: scan a header row for "FQ1 2026"-style labels → build `quarter → column` map
2. **Metric blocks**: scan column A for metric labels (Revenue, EBIT, EBITDA, etc.) → build `metric → starting_row` map
3. **Sub-statistic rows**: within each metric block, scan downward for the explicit text labels in column A ("Median", "Final Est.", "High", "Low") → build `(metric, stat) → row` map
4. **Lookup** is then `data[metric][stat][quarter]` — entirely by name, no offsets

**Sanity checks before trusting the data**:
- Actuals for past quarters should match the company's shareholder letter (e.g., Q1 26 EBIT actual = €715M per Spotify letter — verify xlsx says the same)
- Median should sit between Low and High
- Number of Analysts should be reasonable (>5 for well-covered names)
- For FPIs, verify Currency header shows reporting currency (€) not USD ($)

**Reference implementation** (Python/openpyxl):

```python
SUB_LABELS = {'Actuals/Estimates', 'Final Est.', 'Median', 'High', 'Low',
              'Std. Dev.', 'Number of Analysts', 'Accounting Standard'}
quarter_col = {}  # 'FQ1 2026' -> column index
metrics = {}      # 'EBIT' -> {'Median': row, 'Final Est.': row, ...}
current_metric = None
for r in rows:
    label = cell(r, 1).value.strip()
    if label in SUB_LABELS and current_metric:
        metrics[current_metric][label] = r
    elif label and label not in SUB_LABELS:
        current_metric = label
        metrics[label] = {}

def lookup(metric, stat, quarter):
    return cell(metrics[metric][stat], quarter_col[quarter]).value
```

This pattern survives CapIQ format changes. **Off-by-one offset errors flip beat/miss conclusions** (e.g., reading "High" as Median makes Q1 26 EBIT consensus look like €743M when it's actually €673M — a 10% error that flips a clean beat into a soft miss).

### Table template

```markdown
## Q[N] FY[Y] — actual vs pre-print consensus (reporting currency)

| Metric | Pre-print Consensus (Median) | Actual | Beat / Miss |
|---|---|---|---|
| Revenue | [€X M] | [€X M] | [+/- X%] |
| EPS Normalized | [€X] | [€X] | [+/- X%] |
| Operating Income | [€X M] | [€X M] | [+/- X%] |
| [Unique KPI 1] | [X] | [X] | [+/- absolute] |
| [Unique KPI 2] | [X] | [X] | [+/- absolute] |
| Gross Margin | [X%] | [X%] | [+/- bps] |

Source: CapIQ Consensus xlsx (`sell-side/[file].xlsx`), Median column for FQ[N] [Y].

## Q[N+1] FY[Y] — guide vs current consensus

| Metric | Company Guide | Consensus (post-print) | Delta |
|---|---|---|---|
| Revenue | [€X M] | [€X M, source] | [+/-] |
| Operating Income | [€X M] | [€X M, source] | [+/-] |
| [Unique KPI] | [X] | [X] | [+/-] |

Sources: Q[N] FY[Y] earnings press release (guide); press coverage via Chrome MCP (consensus, e.g., Reuters article 'Spotify reports first quarter results').
```

**If consensus isn't available**: write `consensus not retrieved` in the cell — do NOT estimate or back into a beat/miss judgment from analyst commentary alone. Analyst reactions ("soft," "in-line," "beat") are useful color but not the consensus number itself.

This table is what surfaces beat/miss directly. The narrative around it (why mgmt beat / missed, market reaction logic) is layered in the relevant section. Used downstream:
- Phase 5 (consensus map) carries it forward into the per-driver consensus table
- Phase 6 (asymmetry hunt) uses guide vs consensus to detect "recent inflection" asymmetries
- Phase 7 (direction brief) Setup section references the latest print as setup color

### Section 2 — Products & customers (~400 words)

- **Product portfolio**: 3–5 main products / SKUs / segments. What does each do, who buys it, what does it cost.
- **Customer segments**: enterprise / mid-market / SMB / consumer. Industries, geographies.
- **GTM model**: direct sales / channel / self-serve / hybrid. Sales cycle. Typical deal size.
- **Customer concentration**: top 10 customers as % of revenue (from 10-K — if not disclosed, note it). Major contracts.
- **Pricing**: pricing model (per-seat, per-transaction, tiered, etc.), recent price changes, price elasticity if known
- **Cite**: 10-K Items 1 & 1A, latest investor day deck

### Section 3 — Management (~300 words)

For each of CEO, CFO, and 1–2 other key executives (e.g., COO, CRO, CTO, Chief Product, depending on what matters for this business):
- **Bio (~100w)**: current role start date, prior roles (last 2–3 companies), education
- **Track record assessment**: what did they accomplish at prior roles? Any visible failures? Key relevant experience (e.g., "led IPO at prior company," "managed $5B P&L at GE")
- **Compensation structure**: heavy equity? Long-vesting? Performance-linked? (from DEF 14A)

Plus:
- **Insider ownership**: % of shares held by insiders (DEF 14A, beneficial ownership table)
- **Board composition**: # of independent directors, diversity, any notable directors (industry experts, recent additions, ex-execs of customers/competitors)
- **Cite**: latest DEF 14A, prior DEF 14A for changes, LinkedIn for bio gaps

### Section 4 — History & recent events (~400 words)

- **Founding & history (~150w)**: founding year, founders, original business, key strategic pivots
- **Major milestones**: M&A (>$100M deals), spinoffs, dividend initiations, share buybacks, leadership transitions
- **Recent 12 months (~250w)**: what's happened? New products, layoffs, restructuring, board changes, regulatory actions, major contracts won/lost. Cite the 8-Ks and recent press.
- **Cite**: 10-K Item 1 history paragraph, 8-K filings, press releases

## Style requirements

- **Plain English first**, technical second. The user is building intuition.
- **Quantify**: every section should have at least 3 numbers with sources.
- **Honest about gaps**: if something isn't disclosed (e.g., customer concentration), say so. Don't make up estimates.
- **Cite at sentence level when possible**: e.g., *"AI segment grew 47% YoY in FY25 (10-K p.34) but margins compressed 200bps (10-K p.36)."*
- **Avoid sell-side puffery**: no "premier provider," "best-in-class," "world-class team" unless quoting management. Use neutral, descriptive language.

## Q&A interlude (HEAVY)

After producing the brief, prompt:

> "Phase 2 complete. Company Brief at `working/company_brief.md`. This is the foundation for everything downstream — please ask anything you don't understand about the business before moving on. Common useful questions: explain the unit economics, what does this segment actually sell, how does the pricing model work, who's the CEO and what's their track record, what was the strategic pivot. Or say 'continue' for Phase 3 (Industry Brief)."

Common follow-up requests to be ready for:
- *"Walk me through the revenue lines in more detail"* — drill into segments, give an example transaction
- *"What's the unit economics for this product?"* — gross margin per unit, CAC, LTV if disclosed
- *"Tell me more about the CEO"* — extended bio, prior board seats, communication style on calls
- *"What happened in [event from history section]?"* — pull more detail from 8-K or press
- *"How does this compare to [competitor]?"* — flag this is more Phase 3 territory but answer briefly

When user says continue, advance to Phase 3.

## What this section is NOT

- NOT competitive landscape (Phase 3)
- NOT industry trends (Phase 3)
- NOT a thesis or view (Phases 6–10)
- NOT a financial deep dive — high-level scale only; detailed financials come in Phase 4 (driver decomposition) and Phase 11 (model)

Keep the brief tight. If a section feels too long, cut to the essential facts.
