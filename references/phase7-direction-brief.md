# Phase 7 — Direction Commit

**Goal**: Produce a synthesis brief that summarizes everything from Phases 1–6 in decision-ready form, then have the user commit a direction (long / short / pass). The commit is tentative — revisable in Phase 12 if model surprises arise.

**Output**: `working/direction_brief.md` + chosen direction recorded in `working/direction.md`

## Why this matters

Without an explicit direction, the workflow can't proceed — Phase 8 develops pillars *for* a direction, not in the abstract. But picking a direction is judgment, not data. Phase 7's job is to make the judgment as informed as possible.

## Structure of the synthesis brief

### Section 1 — Setup (~150 words)

The current market state of the name:
- **Price action**: current price, YTD performance, 1Y / 3Y returns, 52-week range position
- **Recent revisions**: # upward / # downward in last 30 / 90 days
- **Street rating distribution**: how many BUY / HOLD / SELL among covering analysts, with target range
- **Recent news / catalysts**: what's moved the stock in the last 30 days?
- **Implied positioning**: is the stock loved (high targets, recent runs) or hated (recent dumps, downgrades)?

This frames the asymmetric setup. A name +50% YTD with universal BUYs is a different setup than a name -30% YTD with rating downgrades — even if the underlying fundamentals are identical.

### Section 2 — Where consensus is stretched (~250 words)

From Phase 5 + Phase 6:
- **Overly optimistic Street assumptions** (if any): drivers where Street has high estimates with thin support. Risk to the long case.
- **Overly pessimistic Street assumptions** (if any): drivers where Street has low estimates despite favorable evidence. Risk to the short case.
- **Most stretched single assumption**: the one that, if it breaks, causes the biggest target move.

Be honest. If both bull and bear cases have stretched assumptions, surface both.

### Section 3 — Asymmetries summary (~300 words)

From Phase 6:
- **Bullish-leaning asymmetries** (count + titles + 1-line summary each)
- **Bearish-leaning asymmetries** (count + titles + 1-line summary each)
- **Either-direction asymmetries** (where resolution could go either way)

Then a paragraph: which asymmetries are highest-conviction (most evidence, biggest impact)? Which are speculative? Where is the evidence strongest — bull side or bear side?

### Section 4 — Tentative read with conviction level (~150 words)

Skill produces a recommendation with reasoning:

> *"Based on Phases 1–6: Tentative read = [LEAN LONG / LEAN SHORT / PASS]. Conviction = [Low / Low-Medium / Medium / Medium-High / High]."*

Reasoning should reference specific asymmetries and their evidence weight. Format:

> *"Tentative LONG, Medium conviction. Two strong bullish asymmetries (#3 sovereign AI uncovered, #5 mgmt guidance methodology change in Q3 not yet in Street numbers) supported by clear evidence; one bearish asymmetry (#7 GM compression risk) is real but appears second-order vs. revenue trajectory. Setup is mixed — stock +28% YTD, Street already 75% BUY, so much of the bull case may be partially priced. Lean is to long-with-the-Street, not against."*

**Critical**: this is *the skill's read*, not the user's commit. The user has full discretion to override.

### Section 5 — Decision questions for user (~100 words)

Three direct questions to prompt commitment:

1. Long, short, or pass?
2. If long or short — high, medium, or low conviction?
3. Why? (one-sentence rationale)

The user's answer becomes `working/direction.md`.

## Q&A interlude (HEAVY)

This is the most important Q&A pause. The user must feel they can interrogate any aspect before committing. After producing the brief:

> "Phase 7 brief at `working/direction_brief.md`. Skill's tentative read: [LEAN X], [conviction]. The decision is yours — interrogate any aspect of the analysis before committing. Common questions: [examples below]. When ready, tell me your direction (long / short / pass), conviction, and one-line rationale."

Common questions to be ready for:
- *"Why didn't you weight asymmetry [N] more heavily?"* — re-examine, possibly update the read
- *"What would you do if you had to bet your own money?"* — express the lean honestly with caveats
- *"What's the bear (or bull) case I'm missing?"* — explicit counterfactual, even if the lean is the other direction
- *"How does this setup compare to historical analogues?"* — pattern matching to similar past setups
- *"What if I just don't know enough?"* — passing is valid; explicitly support that option
- *"Walk me through your reasoning step by step"* — re-derive the read transparently

The user may sit on this for a while. That's fine. Don't push.

## Recording the commit

When the user commits:

```markdown
# [TICKER] Direction Commit
Date: [YYYY-MM-DD]

**Direction**: [LONG / SHORT / PASS]
**Conviction**: [Low / Medium / High]
**Rationale (user)**: [one sentence]
**Rationale (skill's tentative read at the time)**: [one sentence — for posterity if revisions happen]

## Why this matters for downstream phases
- Phase 8 will develop pillars FOR this direction
- Phase 9 will steel-man the OTHER direction (counter-pillars become risks)
- Phase 12 may revisit if model surprises invalidate this direction
```

Save to `working/direction.md`. Confirm to user: *"Direction = [X]. Proceeding to Phase 8 (auto-draft pillars FOR the [X] case)."*

## What if user says PASS?

This is a valid output. Skill:
1. Saves the brief and the pass rationale to `working/direction.md`
2. Skips Phases 8–12
3. Goes straight to Phase 13 (write pitch) but produces a "Pass note" instead of a long/short pitch:

```markdown
# [TICKER] Pass Note
Rating: PASS
Reason: [one paragraph from user's rationale + skill's brief synthesis]

Conditions for revisiting: [list of events that would change the call — e.g., "if mgmt provides cohort retention disclosure," "if guidance is reset down at next earnings"]
```

Pass notes are valuable — they represent disciplined judgment. Don't apologize for them.

## What this is NOT

- NOT a model output (Phase 11)
- NOT pillars (Phase 8)
- NOT a pre-commitment that can't be revised (Phase 12 allows revision)

It's the **moment of judgment** that downstream phases serve.

## Note on base / bull / bear framing

The direction committed here IS the **base case**. It is the analyst's committed view.

Downstream:
- Phase 8 develops pillars FOR the base case (long pillars if direction = long; short pillars if = short).
- Phase 9 steel-mans the OTHER direction — those counter-pillars become **the bear case envelope** around the committed base.
- Phase 11 computes a **bull / base / bear payoff envelope** from the same model by flexing the top 2-3 tornado swing assumptions: bull = pillars overshoot; base = the committed view as built; bear = counter-pillars partially materialize.
- Phase 13 pitch shows this envelope explicitly with a risk/reward skew = (Bull − Spot) / (Spot − Bear) — the "asymmetric payoff" check that buy-side / interview audiences look for.

Important: bull and bear are **not alternative theses**. They are the payoff distribution around the **single committed view**. The skill does not produce three parallel models; it produces one model and uses sensitivities to express the envelope around it.
