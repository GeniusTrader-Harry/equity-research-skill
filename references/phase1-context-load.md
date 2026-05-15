# Phase 1 — Load Context

**Goal**: Fetch all source documents to disk, populate the per-ticker research directory, and produce a working context file for downstream phases. User must end this phase with a navigable archive of source documents AND a `working/context.md` summary.

**Execution principle**: do ALL programmatic work first; the user-blocking sell-side fetch prompt is the **last** step. This way the user can drop notes in any time before Phase 5 (when consensus map is built) without stalling Phases 2–4.

---

## Source hierarchy — which source for which data type (canonical reference)

Every subsequent phase uses this hierarchy. If two sources disagree, the **designated source for that data type** wins.

| Data need | Primary source | Why / notes |
|---|---|---|
| **Company-reported headline numbers** (rev, OI, NI, GM, EPS, FCF) | **Shareholder letter / earnings press release** | Q4 letter shows 5-year annual history in one table; 10-K / 20-F only shows 3 years (IFRS minimum). Identical numbers to filing. |
| **Company-reported KPIs** (subs, MAU, ARPU, comp sales, RPO, NRR, etc.) | **Shareholder letter** | Often KPI tables aren't even in the 10-K / 20-F; they live only in the letter. |
| **Multi-year historical trend** (5+ years) | **Q4 shareholder letter table** | Same reason — 5-year window vs. filing's 3-year window. |
| **Detailed audited cost line-items** (R&D / S&M / G&A split, COGS components) | **10-K / 20-F audited P&L** | The letter shows total operating expenses; the filing splits them. |
| **Segment-level P&L** (segment GM, segment OpEx, segment KPIs) | **10-K / 20-F segment note** | Letter shows segment revenue split only; filing has full segment P&L. |
| **Share count detail** (basic / diluted / SBC vesting / convertibles) | **10-K / 20-F equity & share-count notes** + proxy (US issuers) | Letter shows only headline diluted count. |
| **Tax notes** (effective rate, jurisdictional, deferred tax) | **10-K / 20-F tax note** | Not in the letter. |
| **Risk factors, regulatory, governance, exec comp, related parties** | **10-K / 20-F Item 3-7 + proxy (US)** | Not in the letter at all. |
| **Past-quarter actual vs. pre-print consensus** (beat/miss comparison) | **CapIQ Consensus xlsx** (both Actual and Median rows from one file) | The xlsx has both columns in one place; pulling actual from one source and consensus from another creates noise. Use CapIQ's own Actuals row. |
| **Next-quarter guide vs. Street consensus** | **Web search** (Reuters, FT, Bloomberg, Investing.com) | Press captures the Mean used in headline reactions; CapIQ Median can differ from the press consensus, sometimes meaningfully. |
| **Forward FY+1/2/3 consensus** | **CapIQ Consensus xlsx Median row** | Forward Median is the cleanest. Mean is more sensitive to outliers. |
| **Estimate revisions trend** (analyst upgrades / cuts) | **CapIQ Revisions xlsx** + sell-side notes | Both required for proper context. |
| **Trading multiples (NTM P/E, EV/EBITDA, EV/Sales)** | **CapIQ Multiples xlsx** | History going back N years; cross-check vs. peer set. |
| **Forward strategic direction, mgmt tone** | **Earnings call transcript** + investor day deck | Qualitative only — never use for numerical claims. |
| **Sell-side rating distribution, analyst PTs** | **Sell-side note headlines** | CapIQ Consensus xlsx aggregates but doesn't disclose individual targets. |
| **Industry sizing (TAM, growth rate, share)** | **Industry primer notes** (sell-side) + third-party (IFPI, IDC, Gartner) | Mgmt's own TAM is usually inflated; cross-check. |
| **Real-time price, market cap, 52-wk range, YTD performance** | **Yahoo Finance v8 endpoint** | Free + reliable for OHLC. |
| **Language drift in risk factors year-over-year** | **10-K / 20-F diff** (FYn vs. FYn-1) | Captures shifts in mgmt's articulated risk framing — often the cleanest signal of what mgmt is now worrying about. |

