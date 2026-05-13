---
type: bank-index
bank: story-bank
project: youtube-content-os
status: active
tags: [bank, story, index]
---

# Story Bank

Real stories the creator has lived or observed, captured once so every future script can pull from them without re-explaining context.

## What goes in this bank

One file per story. Anything narrative with a beginning, a tension, and a resolution:

- A client moment (the call where they realized X, the weird request, the breakthrough)
- A personal moment (the time the creator hit bottom, made a mistake, found a counterintuitive insight)
- A viewer moment (what a community member said, something that happened in the comments)
- A small observation that became a framework (the day the creator noticed the pattern)

Captured via `vid-capture` (Story stage). Referenced by `vid-segment` and `vid-intro` when a script needs narrative.

## What does NOT go here

- Numbers, stats, results → `proof-bank/`
- Client quotes or praise → `testimonial-bank/`
- Analogies and metaphors → `metaphor-bank/`
- Frameworks or named systems → `framework-bank/`
- One-line anecdotes without tension. A story needs a change or a reveal.

## Schema

```yaml
---
type: story
project: youtube-content-os
story_type: client              # client | own | viewer
problem_illustrated: 1          # 1 | 2 | 3 | general
client: "[[Client Name]]"       # only for client stories
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [story, problem-{n}, {theme-slug}]
used_in: []
---
```

## Naming

`{short-slug}.md`. Kebab-case, 3-6 words. E.g. `client-missed-onboarding-deadline.md`, `airbnb-photo-swap.md`.

## How entries get used

1. `vid-capture` → Story stage → file written here
2. `vid-segment` / `vid-intro` pull stories by problem tag or theme
3. When used, `used_in` updates and `status` flips to `used`. Obsidian backlinks show which scripts pulled which stories.

See `assets/story-entry-template.md` in `vid-capture` for the body template.
