---
type: reference
scope: shared
loaded_by: [vid-voice-capture, vid-segment, vid-intro, vid-ending, vid-structure, post-write]
status: active
tags: [reference, voice, schema]
---

# Voice Schema and Load Contract

The canonical contract for how the creator's voice is stored and how every writing skill loads it. This file is the single source. The writing skills point here instead of restating the rules.

## Three layers, three jobs

Every piece produced by this system pulls from three non-overlapping layers, and they must stay that way:

1. **Voice (this skill).** HOW the creator generally talks. Grain, cadence, register, signature moves, what they refuse to say. Lives in `foundation/voice-profile.md` plus `foundation/reference-pieces/`. Carries texture, not architecture and not content.
2. **Brain dump (per piece).** WHAT the creator actually said for THIS piece. Their real words, claims, stories, examples, in their phrasing. Lives in `content/pieces/{slug}/brain-dump.md`. The source of truth for substance.
3. **Structure (the writing skills).** The architecture of each beat. Hook arc, segment shape, Pivot-Gap-Bridge ending, CTA, push to the next video. Same best practice for every creator. Lives in `vid-intro`, `vid-segment`, `vid-ending`, `vid-structure`, and the format planners.

A writing skill polishes the brain dump's content, in the voice grain, on the structure spec. Crossing lines causes the failures this system was built against: voice samples that smuggle structure produce repetitive endings; structure prescriptions that lock content produce generic videos; brain dumps polished into "better prose" lose the voice. Keep the layers clean.

The rest of this file specifies the voice layer.

## The principle (read this first)

Voice is reproduced from the creator's real sentences, not from a description of them. Cadence, word choice, and the feel of a real line live in the surface text. An abstracted rule ("self-Q&A, heavy" or "8 em-dashes per 1000 words") is a lossy compression a model can satisfy while still sounding generic.

So the system stores two things, with different jobs:

1. **`foundation/reference-pieces/{voice_context}.md`, the voice engine.** One file per populated `voice_context`. Real passages the creator produced, intact, as `## ` sections inside the file. This is the generation seed. The writing skill reads it and writes in its grain.
2. **`foundation/voice-profile.md`, the thin guardrail.** The short list of things examples cannot teach: what the creator refuses to say, the signature phrases, the energy floor. A constraint layer, not the voice.

Statistics (sentence-length distributions, punctuation counts) are not stored anywhere as generation input. Rhythm is judged at validation time, by ear, against the reference pieces. See [[voice-pressure-test]].

Banned terminology: do not say "voice locked" or "voice-locked drafting" anywhere in output or files. The creator rejected it. The voice is preserved, never "locked."

## Artifact 1: `foundation/reference-pieces/{voice_context}.md`

Curated by `vid-voice-capture`. **One file per populated `voice_context`.** Inside: the creator's real passages as `## ` sections, intact (not trimmed of structure). Each section opens with a `> Demonstrates:` line in plain language, then the verbatim passage.

```yaml
---
type: reference-pieces
project: authentic-ai-os
voice_context: youtube-script
captured: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
sources: ["{source filename}", ...]
tags: [voice, reference-pieces, context-{voice_context}]
---
```

Number: usually 3 to 8 passages, depending on the creator's range. Aim for 2 to 3 per major beat type the creator uses (cold-open, plain teach, live demo, signature analogy, ending). Single-sample beats are prone to structural shadowing in downstream writing; multiple samples per beat dilute that. The number serves coverage and dilution, not a fixed target.

Passages stay **intact**, not stripped of structural content. Stylometric and practitioner evidence is one-directional: flattened voice-only fragments lose the rhythm that IS voice. Whole passages carry the grain. The risk that intact samples cause downstream writing to copy their structural arc is real but is handled by (a) keeping 2 to 3 samples per beat to dilute any single arc, and (b) the explicit voice-only-not-structure clause every writing skill carries (see Load contract). The reference set is voice; structure stays the writing skill's job.

Selection is by stylistic representativeness, not topic. Pick passages that together span the creator's actual range (their calm and charged poles, every distinct register including any live-demonstration register, and their signature moves), not the most frequent or the most on-topic. Range is derived from the creator's tape, not a fixed slot set. See `voice-extraction-methods.md` Step 2.

**A creator-designated improvised moment is never curated as a reference piece.** A creator may have a personal beat they always deliver live and never want scripted. Storing it as a seed would let a writing skill regenerate it, which the creator forbade. It lives only as a refusal in Artifact 2.

## Artifact 2: `foundation/voice-profile.md`

Small. Always loaded. These sections, in order:

### `voice_fingerprint` (required, 2 to 4 sentences)

Prose gestalt. The fastest possible orientation to who this sounds like. Not a field list.

### `signature_phrases` (required, list)

Verbatim recurring phrases, real quotes, not paraphrases. These are high-fidelity anchors that survive generation. If a draft contains or closely echoes one, voice signal is present. If a long piece echoes none, signal is weak.

Recurrence is necessary but not sufficient. A discourse marker ("right?", "you know", "so", "like") can recur across every source and still be filler, not signature: the kind of word any creator uses, and an AI tell. Before locking any candidate that matches a known-filler shape, **surface it to the creator and ask**: "this came up a lot, is it load-bearing for your voice or filler you'd cut?" If the creator says load-bearing, it stays. If filler, route it to `words_avoided` with the reason `filler, drop unless the sentence needs it` so writing skills do not reproduce it. Starter filler hints (to trigger the question, never to auto-block): `right?`, `you know`, `like`, `so`, `okay`, `alright`, `I mean`, `basically`. The list is a prompt for confirmation, not a blacklist; it grows creator by creator. The creator's answer is always the gate.

