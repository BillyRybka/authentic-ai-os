---
type: reference
doc: story-bank-schema
project: authentic-ai-os
status: active
tags: [reference, story-bank, schema, contract]
---

# Story bank schema

The contract for writing story entries to `banks/story-bank/`. Real stories the creator has lived or observed, captured once so every future script can pull from them without re-explaining context.

This bank is written by `vid-capture` (Story stage) when that skill ships. Until then, this schema documents the intended contract.

## What qualifies as a story

One file per story. Anything narrative with a beginning, a tension, and a resolution:

- A client moment (the call where they realized X, the weird request, the breakthrough)
- A personal moment (the time the creator hit bottom, made a mistake, found a counterintuitive insight)
- A viewer moment (what a community member said, something that happened in the comments)
- A small observation that became a framework (the day the creator noticed the pattern)

## What does NOT qualify

- Numbers, stats, results belong in `banks/proof-bank/`.
- Client quotes or praise belong in `banks/testimonial-bank/`.
- Analogies and metaphors belong in `banks/metaphor-bank/`.
- Frameworks or named systems belong in `banks/framework-bank/`.
- One-line anecdotes without tension. A story needs a change or a reveal.

## Schema

```yaml
---
type: story
project: authentic-ai-os
story_type: client              # client | own | viewer
illustrates: without systems and delegation, you drown in client work and never get time to grow
themes: [delegation, systems, time]    # open vocabulary, the angles this lesson touches
client: "[[Client Name]]"       # only for client stories
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [story, {theme-slug}]
used_in: []
---
```

## Naming

`{short-slug}.md`. Kebab-case, 3-6 words. For example: `client-missed-onboarding-deadline.md`, `airbnb-photo-swap.md`.

## How entries get used

1. `vid-capture` writes entries at its Story stage.
2. Per-video skills (intros, segments) pull stories by what they illustrate and theme tags.
3. When used, `used_in` updates and `status` flips to `used`. Obsidian backlinks show which scripts pulled which stories.

## People links

If a story names a recognizable person (a client, a guest), create or update `people/{Full Name}.md` as a stub and wikilink the name both ways, per the vault-integration contract.
