---
name: vid-structure
description: Build the outline for one video. Mine the brain-dump against the locked frame into the main points, shape them to the format, order so the title pays off late, and lock each point's parable, material, principle, and proof. Writes script.md, updates piece.md; vid-intro runs next. Triggers on "structure this video", "build the outline", "plan the body", "what points should this hit", "outline the script", "build the skeleton", "re-structure this piece".
---

# Video Structure

Turn the brain-dump plus the locked frame into a complete plan: the main points shaped to the format, ordered so the title's promise pays off late, every point locked to its parable, its material, its principle, and its proof. `vid-intro` runs next. It hard-stops without this outline, and the transition it writes is the one segment 1 inherits.

**Scope: the plan, never the prose.** No intro, no segment prose, no ending, no title, no thumbnail. It does not re-pick the frame or the format; framing locked those.

## Core principles

- **Plan so completely the writers never re-plan.** Four locks per point: the parable type, the specific material, the principle, the proof. A writer that has to re-pick a block, re-derive a lesson, or hunt for proof is a boundary bug, and the fix is always here, never in the writer.
- **Payoff late is judgment, not a rule.** The viewer clicked holding one question, and once the full answer lands, their reason to stay is gone. So the title's answer lands past the midpoint by default, and the locked format outranks the default.
- **Never fabricate.** No invented stories, numbers, results, or bank entries. Where the banks and the dump have nothing, the plan names the hole and it lands in `## To build`. Flagging the gap is the job.
- **Cuts are logged, never dropped silent.** In the spine, and in script.md's CUTS comment so re-structure runs do not re-propose them. The creator may know a cut is the real gold, which means the frame is wrong.
- **Never pad to a count.** Mining yields what it yields. A gap between the points and the format's shape gets surfaced, thin dump back to `vid-intake` or wrong format back to `vid-framing`, never filled with tangents.
- **Machinery stays invisible.** No step numbers, no "mining complete." The creator sees the spine, then the built plan, then the confirm.

## What loads, and when

Load each file at the step that needs it. Never bulk-load the banks; query one only when a point calls for a specific block.

| File | Step | For |
|---|---|---|
| `content/pieces/{slug}/brain-dump.md` | 1 | the raw material to mine |
| `content/pieces/{slug}/piece.md` | 1 | the locked frame, core payoff, format, goal, title, plus `## The Read` (the Transformation is what the outline has to deliver; absent on older pieces, work from the frame and payoff) |
| `knowledge/format-planners/{format}.md` | 1 | the body shape this format runs |
| `references/brain-dump-mining.md` | 1 | the four tags and the mining sequence |
| `references/point-planning.md` | 2 | the ordering judgment and the four locks |
| `knowledge/parable-decision-matrix.md` | 2 | picking the parable type per point |
| one bank, on demand | 2 | the exact block a point calls for |
| `knowledge/script-tension-architecture.md` | 2 | optional depth when a piece has an unusual arc |
| `assets/script-skeleton-template.md` | 3 | the exact shape of script.md |
| `assets/piece-structure-additions.md` | 3 | the fields to append to piece.md |

Stops: no `brain-dump.md`, point to `vid-intake`. No `frame`, `core_payoff`, `format`, or `goal` in piece.md, point to `vid-framing`. No planner on disk for the locked format, show the seven and let the creator lock a real one.

Re-structure: if piece.md already carries `segment_purposes`, the piece is outlined. Show the existing spine and ask whether to refine or rebuild. Never discard prior points unless the creator says so.

If the pipeline invokes with a slug, skip the "which piece?" question.

## Format spines at a glance

Framing locked the format and this is only the silhouette. Read that one planner for the real shape.