### `refusals` (required)

The rule layer. The only place rules live. Three kinds:

- **Anti-patterns.** Full phrasings the creator would never write. Hard reject in any output. Includes the global product rules (em-dashes, real profanity in place of the clean register) and creator-specific ones.
- **Words avoided.** Each entry is `word to swap (one-line reason)`. The reason is required, not optional. Reasons let the model generalize to unseen offenders ("elevate," "amplify," "transform") instead of catching only the words on the list. Example: `ship to post (software metaphor, reads wrong for content)`. Soft reject, auto-swap.
- **Hard creator rules.** Named, explicit. Common shapes: never script a creator-designated improvised moment (leave the slot, never draft its text); never carpet-bomb an emphasis device or place it on a cadence (it fires at peaks by function, not by frequency).

### `pov_and_energy` (required, hard cap)

Two short paragraphs maximum: one for POV, one for energy. No more. This section is for orientation, not a spec, and bloats over refreshes if left open-ended.

- **POV (2 sentences max).** Which pronoun dominates and when. Example: "Talks to one viewer in 'you.' Uses 'I' for personal stories and 'we' for live build-along."
- **Energy floor (2 sentences max).** What is true even at their calmest. Example: "Conversational but charged. Even at baseline they ask rhetorical questions and address the viewer directly; never goes flat or corporate."

### vid-intro orientation fields (optional)

Kept because `vid-intro` consumes them as a documented input. Populate only if clearly observed across sources, otherwise omit the field (do not write a guess):

- `preferred_hook_types`: which of `question | contrarian | statement | fact | credibility` the creator defaults to.
- `transition_style_preferences`: free text, how they bridge ideas.
- `intro_pacing`: `fast | measured | slow-burn`.

### `context_flex` (required if any context file exists, one line each)

One line per populated `voice_context`: how that context differs from the baseline, and confirmation that `foundation/reference-pieces/{voice_context}.md` exists. This is a pointer, not a sub-profile. No quantitative fields.

### `sources_analyzed` + `update_log` (required)

Every source that fed the profile, with date and `voice_context` tag. One single update log for the whole profile. No per-context logs.

## `voice_context` (the medium axis)

`voice_context` is the delivery medium or mode the creator's voice is in. It is orthogonal to `format` (the structural template of the video). A `listicle` could be delivered as a screen-share `tutorial` or a talking-head `youtube-script`. Do not derive one from the other.

Values: `youtube-script` | `tutorial` | `shorts` | `newsletter` | `linkedin` | `twitter` | `instagram` | `podcast` | `casual` | `talk`.

`instagram` covers both carousel and caption deliveries. Those are layout sub-formats the writing skill handles (`post-write`), not separate voice contexts. The creator talks one way on Instagram; the carousel just chops that voice into slides.

`piece.md` carries `voice_context:` (default `youtube-script`), set by `vid-framing` alongside `format`. Schema home: [[piece-contract]].

## The unified load contract (every writing skill follows this exactly)

When a writing skill (`vid-intro`, `vid-segment`, `vid-ending`, `vid-structure`) produces output:

1. Load `foundation/voice-profile.md` always. The fingerprint, signature phrases, and refusals apply to every line.
2. Read `voice_context` from the piece's `piece.md` (default `youtube-script` if absent).
3. If `foundation/reference-pieces/{voice_context}.md` exists, load it. The `## ` sections inside are the generation seed: read them together to internalize the creator's combined cadence, then write in their grain.
4. If that file does not exist, seed from the `voice_fingerprint` and `signature_phrases` only, and note the gap in the output meta so the creator can add sources for that context.
5. Honor `refusals` as hard constraints. An anti-pattern present is wrong, not "soft." A creator hard rule (a never-script-this moment, an emphasis-cadence ban) is a hard block.
6. Before save, run [[voice-pressure-test]].

**Reference pieces are voice only, not structure.** The passages carry cadence, word choice, register, and signature moves. They do NOT determine the architecture of what you write. Hook arc, segment shape, Pivot-Gap-Bridge ending, CTA, push to the next video, those are the writing skill's spec, the same best practice for every creator. If a reference passage's structural arc conflicts with the spec, follow the spec. Reproduce the grain of the passages, not their order of moves.

Reference pieces are a seed, not a script to mirror. Read them as samples of how the creator talks and reproduce that feel. Signature phrases are anchors (one or two surfacing in long-form is a healthy signal, not a target to hit).

## Refresh and merge logic (vid-voice-capture re-runs)

Per `voice_context`:

- Context has new validated passages and an existing file: append new `## ` sections to the file, tag the profile update log with the date and what was added. Keep prior passages unless the creator retires them.
- Context file exists but new sources no longer validate it: do not silently delete. Mark it `deprecated` in the `context_flex` line with the reason, keep the file. Consumers loading a deprecated context log a warning and fall back to fingerprint-only.
- New context: create the file (`foundation/reference-pieces/{voice_context}.md`), add the `context_flex` line, log it.
- **At every refresh, re-ask the exclusion-rule question:** "Any new moment you always deliver live and never want drafted? Any existing one no longer relevant?" Refusals drift the same way passages do.

A missing context is simply no file. There are no stub files anywhere.

## What this schema does not do

- It does not store rhythm or punctuation numbers. Those are validation instruments only. See [[voice-pressure-test]].
- It does not replace the read-aloud test. If the creator reads output and would reword it, the voice is wrong even if every rule passed.
- It does not invent a voice. `vid-voice-capture` surfaces what is already in the sources. Empty beats guessed.
