# Phase 12 — Iterate if Model Surprises You

**Goal**: When the Phase 11 model produces output that doesn't match the user's expectations from Phases 7–10, iterate explicitly. After 1–2 cycles, model and pillars should converge. If they don't, **pass** is a valid output.

**Output**: `working/phase12_iteration.md` — **always written, even when there are no surprises** — plus revised pillars / assumptions / possibly revised direction when iteration occurs (updates `working/pillars_audited.md` and the model).

**The always-write rule**: a clean run still produces `working/phase12_iteration.md` with at minimum one paragraph ("reconciliation run [date]: no surprises") plus the pillar-band vs model-output reconciliation table from the pre-step below. Why: on disk, "checked and found nothing" must be distinguishable from "never checked" — and the pre-Phase-13 audit checklist reads this file. (Real case: SPOT 2026-05 — the reconciliation was done properly but inside a Phase 11 file; Phase 12 left no artifact and the audit checklist pointed at nothing.)

## Why this phase exists

The thesis-first workflow commits a direction at Phase 7 and develops pillars at Phase 8. Then Phase 11 builds the model expressing that thesis. Sometimes the model output disagrees with the thesis — this is information, not failure. The iteration phase is the structured response.

The goal is **convergence**: the model and the pillars should tell the same story. If they don't, one is wrong.

## Surprise modes

There are 4 standard ways the model surprises you. Each has a defined response.

## Pre-step — pillar ↔ model reconciliation gate

Before treating a discrepancy as one of the four surprise modes below, run a **mechanical reconciliation** between Phase 8/10 pillars and Phase 11 model output. This catches the silent-error class where the pillar document says one thing and the model produces another — and avoids the user having to catch it manually at memo review.

For each surviving pillar from Phase 10, compare:

| Element | Pillar value (from pillars_audited.md) | Model output (from valuation_outputs.yaml / xlsx) | Delta | Within tolerance? |
|---|---|---|---|---|
| Pillar 1 magnitude | e.g., +4-5% FXN ARPU FY28 | e.g., +4.7% FXN | +0.3pp inside band | ✓ |
| Pillar 2 magnitude | e.g., 35.5-36.5% FY28 GM | e.g., 35.8% | inside band | ✓ |
| Pillar 3 magnitude | e.g., 365-375M FY28 subs | e.g., 365M | at low end of band | ✓ |

**Tolerances** (proposed defaults; user can override per pillar):

- Margin / rate pillars: ±50bps
- Growth-rate pillars: ±100bps
- Unit / count pillars: ±5%

### When a pillar lives in an UNDISCLOSED segment — back-derive it as a residual

The reconciliation table assumes each pillar's magnitude can be read directly off the model. **It can't when the pillar is about a sub-business the company doesn't report** — a single-reportable-segment filer, an undisclosed geography, a buried product line. (A pillar about *international margin inflection* cannot be checked against a group-only P&L.) Don't skip the reconciliation — **back-derive the hidden piece as a residual**:

1. **Anchor on a model output you trust** — the group total the model produces (group OI, group revenue).
2. **Subtract the disclosed / assumable piece** — the part you *can* size (e.g. the domestic business at an assumed margin, net of any lever).
3. **Read the pillar's segment as the residual** — `pillar-segment = group − the-other-piece` — and back out its implied margin / growth.
4. **Test the implied figure against the pillar's claimed band.** If the back-derived path lands inside the pillar's magnitude, the model and pillar reconcile *on the pillar's own metric*, even though the metric is never reported.

Two error-traps this method invites — both generalisable:
- **Extrapolate off the DISCLOSED trend, not an arbitrary growth rate.** To size the residual segment's revenue, use the company's own disclosed share/mix trend (e.g. geography-share rising 13%→15%→17%), extrapolated — not a number you picked. A made-up growth rate produces a made-up residual and a false reconciliation.
- **Know the margin profile of anything you net in a bridge.** A ~100%-margin item (a take-rate give-back, a pure-commission line) comes off the **bottom line / OI directly**, not off the margin base — netting it *before* the margin double-counts it. Getting this wrong is what flips a "model ≫ pillar, temper the base" false alarm into the correct "reconciles fine."

