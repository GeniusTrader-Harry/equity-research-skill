---
name: equity-research-customised-process
description: Crack a single stock for an investment view — thesis-first equity research workflow that produces a defensible 5–8 page investment memo with model and sensitivity. Use when the user says "thesis-first on [TICKER]", "crack [TICKER]", "pitch me [TICKER]", "research [TICKER] for an interview", "form a view on [TICKER]", or asks to develop an investment thesis on a single name. Designed for student / recruiting prep, not full sell-side report production. NOT for earnings updates (use earnings-analysis), sector primers (use sector-overview), or 30+ page initiation reports (use initiating-coverage).
---

# Equity Research — Customised Process (Thesis-First)

Produce a defensible 5–8 page investment memo on a single stock by:
1. Understanding the business and industry deeply
2. Forming a direction (long / short / pass) early
3. Developing 2–4 thesis pillars
4. Steel-manning the counter-arguments as risks
5. Auditing pillars for falsifiability and materiality
6. Building one model with sensitivity tables
7. Iterating if model surprises arise
8. Writing the memo with a "What would change my mind" section

**Output**: a 5–8 page markdown memo (~2,500–4,000 words; Section 1 is itself a 1-page verbal-pitchable summary) + supporting Excel model + research archive directory the user can browse and revisit.

---

## Core operating principles

### Principle 1: Skill does data, user does judgment

| Skill does | User does |
|---|---|
| Fetching, downloading, parsing | Forming views |
| Decomposing drivers into trees | Killing pillars |
| Mapping consensus from sources | Committing direction |
| Drafting candidate pillars | Critiquing drafts |
| Drafting candidate killing conditions | Verifying killing conditions |
| Computing materiality, sensitivity, tornado | Accepting/rejecting flags |
| Flagging weak pillars | Deciding what survives |

Skill never picks a direction. Skill never grades pillar quality. Skill surfaces evidence and structure; user makes calls.

### Principle 2: Q&A interludes — every phase boundary is a checkpoint

**The skill must NEVER auto-advance between phases.** After producing each phase output, the skill explicitly pauses with a message like:

> "Phase X complete. Output: [name of file or summary]. Ask any question about the business / output / source data, request edits, or say 'continue' / 'next' to advance."

User questions during interlude are unrestricted in scope and number. User may:
- Ask for clarification on any concept or data point
- Request the skill explore a specific topic deeper
- Request alternative drafts
- Edit the output directly
- Drill into source documents (10-K excerpts, transcript pages, etc.)

Skill responds, then re-prompts: *"Ready to continue, or more questions?"*

User-driven cadence is essential. Some phases get heavy interrogation (Phases 2, 3, 7, 8, 9, 10, 12); others get a quick "continue" (Phases 4, 5, 11, 13). Skill must respect both.

### Principle 3: Manual fetch when programmatic isn't possible

For paywalled / TOS-restricted sources (CapIQ, Bloomberg Terminal, FactSet research), skill prompts the user to fetch manually and drop files into the appropriate directory, then waits for "done." See `references/phase1-context-load.md` for the workflow.

### Principle 4: Vocabulary discipline

- **Direction** = the rating (long / short / pass; BUY / HOLD / SELL)
- **Pillar** = one specific testable argument supporting the direction. Must have 5 elements: claim / driver / mechanism / magnitude / timeframe
- **Killing condition** = a pre-specified event/number that would prove a pillar wrong, written at thesis formation, used for live monitoring after publication

Never call a directional rating a "thesis." A thesis is the *direction + the pillars supporting it*. Pillars are the testable units.

---

## Workflow at a glance

| # | Phase | Output | Q&A weight |
|---|---|---|---|
| 1 | Load context (raw fetches + manual sell-side) | `working/context.md` + populated source dirs | Light |
| 2 | Company Brief (synthesize) | `working/company_brief.md` | **Heavy** |
| 3 | Industry Brief (synthesize) | `working/industry_brief.md` | **Heavy** |
| 4 | Driver decomposition | Customized driver tree | Light |
| 5 | Consensus map | Driver-level consensus + dispersion table | Light–medium |
| 6 | Asymmetry hunt | `working/asymmetries.md` | Medium |
| 7 | Direction commit | Synthesis brief + chosen direction | **Heavy** |
| 8 | Auto-draft pillars FOR direction | 2–4 finalized pillars | **Heavy** |
| 9 | Steel-man (counter-pillars → risks) | Risk list with rejection reasoning | **Heavy** |
| 10 | Pillar audit (3 checks + killing conditions) | Surviving pillars + killing conditions list | **Heavy** |
| 11 | Build one model with sensitivity tables | `deliverables/[ticker]_model.xlsx` + tornado | Light |
| 12 | Iterate if model surprises you | Revised pillars or revised direction | Heavy on surprises |
| 13 | Write pitch | `deliverables/[ticker]_pitch.md` | Light |

