---
type: audit
doc: ygs-writing-lens
project: authentic-ai-os
status: active
created: 2026-07-16
tags: [audit, segment, writing, format-planners, source-material]
---

# The YGS point-writing system, distilled (internal lens doc)

Source: Ed Lawrence, YGS phase 5 (writing) lessons 6-10 and phase 6 (format planners) lessons 1, 2, 5, 8. Internal doc only; skill and knowledge files stay attribution-scrubbed. This is the lens for auditing `vid-segment` and the format planners. Companion to [[2026-07-16-ygs-thumbnail-lens]].

## The core model (lesson 6)

- A point = emotion brick then logic brick, then a transition. Emotion first because feeling opens the viewer to learning ("show, don't tell" then tell). This is dual process theory: system 1 reacts, system 2 learns.
- The felt test for all information: does it feel **new, easy, and inspiring**? That triangle is the standard every point is held to.
- **How often you use emotion is a format decision, not a rule:**
  - Persuasive, story-driven, insight-based, belief-challenging content: emotion + logic on EVERY point (the listicle shape).
  - Instructional, process content: ONE emotion brick up front to set the stakes, then just deliver the steps (the short-process shape). Emotion at every step would slow the follow-along and confuse.
  - Within a lean steps run, insert an emotion brick at a single step ONLY when that step is complex or the viewer would be skeptical it matters. Ask per step: "does this need emotion at all?" Default for lean formats: no.
- Nobody dies if you tweak it. Don't shoehorn emotion; use it when it's the best tool.

## The three emotion tools (lessons 7-9)

The opening question for any emotion brick: **"How can I show the problem, the transformation, or prove this works?"**

1. **Visual demo** (first choice): show the problem (make an invisible problem visible), contrast (before/after, wrong/right), or breakdown (freeze and annotate something real). Mistakes: too much complexity (distill to the core), long explanation before the reveal (lead with the visual), max 3 pointed-out things, point at the exact area.
2. **Story**: the circle is Problem (drop into the worst moment, 1-2 sentences, specific language like "I had not slept for 48 hours") then Action (ONE decision, the most surprising one, max 3) then Outcome (win, loss, or lesson; requires a big transformation between start and end; a twist is the best version; if start and end are similar, don't tell it). Story choice ranking: client story beats own story beats someone else's story beats the viewer's hypothetical story. Never retell famous stories everyone knows.
3. **Metaphor**: swaps a complex idea for a vivid familiar image. Use ONLY when the concept is abstract/technical, previously explained but not landing, dry and data-heavy, or must be remembered. Skip when the idea is already clear. Never two metaphors in one brick. Never explain the metaphor after making it. If it takes half an hour to invent, drop it and use a story or demo instead.

## The logic brick (lesson 10)

- Job: give the vital 20% that produces 80% of the result, structured so it never overwhelms. Not 100% of what they need; the most important slice.
- Three tools: **frameworks** (steps to a result, acronyms, visual shapes: arrows for sequence, triangle/pyramid for core ingredients, cycle for loops, Venn for overlap, funnel for narrowing; pick by asking how the parts relate; name the framework so it feels new), **proof** (comes AFTER the framework lands, answering "has this actually worked for anyone?"; types: own results, client wins, before/afters, live clips; reuse winning proof shamelessly), **checklists / on-screen steps** (progress markers that reduce cognitive load).
- Framework building: dump every point, ask what result the viewer needs, circle the 3 most important, pick the shape, name it.

## Transitions (all lessons)

Two jobs: hook forward (tease the value ahead) and orientation cue (signal movement). After emotion: "now you've seen the problem, here's how to fix it." After logic, into the next point: signal the shift AND promise a result the viewer cares about ("step two, the part that helped me double my sales"). A bare announcement ("lesson number four") is a dead transition; the source calls this out explicitly in the listicle lesson.

## Format structures (phase 6)

- **Short process** (10-20 min): INTRO, one EMOTION, LOGIC steps (max ~8), END. Explicitly NOT emotion-logic alternating. Optional single emotion insert before a hard step.
- **Deep dive** (25+ min): INTRO, PROOF block (~30s concentrated), EMOTION (usually old way vs new way), LOGIC steps with proof reminders throughout (ideally a client win per step transition), END with aggressive CTA. Simplification is the whole game; the viewer must reach the end.
- **Listicle** (10-20 min): INTRO, [EMOTION + LOGIC] per point, END. One story + one lesson per point, fast. Transitions are the lifeline: every one promises a result. Vary the emotion tool across points. Don't bury a process inside a point.
- Planning flow shared by all planners: set ONE goal (sales/emails/views), package first (title + thumbnail), derive the viewer's top 3 questions from the package, messy brain dump, refine to only what pays off the 3 questions, plan emotion (pick via decision matrix), plan logic steps, conversion strategy by goal, write word for word, upload, measure.

## Verdict against our system (2026-07-16)

**Format planners: faithful.** short-process.md, deep-dive.md, and listicle.md carry the structures, the one-parable rule, the proof block, the highest-leverage filter, the transition lifeline, and the decision matrices accurately. The contract layer is not the problem.

**vid-segment gaps found:**

1. **The skill's spine defaults to the listicle shape.** Its identity line and Phase 2 numbered structure are parable-then-principle, with lean formats as a side note ("lean steps may skip it"). The source inverts this for instructional formats: the default for a short-process or deep-dive step is NO parable, and the per-step question ("is this step complex, or would the viewer be skeptical it matters?") is what earns a parable its place. The skill never asks that question. Fix: shape-first framing in Phase 2; the format planner's shape decides, and lean steps ask the insert question instead of defaulting to a parable.
2. **The new/easy/inspiring test is absent as a quality gate.** It exists in our system only as an EXAMPLE framework inside framework-shapes.md. It is the source's felt test for every point. Fix: silent pass/fail segment test at structure lock (mirrors the context/curiosity/clarity move in vid-thumbnail).
3. **Transitions lack the promise-a-result bar.** The skill says "forward hook" and points at transition-bank; the source's bar is concrete: signal the shift AND promise a result the viewer cares about; bare announcements are dead. The listicle planner has this; the skill (which writes ALL formats' transitions) doesn't. Fix: one line in the transition slot.

**Verified present and correct:** story circle (Problem-Action-Outcome with specifics) in parable-principle-shapes.md; proof after framework; the 20% rule in the planners; framework shapes and selection; parable decision matrix; case-study one-arc shape.

**Backlog notes:** `WORKING-NOTES.md` dev files sit in 6 skill folders (vid-segment, vid-framing, vid-ideas, vid-intake, vid-pressure-test, vid-structure); by design the lead deletes them before productization; none have shipped yet. Verify at next release.
