---
type: skill-asset
skill: vid-structure
purpose: exact-shape-of-script.md-on-first-write
last_updated: 2026-05-13
---

# script.md Skeleton Template

The exact shape vid-structure writes to `Content/pieces/{slug}/script.md` after outline lock. vid-intro fills `## Intro`, vid-segment fills each body section, vid-ending fills `## Ending`.

This template is a reference for vid-structure to emit. Do not paste this file into chat. Fill the slots with the locked outline's material.

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

`status: outlined` becomes `status: drafted` when all body segments are written. `tier: 1` flips to `tier: 2` (and back to `status: drafted`) when prose is complete.

## Body shape (segmented formats: Listicle / Short Process / Deep Dive / Roast / Interview)

```markdown
# {title from piece.md, or "{Title TBD via vid-title} {slug}"}

> Tier 1 outline. vid-intro fills ## Intro. vid-segment fills each body section.
> vid-ending fills ## Ending. Material anchors and brick candidates are surfaced
> per section. vid-segment makes the final brick picks at prose-writing time.

## Intro

*To be written by vid-intro after title + thumbnail lock. Refer to piece.md for format and intro adaptation.*

## {Body Section 1 Label}: {one-line material-anchored purpose}

**Material:**
- {brain-dump entry / lesson 1 that lands here}
- {brain-dump entry / lesson 2 that lands here}

**Brick candidates:**
- Story: [[story-slug-1]] | [[story-slug-2]] | (no match; vid-segment may use a different brick)
- Proof: [[proof-slug-1]] | (no match)
- Metaphor: [[metaphor-slug]] | (no match)
- Framework: [[framework-slug]] | (no bank match; vid-segment may invent inline via knowledge/framework-builder.md)
- Visual demo flag: {yes / no}

**Bullet outline:**
- {Setup: what opens this segment}
- {Tension: the emotion brick + logic brick movement}
- {Payoff: the lesson the viewer walks away with}

**Tension role:** {opens easy / midpoint / pre-payoff / title-promise payoff / post-payoff application}
**Outbound handoff:** {the forward-hook into next segment, OR "to ending" if final body section}

## {Body Section 2 Label}: {one-line purpose}

[repeat shape]

...

## {Body Section N Label}: {one-line purpose}

[repeat shape]

## Ending

*To be written by vid-ending. CTA shape per piece.md goal. Pivots to next problem in Top 3.*

---

<!-- 
CUTS (logged at structure-lock time):
- {brain-dump entry slug or label}: {reason} [tangent / off-angle / off-format / future-piece]
- ...

COMBINES applied:
- {entry A} + {entry B} → {merged segment label}: {sharper phrasing wins}
-->
```

## Body shape (narrative format: Case Study)

```markdown
# {title from piece.md}

> Tier 1 outline. Case-study narrative arc, not segmented. vid-intro fills ## Intro.
> vid-segment fills each story beat in order. vid-ending fills ## Ending.

## Intro

*To be written by vid-intro after title + thumbnail lock. Case-study intros lead with the receipt (outcome) or the stakes.*

## Setup: {where the protagonist started}

**Material:** brain-dump entries on protagonist's starting state + stakes
**Bricks:** [[story-slug]] (the stakes-laden open)
**Bullets:** name the stakes → name the goal → what's at stake if it fails
**Tension role:** raises tension to maximum at the open

## Problem: {what was/wasn't working}

**Material:** brain-dump on dead-ends, failed attempts
**Bricks:** [[proof-slug]] if available
**Bullets:** the dead-ends → why each failed → the trapped moment
**Tension role:** deepens stakes

## Action: {what they actually did}

**Material:** brain-dump on the methodology rollout
**Bricks:** [[framework-slug]], [[proof-slug-week-N-traction]]
**Bullets:** the named system → the first pivot → the moment things changed → the breakthrough
**Tension role:** rising action toward Outcome

## Outcome: {the result} (TITLE-PROMISE PAYOFF)

**Material:** brain-dump on final result + timeframe
**Bricks:** [[proof-slug-final-result]], client clip if available
**Bullets:** name the number → name the timeframe → land the moment
**Tension role:** climax. Title's promise lands.

## Lesson + Steps: {the takeaway + what the viewer can do}

**Material:** brain-dump on the one big lesson + 1-3 replicable steps
**Bricks:** [[framework-slug]] (named as the takeaway)
**Bullets:** the ONE lesson → 1-3 viewer steps → tie to offer (per goal)
**Tension role:** application. Convert 'wow' to 'I could do this'.

## Ending

*To be written by vid-ending. Sales-goal CTA placement per format-planner.*

---

<!--
CUTS:
- ...
COMBINES:
- ...
-->
```

## Body shape (News format)

```markdown
# {title from piece.md}

## Intro

*To be written by vid-intro. News intro = 5-10 second hook, no Top 3 questions delay.*

## What Happened: {the event}

**Material:** brain-dump on the facts
**Bricks:** primary sources, screenshots
**Bullets:** lead with the most surprising fact → name the event → cite sources
**Tension role:** opens with maximum specificity

## Why It Matters: {the stakes for the viewer's avatar}

**Material:** brain-dump on the implication / stakes
**Bricks:** [[proof-slug]], [[story-slug-impact]]
**Bullets:** connect to viewer's reality → name what changes → land the named insight
**Tension role:** title-promise payoff territory (~50-60% through)

## What To Do: {the actionable response}

**Material:** brain-dump on the response
**Bricks:** [[framework-slug]] if applicable
**Bullets:** name the response → 1-2 specific actions → urgency cue
**Tension role:** application

## Ending

*To be written by vid-ending. News endings stay tight.*
```

## Conventions

- **Section headers use `##` (level 2).** Sub-points inside a section use `###` (level 3) if needed, but bullet outlines usually suffice.
- **Material lines are bulleted, not prose.** This is Tier 1. Bullets are the deliverable, not full sentences.
- **Brick candidates as wikilinks.** Always `[[slug]]` format. If no bank match, write "(no match; vid-segment may use a different brick)" or note inline-craft route.
- **Tension role is descriptive, not prescriptive.** "Title-promise payoff" / "rising action" / "post-payoff application". vid-segment reads this to know how to write the prose's emotional weight.
- **Outbound handoffs in quotes when concrete.** If the handoff phrasing is locked, write it in quotes. If still a sketch, describe ("forward-hook into the algorithm-mechanism question").
- **Cuts and combines logged in HTML comments at the bottom.** Sticky across re-structure runs.

## Anti-patterns to avoid

- **Prose in the bullets.** Tier 1 is bullets. If you find yourself writing full sentences, save them for vid-segment.
- **Abstract section labels.** Never `## Segment 3: {placeholder}`. Always material-anchored.
- **Empty Material lines.** If a section has no brain-dump material, the section shouldn't exist. Cut it.
- **Locked brick choices in vid-structure.** Surfacing is the job. Locking happens at vid-segment time. Use `|` to list candidates, never single-choice.
- **No tension role.** Every body section names where it sits in the arc. Without this, vid-segment can't write the right emotional weight.