**Critical anti-error rule**: **Always re-pull headline anchor numbers (rev, OI, NI, subs, MAU) from the latest shareholder letter at the start of any phase that uses them.** If the most recent fiscal year just closed (e.g., FY25 results just released), the FY24 numbers you saw last week are now one year stale — and using them as if they were FY25 will corrupt every downstream growth-rate computation. Year-shift is the most common silent data error in this workflow.

## Step 0 — Detect available capabilities

At Phase 1 start, check whether the optional browser-automation MCP is connected (greatly improves anti-bot IR-site access):

```python
# Pseudocode — uses mcp__Claude_in_Chrome__list_connected_browsers if available
browsers = mcp.list_connected_browsers()
chrome_mcp_available = len(browsers) > 0
```

Record the capability in `working/context.md`. If unavailable, the workflow still functions — IR site PDFs sometimes have direct CDN URLs that bypass anti-bot, and the user can always manually fetch and drop into `ir-materials/`.

## Step 1 — Set up directory structure

Create the directory at `~/Claude Projects/Equity Research/[TICKER]/` with these subdirectories:

```bash
mkdir -p "$HOME/Claude Projects/Equity Research/[TICKER]"/{filings,transcripts,ir-materials,sell-side,extractions,working,deliverables}
```

If the ticker directory already exists from a prior session, ask the user: *"I see existing research for [TICKER] from [date]. Refresh sources, or load existing context?"*

**Note on `extractions/` subdirectory**: This directory is populated by **Phase 2 Step 0** (read the 20-F / 10-K and produce structured extractions), not by Phase 1. Phase 1's purpose is staging — fetching raw documents to disk. Phase 2 does the first substantive reading and produces `extractions/20F_extraction.md` + `extractions/headline_anchors.md` before drafting the Company Brief.

## Step 2 — Identify issuer type and fetch SEC filings

**First: identify whether the company is a US domestic issuer or a foreign private issuer (FPI).** This determines the filing types to pull.

### EDGAR access requirements

SEC EDGAR fair-access policy requires:
- **User-Agent header** with name + email (e.g., `"Your Name your.email@example.com"`). Requests without this can be rate-limited or 403'd.
- **Rate limit: 10 requests/sec per IP**. For batch downloads, parallelize sensibly (4–8 in flight is safe).

```bash
# Identify issuer type
curl -s -A "[Name] [email]" "https://data.sec.gov/submissions/CIK[10-digit-CIK].json"
```

The response includes `name`, `tickers`, and recent `filings.recent.form`. If you see 20-F / 6-K instead of 10-K / 10-Q, the company is an FPI.

### US domestic issuer

Fetch:
- **Last 3 years of 10-Ks** → `filings/10K_FY{year}.htm`
- **Last 4 quarters of 10-Qs** → `filings/10Q_{quarter}_FY{year}.htm`
- **Last 2 proxies (DEF 14A)** → `filings/DEF14A_FY{year}.htm` — for executive comp, board composition, insider ownership

### Foreign private issuer (FPI)

Common for non-US companies listed in the US (e.g., Spotify [Luxembourg], Alibaba [Cayman], ASML [Netherlands]).

Fetch:
- **Last 3 years of 20-Fs** (annual reports — usually 200–300 pages, denser than 10-Ks; combine financial + governance + risk in one doc) → `filings/20F_FY{year}.htm`
- **Last 4–5 quarterly earnings 6-Ks** → `filings/6K_{quarter}_FY{year}.htm` (or saved to `transcripts/shareholder_letter_{quarter}_FY{year}.htm` since they typically ARE the shareholder letter)
- **No DEF 14A equivalent** — governance disclosure is embedded in the 20-F. Don't waste cycles looking for proxies.
- **Currency convention** — see "Currency for FPIs" subsection below.

### Currency for FPIs

FPIs report financials in their home currency. **Analysis and model work in reporting currency; final target price expressed in listing currency**. See Phase 11 spec for the full convention and convention table — Phase 1 outputs should record both currencies in `working/context.md` and propagate downstream.

Conversion convention (for stating the target in the listing currency):
- Historical P&L items: average period exchange rate
- Historical balance-sheet items: period-end exchange rate
- Projections: use current spot for the base case