| Format | Spine shape |
|---|---|
| Listicle | N items, each its own point |
| Deep Dive | 3-5 major lessons, each its own point |
| Roast | per-subject reviews, same shape each |
| Interview | per-question, a through-line the host pulls |
| Short Process | one parable up front, then lean steps |
| Case Study | one story arc: Setup, Problem, Action, Outcome, Lesson + Steps |
| News | three tight parts: What Happened, Why It Matters, What To Do |

When the mined material clearly does not fit the locked format (eleven separate lessons, but the format is case study, which is one story), surface it before proposing a spine and give the creator two routes: re-frame to a format that fits, or pick the one thing this format can carry and demote the rest. They decide. Never force-fit, and never re-ask the format from scratch.

## The workflow

Three steps. The creator sees two proposals (the spine, then the built plan) and one confirmation.

### 1. Rough the spine

1. **Mine the dump against the frame.** Every block gets one tag: main point, subpoint, combine, or tangent. Silent work; the method and a worked tagging pass are in `references/brain-dump-mining.md`.
2. **Check the fit.** If the surviving material does not fit the locked format, surface it now rather than shaping a spine around a mismatch.
3. **Shape the survivors to the format.** Lay the main points into the planner's body shape. Each main point gets a couple of subpoints that state, in a line, what it actually says.
4. **Show the spine.** Points, subpoints, and the cuts. The creator adds, cuts, merges, reorders. Lock the spine before anything gets built out.

### 2. Build out the plan

1. **Order the locked spine.** Withhold what the avatar does not already believe, front-load what they already know, and let the format set how late "late" is. The judgment and a worked reorder are in `references/point-planning.md`.
2. **Lock all four per point.** This is the step the writers count on; a half-built plan here becomes a re-interview there, one segment at a time.
3. **Mark the arc.** The central question, which point pays off the title, and 1 or 2 threads. That becomes `tension_plan`.
4. **Show the built plan.** Point by point, with one line on why the order changed. The creator locks or adjusts a point. No prose.

### 3. Write it down

1. **Write script.md** per `assets/script-skeleton-template.md`.
2. **Append to piece.md** per `assets/piece-structure-additions.md`.
3. **Confirm in one line:** format, point count, which point pays off the title, what still needs building, handed to `vid-intro`.

Worked sessions (a clean run, a re-structure, a format mismatch) are in `references/structure-conversation-examples.md`.

## Output and handoff

`content/pieces/{slug}/script.md`, the skeleton: an empty `## Intro` stub for `vid-intro`, one body section per point carrying only its **Parable:** and **Principle:** plan lines, an empty `## Ending` stub for `vid-ending`, a `## To build` list of the blocks the banks did not have, and the CUTS comment.

`content/pieces/{slug}/piece.md`, appended: `status: drafting`, `segment_purposes`, `segments_completed: []`, `tension_plan`, `last_updated`. Append only, never overwriting another skill's fields; the ownership map is in `knowledge/piece-contract.md`.

Then `vid-intro`, which reads the outline and writes the opening the first segment inherits.

## Before you save

- Every point carries all four locks, or a named `to build` where the material genuinely does not exist yet.
- Every `to build` flag has a matching row in `## To build`. An empty list means the script is fully sourced.
- Headers are material-anchored. Never `## Point 3: {placeholder}`.
- Cuts are logged, in the spine the creator saw and in the CUTS comment.
- `tension_plan` names the central question, the point that pays off the title, and any threads.
- After the payoff point, nothing is left running that the viewer already got. If a later point exists, it opens something new.
- Parable and principle are one line each. No prose anywhere in the file.
- No em-dashes, and the point headers read the way the creator talks.

## References for depth

- `references/brain-dump-mining.md`: the four tags, the mining sequence, the tag-disagreement protocol.
- `references/point-planning.md`: the ordering judgment and the four locks, with worked examples and how the locks flex by format.
- `references/structure-conversation-examples.md`: full sessions, including a re-structure and a format mismatch.
- `assets/script-skeleton-template.md` and `assets/piece-structure-additions.md`: the exact shape of both files this skill writes.
