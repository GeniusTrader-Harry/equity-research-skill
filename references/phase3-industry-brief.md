# Phase 3 — Industry Brief

**Goal**: Produce an industry / competitive landscape synthesis that situates the company in its market. This is where moats, competitive position, and structural tailwinds/headwinds are described — all of which feed Phases 4–7.

> **Length principle:** word counts in this spec are **indicative only — never a cap**. Completeness first; never drop material content to hit a length.

**Output**: `working/industry_brief.md`

Citation discipline applies to every numeric claim in this phase's output: `[source, p.N]` / `[source]` / `[est, not disclosed]`, validated by `scripts/validate_citations.py` before saving — see SKILL.md "Important behaviors".

## Structure

Four sections. Cite every quantitative claim.

### Section 1 — Market size & structure (~400 words)

- **Industry definition**: what market is this company in? Be precise. "Cloud software" is too broad; "data warehousing" is better. Include adjacencies the company plays in.
- **TAM**: total addressable market with source (Gartner, Forrester, IDC, mgmt's own framing). Note when sources disagree.
  - Note: TAM estimates from sell-side and management are usually inflated. Triangulate with Gartner/IDC if possible.
- **Growth rate**: industry historical 5yr CAGR + projected forward CAGR with source
- **Segmentation**: by product type, geography, end market, customer size. Use a table.
- **Structure**: fragmented vs. consolidated. Top 5 market share. HHI if relevant for regulated industries.
- **Value chain**: where in the value chain does the company play? Who are upstream suppliers, downstream customers, complementors?
- **Cite**: industry primer (if user fetched), 10-K Item 1, sell-side industry reports, third-party research firms

### Section 2 — Competitive landscape (~600 words)

This is the most important section. The user needs to understand who the company competes against and how.

**5–8 key competitors** — for each:
- Name and brief description
- Direct or indirect competitor (and on which products/segments)
- Approximate revenue (or market cap if private)
- Estimated market share or relative position
- Key strengths vs. the company
- Key weaknesses vs. the company

**Use a comparison table** with rows = competitors, columns = ($ revenue / market share / key strengths / key weaknesses).

**Then narrative analysis**:
- Who's the company's #1 threat and why?
- Where does the company have clear advantage? Clear disadvantage?
- Are competitors converging (everyone moving toward same product) or diverging?
- New entrants worth flagging? Big tech / startups / international players?

**Moats**: identify which apply, with evidence:
- Network effects (e.g., marketplace, social platform)
- Switching costs (e.g., enterprise software contracts, data lock-in)
- Cost advantages (e.g., scale, geographic, regulatory)
- Brand / consumer mindshare
- Distribution / shelf space
- Patents / IP
- Regulatory moats (licensed industries)

For each moat, rate: Wide / Narrow / None — and **state the evidence** (don't just assert).

### Section 3 — Trends & drivers (~400 words)

- **Secular tailwinds (2–4)**: long-duration trends pushing the industry up. Be specific (not "AI" — say "enterprise inference compute scaling with token consumption").
- **Secular headwinds (2–3)**: structural pressures. E.g., commoditization, deflation, regulatory tightening, substitution risk.
- **Cyclical position**: where in the cycle? Early / mid / late? Last cycle peak/trough.
- **Regulatory environment**: relevant regulators, recent rule changes, pending rule changes, antitrust risk.
- **Technology shifts**: any disruptive tech reshaping the industry (e.g., AI, blockchain, energy transition)?
- **Cite**: industry primer, sell-side notes, 10-K risk factors, recent press, regulatory dockets

### Section 4 — Where the company sits (~300 words)

- **Positioning vs. competitors**: leader / challenger / niche / laggard? On which dimensions?
- **Value chain location**: where in the chain? Upstream commodity exposure or downstream consumer-facing?
- **Pricing power**: high (low-elasticity demand, high switching costs) / medium / low (commodity-like). Evidence?
- **Defensibility**: how hard is this position to dislodge over 5 years? What would a successful attack look like?
- **Strategic chokepoints**: any single point of failure? (e.g., one customer = 30% of revenue, one supplier = sole source of key input, one regulator decision = existential)

## Sources for industry data

In priority order:
1. **Sell-side industry primers** in `sell-side/` (best — most current and most analytical) — *only if `research_notes_available: true`*; under Mode A skip to 2–7 and use `working/street_view.md` for the Street layer
2. **The company's own 10-K Item 1 / 20-F Item 4** — companies disclose competitors and industry framing
3. **Competitor 10-Ks** — useful for cross-checking market share claims
4. **Gartner / Forrester / IDC** via web search (often paywalled, but headline numbers are usually free)
5. **Trade publications**: e.g., Semiconductor Engineering for semis, Modern Healthcare for health, etc.
6. **Substack analysts** for the relevant sector
7. **University or workplace library subscriptions** if user has accessed: Bloomberg's BI sector research, Refinitiv industry reports

If multiple sources disagree (common for TAM): show the range and pick a sensible midpoint, noting the spread.

## Q&A interlude (HEAVY)

After producing the brief, prompt:

> "Phase 3 complete. Industry Brief at `working/industry_brief.md`. This sets up the competitive context for the rest of the workflow. Common useful questions: who's the real threat, where does pricing power come from, what's the moat, what would disrupt this industry, why aren't more entrants in this space. Or 'continue' to Phase 4 (driver decomposition)."

Common follow-up requests:
- *"Tell me more about [competitor X]"* — extended profile, recent moves
- *"Why is the moat wide/narrow?"* — supply more evidence, be honest about counterarguments
- *"What's the worst-case scenario for the industry?"* — bear case at industry level (different from company bear case)
- *"How does this industry compare to [analogous industry]?"* — pattern matching to historical cycles or other markets

When user says continue, advance to Phase 4.

## What this is NOT

- NOT a thesis on the company (Phases 7–10)
- NOT a forecast — describe the present, not the future you're betting on
- NOT a list of every competitor — focus on the 5–8 that actually matter

Be honest about uncertainty. Industry analysis is full of estimates and judgment calls; flag when something is well-documented vs. when it's the analyst's read.