Note: this translation is mechanical bookkeeping, not a thesis driver. **FX as a tornado sensitivity is a separate question** — only included when there's a real economic FX mismatch (revenue currency mix ≠ cost currency mix, or material revenue in a currency other than the modeling currency). See Phase 11 spec for assessment rules and examples.

Record both reporting currency and modeling currency in `working/context.md`. This must propagate to Phase 11 model.

### 6-K exhibit pattern (FPI quirk)

**Important**: many FPIs file 6-Ks as a thin wrapper (~10 KB) + an `ex99-*.htm` exhibit (50–100 KB+) that holds the actual content. A naïve download of the primary document returns only the wrapper.

Workflow:
1. Pull the accession index: `https://www.sec.gov/Archives/edgar/data/{CIK}/{accession-no-dashes}/index.json`
2. Inspect items. If the primary `.htm` is <20 KB and there's an `ex99-1.htm` ≥50 KB, download the exhibit.
3. The exhibit is usually the Shareholder Update / earnings press release / investor letter.
4. Save both for completeness: `filings/6K_{quarter}_FY{year}.htm` (wrapper) and `transcripts/shareholder_letter_{quarter}_FY{year}.htm` (exhibit).

### File format

Save as **`.htm`** (the format EDGAR serves). PDF conversion is optional and unnecessary — Read tool reads HTML fine, and the inline formatting / hyperlinks are preserved.

### Storage

Store EDGAR filing URLs in `working/source_index.md` with date-fetched timestamps so future-you can re-pull if needed. (This file is a formal Phase 1 output — see Step 8.)

## Step 3 — Fetch earnings call transcripts

Pull **last 4 earnings call transcripts** into `transcripts/`:

```
transcripts/earnings_call_{quarter}_FY{year}.htm
```

### Sources (in priority order)

1. **Motley Fool** (`fool.com/earnings/call-transcripts/...`) — **best free source**, full transcripts, no paywall, works for most US-listed names including FPIs (e.g., Spotify, Alibaba, ASML)
2. **Company IR site** — sometimes hosts official transcripts (rare; more common for European names)
3. **Seeking Alpha** — full transcripts paywalled; partial previews accessible. Their site has anti-bot protection (403 on naïve curl) — use only via Chrome MCP if user has a logged-in session
4. **AlphaStreet** — coverage is hit-or-miss; check if Motley Fool fails

### Finding Motley Fool URLs

Direct guessing rarely works (URL slugs vary). Use a search engine:

```bash
curl -sL -A "Mozilla/5.0" "https://html.duckduckgo.com/html/?q=site:fool.com+[ticker]+earnings+call+transcript+[year]" \
  | grep -oE 'fool\.com/earnings/call-transcripts/[^"<>]*'
```

DuckDuckGo's HTML search avoids the JavaScript-only block on Google. Returns the slugged URLs you can then fetch directly.

### When transcripts don't exist

Some companies (rare, mostly small-caps or specific Asian ADRs) don't have public call transcripts. Note in `context.md` and rely on the shareholder letter / 6-K exhibit captured in Step 2 as the substitute.

If user has Bloomberg/Refinitiv access, those have higher-quality transcripts. Note this and offer the manual-fetch workflow (Step 5 pattern) as an alternative.

## Step 4 — Fetch IR materials and produce language diff

Target outputs in `ir-materials/`:
- **Quarterly Shareholder Decks** (FPIs and some US issuers) → `Q{n}-{year}-Shareholder-Deck.pdf` — typically hosted on the Q4 Inc. CDN (`s29.q4cdn.com/{CIK}/files/doc_financials/...`)
- **Most recent investor day deck** → `investor_day_{year}.pdf`
- **Latest earnings deck** → `q{quarter}_fy{year}_earnings_deck.pdf` (sometimes embedded as JPG slides in the corresponding 6-K accession for FPIs)

### Anti-bot blocks on IR sites — fallback ladder

Most institutional IR sites (Spotify, Unilever, etc.) return **HTTP 403** to naïve curl due to anti-bot protection (Akamai, Cloudflare Bot Manager). Fallback options in order:

