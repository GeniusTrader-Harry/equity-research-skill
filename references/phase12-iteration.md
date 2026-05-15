# Phase 12 — Iterate if Model Surprises You

**Goal**: When the Phase 11 model produces output that doesn't match the user's expectations from Phases 7–10, iterate explicitly. After 1–2 cycles, model and pillars should converge. If they don't, **pass** is a valid output.

**Output**: revised pillars, revised assumptions, possibly revised direction. Updates `working/pillars_audited.md` and the model.

## Why this phase exists

The thesis-first workflow commits a direction at Phase 7 and develops pillars at Phase 8. Then Phase 11 builds the model expressing that thesis. Sometimes the model output disagrees with the thesis — this is information, not failure. The iteration phase is the structured response.

The goal is **convergence**: the model and the pillars should tell the same story. If they don't, one is wrong.

## Surprise modes

There are 4 standard ways the model surprises you. Each has a defined response.

### Surprise 1 — Math doesn't reach the implied target

**Symptom**: pillars imply 18% upside; model spits out 9%.

**Diagnosis**: the pillars don't move the target as much as you thought. Two possibilities:
- **Materiality miscalculation**: Phase 10 mat-test was wrong (used wrong base assumption, wrong multiple, etc.)
- **Insufficient pillars**: 2 pillars aren't enough; need a third to close the gap

**Response**:

1. **Re-run the materiality test** in the model. Verify each pillar's actual target impact.
2. If a pillar is contributing less than Phase 10 estimated, sharpen it (more aggressive defensible magnitude) or drop it.
3. If pillars are correctly contributing but total is short, go back to **Phase 6 asymmetries** — find another asymmetry that supports the direction. Develop it as a new pillar (Phase 8), audit it (Phase 10), add to model (Phase 11).
4. If no additional asymmetries available, accept the smaller upside or downgrade conviction.

### Surprise 2 — Implied multiple is unreasonable

**Symptom**: DCF target implies 38x P/E; comp set trades at 22x. Or DCF gives 15x P/E for a 25% grower (too low).

**Diagnosis**: the model's terminal value or growth assumptions are doing more work than they should.

**Response**:

1. **Decompose the implied multiple**: pull the equivalent earnings multiple from the DCF target / forward EPS. Compare to comps.
2. **Identify which assumption is responsible**:
   - High terminal growth rate (>3%)? Likely too aggressive.
   - Long explicit forecast period (>10 years)? Compounds error.
   - Terminal margin assumption far above peers? Defensible only if pillars justify it.
3. **Choose**:
   - Option A: **temper the assumption** to match comps. Target moves down. Maybe direction stays valid but with less upside.
   - Option B: **write a new pillar** that justifies the multiple expansion (e.g., *"Re-rating to peer X as business mix shifts"*). This is a legitimate move if the rerating is itself defensible.
   - Option C: **accept the multiple gap** and note in the pitch that the thesis depends on the multiple holding.

### Surprise 3 — One pillar does 75%+ of the work

**Symptom**: tornado chart shows one assumption dominates the others.

**Diagnosis**: the thesis is one-pillar fragile. If that one pillar dies (Phase 10 killing condition triggers), the entire thesis collapses.

**Response**:

1. **Acknowledge honestly**: this is a one-pillar thesis. Don't pretend otherwise.
2. **Choose**:
   - Option A: **find more pillars** to distribute risk. Back to Phase 6 — look for asymmetries on other drivers.
   - Option B: **honestly write the pitch as a one-pillar thesis**. State explicitly: *"The call rests primarily on Pillar 1. If [killing condition] triggers, the rating moves to PASS."* This is a defensible posture for genuinely strong single-asymmetry plays (e.g., a clear regulatory catalyst, a binary product launch).
3. **Update conviction**: one-pillar theses usually warrant Medium conviction at most, not High. Even if the pillar is strong.

### Surprise 4 — Stress test breaks the thesis

