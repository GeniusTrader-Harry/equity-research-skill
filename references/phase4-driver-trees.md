# Phase 4 — Driver Decomposition

**Goal**: Break revenue and margin into their multiplicative drivers so downstream phases (consensus map, asymmetries, pillars) can be tied to specific levers. The driver tree is the *vocabulary* the rest of the workflow uses.

**Output**: a markdown file `working/driver_tree.md` with the customized tree.

Citation discipline applies to every numeric claim in this phase's output: `[source, p.N]` / `[source]` / `[est, not disclosed]`, validated by `scripts/validate_citations.py` before saving — see SKILL.md "Important behaviors".

## The principle

Every thesis pillar must route through a driver. So the tree must:
- Cover all material revenue and margin levers
- Use units that match how the business actually reports
- Be customized for hybrid / non-standard businesses

A wrong tree corrupts everything downstream. Spend the time to get this right.

---

## Step 0 — Open the extractions BEFORE drafting any absolute number (MANDATORY)

Open both:
- `extractions/headline_anchors.md` (5-year P&L + KPI history)
- `extractions/20F_extraction.md` (full structured extraction)

**Every absolute number in the driver tree (revenue, OI, GM, subs, MAU, ARPU, R&D, S&M, G&A, segment metrics) must be copied verbatim from these extractions, never drafted from memory.**

This step exists because: an earlier iteration of this skill on SPOT used FY24 numbers as if they were FY25 (one-year shift error), silently corrupting every growth-rate computation downstream. The mechanism that prevents this is *always re-pulling anchors from the extraction file at the start of Phase 4*, regardless of what you "remember" the numbers to be.

**Also verify the extraction itself is still current**: confirm `headline_anchors.md` reflects the latest reported period — if a new earnings release landed since Phase 2 ran, refresh the extractions before drafting (SKILL.md re-pull rule).

Specific checks before drafting:
- Latest fiscal year revenue, OI, NI, EPS, FCF — from anchors file, with citation tag
- Latest fiscal year subs / MAU / ARPU / segment splits — from anchors file
- Detailed cost-line splits (R&D / S&M / G&A) — from 20-F extraction
- Segment GM (if reported separately) — from 20-F segment note extraction
- Share count — from 20-F equity note extraction

If any of these are needed in the driver tree but absent from extractions, **apply the source-fallback rule** from SKILL.md: open the underlying filing directly and add to the extraction file. Never skip a needed data point or use a memory-derived estimate as if it were a fact.

---

## MAU / free-user classification rule (for DSPs, ad-supported platforms, two-sided marketplaces)

In any business where free users generate ad revenue, the **free user count is a direct revenue driver, not a leading indicator**. The driver tree must classify these nodes correctly:

| Node | What it is | Where it goes |
|---|---|---|
| Free MAU / non-paying user count / ad-impressions volume | Direct volume input for ad revenue | **Swing driver of ad-supported revenue** |
| Total MAU (paid + free combined) | Engagement metric, funnel for paid conversion | Leading indicator (not in current-quarter revenue identity) |
| Paid sub count | Direct volume input for subscription revenue | **Swing driver of subscription revenue** |

Be explicit in the tree about which MAU figure each node refers to. Conflating total MAU with free MAU misses the ad-segment volume driver.

This rule generalizes from a SPOT failure: total MAU was initially listed as a non-driver, but free MAU (Total MAU minus Premium subs) is the volume input for Ad-supported revenue and IS a swing driver.

---

## Marking estimated / non-disclosed drivers

When a driver value is sell-side modeled, an industry rule-of-thumb, or a calibration estimate rather than company-disclosed, mark with `[est, not disclosed]` inline. Examples:

- `Monthly churn rate ~3.5% [est, not disclosed; sell-side annual gross churn 10-15% range — JPM, Bernstein]`
- `Individual tier ~50% of subs [est, not disclosed; sell-side modeled — Wolfe init]`
- `Discovery Mode share of streams ~2% [est, not disclosed]`

