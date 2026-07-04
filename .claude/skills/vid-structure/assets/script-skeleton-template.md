---
type: skill-asset
skill: vid-structure
purpose: exact-shape-of-script.md-on-first-write
last_updated: 2026-07-01
---

# script.md Skeleton Template

The exact shape vid-structure writes to `content/pieces/{slug}/script.md` after the plan locks in Phase 3. `vid-intro` fills `## Intro`, `vid-segment` writes each body section, `vid-ending` fills `## Ending`. Do not paste this file into chat. Fill the slots with the locked plan.

## Frontmatter

```yaml
---
type: script
piece: [[piece-slug]]
status: outlined
tier: 1
last_refreshed: {YYYY-MM-DD}
---
```

## Body shape

Every body section is the same shape: a material-anchored header, then the parable and the principle picked in Phase 2. Nothing else per section. Setup and payoff lives once in piece.md (`tension_plan`), not repeated here. The forward-hook transition is the writer's to compose.

```markdown
# {title from piece.md, or "Title TBD"}

> Tier 1 outline. vid-intro fills ## Intro. vid-segment writes each body section.
> vid-ending fills ## Ending.

## Intro
*vid-intro fills this after title and thumbnail lock.*

## {Section header}: {the point, in the creator's own material}
**Parable:** {type}. {what it shows}. [[block-slug]] (or "to build")
**Principle:** {the framework or lesson}. Proof: [[proof-slug]] (or "to build")

## {next section}
[same shape]

## Ending
*vid-ending fills this. CTA per piece.md goal.*

## To build
- [ ] {section} / {block type}: {what's needed} (no bank match)

<!--
CUTS (sticky across re-structure runs):
- {brain-dump entry}: {reason} [tangent / off-angle / off-format]
-->
```

## Section headers by format

The per-section shape (parable + principle) is identical for every format. Only the headers change, per the locked format's planner:

- **Listicle / Deep Dive:** `## Item 1: {point}` ... or `## Lesson 1: {concept}` ...
- **Short Process:** `## Step 1: {action}` ... (lean steps; the one parable sits up front)
- **Roast:** `## Subject 1: {name}` ...
- **Interview:** `## Q1: {question}` ...
- **Case Study:** `## Setup` -> `## Problem` -> `## Action` -> `## Outcome` -> `## Lesson + Steps` (one story arc, not numbered points)
- **News:** `## What Happened` -> `## Why It Matters` -> `## What To Do`

## Conventions

- **Headers are material-anchored.** Never `## Point 3: {placeholder}`. Name the actual lesson the point carries.
- **Parable and principle are one line each.** This is the plan, not prose. Wikilink real blocks; write "to build" where the bank had no match.
- **Every "to build" flag gets a row in `## To build`.** That list is the single record of what still needs sourcing. An empty list means the script is fully sourced.
- **Cuts logged in the HTML comment**, sticky so re-structure runs do not re-propose them.
