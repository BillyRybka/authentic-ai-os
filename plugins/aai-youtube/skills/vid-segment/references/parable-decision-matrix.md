---
type: reference
scope: shared
loaded_by: [vid-structure, vid-segment, vid-ending]
status: active
tags: [reference, parable, decision-matrix]
---

# Parable Decision Matrix

Five questions decide which parable a segment uses. This file is the PICK logic only; the craft of executing each type lives in its own file, loaded only when that type is chosen. Claude reads this silently at structure-pass time; the creator sees candidates, never the matrix.

## The matrix

Ask in order. Every YES becomes a candidate.

1. **Is the problem invisible or hard for the viewer to see / feel?** YES → Visual Demo: Show-the-Problem
2. **Will a clear before-and-after silence doubt about why the old way doesn't work?** YES → Visual Demo: Contrast
3. **Is there a real-world example or thumbnail / page / clip that can be paused, zoomed, or annotated to make the point?** YES → Visual Demo: Breakdown
4. **Does the viewer need to FEEL the pain or urgency of staying stuck?** YES → Story
5. **Is the idea abstract, hard to grasp, or too familiar to feel fresh?** YES → Metaphor

Multiple YES: surface ALL matched types as candidates (1-3), each with a one-line why. The types are peers, not a ranked hierarchy; pick by fit to THIS segment's idea and the creator's voice. Don't auto-default to Visual Demo because it scored first.

All NO: the segment is probably a tight principle-only step (the short-process and deep-dive default) or the emotional setup was supplied by an earlier segment. Confirm with the format planner before writing. Don't force a parable that no question earned.

If the type choice and the format planner conflict, the format planner wins. The parable exists for a structural reason in the format, even when the matrix doesn't fire.

## Fit cues when several match

- Visual demos land fastest when the viewer's eye can do the cognitive work.
- Stories carry farthest when the viewer needs to feel the consequence and the creator has a real lived moment to anchor.
- Metaphors compress hardest when the idea is abstract or over-familiar and the comparison is one the avatar already knows.

## The types, and where their craft lives

**Show-the-Problem** turns invisible into visible (dissolved sugar becomes a stack of cubes). Boundary: if the problem is ALREADY visible, this type adds nothing; use Contrast instead. Craft: `references/visual-demo-builder.md` inside vid-segment.

**Contrast** is side-by-side old way vs new way, and needs one side to be CLEARLY worse. Boundary: if the two sides are really a tradeoff or a preference, it's not a contrast; drop it or use Breakdown. Max 3 pointed-out differences. Craft: `references/visual-demo-builder.md` inside vid-segment.

**Breakdown** pauses, zooms, and annotates something real on screen. Boundary: the shot must be cropped to the single element being taught; arrows flying over a cluttered screen teach nothing. Craft: `references/visual-demo-builder.md` inside vid-segment.

**Story** runs Problem-Action-Outcome in 20-30 spoken seconds, starting at the WORST moment, not the first thing that happened, with real names and numbers. Boundary: a story with no specifics ("my client was struggling, we tried something, it worked") activates nothing; if the bank entry is that thin, route to `vid-bank` to dig deeper before pulling. Craft: `knowledge/story-capture-guide.md`, pull filter: `knowledge/story-pulling-criteria.md`.

**Metaphor** swaps an abstract idea for one familiar image in three sentences or fewer. Boundary: one metaphor per parable, never mixed, never explained after the fact; if it needs a paragraph, it isn't working, use a story or demo. Craft lives with `vid-bank` (route there to build one), integration rules: `knowledge/metaphor-integration.md`.

## Bridge to the principle

Every parable hands off in one sentence: "So what does that actually mean for you?" / "Here's how to apply this in real life." / "Here's how to fix that, step by step." Don't drag it; the viewer is primed, deliver the lesson.

## What about Testimonials and Frameworks?

Not parable types. They're principle components pulled IN ADDITION to the parable:

- **Testimonial**: social proof inside the principle, verbatim quote in a `> [!quote]` callout. Placement rules: `knowledge/proof-placement-rules.md`.
- **Framework**: IS the principle when the segment teaches a creator-owned named system; the parable sets it up. Shapes and build: `knowledge/framework-builder.md`.

## How the skills use this file

At structure time (vid-structure per point, vid-segment Phase 2, vid-ending only when the close opens on a fresh emotional beat):

1. Ask the 5 questions silently against the segment's job
2. Surface every YES as a candidate, plus the format planner's shape default
3. For each candidate type, surface 0-3 matching bank candidates
4. The creator picks the type and the material; then load that type's craft file, and only that one
