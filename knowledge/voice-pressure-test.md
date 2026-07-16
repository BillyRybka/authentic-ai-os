---
type: reference
scope: shared
loaded_by: [vid-voice-capture, vid-segment, vid-intro, vid-ending, vid-structure]
status: active
tags: [reference, voice, pressure-test]
---

# Voice Pressure Test

How a writing skill validates its output before saving. Read [[voice-profile-schema]] first for what is stored and why. This file is the check.

## Why pressure-test

The brain dump is the voice. The reference pieces show its grain. Between input and output, Claude adds connective tissue (transitions, restructuring, light polish). Drift happens in that connective tissue. The pressure test catches it before the creator does.

It validates by ear against the creator's real passages. It does not compare against stored numbers, because no numbers are stored. Rhythm is a thing you hear, not a target you hit.

## When to run

- At the end of any writing skill (`vid-intro`, `vid-segment`, `vid-ending`, `vid-structure`) before output is saved.
- At the end of `vid-voice-capture` when the creator reads the curated passages back.
- When a creator says "this doesn't sound like me": run it against the rejected piece, find what it violates, log for the next refresh.

## Pass 1: guardrail check (always runs)

Against `foundation/voice-profile.md`:

1. **Signature phrases.** Does the piece contain or closely echo at least one? Long-form should surface one or two naturally. Zero is a weak-signal flag, not an automatic fail. Never pad to hit a count.
2. **Refusals: anti-patterns.** Scan for any. Even one is a hard reject. Includes em-dashes and real profanity in place of the clean register.
3. **Refusals: words avoided.** Each hit is a soft reject. Auto-swap to the paired replacement or flag.
4. **Refusals: creator hard rules.** The named rules (for example: no scripted text anywhere for a creator-designated improvised moment, no carpet-bombed or cadence-placed emphasis device). Any breach is a hard reject.
5. **POV and energy.** Does the pronoun use match the creator's default? Does the piece sit at or above the energy floor? Qualitative. Claude makes the call and flags if unsure.

## Pass 2: grain check (only if a reference-pieces folder exists for the piece's `voice_context`)

No statistics. The method is the ear.

1. Load the passages in `foundation/reference-pieces/{voice_context}.md` (the `## ` sections inside).
2. Read a representative reference passage aloud, then read the produced section aloud right after it.
3. Judge, by that back-to-back read: does the output's sentence-length variation, paragraph shape, opener move, and energy feel like it came from the same person in the same mode? Real voice mixes short punchy lines with longer ones that earn their length. A section that runs all-uniform reads as a summary even when every word-rule passed.
4. If the output drifts from the reference grain (flat rhythm, wrong opener default, energy off for this context), it is a soft reject. Restructure toward the reference feel, do not bolt on phrases.

If no folder exists for this `voice_context`, Pass 2 is skipped. Note the gap in the output meta so the creator can add sources for that context. If the `context_flex` line marks the context `deprecated`, log a warning and run Pass 1 only.

## Severity tiers

- **Hard reject.** Anti-pattern present, creator hard rule breached, or POV violation. Do not save. Restructure.
- **Soft reject.** Words-avoided hit, or grain clearly off against the reference pieces. Auto-swap if possible, otherwise flag for creator review before save.
- **Soft warn.** Zero signature-phrase echo in long-form, or opener default not matched. Flag in meta, allow save.
- **Pass with note.** Within tolerance. Save with a one-line summary in `piece.md`.

## The read-aloud test (final arbiter)

After the checks:

> "Read the output aloud. If you would reword anything, the test failed."

This overrides every mechanical pass. Numbers and pattern-matching can pass while the output still feels off. The creator's mouth knows. If they would reword: drop back to the brain dump, find what got over-polished, restructure preserving the creator's exact phrasing for that beat.

## Reporting the result

Each writing skill surfaces its voice-check result to the creator in chat (pass / soft-warn / soft-reject / hard-reject, plus any flags) at save time, so the creator sees it live. It is NOT persisted to `piece.md`.

The check's job is to protect the prose in the moment. Sharpening voice over time is a separate mechanism: when the creator reacts to a line ("I'd never say that", "drop that word"), `vid-voice-update` catches the reaction and writes the rule into `foundation/voice-profile.md`. That live reaction, not a stored log, is what improves the profile. If a persisted history is ever needed (for a future `vid-measurement` or a `vid-voice-capture` drift report), add the field back then, with that reader on the other end.

## Failure modes

- **Reference set thin or absent for a context.** Pass 2 skipped, gap noted. Suggest the creator add sources for that `voice_context`.
- **Brain dump conflicts with the guardrail.** The brain dump wins. It is the creator's actual words for this piece. If the new pattern persists across pieces, update the profile at the next refresh.
- **Passes mechanically but the creator rejects it on read-aloud.** The ear caught what the checks missed. Log what the creator changed. That is a candidate refusal or a sign the reference set needs a better passage.