---

## How to execute the workflow

When the skill triggers, the orchestrator does the following in order:

1. **Confirm ticker and intent.** Ask the user "Ticker?" if not provided. Confirm the goal is full thesis-first research (not a quick lookup).

2. **Set up directory structure** at `~/Claude Projects/Equity Research/[TICKER]/` with subdirectories:
   ```
   filings/         # 10-K / 10-Q / DEF 14A (US issuers) OR 20-F / 6-K (foreign private issuers). HTM as filed; PDF optional.
   transcripts/     # Earnings call transcripts (Motley Fool / Seeking Alpha / IR site)
   ir-materials/    # Investor day decks, latest earnings deck, 10-K/20-F language diff
   sell-side/       # USER POPULATES manually (CapIQ / Bloomberg / FactSet — TOS-restricted, no auto-scrape)
   extractions/     # Structured primary-source extractions (20F_extraction.md, headline_anchors.md) — produced by Phase 2 Step 0
   working/         # Skill-synthesized files
   deliverables/    # Final model + memo
   ```

3. **Execute phases sequentially.** For each phase:
   - Load the corresponding `references/phaseN-*.md` file
   - Follow its instructions
   - Produce the output file
   - Pause with the standard Q&A interlude prompt
   - Wait for user "continue" / "next" before advancing

4. **Reference files (loaded on demand per phase):**
   - Phase 1 → `references/phase1-context-load.md`
   - Phase 2 → `references/phase2-company-brief.md`
   - Phase 3 → `references/phase3-industry-brief.md`
   - Phase 4 → `references/phase4-driver-trees.md`
   - Phase 5 → `references/phase5-consensus-map.md`
   - Phase 6 → `references/phase6-asymmetry-hunt.md`
   - Phase 7 → `references/phase7-direction-brief.md`
   - Phase 8 → `references/phase8-pillar-template.md`
   - Phase 9 → `references/phase9-steel-man.md`
   - Phase 10 → `references/phase10-pillar-audit.md`
   - Phase 11 → `references/phase11-model-build.md`
   - Phase 12 → `references/phase12-iteration.md`
   - Phase 13 → `references/phase13-pitch-template.md`

5. **Reuse existing skills where appropriate.** The DCF mechanics in Phase 11 should leverage `financial-analysis:dcf-model` patterns. Pillar tracking format in Phase 10 borrows from `equity-research:thesis`.

6. **Always end the workflow with the pitch document and a recap message** summarizing rating, target, pillars, and what to monitor.

---

## Important behaviors

- **NEVER fabricate figures.** This is the highest-priority rule. Every quantitative claim in any phase output (Phases 1–10 and the memo) must be verified from a primary source on disk (filings, transcripts, shareholder letters, sell-side notes, market-data exports). If a number is not available from a source, write `[not disclosed]` or `[needs sell-side pull]` — never invent a plausible-sounding placeholder. The ONLY phase where unverified numbers are permitted is **Phase 11 (Build model)**, where forecast inputs are *assumptions* by definition — and even then, every assumption must have a documented basis (Street consensus, mgmt guidance, computed from historical trend, or explicit pillar claim from Phase 8). Plausibility ≠ fact. If you catch yourself rounding "I think it's around X" into "X" — stop and verify or flag.
- **No fake precision.** Never attach specific page numbers, take rates, percentages, or counts to a claim unless that specific number has been verified in the source during this session. The failure mode is *plausible* precision — e.g., "10-20% transaction fee" or "p.7 of the JPM note" — both can be made up while *feeling* researched, because the substance you're attaching them to may be defensible. If you are confident about the substance but cannot verify a specific number / page, write the substance in generic form ("per Wolfe initiation", "industry standard for DSPs", "sell-side estimates", "trade press reporting") — never invent precision. The test before citing a page number: can you point to the line on the page right now? If not, generalize the citation. This rule is a tighter sibling of "NEVER fabricate" — the former covers literal made-up numbers; this one covers fake precision wrapped around real substance.
- **Pre-write claim test for every number.** Before writing any specific number (percentage, $/€ amount, count, page reference) in any phase output, run the claim test:
  - Is it disclosed in a primary source I read THIS SESSION? → cite with source + page
  - Is it computed from primary disclosures? → cite as `[computed from X, Y]`
  - Is it from a sell-side note? → OPEN AND VERIFY the page before writing the citation
  - None of the above? → omit the number. Write `[not disclosed]` or describe qualitatively. Never write "approximately X" as a workaround for "I don't know X."
