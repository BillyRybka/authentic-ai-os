---
type: reference
scope: shared
loaded_by: [vid-voice-capture, vid-segment, vid-hook, vid-ending, vid-structure, vid-foundation]
status: active
tags: [reference, voice, pressure-test]
---

# Voice Pressure Test

How writing skills validate produced output against `foundation/voice-profile.md` to ensure voice preservation. Used both during writing (to catch drift before saving) and during the vid-voice-capture read-aloud step (to confirm captured patterns are real).

## Why pressure-test

The brain dump is the voice. The voice profile is the preservation checklist. Between input and output, Claude adds connective tissue (transitions, restructuring, light polish). Drift happens in that connective tissue. The pressure test catches it before the creator does.

## When to run

- **At the end of any writing skill** (vid-segment, vid-hook, vid-ending) before output is saved
- **At the end of vid-voice-capture Stage 6** to validate that extracted patterns survive the creator's own read-aloud
- **When a creator says "this doesn't sound like me"** — run pressure test against the rejected piece, find which patterns the output violates, log for next refresh

## The two-pass check

### Pass 1: Core profile validation (Layer 1)

Always runs. Checks the produced output against the cross-context core fields.

For each output paragraph, verify:

1. **Recurring phrases.** Does the piece contain at least one core recurring phrase, or echo one closely? Long-form pieces should contain 2-3. If zero, voice signal is weak.

2. **Anti-patterns.** Scan for any phrase in `anti_patterns`. Hard reject — even one anti-pattern means the output failed.

3. **Words avoided.** Scan for any word in `words_avoided`. Each hit is a soft reject — flag for manual review or auto-swap to the preferred replacement.

4. **POV consistency.** Does the output match the creator's POV defaults? "I" used for what they use I for, "you" used appropriately, no rogue "we"-as-plural drift.

5. **Energy match.** Does the piece feel like the energy_baseline? Reading it aloud, does it match the descriptor? This is qualitative — Claude makes the call but flags if uncertain.

6. **Rhetorical baseline.** If the creator uses metaphors every 3-4 paragraphs and the output has zero metaphors in 12 paragraphs, flag. Same for rhetorical questions, callbacks, etc.

### Pass 2: Context map validation (Layer 2)

Runs only if a context map exists for what the skill is producing.

For each section of output, verify against the matched context map:

1. **Sentence rhythm.** Does the actual rhythm of the output approximate the creator's distribution for this context? If the creator's YouTube voice is 75% short sentences and the output is 30% short, the rhythm is wrong.

2. **Paragraph structure ratio.** If the creator's newsletter is 65% single-sentence paragraphs and the output is 20%, the structure is wrong for context.

3. **Punctuation signature.** If the context map says "9 em-dashes per 1000 words" and the output has 1 in a 1500-word piece, the punctuation pattern is off.

4. **Opener pattern.** Does the piece open with the dominant opener for this context? If the creator's YouTube is 70% question-opens and the script opens with a declaration, flag (could be intentional, could be drift — surface for review).

5. **Closing pattern.** Does the close match the context's CTA pattern?

6. **Energy modulation.** Does the energy match the modulation note for this context (dialed up for YouTube vs. dialed down for email)?

7. **Format-specific phrases.** If the context map has phrases that should appear in this format, are they present or echoed?

## Severity tiers

Not every drift is equal. Use these tiers:

- **Hard reject** — anti-pattern present, or POV violation. Don't save. Restructure.
- **Soft reject** — word from `words_avoided` present, or sentence rhythm severely off. Auto-swap if possible, otherwise flag for creator review before save.
- **Soft warn** — opener pattern doesn't match dominant context default, or a recurring phrase is absent in long-form. Flag in output meta but allow save.
- **Pass with note** — patterns within tolerance. Save with a one-line voice-pressure-test summary in meta.

## The read-aloud test

After all quantitative checks, run the human-in-the-loop check:

> "Read the output aloud. If you'd reword anything, the test failed."

This is the final arbiter. Numbers and pattern-matching can pass while the output still feels off. The creator's mouth knows.

In standalone vid-voice-capture (Stage 6), the read-aloud runs against quoted patterns from the profile itself. In writing skills, the read-aloud runs against the produced piece.

If creator reads aloud and would reword: drop back to brain dump, find what was over-polished, re-structure preserving creator's exact phrasing for that beat.

## Logging

Each writing skill that uses pressure-test logs its result in the piece's `meta.md`:

```yaml
voice_pressure_test:
  date: YYYY-MM-DD
  result: pass | soft-warn | soft-reject | hard-reject
  layer1_pass: true | false
  layer2_context: youtube-script | newsletter | linkedin | etc
  layer2_pass: true | false
  flags: [list of any soft warnings or rejects]
  read_aloud_confirmed: true | false
```

This log feeds future refresh runs of vid-voice-capture — repeated drift on the same field signals the profile needs updating.

## What pressure-test does NOT do

- It doesn't generate. It validates.
- It doesn't override creator brain dump phrasing — if the creator's actual words seem to violate a captured pattern, the brain dump wins. The profile is descriptive, not prescriptive.
- It doesn't replace the read-aloud test. Quantitative checks are a pre-filter; the creator's ear is final.
- It doesn't enforce one-size-fits-all. Layer 2 context maps exist precisely so the test adapts to format.

## Failure modes

- **Profile drift.** If pressure-test repeatedly fails on the same pattern across multiple pieces, the profile is stale. Trigger vid-voice-capture refresh.
- **Context-map mismatch.** Writing skill producing for a context that has no map yet. Falls back to core only. Note the gap; suggest creator gather more sources for that context.
- **Brain dump conflicts with profile.** If the creator's brain dump for THIS piece uses phrasing that contradicts the profile, the brain dump wins. Update the profile in the next refresh if the new pattern persists.
- **Output passes mechanically but creator rejects in read-aloud.** The mechanical pass missed something the ear caught. Log what creator changed; that's a candidate field for the profile or an addition to anti-patterns.
