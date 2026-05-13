---
type: bank-index
bank: metaphor-bank
project: youtube-content-os
status: active
tags: [bank, metaphor, index]
---

# Metaphor Bank

Analogies and metaphors the creator uses to make abstract ideas concrete. Each entry is a reusable comparison that lands with the creator's avatar. Captured once, pullable from any script.

## What goes in this bank

One file per metaphor. Examples:

- **Everyday metaphors**: "Hiring without SOPs is like handing someone the keys to your car without a license"
- **Food metaphors**: "A business without documented processes is like a restaurant with no recipes"
- **Sports metaphors**: "A solo founder is the player-coach"
- **Travel/journey metaphors**: "Building from services to systems is swapping a taxi meter for an Uber app"

Metaphors come from the creator, not Claude. Captured via `vid-capture` (Metaphor stage). Do not invent metaphors. They sound wrong on camera.

## What does NOT go here

- Stories → `story-bank/` (a metaphor compares A to B in a sentence, a story has tension and resolution)
- Frameworks or named systems → `framework-bank/`
- Single clever phrases without a comparison structure. A punchline isn't a metaphor.
- Metaphors Claude invented. Capture only phrases the creator already uses or explicitly adopts.

## Schema

```yaml
---
type: metaphor
project: youtube-content-os
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

`{short-slug}.md`. Kebab-case, references the concept or the metaphor object. E.g. `car-without-license.md`, `restaurant-with-no-recipes.md`, `player-coach.md`.

## Body sections

See `assets/metaphor-entry-template.md` in `vid-capture`. Key sections:

1. **The concept**: what abstract idea this metaphor clarifies
2. **The metaphor**: the comparison, in the creator's wording
3. **Why it lands**: the point of comparison
4. **Visual treatment**: if `visual: true`, what the prop or graphic would be
5. **When to use it**

## How entries get used

1. `vid-capture` → Metaphor stage → file written here
2. `vid-segment` pulls matching metaphors when explaining complex points
3. `vid-intro` may pull a short metaphor for the Problem statement
4. When used, `used_in` updates and `status` flips to `used`