- **No orphan numbers in outputs.** Every numeric claim must have an inline citation `[source]`, `[computed]`, or `[not disclosed]`. Grep-enforceable: `\d+%` or `\d+M` not followed by `[...]` should return zero before saving any output. Run this check as a final step.
- **My modeling vs. sourced fact must be visually distinct.** When a number is my own modeling extrapolation (not from any source), state explicitly: "my modeling: ~X% based on [methodology]" — never embed it as if it were disclosed or sell-side. The reader needs to know which side of the line each number sits on.
- **Phase 11 fresh derivation — back-of-envelope numbers from earlier phases never become model inputs without independent primary-source derivation.** Pillar magnitudes asserted in Phases 8/10 (e.g., "+50-150bps GM vs Street," "+€110-330M FY28 GP delta," "approximately 2-7% PT impact") are *qualitative structuring tools*. The model in Phase 11 re-derives every input from primary sources (20-F line items, shareholder-letter actuals, sell-side consensus xlsx) — shares, tax rate, capex, WC, WACC components, multiples. If the rebuilt model disagrees with a pillar magnitude, that's a Phase 12 surprise trigger, not an error to silently align away. Track record across runs: every back-of-envelope chain caught at least one error when surfaced for review. See `references/phase11-model-build.md` Step 0 for the full rule.
- **Every numeric claim has an inline citation.** Three accepted forms:
  - `[source, p.N]` — verified, number and page checked: e.g., `€17,186M [Q4 25 letter, p.3]`
  - `[source]` — substance verified, exact page not opened: e.g., `~70% royalty share [Wolfe init]`
  - `[est, not disclosed]` — acknowledged as not a fact: e.g., `Family tier ~25% of subs [est, not disclosed]`

  No bare numbers in any phase output. A claim like `Family ~25%` must be either cited or flagged as an estimate. Enforceable at proofread time: grep for `\d+%` not followed by a `[...]` marker should return zero.
