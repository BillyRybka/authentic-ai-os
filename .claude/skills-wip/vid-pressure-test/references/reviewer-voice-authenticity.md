---
type: reference
skill: vid-pressure-test
reviewer: voice-authenticity
tags: [reviewer-rubric, voice]
---

# Voice-Authenticity Reviewer Rubric

Phase 2 reviewer 2. Fresh-context spawn. Single job: every line in the script must survive the read-aloud test in the creator's voice. Lines that fail get flagged with a suggested rewrite.

## What to scan

Read script.md sentence by sentence. For each sentence, ask:

1. Would the creator say this out loud on camera, exactly as written?
2. Does the phrasing match the grain of the reference pieces for this piece's `voice_context`?
3. Does it use any word from the guardrail's `refusals` (words avoided)?
4. Does it match any anti-pattern or breach a creator hard rule in the guardrail's `refusals`?
5. Does it use a required swap from Context/brand.md without applying the swap?

## Sources of truth

1. `foundation/reference-pieces/{voice_context}.md`: the creator's real intact passages for this delivery medium, as `## ` sections. The gold standard and the seed. Read `voice_context` from piece.md (default `youtube-script`).
2. `foundation/voice-profile.md`: the thin guardrail (fingerprint, signature phrases, refusals, POV/energy). Constraints only. Contract in `knowledge/voice-profile-schema.md`.
3. `Context/brand.md`: banned words and required swaps.

The reference pieces are the gold standard. If a line reads sharper or weaker than the reference pieces in the same `voice_context`, that is a calibration signal. Rhythm is judged by ear against them, never against stored numbers.

## Severity tiers

**Hard issue (voice violation):**

- Word from the guardrail's `refusals` (words avoided) used in the script
- Banned word from brand.md used without the required swap
- Anti-pattern or breached creator hard rule from the guardrail's `refusals` (e.g., contrast-template, hedge stack, AI-default phrasing, a scripted improvised moment) clearly present
- Em-dashes anywhere

**Soft issue (worth flagging):**

- Rhythm mismatch from reference-pieces (sentence too long, too clipped, wrong cadence)
- Generic phrasing where creator usually goes specific
- Energy mismatch (script is flat where reference-pieces hit harder)
- A line that reads fine but feels like a Claude default rather than the creator

## Returning the top 3

Rank by severity. Hard violations first. Then anti-patterns. Then rhythm mismatches.

Each issue surfaces with:

```
Reviewer: voice-authenticity
Location: {section} line {N}
Quote: "{exact text from script.md}"
Issue: {what voice rule failed and why}
Suggested rewrite: "{the line rewritten in the creator's voice}"
```

The suggested rewrite must itself pass the read-aloud test. Read it in your head as if the creator is speaking. If you would reword it, do not suggest it.

## Worked examples

### Example 1: words-avoided violation (HARD)

The guardrail `refusals` list words avoided: leverage, unlock, elevate, ecosystem.

Script line: "...so you can leverage this for any video."

```
Location: Segment 1 line 12
Quote: "...so you can leverage this for any video."
Issue: "leverage" is a refusal (word avoided). The creator never uses it in the reference pieces.
Suggested rewrite: "...so you can use this on any video."
```

### Example 2: brand.md required swap missed (HARD)

brand.md says: required swap "ship" -> "post" for content references.

Script line: "When you ship your next video..."

```
Location: Ending line 5
Quote: "When you ship your next video..."
Issue: "ship" must swap to "post" per brand.md (software metaphor for content).
Suggested rewrite: "When you post your next video..."
```

### Example 3: contrast-template anti-pattern (HARD)

The guardrail `refusals` include the anti-pattern "contrast-template (not X, but Y)".

Script line: "It is not about doing more. It is about doing the right things."

```
Location: Segment 3 line 1
Quote: "It is not about doing more. It is about doing the right things."
Issue: Classic contrast-template structure ("not X, but Y"). Anti-pattern in the guardrail refusals. Creator does not use this rhythm in the reference pieces.
Suggested rewrite: "Doing more is not the move. Doing the right things is." OR cut and rewrite from creator's actual phrasing in brain-dump.
```

### Example 4: rhythm mismatch from reference-pieces (SOFT)

reference-pieces show creator opens body segments with short declarative sentences (5-9 words).

Script segment 2 opens: "There are a few things I want to walk through here that took me a while to figure out, and I think they will save you a lot of time."

```
Location: Segment 2 line 1
Quote: "There are a few things I want to walk through here that took me a while to figure out, and I think they will save you a lot of time."
Issue: 30-word run-on opener. Reference-pieces show 5-9 word openers for body segments. The rhythm is off.
Suggested rewrite: "Here is what took me three years to figure out." (10 words; sharper opener matching reference-pieces style.)
```

### Example 5: AI-default phrasing (HARD)

Script line: "Let me show you exactly how to dive into this strategy."

```
Location: Intro line 6
Quote: "Let me show you exactly how to dive into this strategy."
Issue: "dive into" is a banned transition phrase per transition-bank Tier 1 AND a guardrail refusal anti-pattern.
Suggested rewrite: "Here is exactly how this works." OR mirror the creator's actual transition from the reference pieces.
```

## What this reviewer does NOT catch

- Fabricated claims or unsupported numbers (source-traceability)
- Banned generic phrases like "in this video" that are AI-tells not voice violations (AI-slop reviewer)
- Setup-payoff structure or thread closure (retention-logic)

If a phrase is BOTH a banned phrase (AI-slop) AND a voice violation (a guardrail refusal), it will get caught by both. That is fine. Consolidation in Phase 3 will dedup with both attributions.

## The read-aloud test as the meta-check

After surfacing the 3 issues, the reviewer asks itself: "Would the creator agree with these flags when they read the script aloud?" If two or more flags feel debatable, the reviewer is reading too aggressively. Re-rank. Surface only the lines that clearly fail.
