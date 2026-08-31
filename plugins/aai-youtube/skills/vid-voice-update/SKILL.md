---
name: vid-voice-update
description: Triage a creator's mid-draft voice signal and surgically update foundation/voice-profile.md when, and only when, the correction is permanent. Three signal types are handled. Hard rule ("never use X", "swap Y for Z", "I'd never write that") appends to refusals and re-runs the voice audit on the in-progress draft. One-time edit ("this line is off here", "doesn't fit this segment") rewrites the line in place and saves nothing. Preference shift ("I don't love that", "try something else") is ambiguous, so the skill asks the creator which it is, then routes. Triggers on "never use X", "I'd never say that", "swap Y for Z", "I hate that word", "drop X from my voice", "voice update", "add a refusal", or any mid-draft creator reaction that signals a voice correction.
---

# Voice Update

Reading the signal correctly is the work. Not every correction is a permanent rule. Some are one-time fits-this-line-only edits. Some are vague preference shifts the creator has not yet decided about. The skill triages, asks when it cannot tell, and writes to `foundation/voice-profile.md` refusals only when the correction is permanent.

This skill is sibling to the writing skills. `vid-intro`, `vid-segment`, and `vid-ending` hand off to it when the creator reacts to a generated line. It is also callable standalone when the creator wants to add a rule outside a draft session.

> **Resolving `knowledge/` paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist, load `knowledge/X.md` relative to the repo root instead.

## What this produces

Depends on the signal type:

- **Hard rule**: one new entry in `foundation/voice-profile.md` refusals (words-avoided with reason, anti-pattern, or hard creator rule depending on shape), and a pressure-test or voice-audit re-run on the in-progress draft so it picks up the new rule. No other files touched.
- **One-time edit**: zero file changes to `foundation/`. The current draft line is rewritten in place by the calling writing skill, not by this one.
- **Preference shift, confirmed permanent**: same as hard rule.
- **Preference shift, confirmed one-time**: same as one-time edit.

## Invocation modes

**Sub-skill (most common).** A writing skill (`vid-intro`, `vid-segment`, `vid-ending`) hands off when the creator reacts to a line during the read-aloud or review step. The writing skill provides the line, the creator's reaction, and the piece slug. This skill triages, applies, and returns control with a status (`{applied: refusal | rewrite_only | none, refusal_added?, rerun_recommended?}`).

**Standalone.** The creator invokes directly with a new rule outside an active draft. Skill captures the rule, classifies, writes, confirms. No re-run because no in-progress draft to re-run against.

## When to run

- A writing skill detected a creator-reaction phrase during draft review
- The creator explicitly says "add a refusal" or "update my voice"
- The creator pastes a line they corrected in a published piece and wants the rule captured

## Prerequisites

- `foundation/voice-profile.md` exists (the file this skill appends to)
- `knowledge/voice-profile-schema.md` (for refusal shape and section structure)

If `voice-profile.md` does not exist, refuse to run and tell the creator to run `vid-voice-capture` first.

## Load at session start

1. `foundation/voice-profile.md` (the target file)
2. `knowledge/voice-profile-schema.md` (refusal shape: words-avoided as `word to swap (reason)`, anti-pattern as full phrasing, hard creator rule as named explicit rule)

That is the full load. This is a surgical-write skill, not an analysis skill.

## The three signal types

### Hard rule (permanent)

Pattern signals: `never use X`, `always Y`, `I'd never write that`, `I hate X`, `swap Y for Z`, `drop X`, `cut X from my voice`, `don't ever say X`.

Action: classify the rule shape, then append to `foundation/voice-profile.md` refusals.

Refusal shapes (from `knowledge/voice-profile-schema.md`):

- **Words-avoided**: a single word or short phrase to swap. Entry format `word to swap (one-line reason)`. The reason is required so future drafts can generalize to unseen offenders.
- **Anti-pattern**: a structural phrasing the creator never uses (a contrast template, a hedge stack, an opening cliche). Full phrasing entry, not a swap.
- **Hard creator rule**: a named explicit rule the creator declares (a never-script moment, a peak-only intensity device, a banned register shift).

Ask which shape applies if it is not obvious from the creator's phrasing. Default to words-avoided for single-word reactions.

### One-time edit (local)

Pattern signals: `this line specifically`, `here`, `in this segment`, `for this piece`, `doesn't fit this part`, `just this once`.

Action: do not write to `foundation/`. Return to the calling writing skill with a rewrite suggestion or accept the creator's rewrite as-is. The skill is acting as a gate that says "this is local, not a rule." Save nothing permanent.

### Preference shift (ambiguous)

Pattern signals: `I don't love that`, `try something else`, `that's not it`, `not quite right`, `feels off`, `something better`.

Action: ask the creator one direct question:

> "Do you want this avoided in future drafts too, or just for this line?"

Wait for the answer. If permanent, route to the hard-rule path. If one-time, route to the one-time-edit path. If the creator is still undecided after the question, treat as one-time and note in chat: "Treating as one-time edit. If the same reaction comes up again, I will surface the pattern for a permanent rule."

## Stage 1: Read the signal

Capture from the creator's reaction:

1. **The exact word, phrase, or pattern** they flagged
2. **The replacement** they gave, or ask if they did not give one (some refusals do not need a replacement; an anti-pattern is a full ban)
3. **The reason** in one line. "Corporate." "Hype." "Sounds like ChatGPT." "I just do not talk that way." The why is load-bearing for the schema's required reason field and for future edge cases.

If any of these are missing for a hard-rule candidate, ask one direct question before proceeding. Do not guess.

## Stage 2: Classify and confirm

Pick the signal type using the pattern lists in the three-signal section. If the pattern is ambiguous (preference shift), ask the one direct question. If hard rule, confirm the shape (words-avoided vs anti-pattern vs hard creator rule) if not obvious from phrasing.

Do not classify silently when ambiguous. The creator's word is the gate.

## Stage 3: Apply

**Hard rule applied:**

Open `foundation/voice-profile.md`. Find the `refusals` section. Append the new entry to the right sub-section:

- Words-avoided list (look for the `**Words avoided**` heading or equivalent): add a new line `word to swap (reason)`. Match the existing format in the file; do not restructure.
- Anti-pattern list (look for `**Anti-patterns**`): add the full phrasing.
- Hard creator rules (look for `**Hard creator rules**`): add the named rule.

If the section heading does not exist (the file is freshly created and only has the header), create the section with the heading style used elsewhere in the file. The schema in `knowledge/voice-profile-schema.md` defines the required headings.

Append a one-line note to the `update_log` section of `voice-profile.md`: the date, the entry added, and the trigger ("appended by vid-voice-update on 2026-MM-DD: words-avoided `leverage to use` (corporate)").

**One-time edit applied:**

Hand the corrected line back to the calling writing skill if invoked as sub-skill. If standalone, do not write to anything; just confirm to the creator.

## Stage 4: Re-run if permanent

When a hard rule was applied AND an in-progress draft exists (sub-skill mode with a piece slug), invoke `vid-voice-audit` on `content/pieces/{slug}/script.md`. The audit picks up the new refusal on its load. Surface to the creator only the new findings caused by the rule that did not exist before the append (if the audit reports unchanged, the rule did not catch anything in the current draft, which is fine).

Standalone mode skips this stage. No draft to re-run against.

## Stage 5: Report

Tell the creator exactly what changed, in one short block.

For a hard rule:

```
Added "leverage" as a words-avoided refusal:
- foundation/voice-profile.md: appended to refusals.words_avoided
- Reason: "corporate, the creator just uses things"
- Re-ran vid-voice-audit on this piece. {N new flags surfaced | no new flags}
- Future drafts will swap "leverage" automatically.
```

For a one-time edit:

```
Rewrote the line locally. Saved nothing to voice-profile.md.
This was a one-time edit, not a rule.
```

For a preference shift confirmed one-time:

```
Treating as one-time. If the same reaction comes up again, I will surface the pattern.
```

## Anti-patterns

- Do not save a one-time edit to refusals. The creator was clear it was local; respect it.
- Do not classify a preference shift silently. Ask. The creator's confirmation is the gate.
- Do not write a refusal without the creator's exact words. Paraphrasing the trigger word loses the rule's specificity.
- Do not invent a rule from one offhand comment that did not match any signal pattern. Some chat lines are not signals. If the pattern does not fit any of the three types, do nothing and continue the draft.
- Do not auto-add inflections to a words-avoided entry. The creator said `leverage`. Add `leverage` with the reason; downstream skills generalize from the reason, not from a regex.
- Do not skip the re-run when a hard rule lands during a draft. The point of the mid-draft path is that the current draft picks up the rule.
- Do not run when `voice-profile.md` does not exist. The skill is an append-only update tool; it does not bootstrap the profile. `vid-voice-capture` does that.

## Failure modes

- **Voice-profile.md absent.** Refuse to run. "Run vid-voice-capture first to build the voice profile, then this skill can update it."
- **Refusal section heading missing.** Create the heading per the schema, then append.
- **Creator confirms permanent but the entry is already in the refusals.** Confirm to the creator: "Already in your voice profile (`leverage to use`, added YYYY-MM-DD). No change." Do not write a duplicate.
- **Creator gives a reason that contradicts an existing refusal.** Surface the conflict. "You have `leverage to use (corporate)` already. Your new note says `leverage to win (verb form is fine)`. Update the existing entry, add a new one, or leave it?" Do not silently merge or overwrite.
- **Sub-skill mode but no piece slug provided.** Treat as standalone for the apply step; skip the re-run.

## References

- `knowledge/voice-profile-schema.md`: refusal shape, section structure, words-avoided reason requirement.
- `vid-voice-audit` (skill): the audit invoked after a hard-rule append.
- `vid-voice-capture` (skill): the heavy-rebuild sibling. Same target file, different scale.

## Related skills

- `vid-voice-capture` rebuilds the voice profile from scratch quarterly. This skill is the surgical update between rebuilds.
- `vid-voice-audit` reads the voice profile during pre-publish checks. New refusals land in the audit on next run.
- `vid-intro`, `vid-segment`, `vid-ending` invoke this skill as a sibling when the creator reacts to a line during draft review.