**Symptom**: flexing the swing assumption -1σ collapses the target by 30%+. Or the implied target crosses below current price under modest bearish flex.

**Diagnosis**: thesis has no margin of safety. Even if your central assumptions are right, the asymmetry of being wrong is too painful.

**Response**:

1. **Quantify the asymmetry**: compute upside in central case vs. downside in -1σ case. Are they comparable? (E.g., +20% upside vs. -25% downside is **negative asymmetry** for a long.)
2. **Choose**:
   - Option A: **temper the central case assumptions**. Build in cushion. Target moves down. Conviction may rise because margin of safety improves.
   - Option B: **flip direction**. If the bear case is structurally easier than the bull case, the original direction commit was wrong. Back to Phase 7.
   - Option C: **pass**. Sometimes the right answer is "I see the bull case but the asymmetry is unfavorable."

## Iteration mechanics

Each iteration is a cycle through the relevant phases. Don't re-run from scratch — surgically update.

### Single-phase iteration
- Materiality recompute → just re-run Phase 10 Check 2 with updated model
- Pillar sharpening → update Phase 8 pillar; re-run Phase 10 audit on it
- New pillar addition → Phase 6 (find asymmetry) → Phase 8 (draft) → Phase 10 (audit) → Phase 11 (add to model)

### Multi-phase iteration
- Direction flip → back to Phase 7 commit; Phases 8–11 re-run for new direction (most painful)
- Pass → skip to Phase 13 pass note

## Convergence criteria

Stop iterating when:
1. The model's central target matches your pillar-implied upside within a reasonable range (e.g., model says +15%, pillars implied +18% — close enough)
2. The tornado shows reasonable diversification across pillars (no single bar >60%)
3. The stress test shows acceptable asymmetry (e.g., +25% upside vs -15% downside for a long)
4. All surviving pillars from Phase 10 are reflected as model assumptions and showing material impact

If after **2 iteration cycles** none of these are true, recommend **pass** with documented reasoning. Forcing a thesis through is worse than admitting the call doesn't work.

## Q&A interlude (HEAVY ON SURPRISES)

When a surprise hits, prompt:

> "Phase 12: model surprise detected — [describe surprise mode]. Recommend: [diagnosis]. Options: [A/B/C as relevant]. Take time to think. Common questions: 'why is the math short?', 'can we find another pillar?', 'should we flip direction?', 'is pass the right call?' When ready, say which option, or describe a different response."

User may sit on this. Don't push. Genuine discomfort here is a feature — it's the moment of confronting whether the thesis actually holds.

## Recording iterations

Each iteration cycle gets a log entry:

```markdown
## Iteration 1 — [date]
Trigger: [surprise mode]
Diagnosis: [what was wrong]
Response: [option chosen]
Changes: [what got updated — pillar, assumption, direction]
Result: [did it converge? what's the new target?]
```

Append to `working/iterations.md`. Useful for the pitch's transparency: showing your work.

## When to advance to Phase 13

Advance when:
1. Model is stable
2. Pillars are stable
3. Direction is stable
4. The user has confirmed they're satisfied with the convergence

Confirm: *"Phase 12 converged. Final target: [X], implying [Y]% [upside/downside]. [N] pillars surviving with [M] killing conditions. Proceeding to Phase 13 (write pitch)."*

If the user lands on **pass**: skip directly to Phase 13's pass-note format.

## What this is NOT

- NOT a free-for-all to redo everything
- NOT a license to abandon discipline (pillars without evidence)
- NOT a place to massage assumptions to make the target work

It's a structured place for the model to challenge the thesis, and for the analyst to honestly respond.

## Critical: convergence is honest, not forced

If you can't get model and pillars to agree after 2 cycles, the honest call is **pass**. Forcing convergence by:
- Inflating pillar magnitudes
- Adopting unjustified assumptions
- Inventing pillars without evidence

...produces a fragile thesis that will embarrass you at the next earnings call. Pass is better.
