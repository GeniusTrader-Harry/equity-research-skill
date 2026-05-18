# Phase 9 — Steel-Man (Counter-Pillars → Risk List)

**Goal**: Draft the **strongest possible counter-arguments** to the chosen direction. Don't strawman the other side. The counter-pillars become the risk section of the pitch — they don't become a parallel thesis.

**Output**: `working/risks.md` with 2–3 counter-pillars. Tight: ~1 page total, ~150-200 words each.

## Why this matters

A thesis that hasn't been steel-manned is one you haven't tested. Two values:

1. **Methodological honesty**: confront the strongest version of disagreement, not a weak version you can dismiss.
2. **Pitch defense**: every interviewer's first question is *"what's the bear case?"* — pre-drafted rejection separates a confident analyst from a wishful one.

## Steel-manning vs straw-manning

- **Straw-manning**: "The bear case is [obviously weak version]." Useless, dishonest, caught immediately.
- **Steel-manning**: "The strongest bear case is [the version a smart short-seller would argue, with the best evidence]. We reject it because [specific evidence-grounded reasons]."

If you can't steel-man the other side, you don't understand the trade.

## Process

### Step 1 — Pull opposite-direction asymmetries from Phase 6

If Phase 7 chose LONG: pull bearish-leaning asymmetries.
If SHORT: pull bullish-leaning.

These are your raw material. Don't invent new counter-arguments — use what the evidence already surfaced.

### Step 2 — Draft 2–3 counter-pillars, tight format

Each counter-pillar has three short sections only:

1. **Claim** (2-3 sentences) — what bear has to be true, in its strongest defensible form. Don't tone it down.
2. **Mechanism** (1-2 sentences) — why this would damage the thesis. Which thesis pillar(s) it hits.
3. **Why I reject** (3 bullets max, each with verifiable citation) — evidence-grounded rejection, not vibes.

**Do NOT include in Phase 9 output**:
- Severity / target-price-impact estimates — gut-sized at this stage; Phase 11 model produces real numbers
- "What would make this real" subsection — overlaps with Phase 10 killing conditions; defer
- 5-element claim/driver/mechanism/magnitude/timeframe template — that's for offensive pillars; counter-pillars don't need full structure
- Summary scorecard table — adds length without information
- Lengthy direction-commit defense — if your pillars hold, the rejections speak for themselves

Target length per counter: ~150-200 words. Total file: ~1 page.

### Step 3 — Acceptable vs unacceptable rejections

Acceptable rejection reasons (each must cite specific evidence):
- **Lower probability**: evidence weight favors the thesis side, with specific evidence cited
- **Already priced in**: cite multiple compression, sentiment indicators, or short interest
- **Structural mitigant**: a specific mechanism the counter ignores, with source
- **Beyond timeframe**: counter is real but plays out longer than the investment window

Unacceptable rejections (red flags — push back):
- *"Management says it won't happen"* — mgmt always says this. Not evidence.
- *"Hasn't happened yet"* — neither has the bull thesis.
- *"The Street doesn't worry about it"* — Street consensus is what you're betting against.
- *"Feels low probability"* — vibes are not evidence.

If you can't articulate a non-vibey rejection, the counter may be **stronger than your pillars** — sign to revisit Phase 7.

### Step 4 — Output format

```markdown
# [TICKER] Counter-Pillars / Risks (Phase 9 Steel-Man)
Direction: [LONG / SHORT], [conviction]

[1-sentence framing: severity → Phase 11 model; killing conditions → Phase 10.]

## Counter-Pillar 1 — [title]
**Claim**: [2-3 sentences, strongest form]
**Mechanism**: [1-2 sentences, which pillar(s) hit]
**Why I reject**:
- [bullet with citation]
- [bullet with citation]
- [bullet with citation]

## Counter-Pillar 2 — [title]
[same format]

## Counter-Pillar 3 — [title]
[same format]

## Q&A interlude
[1-2 sentences prompting "finalize" or "interrogate/sharpen"]
```

### Step 5 — Q&A interlude (HEAVY)

Prompt:
> "Phase 9: [N] counter-pillars drafted with claim + mechanism + rejection. Severity and killing conditions deferred to Phases 10-11. Review the rejections — any weak? Common asks: 'sharpen the bear case on [N],' 'I don't buy the rejection on [M] — push harder,' 'is there a stronger counter we're missing?' When satisfied, say 'finalize.'"

Common iterations:
- *"Counter [N] too weak"* — draft more aggressive version, push magnitude
- *"Rejection on [M] is hand-wavy"* — provide harder evidence, or admit the counter weakens the thesis
- *"Strongest possible bear case?"* — synthesize from all bearish evidence
- *"Should we pivot direction?"* — if steel-manned counter is as strong as the thesis, real question. Honest answer beats commitment.

### Step 6 — If steel-manning kills the thesis

If counters are as strong or stronger than the direction:
- Don't force through. Pause.
- Recommend: revisit Phase 7. Options: flip, downgrade conviction, or pass.
- This is a feature. Surviving steel-manning makes the thesis more defensible.

### Step 7 — Finalize

When user says "finalize":
- Lock counter-pillars
- Confirm: *"[N] counter-pillars locked. Proceeding to Phase 10 (pillar audit with killing conditions)."*

## How Phase 9 feeds downstream phases

- **Phase 10** uses the counter-pillars to stress-test the thesis pillars. Killing conditions for each thesis pillar are drafted there using the counter-pillar mechanics as triggers.
- **Phase 11** quantifies severity. The model's bear-case envelope is built using the counter-pillar mechanics as the swing-down assumption set.
- **Phase 13** pitch risk section uses the Phase 9 claim + mechanism + compressed rejection. Don't paraphrase between phases.

## What this is NOT

- NOT a parallel thesis (no bull/bear/base full theses)
- NOT a list of every risk imaginable (only the strongest 2–3)
- NOT a 10-K risk section (hundred items, all hedged) — this is 2–3 specific arguments with rejection
- NOT a quantification exercise — severity belongs in Phase 11

## Critical reminder

The skill must NOT default to weak counter-arguments because they're easier to dismiss. If the user accepts a weak counter, push back: *"This counter feels weak. The strongest bear case is more like [X]. Want to take that on?"*

Honest test: would a smart short-seller (if you're long) or a smart bull (if you're short) recognize this as their argument? If not, sharpen.
