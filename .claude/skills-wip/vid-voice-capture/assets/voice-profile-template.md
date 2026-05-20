---
type: foundation
doc: voice-profile
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
contexts_populated: []
tags: [foundation, voice, creator-identity]
---

# Voice Profile

This is the thin guardrail, not the voice. The voice lives in `foundation/reference-pieces/{voice_context}.md` (one file per populated context, real passages as `## ` sections, the seed writing skills write from). This file is the short list of what examples cannot teach. No rhythm or punctuation numbers belong here; rhythm is judged by ear against the reference pieces. See `knowledge/voice-profile-schema.md`.

This template ships with empty placeholders only. The creator's real passages and patterns are written into their own `foundation/` workspace, never into this template.

---

## Voice fingerprint

[2 to 4 sentences. Who this sounds like, fast. Prose, not a field list.]

## Signature phrases

Verbatim recurring quotes that hold across contexts. Real quotes, never paraphrased.

- "[exact quote]"
- "[exact quote]"
- "[exact quote]"

## Refusals

The only rules in this system. Everything else is shown by the reference pieces.

**Anti-patterns** (full phrasings the creator would never write; hard reject in any output):

- [phrasing], [reason if known]
- Em-dashes anywhere (global product rule).
- Real profanity in place of the clean register (global if it applies to this creator).

**Words avoided** (soft reject, auto-swap). Each entry must include the one-line reason; reasons let the model generalize to unseen offenders, not just catch the words on this list.

- [word] to [swap] ([one-line reason])
- [word] to [swap] ([one-line reason])

**Creator hard rules** (named, explicit, hard block):

- [e.g. never script the {improvised moment}: leave the slot, never draft the text]
- [e.g. never carpet-bomb or cadence-place {emphasis device}: it fires at peaks by function]

## POV and energy

Hard cap: two short paragraphs, two sentences each. Orientation, not a spec. This bloats over refreshes if left open-ended.

- **POV (2 sentences max):** [which pronoun dominates and when. e.g. "Talks to one viewer in 'you.' Uses 'I' for personal stories and 'we' for live build-along."]
- **Energy floor (2 sentences max):** [what is true even at their calmest. e.g. "Conversational but charged. Even at baseline they ask rhetorical questions and address the viewer directly; never goes flat or corporate."]

## vid-intro orientation (optional)

Populate only if clearly observed across sources. Omit any line you would be guessing.

- preferred_hook_types: [subset of: question | contrarian | statement | fact | credibility]
- transition_style_preferences: [free text]
- intro_pacing: [fast | measured | slow-burn]

## Context flex

One line per populated voice_context. State how it differs from baseline and confirm the reference file exists. Mark deprecated contexts here.

- `youtube-script`: [how it flexes from baseline]. Reference file: `foundation/reference-pieces/youtube-script.md`
- `{context}`: [deferred, needs {medium} source material] OR [deprecated YYYY-MM-DD, reason]

## Sources analyzed

Every source that fed this, with date and voice_context tag.

- [source, voice_context, YYYY-MM-DD]

## Update log

- YYYY-MM-DD: Initial build. Reference sets: [contexts]. Guardrail populated. Deferred: [contexts].