Do not write a bare number for an estimated driver. Per SKILL.md inline-citation rule, the marker is mandatory.

---

## Business-specific complications section is MANDATORY

After fitting the closest template (below) and producing the standard revenue + margin tree, write a third section titled "Business-specific complications" that lists places where the standard template fails for this company. This is where the genuine analytic value of the driver tree lives. Examples of what belongs:

- Variable-vs-fixed COGS split (e.g., %-of-revenue royalty contracts where price hikes are GM-neutral)
- Bundling / revenue-allocation levers (e.g., audiobook bundling that reclassifies music revenue)
- Regulatory-cap mechanics (utilities, healthcare reimbursement)
- FX translation vs. economic exposure split (multinational FPIs)
- SBC treatment vs. peer convention (some firms add back, some don't)
- Customer / supplier / channel concentration
- Segment cross-subsidization
- Two-sided platform pricing dynamics
- Inventory channel build/burn cycles
- Non-standard accounting (long-term contracts, deferred revenue, multi-element bundles)

This section should be 3-6 short subsections. Each subsection states the complication, explains the mechanism, and notes the directional implication for the model.

---

## Templates by business type

These are starting points. Customize aggressively.

### SaaS / subscription software

```
Revenue:
├── New ACV (annual contract value)
│   ├── Pipeline coverage × close rate × average deal size
│   └── Or: # new logos × $ per logo
├── Existing ACV (retention)
│   ├── Net Revenue Retention (NRR) = Gross retention × Expansion rate
│   ├── Gross retention = 1 − churn rate
│   └── Expansion = upsell ARPU growth
└── Other (services, transactional, partner) — usually <10%

Margin:
├── Gross margin (~75–85%)
│   └── Driven by: cloud infra costs / revenue, support costs / customer
├── S&M as % of revenue (~30–50%; declining at scale)
├── R&D as % of revenue (~15–25%; relatively sticky)
├── G&A as % of revenue (~10–15%; declining at scale)
└── Stock-based comp (treat as real cost — often 15–25% of revenue)
```

### Consumption / usage software (Snowflake-style)

Different from SaaS. Revenue is volatile because customers can optimize usage:

```
Revenue:
├── Customer count × Average revenue per customer
├── Where: ARPU = base usage × usage growth − optimization
└── Net revenue retention is more volatile than SaaS — break out volume vs. price

Margin:
├── Gross margin
│   └── Driven heavily by infra cost negotiation (cloud commits, hardware deals)
├── (Same OpEx structure as SaaS)
```

### Semiconductors

```
Revenue:
├── Volume (units × ASP)
│   ├── Volume by end-market: datacenter, gaming, auto, IoT, mobile, industrial
│   └── ASP trajectory (declining as nodes mature, or rising if mix-shifts to high-end)
├── Capacity utilization (in fabs)
└── Inventory cycle (channel build vs. burn)

Margin:
├── Gross margin (very mix- and utilization-sensitive; 40–75%)
├── R&D as % (high; 15–25% — chip design intensive)
├── SG&A as % (5–10%)
└── Capex as % of revenue (huge for foundries; lighter for fabless)
```

### Retail / consumer

```
Revenue:
├── Stores × Sales/store
│   ├── Sales/store = Traffic × Conversion × Basket size
│   └── Or: Comp sales (% YoY, like-for-like)
├── E-commerce % of sales
└── International / new market expansion

Margin:
├── Gross margin (mix, sourcing, FX, promotion intensity)
├── Occupancy (rent + utilities) as % of revenue
├── Labor as % of revenue
├── Marketing as % of revenue
└── Other SG&A
```

### Banks / financials

```
Revenue:
├── Net Interest Income (NII)
│   ├── Average earning assets × Net Interest Margin (NIM)
│   └── NIM = yield on assets − cost of funds
├── Fee income (advisory, trading, asset management, deposit fees)
└── Other (insurance, ancillary)

Margin / profitability:
├── Efficiency ratio (OpEx / revenue) — target <60% for high-quality banks
├── Provision for credit losses / total loans
├── Cost of risk (% of loan book per year)
├── Capital ratios (CET1, Tier 1) — drives capital return capacity
└── ROTCE (return on tangible common equity)
```

### Healthcare / pharma

```
Revenue:
├── By drug / device:
│   ├── Volume (scripts, patients) × Price
│   └── Patent cliff timing (loss of exclusivity dates)
├── Pipeline NPV (probability-weighted future drugs)
└── Geographic mix

Margin:
├── Gross margin (high for branded ~80%; low for generics ~30%)
├── R&D as % (massive — 15–25%)
├── SG&A — sales force-driven for branded
└── Royalty / milestone payments
```

### Industrials / manufacturing

```
Revenue:
├── Backlog × Conversion rate
├── Book-to-bill ratio
├── Price × Volume by product line
├── Aftermarket / services attachment rate
└── Cyclical position

Margin:
├── Gross margin (price-cost spread)
├── Operating leverage on volume
├── Aftermarket margin uplift (services higher than original equipment)
└── Working capital turns
```

## How to customize

For most businesses, the templates above need modification. Common patterns:

- **Hybrid businesses (e.g., Palantir = software + services + government)**: split revenue tree into separate sub-trees, then aggregate. Different segments have different unit economics.
- **Concentration risks**: if one customer / channel / supplier is >20% of business, add a node specifically for it.
- **Regulatory caps**: if pricing is capped (utilities, healthcare reimbursement), model the cap as a separate node.
- **FX exposure**: for multinationals, add a currency translation layer.
- **Buyback impact on EPS**: if material, model share count separately (not just net income).

## Process for this phase

1. **Pick the closest template** based on Phase 2 business model description
2. **Customize**: add nodes for company-specific economics, remove nodes that don't apply
3. **Tag each node with units**: % YoY for growth metrics, $ for absolute, bps for spreads, # for counts
4. **Identify swing drivers**: which 3–5 nodes, if they move, materially change the price target? Mark these — they're the focus for Phases 5–6.
5. **Deep-dive each swing driver's economics (MANDATORY — the depth gate).** *Identifying* a swing driver is not *decomposing* it. For each swing driver — and for each Phase-1 "key debate" that is a structural driver (`context.md` "Key debates / crux", Step 5c) — research its **current economics to depth**: is it profitable / what's the contribution / how much does it make or lose, and at what **stage** (investment / inflection / harvest)? **Reconstruct what the company doesn't disclose** — segment margin, take-rate, a buried sub-business's P&L (Temu inside PDD, AWS-historically inside Amazon, international-margin inside TCOM) — by triangulating consolidated figures + segment/geography splits + peer benchmarks, AND pulling **management's own answers from the earnings-call Q&A** (analysts ask these exact questions on the record). Flag every reconstructed number `[est, derived]`. This is where *"is the growth engine actually making money?"* gets a **quantified** answer, not a qualitative gesture. Worked template: the TCOM international-economics reconstruction (breakeven-to-loss triangulation + the management margin quotes).
6. **Document the tree** in `working/driver_tree.md`

## Q&A interlude (LIGHT–MEDIUM)

This phase is mostly mechanical given Phases 2–3. Common questions:
- *"Why is X separated out? Couldn't it be lumped with Y?"* — explain the rationale (different unit economics, materially different growth rates, etc.)
- *"What's the difference between bookings, billings, and revenue?"* — yes, this is real. Bookings = signed contract value. Billings = invoiced. Revenue = recognized per GAAP. The gap matters for SaaS.
- *"For [segment X], what's the right way to model it?"* — drill in.

When user says continue, advance to Phase 5 (Consensus map).

## What this is NOT

- NOT a financial model (Phase 11)
- NOT consensus estimates (Phase 5)
- NOT a thesis (Phases 6–10)

It's the **skeleton** — empty cells that subsequent phases will populate.
