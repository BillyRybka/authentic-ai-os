---
type: template
name: reference-pieces file
project: authentic-ai-os
tags: [template, voice, reference-pieces]
---

# Template: `foundation/reference-pieces/{voice_context}.md`

The voice engine for one `voice_context`. One file per populated context. Inside: every selected passage as a `## ` section, intact, the creator's exact words.

Writing skills load the whole file when the piece's `voice_context` matches. They read it as voice grain only, not as a structural template. The architecture of what they write is fixed by the writing skill's own spec.

This template ships with empty placeholders only. Real creator passages live only in the creator's own `foundation/` workspace, never in this template.

## Shape

```markdown
---
type: reference-pieces
project: {project}
voice_context: {context-key}
captured: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
sources: ["{source filename}", ...]
tags: [voice, reference-pieces, context-{context-key}]
---

# Reference pieces: {voice_context}

Real creator passages in the {voice_context} voice_context. Loaded by writing skills as the voice seed: cadence, word choice, register, signature moves. Structure of any output piece is the writing skill's spec, not these passages.

## {short-slug-1}

> Demonstrates: [one line, plain language: the mode and energy this passage shows, in the creator's own range, not a fixed slot. e.g. how they sound demonstrating something live, or at their calmest, or doing their signature move.]

[The creator's exact words, verbatim, intact. Not cleaned, not rephrased, not stripped of structural elements. Long enough that the rhythm is audible, short enough that there is no filler.]

## {short-slug-2}

> Demonstrates: [...]

[verbatim passage]

## {short-slug-3}

> Demonstrates: [...]

[verbatim passage]
```

## Rules

- One file per populated `voice_context`. Never one file per passage.
- Aim for 2 to 3 passages per major beat type the creator uses (single-sample beats are prone to structural shadowing downstream).
- Passages stay intact. Do not trim structural elements out, that loses the rhythm the model needs.
- Do not curate an improvised, creator-designated moment (a beat they always deliver live, never want scripted) as a passage. It goes in `voice-profile.md` refusals as a hard rule instead.
- Add or retire sections per the refresh logic in `voice-profile-schema.md`. Append new `## ` sections; do not silently delete.
