---
type: reference
doc: metaphor-bank-schema
project: authentic-ai-os
status: active
tags: [reference, metaphor-bank, schema, contract]
---

# Metaphor bank schema

The contract for writing metaphor entries to `banks/metaphor-bank/`. Analogies and metaphors the creator uses to make abstract ideas concrete. Each entry is a reusable comparison that lands with the creator's avatar. Captured once, pullable from any script.

This bank is written by `vid-capture` (Metaphor stage) when that skill ships. Until then, this schema documents the intended contract.

## What qualifies as a metaphor

One file per metaphor. Examples:

- **Everyday metaphors**: "Hiring without SOPs is like handing someone the keys to your car without a license"
- **Food metaphors**: "A business without documented processes is like a restaurant with no recipes"
- **Sports metaphors**: "A solo founder is the player-coach"
- **Travel/journey metaphors**: "Building from services to systems is swapping a taxi meter for an Uber app"

Metaphors come from the creator, not Claude. Do not invent metaphors. They sound wrong on camera.

## What does NOT qualify

- Stories belong in `banks/story-bank/`. A metaphor compares A to B in a sentence; a story has tension and resolution.
- Frameworks or named systems belong in `banks/framework-bank/`.
- Single clever phrases without a comparison structure. A punchline is not a metaphor.
- Metaphors Claude invented. Capture only phrases the creator already uses or explicitly adopts.

## Schema

```yaml
---
type: metaphor
project: authentic-ai-os
concept: "short concept name"   # what the metaphor clarifies
category: everyday              # food | cars | clothes | sports | travel | everyday | other
visual: false                   # true if metaphor depends on a prop/graphic; false if pure speech works
problem_illustrated: 2          # 1 | 2 | 3 | general
captured: YYYY-MM-DD
status: captured
tags: [metaphor, category-{slug}, visual-metaphor OR non-visual-metaphor, {theme-slug}]
used_in: []
---
```

## Naming

`{short-slug}.md`. Kebab-case, references the concept or the metaphor object. For example: `car-without-license.md`, `restaurant-with-no-recipes.md`, `player-coach.md`.

## Body sections

1. **The concept**: what abstract idea this metaphor clarifies
2. **The metaphor**: the comparison, in the creator's wording
3. **Why it lands**: the point of comparison
4. **Visual treatment**: if `visual: true`, what the prop or graphic would be
5. **When to use it**

## How entries get used

1. `vid-capture` writes entries at its Metaphor stage.
2. Per-video skills pull matching metaphors when explaining complex points.
3. When used, `used_in` updates and `status` flips to `used`.
