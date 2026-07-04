---
name: vid-structure
description: Build the outline for one video. Mine the brain-dump against the locked angle into the main points, shape them to the locked format, order them so the title pays off late, and plan the parable and principle for each point. Writes script.md for vid-segment to write from, updates piece.md. Runs after the angle and format are locked, standalone or via the pipeline. Use whenever the creator wants the video outlined or the body planned: "structure this video", "build the outline", "plan the body", "what points should this hit", "outline the script", "map the brain dump into points", "I'm ready to outline this", "build the skeleton", "re-structure this piece".
---

# Video Structure

Turn the raw brain-dump plus the locked angle into a complete outline: the main points, shaped to the format, ordered so the title's promise pays off late, with the parable and principle picked for each point. The writer (`vid-segment`) picks it up and writes prose from it. It never re-plans.

**This skill outlines. It does not write prose.** No intro, no segment prose, no ending, no title, no thumbnail. It does not re-pick the angle or the format; framing locked those. It plans, `vid-segment` writes.

## What it produces

- `content/pieces/{slug}/script.md`: the outline skeleton. An empty `## Intro`, one body section per point (each with its parable and principle picked), an empty `## Ending`, and a `## To build` list of blocks the banks did not have yet.
- `content/pieces/{slug}/piece.md` updates: `status: drafting`, `segment_purposes` (the point list), `segments_completed: []`, `tension_plan` (the setup/payoff plan: central question, which point pays off the title, any threads), `last_updated`.

## Prerequisites

- `content/pieces/{slug}/brain-dump.md` exists with raw material. Missing, redirect to `vid-intake`.
- `content/pieces/{slug}/piece.md` has `selected_angle`, `core_payoff`, `format`, `goal` (framing wrote these). Missing, redirect to `vid-framing`.
- `knowledge/format-planners/{format}.md` exists for the locked format. Missing, show the available formats.

If the pipeline invokes with a slug, skip the "which piece?" question and go straight to Phase 1. If `piece.md` already has `segment_purposes`, this piece is already outlined: show the existing spine and ask whether to refine it or rebuild from scratch. Do not discard prior points unless the creator says so.

## What loads, and when

| File | When | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | Phase 1 | the raw material to mine |
| `content/pieces/{slug}/piece.md` | Phase 1 | the locked angle, payoff, format, goal |
| `knowledge/format-planners/{format}.md` | Phase 1 | the body shape for the locked format |
| `references/brain-dump-mining.md` | Phase 1 | how to tag material into main points, subpoints, combines, and cuts (depth) |
| `knowledge/parable-decision-matrix.md` | Phase 2 | pick the parable type per point |
| one bank folder | Phase 2, on demand | only when a point calls for a specific story / proof / metaphor / framework |
| `assets/script-skeleton-template.md` | Phase 3 | the exact script.md shape to write |

Never load all the banks up front. Query one bank only when a point needs a specific block.

## The flow

Three phases. The creator sees two proposals (the spine, then the built-out plan) and one confirmation. Never announce phase numbers.

### Phase 1: Rough the spine

Load the brain-dump, piece.md, and the locked format's planner.

1. **Mine the brain-dump against the angle.** Tag each lesson, story, or aside: a **main point** (serves the payoff on its own), a **subpoint** (supports a main point), a **combine** (merges with another), or a **tangent** (cut). Depth in `references/brain-dump-mining.md`. Do this silently.
2. **Shape the survivors to the format.** The planner defines the body shape (table below). A listicle is N items, a case study is one story arc, news is three parts. Lay the main points into that shape. Each main point gets a couple of subpoints that state, in a line, what it actually says.
3. **Show the spine.** Main points and subpoints, roughly ordered, plus the cuts (logged, never dropped silent). The creator adds, cuts, merges, or reorders. Lock the spine before building anything out.

### Phase 2: Build out the plan

Load the parable decision matrix. Query a bank only when a point calls for a specific block.