1. **Chrome MCP** (`mcp__Claude_in_Chrome__*`) — if connected (Step 0). Uses the user's real, logged-in Chrome session — no anti-bot 403. Navigate to the IR page, extract PDF URLs via `read_page` (filter `interactive`), then curl the URLs directly (they typically resolve to public CDNs like `s29.q4cdn.com`).
2. **Direct CDN guessing** — once you know one IR-PDF URL pattern (e.g., `s29.q4cdn.com/{number}/files/doc_financials/{year}/q{n}/Q{n}-{year}-Shareholder-Deck-FINAL.pdf`), the same pattern usually works for older quarters. Curl directly.
3. **Embedded materials in SEC filings** — investor day or earnings deck slides are sometimes filed as JPG/PNG exhibits inside the related 6-K. Pull from EDGAR `index.json` (Step 2 exhibit pattern).
4. **Playwright with `channel='chrome'`** — if Chrome MCP isn't available, fall back to Playwright using the user's Chrome profile.
5. **Manual fetch fallback** — prompt user to visit IR site, save PDFs, drop into `ir-materials/`. Same pattern as Step 5 sell-side workflow.

### Image-only slides — OCR considerations

When slides are filed as JPG/PNG images (e.g., FPI 6-K exhibits), the content is rendered pixels, not searchable text. Behavior:
- **Default**: skip image-only slides if a parallel text source exists (shareholder letter HTML, earnings call transcript). The text usually has the same numbers.
- **OCR**: only run OCR (e.g., Tesseract) if no parallel text source exists. Flag for the user when this happens — manual review of the images may be faster than OCR.

### Annual report language diff

Produce a markdown diff between the most recent annual filing (10-K or 20-F) and the prior year, saved to `ir-materials/AR_language_diff.md` (use `AR_` prefix to be issuer-agnostic).

**Two depth tiers:**

| Tier | Scope | Effort |
|---|---|---|
| **Quick** (default) | Risk-factor sub-heading diff (additions, removals, rephrasings). Captures the highest-signal structural changes. | Single Python pass with regex on bold/italic headers; ~30 seconds. |
| **Deep** (opt-in) | Full text diff of Item 5 MD&A + Critical Accounting Estimates + Segment Reporting sections. Captures narrative shifts that don't show up as heading changes. | Requires text extraction + diffing; ~5 minutes. Use when Quick tier surfaces something worth digging into. |

Quick tier output structure:

```markdown
## Risks REMOVED — implicitly bullish/bearish
[heading text + brief why-it-matters]

## Risks ADDED — newly flagged
[heading text + brief why-it-matters]

## Quantitative summary
| | FY[Y-1] | FY[Y] |
|---|---|---|
| Total headings | N | M |
| Carried over | X | X |
| Added | — | A |
| Removed/rephrased | R | — |
```

**The language diff is itself a signal** — what management added or removed often telegraphs concerns or strategic shifts before they appear in numbers.

## Step 5 — Pull market data

### Working endpoint (as of 2026)

Yahoo's `/v7/finance/quote` is deprecated and returns "Unauthorized." Use the chart endpoint instead:

```bash
curl -s "https://query1.finance.yahoo.com/v8/finance/chart/[TICKER]?interval=1d&range=2y" \
  -H "User-Agent: Mozilla/5.0"
```

The `meta` object carries `regularMarketPrice`, `currency`, `fiftyTwoWeekHigh`, `fiftyTwoWeekLow`, `regularMarketDayLow/High`, `regularMarketVolume`. The `timestamp` + `indicators.quote[0].close` arrays give the trailing close series — use to compute YTD/1Y/3Y returns.

### Fallback list if Yahoo v8 fails

| Source | Use case | Notes |
|---|---|---|
| **Stooq.com** | Free OHLC CSV | `https://stooq.com/q/d/?s=[ticker].us&d1=YYYYMMDD&d2=YYYYMMDD&i=d` |
| **Google Finance** | Real-time quote | Scrape via Chrome MCP if needed |
| **TradingView** | Charting + metrics | Requires Chrome MCP |
| **Bloomberg/Refinitiv** | Authoritative if user has access | Manual fetch |