Document the chain (the step table + the trap you avoided) as the audit trail — a back-derivation that isn't shown reads as hand-waving.

### When two effects are ENTANGLED in one reported line

The table checks each pillar in isolation against its band. That **misfires when two thesis elements (or a pillar and its risk) hit the same reported metric with opposite signs** and partially cancel — e.g. a margin-accretive pillar and a margin-dilutive risk both flowing into the *single* reported group margin, so the blended line looks flat even though the pillar is "working." A naïve gate flags the flat line as a pillar *failure*; it isn't.

Detection: before declaring a pillar's reconciliation failed, ask **"does any other pillar or risk touch this same reported line with the opposite sign?"** If yes, **reconcile at the decomposed level** (the back-derivation above), not the blended line — the blended line structurally hides both effects. The consequence is usually a real thesis insight, not a model change: the accretive pillar's value is *conditional* on the offsetting risk not biting, and that entanglement belongs in the memo (it is often why conviction is capped and why the visible upside is carried by the re-rate, not the operating line).

### Resolution decision tree — when reconciliation fails

If any pillar's model output lies outside its claimed magnitude band, follow this decision tree rather than treating it as ad-hoc surprise:

1. **Is the gap within tolerance?** If yes, document the small drift in the model_summary.md reconciliation table and move on. No revision needed.