1. **Order for setup and payoff.** Sequence the points so the title's promise pays off late, past the midpoint. Mark the point that carries it. Note any thread (a setup in one point paid off in a later one).
2. **Plan each point's two bricks.** The **parable** (pick the type from the matrix, then the specific story / metaphor / demo, from the bank if you have it or flagged to build) and the **principle** (the framework or lesson, plus the proof).
3. **Show the built plan.** The creator locks or adjusts a point. No prose. This is what the writer works from.

### Phase 3: Write it down

1. **Write script.md** per `assets/script-skeleton-template.md`: the intro stub, one body section per point (parable and principle, nothing else per section), the ending stub, and the `## To build` list (every "to build" flag from Phase 2).
2. **Update piece.md:** `status: drafting`, `segment_purposes`, `segments_completed: []`, `tension_plan` (the setup/payoff plan), `last_updated`.
3. **Confirm in one line:** format, point count, which point pays off the title, blocks to build, handed off.

## Format shapes

Framing locked the format. Read that one planner for the full shape. At a glance:

| Format | Spine shape |
|---|---|
| Listicle | N items, each its own point |
| Deep Dive | 3-5 major lessons, each its own point |
| Roast | per-subject reviews, same shape each |
| Interview | per-question, a through-line the host pulls |
| Short Process | one parable up front, then lean steps |
| Case Study | one story arc: Setup, Problem, Action, Outcome, Lesson + Steps |
| News | three tight parts: What Happened, Why It Matters, What To Do |

If the mined material clearly does not fit the locked format (eleven separate lessons but the format is case study, which is one story), surface it and propose a switch. The creator says yes or no. Do not ask what format they want when it is already locked, and do not force-fit.

## Setup and payoff (the ordering discipline)

Setup and payoff is how the whole video keeps the viewer. A setup raises curiosity, a payoff closes it. The title is the biggest setup, so its answer lands late, not in point 1 (early payoff is the top retention killer). Threads are setups that span points: open a loop here, close it there. Tension is not a thing you build, it is the meter that tells you the setups and payoffs are working. Keep it above zero until the end.

The outline owns the order and the threads. The writer composes the actual forward-hook lines. This skill does not write transitions.

## Rules (and why)

- **Outline, never prose.** The output is a plan of picked blocks and points, not sentences. Prose is `vid-segment`'s job. Writing prose here breaks the two-tier split.
- **Points are material-anchored.** Every point names the actual brain-dump material it carries, never an abstract label like "point 3, the second idea." The writer needs to know which lesson lands where.
- **Blocks are picked, not surfaced.** Phase 2 locks the parable and principle so the writer does not re-plan. If a block is not in the banks, flag it to build, never invent it.
- **Never fabricate.** No invented stories, numbers, results, or bank entries. If the banks are empty for a point, say so and flag it to build.
- **Cuts are logged.** A tangent gets logged as a cut, never dropped silent. The creator may know a cut is the real gold, which means the angle is wrong.
- **Payoff late.** Push the title's answer past the midpoint. The exact spot depends on the format.
- **Machinery stays invisible.** No phase numbers, no "mining complete." The creator sees the spine, then the plan, then the confirm. If they say the outline is obvious, surface once and lock on confirm.

## Reference index

| File | When to read it |
|---|---|
| `references/brain-dump-mining.md` | Phase 1, how to tag material against the angle |
| `references/structure-conversation-examples.md` | worked sessions: clean run, re-structure, format mismatch |
| `assets/script-skeleton-template.md` | Phase 3, the exact script.md shape |
| `knowledge/format-planners/{format}.md` | Phase 1, the locked format's body shape |
| `knowledge/parable-decision-matrix.md` | Phase 2, picking the parable type per point |

## Related skills

- `vid-intake` writes `brain-dump.md`, this skill mines it.
- `vid-framing` writes the framing fields in `piece.md` (`selected_angle`, `core_payoff`, `format`, `goal`), this skill reads them.
- `vid-segment` writes each point's prose from the outline this skill produces.
