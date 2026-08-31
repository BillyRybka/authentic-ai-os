---
type: reference
skill: vid-pressure-test
reviewer: ai-slop
tags: [reviewer-rubric, ai-slop]
---

# AI-Slop Reviewer Rubric

Phase 2 reviewer 3. Fresh-context spawn. Single job: catch the prose patterns that read as AI-written even when each individual sentence is grammatically fine. AI-slop is what cold viewers detect in the first 10 seconds that makes them tap away.

## What AI-slop is

The signature of unedited LLM output. Common shapes:

- **Banned transition phrases.** "Let me dive in." "Let's talk about." "Now let me show you." "At the end of the day." "It is worth noting." "Here is the thing." (Tier 1 of transition-patterns, plus the house banned-word list.)
- **Vague value language.** "Move the needle." "Unlock." "Elevate." "Transform." "Game changer." "Insane." "Revolutionary." (See feedback memory `feedback_no_vague_ai_language`.)
- **Announcing transitions.** "Now I want to share something important." "Here is where it gets interesting." "Let me explain why this matters."
- **Three-item-list crutch.** Every paragraph closes with a rule-of-three list. Reads as AI-default.
- **Em-dashes.** House rule: zero em-dashes in any productized output. The em-dash is the AI tell the house rules define against.
- **Hedge stacks.** "Maybe you might want to perhaps consider..." Hedges undermine stakes.
- **Generic CTAs.** "Smash the like button." "Don't forget to subscribe." Anti-patterns per voice-profile.
- **Filler openers.** "So..." or "Alright..." or "Let's see..." stacked at the front of multiple sentences in a row.
- **The "it is worth noting" tell.** Any sentence that starts with meta-commentary about the importance of what follows, instead of just stating the thing.

## Sources of truth

1. `foundation/voice-profile.md` `refusals`: the creator's words-avoided and anti-patterns
2. `knowledge/transition-patterns.md` Section 4: Tier 1 banned phrases (auto-reject)
3. `knowledge/intro-architecture.md`: banned transitions
4. The universal AI-slop list in the severity tiers below (vague AI language, weak verbs, and the em-dash hard rule apply to every creator, no file needed)

## Severity tiers

**Hard issue (auto-fail):**

- Em-dashes anywhere
- Tier 1 banned phrase from transition-patterns Section 4 (let me dive in, let me tell you, let's talk about, and finally / lastly)
- Word from the voice-profile `refusals` used raw (a words-avoided term, or a required swap left unapplied)
- Vague value words ("leverage," "unlock," "elevate," "transform," "move the needle," "game changer") in copy that should be specific

**Soft issue (worth flagging):**

- Announcing transition that could be cut to just do the thing
- Hedge stack that undermines stakes
- Three-item-list crutch repeated in 3+ paragraphs
- Filler opener stacking
- "It is worth noting" / "it is important to remember" meta-commentary

## Returning the top 3

Rank by severity. Em-dashes first (zero-tolerance house rule). Then Tier 1 banned phrases. Then vague value words. Soft issues only surface if there are fewer than 3 hard issues.

Each issue:

```
Reviewer: ai-slop
Location: {section} line {N}
Quote: "{exact text from script.md}"
Issue: {what AI-slop pattern fired and why}
Suggested fix: {specific replacement or "just cut this line"}
```

## Worked examples

### Example 1: Tier 1 banned phrase (HARD)

Script transition: "Let me dive into the first thing."

```
Location: Transition after Intro
Quote: "Let me dive into the first thing."
Issue: "dive into" is Tier 1 banned per transition-patterns Section 4. Auto-reject.
Suggested fix: "Here is the first thing." OR mirror the creator's transition style from reference-pieces.
```

### Example 2: em-dash (HARD)

Script line contains an em-dash between "simple" and "just stop" (the character is intentionally not pasted in this example file per house rule).

```
Location: Segment 1 line 4
Quote: [script line with em-dash between "simple" and "just stop"]
Issue: Em-dash. House rule, zero tolerance.
Suggested fix: "The fix is simple. Just stop doing it." (period) OR "The fix is simple, just stop doing it." (comma).
```

### Example 3: vague value language (HARD)

Script line: "This one shift will unlock your growth."

```
Location: Intro line 3
Quote: "This one shift will unlock your growth."
Issue: "unlock" is vague AI-language. Per feedback memory, creator never uses it. Use specific outcome instead.
Suggested fix: "This one shift doubled my monthly views." (or whatever specific number actually applies from brain-dump).
```

### Example 4: announcing transition (SOFT)

Script line: "Now let me show you something I think you will find interesting."

```
Location: Segment 2 opener
Quote: "Now let me show you something I think you will find interesting."
Issue: Announcing transition. Tells the viewer to expect interesting content instead of just being interesting.
Suggested fix: Cut the announcement. Open with the thing itself. "Three months ago I tried..." or whatever the actual content is.
```

### Example 5: three-item-list crutch (SOFT)

Across segments 1, 2, and 3, every paragraph ends with a three-item rule-of-three list. (e.g., "...stronger, faster, and more durable." / "...time, focus, and energy." / "...what works, what does not, and why.")

```
Location: Segments 1-3 (pattern across multiple closes)
Quote: "...stronger, faster, and more durable." (1 of 3 instances)
Issue: Rule-of-three closing list repeated in every paragraph. Reads as AI-default rhythm. Reference-pieces vary cadence.
Suggested fix: Break the pattern. Convert one or two of these closes to a single sharp statement, or to a contrast pair, or to a single-word punch.
```

## What this reviewer does NOT catch

- Untraceable claims (source-traceability)
- Voice violations against creator-specific guardrail refusals (voice-authenticity reviewer)
- Retention or structure problems (retention-logic)

There IS overlap with voice-authenticity for things like "dive into" (which is both AI-slop and a voice violation). That overlap is fine. Phase 3 consolidation dedups with both attributions, which signals to the creator that two independent lenses caught the same thing.

## A note on tone

The reviewer's job is to flag, not to scold. Surface what fired and why. Suggest a fix in the creator's voice (mirror reference-pieces rhythm). The creator decides.

## A meta-check before returning

After ranking the top 3, ask: "Would I want to read this script after these fixes?" If yes, the fixes are correct. If the script would still read as AI-slop after these 3 fixes, there are more issues than the cap allows. Surface the 3 worst, but note in the issue blob: "additional slop patterns detected; consider a second pass after these fix."