2. **If outside tolerance — first, is the gap a multiple RE-RATE rather than a loose joint?** If the discrepancy is in *target upside* (not a specific operating-magnitude band), decompose estimate-driven vs re-rate-driven upside before assigning blame — a defensible re-rate is a legitimate resolution, not an error (see Surprise 1's FIRST question). Only if it isn't the re-rate, ask **which side is more defensible:**
   - The **pillar** was written from primary research, sell-side anchors, and management commentary. If that evidence is robust, the model assumption is probably the loose joint — re-examine which model input is producing the gap.
   - The **model** is a mechanical synthesis of multiple assumption choices. If a pillar magnitude was set too aggressively in Phase 8 without working backward through the model, the pillar is the loose joint.
   - Ask: where would I have higher confidence if I had to bet? That's the side to keep.

3. **What's the minimum-assumption change that closes the gap?** Don't restructure the whole thesis if a single assumption flex closes the gap. Examples (generalised, content-agnostic):
   - If a margin pillar is +200bps above model: probably a pricing-flow-through assumption is too modest, OR a cost-line headwind in the model is too steep. Touch the one assumption that has the cleanest causal link to the pillar's mechanism, not multiple at once.
   - If a volume pillar is below the model: check whether a conversion-ratio assumption or a geographic mix-weight is inconsistent with the pillar's evidence.

4. **Document the alternative considered.** In `working/phase12_iteration.md`, write down the alternative resolution paths you considered AND why you chose the one you chose. This is the audit trail when the user revisits the workflow in a future round.

5. **Update both sides and re-reconcile.** If you changed the model, the new model output may shift other pillars' reconciliation — rerun the table. If you changed a pillar, the pillar's killing conditions may need recalibration (see Phase 10 Gate D).

Only after the reconciliation gate is clean should you proceed to interpret remaining gaps via the four surprise modes below.

### Surprise 1 — Model target and pillar-implied upside don't match (either direction)

**Symptom**: the model's upside and the operating pillars' implied edge diverge — pillars imply 18% but the model gives 9% (model *short*), **or** the model gives 32% when the operating pillars only justify ~10% (model *over*). Both are this surprise; the response differs.

**FIRST question — before hunting for a "loose joint": is the gap the multiple RE-RATE?**
A forward-multiple target has two return sources: the operating estimate *and* the applied multiple moving from spot to target. The operating pillars only speak to the first. So **a model that shows more upside than the pillars "justify" is frequently not an error — the gap is a multiple re-rate** (e.g. from a distressed trough multiple back toward the peer/own-history range). Before treating the gap as a miscalculation:
- **Decompose the upside into estimate-driven vs re-rate-driven.** Hold the multiple flat at spot and re-read the target — that isolates the operating contribution; the remainder is the re-rate.
- **If the re-rate explains the gap, that is a legitimate, nameable resolution** — *not* a loose joint to reconcile away. Name it ("the upside is a re-rate call on a distressed setup, not an operating beat"), confirm the re-rate target multiple is defensible against the triangulation (Surprise 2), and **attach a killing condition to it** (what keeps the multiple suppressed). Write the pitch to say this plainly rather than implying the operating pillars carry the whole target.
- Only if the gap is **not** explained by a defensible re-rate do you proceed to the "model short / model over" diagnoses below.

**If the model is SHORT (pillars > model):** the pillars don't move the target as much as you thought —
- **Materiality miscalculation**: Phase 10 mat-test was wrong (wrong base assumption, wrong multiple, etc.) → re-run the materiality test in the model; verify each pillar's actual target impact.
- **Insufficient pillars**: 2 pillars aren't enough → go back to **Phase 6 asymmetries**, find another, develop it (Phase 8 → 10 → 11).
- If a pillar contributes less than Phase 10 estimated, sharpen it (more aggressive defensible magnitude) or drop it.
- If pillars are correct but total is short and no asymmetry remains, accept the smaller upside or downgrade conviction.

**If the model is OVER (model > pillars) and it is NOT the re-rate:** an assumption is too aggressive somewhere — find the loose joint (a growth or margin input running ahead of its evidence) and temper it, rather than banking upside the pillars can't support.

### Surprise 2 — Applied multiple isn't defensible

**Symptom (default / forward-multiple path)**: the base-case applied multiple sits outside the triangulated range — e.g. you're applying 11× FY+2 EV/EBITDA when peers trade 7.5–10.5×, own 5-year range tops out at ~10×, and sell-side PTs imply 7.7–10.7×. The PT is leaning on a re-rate nobody else assumes.

**Symptom (DCF path)**: DCF target implies 38x P/E; comp set trades at 22x. Or DCF gives 15x P/E for a 25% grower (too low). Here the *output* multiple is the tell.

**Diagnosis**: on the default path the multiple is **chosen explicitly**, so the question is whether the choice is justified against the three anchors. On the DCF path the multiple is an *output*, so the terminal value or growth assumptions are doing more work than they should.

**Response (default path):**

1. **Re-check the triangulation**: where does the applied multiple sit vs (a) peer forward multiples, (b) own ~5-year range, (c) sell-side PT-implied? If it's inside the range, it's defensible — document which anchor supports it and move on.
2. **If you're paying a premium / discount to the range, name the pillar that justifies it** (quality / growth differential, backlog visibility, margin re-rating). A premium with no pillar behind it is the surprise — temper the multiple to the range, OR write a defensible re-rating pillar.
3. **Choose**:
   - Option A: **move the applied multiple back into the triangulated range.** Target moves; direction may stay valid with less upside.
   - Option B: **write a new pillar** that justifies the premium/discount (e.g., *"Re-rating to peer X as mix shifts"*). Legitimate if the re-rate is itself defensible and falsifiable.
   - Option C: **accept the gap** and state in the pitch that the thesis depends on the multiple holding — and add a killing condition on it.

**Response (DCF path):**

1. **Decompose the implied multiple**: pull the equivalent earnings multiple from the DCF target / forward EPS. Compare to comps.
2. **Identify which assumption is responsible**:
   - High terminal growth rate (>3%)? Likely too aggressive.
   - Long explicit forecast period (>10 years)? Compounds error.
   - Terminal margin assumption far above peers? Defensible only if pillars justify it.
   - **If the terminal value is doing most of the work and the inputs are unknowable, that's a signal the name should have been valued on a forward multiple in the first place — revisit the Phase 11 Step 0 method gate.**
3. **Choose**: temper the assumption to match comps (Option A), write a re-rating pillar (Option B), or accept and disclose the dependence (Option C) — same three moves as above.

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

Append to `working/phase12_iteration.md` (the same file as Step 4's audit trail — one canonical iteration log; the pre-Phase-13 checklist reads this filename). Useful for the pitch's transparency: showing your work.

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