### Data to capture

- Current price, market cap, shares outstanding
- 52-week range, YTD performance, 1Y / 3Y / 5Y returns, position in 52w range
- Forward P/E, EV/EBITDA, P/Sales (consensus-based, may need Phase 5 data to fill)
- Street consensus revenue and EPS for next 3 fiscal years (from sell-side if available; from Yahoo/Substack if not)
- Recent rating changes (last 90 days)
- Short interest as % of float

Save to `working/market_data.md`.

### Setup flag

If the stock is in significant drawdown (e.g., >25% off 52w high) or near 52w high after a big run, **flag this in `context.md`** as a setup signal that will shape the Phase 7 direction commit.

## Step 6 — Produce `working/source_index.md`

Audit-trail file listing every source fetched, with date-fetched timestamps, paths, and URLs. Structure:

```markdown
# [TICKER] — Source Index
Date fetched: [YYYY-MM-DD]

## SEC EDGAR filings (filings/)
| Form | Period | Filed | Path | URL |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Shareholder letters / 6-Ks (transcripts/)
[same table format]

## Earnings call transcripts (transcripts/)
[same]

## IR materials (ir-materials/)
[same]

## Sell-side notes (sell-side/)
PENDING USER MANUAL FETCH — see Phase 1 Step 8.

## Market data
working/market_data.md populated [date] from [source].
```

This file is the authoritative record of what was loaded and from where. Future re-runs check this to decide what's stale.

## Step 7 — Produce initial `working/context.md`

This is a **raw working store**, not a readable narrative (Phase 2 produces the readable Company Brief). Structure:

```markdown
# [TICKER] — Context Load Summary
Date: [YYYY-MM-DD]
Issuer type: [US domestic / Foreign private issuer ({country})]
Reporting currency: [USD / EUR / etc.]
Model currency (per Phase 11): [USD / EUR / etc.]
Chrome MCP available: [yes/no]

## Source documents
- Filings: [list with paths and filing dates]
- Transcripts: [list]
- Shareholder letters (FPI only): [list]
- IR materials: [list, including any gaps from IR site blocks]
- Sell-side notes: PENDING MANUAL FETCH (see Step 8) or "free aggregators only"

## Market snapshot
[from Step 5 — include drawdown/run flag]

## Annual report language drift highlights
[3–5 most material changes from the language diff]

## Notable items flagged for later phases
- [e.g., "Mgmt changed CFO Q3 FY25 — will affect mgmt assessment in Phase 2"]
- [e.g., "Risk factors added new section on AI substitution Q4 FY24 — flag for Phase 6 asymmetry hunt"]
- [e.g., "Stock off 46% from 52w high — major setup signal for Phase 7"]
```

`context.md` will be updated again after Step 8 to record sell-side notes.

## Step 8 — Sell-side notes (user-fetch workflow)

**This is now the last step before the Q&A interlude.** All programmatic work is done; the user-blocking pause is at the end so it doesn't stall earlier work.

**Critical**: do NOT attempt programmatic access to CapIQ, Bloomberg, FactSet, or other paywalled research platforms — even via Chrome MCP. Their TOS explicitly prohibits automated/scripted access, and the user risks losing their subscription (and possibly their institutional access). Chrome MCP can technically drive these sites, but doing so crosses the TOS line. Use Chrome MCP for public/personal-sub sources only (FT, WSJ, Substack, IR sites). Manual fetch is the right pattern for institutional research platforms.

Instead, prompt the user with this exact workflow:

> "Programmatic Phase 1 work is complete. Source archive at `~/Claude Projects/Equity Research/[TICKER]/`.
>
> One remaining manual step: please log into CapIQ (or Bloomberg / FactSet / your institutional library equivalents) and download the following into `~/Claude Projects/Equity Research/[TICKER]/sell-side/`. Save research as PDFs and data screens as PDF/PNG exports.
>
> **Research notes**:
>
> | Item | Time window | Notes |
> |---|---|---|
> | 1–2 **initiation reports** | Most recent available, regardless of age (prefer ≤5y old). | Frameworks don't go stale fast. **Important**: CapIQ's "Initiation of Coverage" filter often mis-labels short update notes as initiations. Real initiations are typically **30–80 pages**. Filter by page count and remove date filters to find actual full-length initiations. |
> | 2–3 **regular update notes** | **Last 60–90 days** (post most recent earnings event). | Update notes show current Street thinking. Use Report Type = "Comprehensive Report" or "Equity Research Report" — NOT "Initiation of Coverage" which catches short notes. |
> | 1 **industry primer / deep-dive** | Any age; prefer last 3 years. | Frameworks. Older OK if industry hasn't structurally changed. |
>
> Sector-specific bank coverage priorities — see table below.
>
> **Data exports — be explicit about time periods, metrics, and currency**:
>
> | Item | Time window | Metrics | Currency | Where in CapIQ |
> |---|---|---|---|---|
> | **Consensus estimates** | **From most-recent reported quarter through FY+3 quarterly** (e.g., FQ1 2025 → FQ2 2028+). The historical quarters carry pre-print Median which is needed for Phase 2 § 1b past-quarter beat/miss. Forward quarters drive Phase 5 driver consensus map. | revenue, EPS Normalized + GAAP, **EBIT (Operating Income)**, EBITDA, FCF, gross margin, sector-specific KPIs (e.g., MAU, subs, GMV, RPO). Include high/median/low + # of estimates. | **Reporting currency** (EUR for SPOT, not USD) | Estimates tab → export; under export options set Currency = Reporting |
> | **Estimate revisions trend** | Both **30-day** AND **90-day** snapshots | up/down revision counts on revenue + EPS | Reporting | Estimates → Revisions |
> | **Comps trading multiples** | As of today | NTM P/E, EV/EBITDA, P/S, FCF yield + 3-yr fwd growth rates for peer set | USD (cleanest for cross-peer comparison) | Trading Multiples / Comparables tab |
> | **Own multiple history** | **Last 5 years** | NTM P/E AND EV/EBITDA (whichever is more meaningful for the sector) | USD | Trading Multiples → Historical |
>
> Note: industry-level sizing data (TAM, market share by player, growth rates) is NOT cleanly available from CapIQ's tabs — those are financial-data-aggregated-by-GICS, not consumer-industry sizing. Get industry sizing from (a) the industry primer / deep-dive note above, (b) free public sources like IFPI Global Music Report / IDC / Gartner / OECD, (c) the company's own annual filing Item 1 (US) or Item 4 (FPI), (d) Substack analysts for the sector. Skill can grab these autonomously — no manual fetch needed.
>
> Tell me 'done' when you've saved the files, 'skip' to proceed without notes (I'll fall back to free aggregators), or 'defer' if you want to do this later before Phase 5."

### What counts as a "real" initiation vs. a mislabeled short note

CapIQ's "Initiation of Coverage" filter is unreliable — many post-event recaps, debriefs, and invites get tagged as initiations. Quality signals:

| Signal | Real initiation | Mislabeled short note |
|---|---|---|
| Page count | 30–80 pages | ≤15 pages |
| Title pattern | "Initiating Coverage at [Rating]; [Company] is [thesis]" | "Q[N] Recap", "Equity Snap", "Invite:", "Reminder:" |
| Bank | Bulge bracket or substantive specialty firm | Same banks may also file short notes |
| Content | Full thesis, framework, business deep-dive, model | Single event commentary |

Filter by page count (>30) to surface the real ones.

### Sector-specific bank coverage priorities

When user asks which banks to prioritize, default to:

| Sector | Top 3 most active |
|---|---|
| Mega-cap tech | GS, MS, JPM |
| Software / SaaS | MS, GS, JPM, Barclays |
| Semis | MS, JPM, BofA, Cantor |
| Consumer / retail | GS, Citi, JPM, Barclays |
| Financials | GS, JPM, Wells Fargo, MS |
| Healthcare / biotech | GS, MS, Cowen, Jefferies |
| Energy | GS, JPM, RBC, BofA |
| Media / streaming (e.g., SPOT, NFLX) | MS, JPM, GS |
| Industrials | GS, MS, Citi, Barclays |

