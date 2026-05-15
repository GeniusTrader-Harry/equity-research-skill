# Phase 9 — Steel-Man (Counter-Pillars → Risk List)

**Goal**: Draft the **strongest possible counter-arguments** to the chosen direction. Don't strawman the other side. The counter-pillars become the risk section of the pitch — they don't become a parallel thesis.

**Output**: `working/risks.md` with 2–3 counter-pillars + skill's reasoning for why each is rejectable but real.

## Why this matters

A thesis that hasn't been steel-manned is a thesis you don't actually believe — you just haven't tested it. Two specific values:

1. **Methodological honesty**: forces you to confront the strongest version of disagreement, not a weak version you can easily dismiss
2. **Pitch defense at interviews/PMs**: every interviewer's first question is *"what's the bear case?"* — having pre-drafted the strongest counter and your specific reasons for rejecting it is what separates a confident analyst from a wishful one

## Steel-manning vs. straw-manning

- **Straw-manning**: "The bear case is [obviously weak version that's easy to dismiss]." — useless, dishonest, gets caught immediately.
- **Steel-manning**: "The strongest bear case is [the version a smart short-seller would argue, with the best evidence available]. We reject it because [specific reasons grounded in evidence]."

If you can't steel-man the other side, you don't understand the other side, which means you don't understand the trade.

## Process

### Step 1 — Pull opposite-direction asymmetries from Phase 6

If Phase 7 chose LONG: pull bearish-leaning asymmetries from Phase 6.
If Phase 7 chose SHORT: pull bullish-leaning asymmetries.

These are your raw material. Don't invent new counter-arguments — use the ones the evidence already surfaced.

### Step 2 — Draft 2–3 counter-pillars in the same 5-element format

Each counter-pillar follows the Phase 8 template:

> *"[Driver] will [opposite direction] [magnitude] by [date] because [mechanism], driving [adverse P&L impact]."*

**Critical**: the counter-pillar must be in the **strongest** form. Don't tone it down. If the bearish argument is "GM compresses 600bps," write 600bps, not 200bps.

### Step 3 — For each counter-pillar, write the rejection reasoning

Why are you NOT going with the counter? Acceptable reasons:

- **Lower probability**: the evidence base supports your direction more than this one (cite specific evidence weight)
- **Smaller magnitude**: even if true, this counter-pillar moves the target less than your direction's pillars (we'll quantify in Phase 10)
- **Already priced in**: the market is already discounting this risk (cite multiple compression / sentiment indicators)
- **Mitigated by [X]**: there's a structural mitigant the counter-pillar ignores
- **Slower timeframe**: the counter-pillar is real but plays out over a longer horizon than your investment timeframe

**Unacceptable reasons** (these are red flags — push back):
- *"Management says it won't happen"* — mgmt always says risks won't happen. Not evidence.
- *"It hasn't happened yet"* — neither has your bull thesis yet.
- *"The Street doesn't worry about it"* — Street consensus is what we're betting against; their non-worry isn't evidence.
- *"Just feels low probability"* — vibes are not evidence.

If you can't articulate a non-vibey rejection, the counter-pillar may be **stronger than your thesis pillars** — a sign you should re-examine the direction commit (kicks back to Phase 7).

### Step 4 — Format the output

```markdown
# [TICKER] Counter-Pillars / Risks
Direction taken: [LONG / SHORT]
Counter-pillars are the strongest arguments for the OPPOSITE direction.

## Counter-Pillar 1 — [title]
**Statement**: "[full 5-element sentence]"

**Why we reject this** (steel-manned rejection):
[paragraph with specific evidence — not vibes]

**What would make this real**:
[the conditions under which this counter would actually win — feeds Phase 10 killing conditions for your pillars]

**Severity if it plays out**: [estimated target price impact — back-of-envelope; Phase 10 will sharpen]

---

## Counter-Pillar 2 — [title]
[same format]

---

## Counter-Pillar 3 — [title]
[same format]
```

### Step 5 — Q&A interlude (HEAVY)

Prompt:

> "Phase 9: [N] counter-pillars drafted with rejection reasoning. These will become the risk section of the pitch. Review the rejections — are any of them weak? If so, that's a signal to revisit Phase 7 direction. Common asks: 'sharpen the bear case on [N],' 'I don't buy the rejection on [M] — push harder,' 'is there a stronger counter we're missing?' When satisfied, say 'finalize.'"

Common iterations:
- *"Counter [N] is too weak — make it stronger"* — draft a more aggressive version, push the magnitude
- *"The rejection on [M] is hand-wavy"* — provide harder evidence, or admit the counter is real and weakens your thesis
- *"What's the strongest possible bear (or bull) case?"* — synthesize from all bearish/bullish evidence regardless of source
- *"Should we pivot to short (or long) instead?"* — if the steel-manned counter is genuinely as strong as your thesis, this is a real question. Honest answer matters more than commitment.

### Step 6 — If steel-manning kills the thesis

If during Phase 9 the user concludes the counter-arguments are as strong or stronger than the chosen direction:

- Don't force through. Pause.
- Recommend: revisit Phase 7 direction commit. Options: flip direction, downgrade conviction, or pass.
- This is a feature, not a failure. Steel-manning that survives the work is a *more* defensible thesis.

### Step 7 — Finalize

When user says "finalize":
- Lock counter-pillars and rejection reasoning
- Save to `working/risks.md`
- Confirm: *"[N] counter-pillars locked as risks. Proceeding to Phase 10 (pillar audit)."*

## How counter-pillars feed Phase 13 (the pitch)

In the final pitch, the risks section reads:

```
Risks:
1. [Counter-pillar 1 in compressed form]
   Why we still hold the call: [rejection reasoning compressed]
2. [Counter-pillar 2]
   ...
```

Don't paraphrase between phases. The Phase 9 rejection reasoning is what appears in the pitch. Sharpen now to avoid rewriting later.

## What this is NOT

- NOT a parallel thesis (we're not building bull/bear/base full theses)
- NOT a list of every risk imaginable (only the strongest 2–3 counter-arguments)
- NOT a generic risk section like a 10-K (those are a hundred items, all hedged; this is 2–3 specific arguments with rejection reasoning)

## Critical reminder

Steel-manning is hard. The skill must NOT default to weak counter-arguments because they're easier to dismiss. If the user accepts a weak counter, the skill should push back: *"This counter feels weak. The strongest bear case for this name is more like [X]. Want to take that on?"*

The honest test: would a smart short-seller (if you're long) or a smart bull (if you're short) recognize this as their argument? If not, sharpen.
