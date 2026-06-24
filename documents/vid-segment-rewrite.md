---
type: project-doc
doc: vid-segment-rewrite
project: authentic-ai-os
status: planning
date: 2026-06-23
tags: [project, vid-segment, rewrite, streamline]
---

# vid-segment rewrite plan

The agreed direction for streamlining vid-segment. Read-only investigation done. Nothing rebuilt yet. Decisions and moving-items tracked here so they do not get lost.

## The job (locked)

vid-segment takes one already-planned point, reads the segment card from vid-structure (what the point is, its tension role, what comes next, and what material has been prepared), and writes that one point as finished script prose in the creator's voice. It is the writer for a single point. It does not plan, build references, decide the segment strategy, or hunt material. vid-structure did that.

## The mental model (baked into the skill, not loaded at runtime)

A point shows then tells: parable (the show) then principle (the tell). Use these as functions reached for by judgment, not a rigid slot order and not Ed's old emotion/logic labels.

Not every video type needs the same per-segment parable -> principle loop. Story, belief-change, persuasive, and insight-heavy videos usually benefit from the fuller show-then-tell movement inside major points. Tutorial, process, case-study, or deep-dive videos may put the main parable/emotional setup near the beginning of the video, then run leaner principle-heavy segments after that. vid-segment follows the segment card's intended shape instead of forcing every segment into the same loop.

The craft of writing a point lives IN the skill's instructions. The skill never opens an external how-to-write-a-point document.

## Transition (light, not a third brick)

Include it on the structure card, but lightly. It is not a formal brick equal to parable and principle.
- Treat it as the question: "What does this segment make the viewer want next?"
- Not as the instruction: "Now write a formal transition paragraph."
- Sometimes one sentence, sometimes baked into the last line of the principle, sometimes not needed because the format already supplies the next step.
The segment almost always knows where it hands off, because the outline tells it. Keep it useful, not rigid.

## Load model (three tiers)

- Always, together (the act of writing a point): parable/principle judgment + transition + setup/payoff craft, plus the segment card, the point's prepared material, and the voice reference. One cluster, because these shape each other.
- Only when that block or claim is in play (light): the story, metaphor, or proof reference for the block actually being written, and the visual-callout and visual-proof-callout conventions when a visual or a claim lands.
- Never inline: full demo or framework interviews.

## Lean process (four steps)

1. Read the segment card and the point's prepared material. No re-deciding the strategy, no building references, no re-querying banks. vid-structure already did that.
2. Write the point: parable, principle, light transition, in voice. Proof after the framework. Visual and visual-proof callouts dropped as they come up.
3. One voice check, not three.
4. Save and mark the segment done.

If a block's material is genuinely missing, flag it as an upstream gap. Do not build it here.

## What is moving OUT of vid-segment (so we do not forget)

- Framework build (the 5-step interview): currently inline. Move to vid-capture Stage F (framework already lives there). vid-segment just writes a framework that already exists.
- Visual-demo build (the 3-step brainstorm): currently inline, no home today. Proposed new skill vid-demo (on the build list).
- Re-querying the banks: vid-structure already surfaced the blocks. vid-segment reads that result, does not re-query.
- The two extra voice passes: the deep voice audit moves to vid-voice-audit at the full-script stage (inside vid-pressure-test). vid-segment keeps one light check.
- Cleanup: delete WORKING-NOTES.md, convert markdown tables to lists, fix the dangling banks/transition-bank.md reference.

## Open decisions (need Billy's call)

1. Voice: one light check in vid-segment plus the deep audit at the full-script stage. Confirm, or cut the per-segment deep check entirely?
2. Visual demo home: a new vid-demo skill, or a non-saving stage inside vid-capture?
3. Framework build: confirm it lives in vid-capture and vid-segment only references a built one.
4. Case study currently runs as "one big parable across the whole body." Keep it as a documented format exception, or make every format follow the same per-segment functions?

## Status

Investigation and diagnosis complete (read-only). Fuller diagnosis record is in the session scratchpad. Nothing in the skill rebuilt yet. Next: lock the four decisions, then rewrite vid-segment to this spec. vid-demo to be added to the build-plan skills inventory once confirmed.