Bloomberg's consensus tab shows which analysts are most active per name — defer to that when in doubt.

**While waiting, accept user questions** — this is part of the Q&A interlude principle. Common questions:
- *"What's the difference between an initiation and an update?"* — Initiations are first-time coverage reports (deeper, ~30–80 pages, full thesis + framework). Updates are shorter (~5–15 pages, post-earnings or event-driven).
- *"Which banks should I prioritize?"* — Prefer the banks that have the most active sector coverage. For mega-cap tech: GS, MS, JPM. For consumer: GS, Citi, JPM. For semis: MS, JPM, BofA. For financials: GS, JPM, Wells Fargo. Bloomberg's consensus tab shows which analysts are most active.
- *"What if there's no recent initiation?"* — Common for large-cap names. Skip the initiation step and pull 3–4 update notes instead.
- *"How do I find the industry primer?"* — In CapIQ, search under "Research" → filter by "Industry Reports" or search the company's industry name.

When user says "done":
- List files in `sell-side/`, update `context.md` and `source_index.md`
- Reply: *"Found N notes: [filenames with bank + type + date]."*

When user says "skip":
- Fall back to free aggregators (Step 9) and note the limitation in `context.md`.

When user says "defer":
- Proceed to Phase 2. Re-prompt at start of Phase 5 (or earlier if user supplies notes).

## Step 9 — Free aggregator fallback (only if user skipped sell-side)

Gather free Street view from:
- **Seeking Alpha** — analyst price target distribution, ratings, summary blurbs (page is anti-bot; use Chrome MCP if connected)
- **Yahoo Finance** — aggregated price targets, rating distribution, recent revisions
- **StreetAccount** (free tier) — recent headlines and brief summaries
- **Substack analysts** for the relevant sector:
  - Semis: Doug O'Laughlin (Fabricated Knowledge)
  - Tech / value: Modest Proposal
  - Financials: Net Interest
  - Generalist: Fundamental Edge
- **Twitter/X $-tags** — directional sentiment, particularly for short-term setups

Save raw aggregator content as `sell-side/aggregator_summary.md`. Flag in `context.md` that "Street view based on aggregated sources only; full notes unavailable."

## Step 10 — Q&A interlude

Pause with:

> "Phase 1 complete. Source archive at `~/Claude Projects/Equity Research/[TICKER]/`. Working summary at `working/context.md`. You can browse the source documents directly. Ask any question about what was loaded, or say 'continue' to advance to Phase 2 (Company Brief)."

Wait for user response. If user has questions, answer with citations to the source files. When user says continue, advance to Phase 2.

---

## Failure modes to handle

- **Filing not on EDGAR**: company may be FPI (20-F instead of 10-K — see Step 2 FPI section) or delisted. Pull what's available; note gap in `context.md`.
- **6-K wrapper without content**: most FPIs use ex99-* exhibits. Always inspect the accession `index.json` and pull the largest `.htm` exhibit if the primary doc is <20 KB.
- **Transcript paywalled**: Seeking Alpha is the common offender. Use Motley Fool first (almost always free), fall back to user manual-fetch or Chrome MCP if needed.
- **Anti-bot 403 on IR site**: standard for institutional IR sites (Akamai/Cloudflare). Use the Step 4 fallback ladder (Chrome MCP → CDN guess → 6-K exhibits → Playwright → manual fetch).
- **Yahoo v7 endpoint returns Unauthorized**: use v8 chart endpoint (Step 5). If v8 fails, use Stooq or Chrome-MCP scrape.
- **No 4 quarters available**: company may be newly public. Pull what exists, note in `context.md`.
- **Non-USD reporting currency**: flag in `context.md` (Reporting / Model currency) and propagate to Phase 11 model. Conversion convention: average rate for P&L, period-end for B/S. FX as a sensitivity input.
- **EDGAR rate limit**: 10 req/sec per IP. For batch downloads, parallelize ≤8 in flight. Honor User-Agent header (name + email).
- **Image-only slides**: skip if parallel text source exists; OCR only as last resort. Flag for user.