- **Source-fallback rule — never skip a needed data point.** When the first-choice source for a data type doesn't contain a needed number, fall back to the next layer rather than omitting the data point. Specifically:
  - Headline number missing from shareholder letter → check the 10-Q (quarterly) or 10-K / 20-F (annual)
  - Detailed cost line missing from MD&A → check the audited P&L line items in the F-pages / Item 8
  - Segment metric missing from segment note → check the operational review in MD&A
  - KPI missing from press release → check the investor day deck or earnings call transcript

  If after the fallback ladder the data point is genuinely not disclosed anywhere, mark inline as `[not disclosed]` — never just omit. Omission silently corrupts comparisons (you can't tell whether the value was zero, unknown, or deliberately skipped).
- **Data source hierarchy — by purpose, not by file.** Each data type has a designated source. Pulling the same number from the wrong source corrupts comparisons.
  - **Company-reported actuals, headline numbers & KPIs** (revenue, OI, NI, GM, EPS, subs, MAU, ARPU) → **Shareholder letter / earnings press release** (clean multi-year tables; identical numbers to the audited filing, faster to find).
  - **Detailed audited line-items** (R&D / S&M / G&A separately, segment P&L, share count detail, tax reconciliation, lease/debt schedules, risk factors, governance, exec comp) → **10-K / 20-F / proxy**. The shareholder letter doesn't split these.
  - **Past-quarter actuals vs. pre-print consensus** (beat/miss table) → **CapIQ Consensus xlsx** (the xlsx has both the Actual and the Median pre-print consensus in one file — avoids cross-source mismatch). **Do NOT pull the actual from the shareholder letter when comparing to CapIQ consensus** — use CapIQ's own actuals row for internal consistency.
  - **Next-quarter guide vs. Street consensus** → **Web search** (Reuters/FT/Bloomberg/Investing.com). Press captures the Mean used in headlines; CapIQ Median can differ from the press consensus.
  - **Forward FY+1/2/3 consensus** → **CapIQ xlsx Median row**.
  - **Qualitative strategic context** (forward direction, mgmt tone, market reaction) → **Earnings call transcript** + sell-side analyst notes. Not for numerical claims.

  **Always re-pull the headline anchor numbers from the most recent shareholder letter at the start of any phase that uses them.** A year-stale anchor (e.g., FY24 actuals used after FY25 results are out) will systematically corrupt every downstream figure. See `references/phase1-context-load.md` for the full source-hierarchy table.
- **Always compare the latest quarterly results to consensus expectations.** Whenever a phase output references the most recent quarter, include the **pre-print consensus** alongside the actual figure for revenue, EPS, MAU/subs (or other KPIs central to the business), and forward guidance. Source the consensus from sell-side notes (pre-print updates), aggregator data (Refinitiv I/B/E/S via CapIQ), or company-provided reconciliations. If consensus isn't available, say "consensus not retrieved" — never guess at the magnitude of beat/miss.
- **Never skip the Q&A interlude.** Even if the user has been silent, prompt them at every phase boundary.
- **Never write a thesis pillar without all 5 elements.** Drafts that lack any of (claim / driver / mechanism / magnitude / timeframe) must be flagged and rewritten before being shown to user.
- **Never auto-pick a direction.** Phase 7 produces a *tentative read with conviction level*, but the user commits.
- **Save killing conditions verbatim.** What's drafted in Phase 10 is what appears in the Phase 13 pitch under "What would change my mind." Don't paraphrase between phases.
- **Pass is a valid output.** If Phase 12 iteration doesn't converge after 1–2 rounds, recommend "pass" and document why. Better than a forced thesis.
- **Manual fetch waits forever.** When prompting the user to drop CapIQ notes into `sell-side/`, wait indefinitely. Don't time out and proceed without notes unless the user says "skip."

---

## Pre-Phase-13 audit checklist (mandatory before drafting memo)

Before opening Phase 13 to draft the memo, the skill runs a four-check internal-consistency audit across the working/ files. **Do NOT advance to Phase 13 if any check fails** — fix the working files first. The memo is a synthesis layer; if the inputs disagree, no amount of memo iteration will fix it.

| Check | Source | Mechanic |
|---|---|---|
| **A. Pillar magnitudes ↔ model output** | `working/pillars_audited.md` vs `working/valuation_outputs.yaml` (or xlsx) | Every pillar's claimed magnitude must reconcile to the model output within tolerance (margin pillars ±50bps; growth pillars ±100bps; volume pillars ±5%) OR the gap must be documented in `working/phase12_iteration.md` |
| **B. Killing conditions ↔ pillar claims** | `working/killing_conditions.md` vs `working/pillars_audited.md` | Every KC must link to a specific pillar and (where relevant) a specific model assumption. KC base-case calibration check (Phase 10 Gate D) must have passed |
| **C. Valuation single-source-of-truth** | All working/ files referencing PT / bull / bear / skew / WACC | Every valuation number across all working files must trace back to `working/valuation_outputs.yaml`. Grep working/ for hard-coded values; replace orphans with yaml references or update to match |
| **D. External anchor traceability** | Every external anchor cited in pillars_audited.md or risks.md | Every cited sell-side estimate, consensus median, regulatory threshold, or peer benchmark must be traceable to the source file with the data point quoted — and the cited forecast horizon must be within the source's actual coverage (per Phase 5 anchor existence matrix; per Phase 10 Gate A) |

Run the audit; report failures explicitly to the user; pause for fixes before Phase 13. If all four pass, advance.

## User preferences layer

Across multiple memos a given user develops settled stylistic preferences that, captured once, should drive the *first* draft of every future memo rather than re-iterating from defaults each time. Examples of preferences worth capturing: bullets-vs-prose balance, "Thesis" vs "Pillar" terminology, methodology placement (body vs appendix), inclusion or omission of optional sections (comps cross-check, sell-side reconciliation, Management subsection, named long-duration-competitive-threat sub-section), preferred header conventions, page-count target.

Capture preferences in either:

- The user's auto-memory: `~/.claude/projects/-Users-[username]/memory/` (persistent across all conversations)
- A skill-local `preferences.md` if user wants the preferences scoped just to equity research

Reference these at Phase 13 start so the first draft of every future memo matches established conventions. Settled preferences that conflict with the template default should follow the user's preference, not the template.

## Style notes for outputs

- Plain English over jargon. The user is a student building intuition, not an MD pretending sophistication.
- Quantify whenever possible. Pillars without numbers are vibes.
- Cite sources with file path and page/section. E.g., *"FY24 10-K p. 47"* or *"Q3 FY25 transcript, CFO opening remarks."*
- Prefer markdown tables over prose for comparative data (driver trees, consensus maps, sensitivity outputs).
- **The memo is 10-18 pages (~5,000-8,000 words) with cover + 2 appendices.** Cover is the verbal-pitchable summary; body sections carry the depth; Appendix A has DCF mechanics, Appendix B has key model assumptions. If the overall memo spills past 18 pages, tighten — but the previous 5-8 page target was too tight for an interview-grade memo with a DCF appendix.
