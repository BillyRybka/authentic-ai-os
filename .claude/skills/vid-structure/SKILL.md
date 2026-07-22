---
name: vid-structure
description: Build the outline for one video. Mine the brain-dump against the locked angle into the main points, shape them to the format, order so the title pays off late, and lock each point's parable, material, principle, and proof. Writes script.md, updates piece.md; vid-intro runs next. Triggers on "structure this video", "build the outline", "plan the body", "what points should this hit", "outline the script", "build the skeleton", "re-structure this piece".
---

# Video Structure

Turn the brain-dump plus the locked angle into a complete plan: the main points shaped to the format, ordered so the title's promise pays off late, every point locked to its parable, its material, its principle, and its proof. `vid-intro` runs next. It hard-stops without this outline, and the transition it writes is the one segment 1 inherits.

**This skill plans. It never writes prose.** No intro, no segment prose, no ending, no title, no thumbnail. It does not re-pick the angle or the format; framing locked those.

## What it produces

- `content/pieces/{slug}/script.md`: the skeleton. An empty `## Intro` stub for `vid-intro`, one body section per point (each carrying only its **Parable:** and **Principle:** plan lines), an empty `## Ending` stub for `vid-ending`, and a `## To build` list of the blocks the banks did not have.
- `content/pieces/{slug}/piece.md` updates: `status: drafting`, `segment_purposes` (the point list), `segments_completed: []`, `tension_plan` (the central question, which point pays off the title, any threads), `last_updated`.

## Prerequisites

- `content/pieces/{slug}/brain-dump.md` exists with raw material. Missing, redirect to `vid-intake`.
- `content/pieces/{slug}/piece.md` has `selected_angle`, `core_payoff`, `format`, `goal` (framing wrote these). Missing, redirect to `vid-framing`.
- `knowledge/format-planners/{format}.md` exists for the locked format. Missing, show the available formats.

If the pipeline invokes with a slug, skip the "which piece?" question. If `piece.md` already has `segment_purposes`, the piece is already outlined: show the existing spine and ask whether to refine or rebuild. Never discard prior points unless the creator says so.

## The bar: a plan the writers never re-plan

A point is planned when the writer could start typing with zero decisions left. Four locks per point:

1. **The parable type**, picked from `knowledge/parable-decision-matrix.md`. The pick, not a shortlist.
2. **The specific material.** The exact bank block (a wikilink) or the exact brain-dump moment it runs on. "A story from the bank" is not a material.
3. **The principle, stated as the lesson itself.** Not "something about ownership": the sentence the viewer could repeat back.
4. **The proof, linked or flagged.** `Proof: [[proof-slug]]` rides the principle line. Where the banks and the dump have nothing, the line says `to build` plus exactly what is needed, and the gap lands as a row in `## To build`. Never invent to fill a hole.

Worked, from a locked listicle plan:

> Thin:
>
> ```
> ## Mistake 3: No owner
> **Parable:** story, a client story about ownership
> **Principle:** assign an owner
> ```
>
> Complete:
>
> ```
> ## Mistake 3: No owner assigned to the process
> **Parable:** story. [[story-bank/agency-owner-fired-himself]]: Marcus had a process but no owner, so it defaulted back to him.
> **Principle:** a process with no owner defaults back to you. Assign the owner.
> ```
>
> The thin one leaves the writer three decisions: which story, what it shows, what the lesson says. Every leftover decision becomes a re-interview with the creator, one segment at a time. The complete one leaves only words to write.

> A gap named, not filled:
>
> ```
> ## Mistake 4: You document it once and never update it
> **Parable:** to build. Needs a quick real example of a stale document causing a miss.
> **Principle:** the document is a living thing; reality changes, the doc follows.
> ```
>
> The banks had no match and the dump had no moment, so the plan names the hole. Filling it with an invented example is fabrication. Flagging it is the job.

The locks flex by format. Persuasive formats (Listicle, Roast, Interview) run parable + principle at every point. Instructional formats (Short Process, Case Study, Deep Dive, News) run one parable arc up front, then steps: the parable line tracks the arc ("story (continued)") and locks `none` where an earlier section already carried the emotion. Never force a fresh parable onto a step; the format planner owns that call.

A writer that has to re-pick a block, re-derive a lesson, or hunt for proof is a boundary bug: the planning leaked downstream. The fix is always here, never in the writer.

## Ordering: payoff late is judgment, not a rule

The title is the biggest setup the video makes, so its full answer lands late, past the midpoint. That is a default with a mechanism, not a commandment: the viewer clicked holding one question, and once the full answer lands, their reason to stay is gone. `knowledge/script-tension-architecture.md` owns the cross-segment mechanics. This section is the ordering judgment you apply per point.

**Withhold what the avatar does not already believe.** The point that answers the title, or inverts advice the avatar follows right now, is the payoff. Earlier points deliver pieces: context, mistakes, the mechanism. Each closes a small curiosity while the central one stays open.

**Front-load what the avatar already knows.** A point the avatar gets in one line is recognition, not revelation. Land it fast and move on; stringing out what the viewer already got is what earns "get to the point." The test after any payoff lands: does the avatar still want to know something? If yes, keep going. If no, the next point must open a new loop.

**Let the format set how late "late" is.** News pays off at "why it matters," minutes in. A Short Process pays off at the final step by construction. A Listicle holds the biggest item for last. The locked format's planner carries that arc, and it outranks the default.

Worked, listicle, title "The 'best practices' quietly killing your channel":

> Weak order: 1. 'just post consistently' 2. copying thumbnails 3. the 5-second hook 4. overpromising titles. The named answer lands 90 seconds in. Everything after is bonus footage, and the viewer leaves.
>
> Locked order: 1. copying the big channels' thumbnails 2. the '5-second hook' myth 3. titles that overpromise 4. 'just post consistently' (title payoff). Item 4 is the advice the avatar follows right now, so it is the one worth withholding. Items 1-3 each close their own small question while "which best practice is killing mine?" stays open to the end.

Then mark the plan: which point pays off the title, plus 1-2 threads (a setup one point opens, a later one closes). It all lands in `tension_plan`. The writers read it; they do not re-derive it.

## The flow

Three phases. The creator sees two proposals (the spine, then the built plan) and one confirmation. Never announce phase numbers.

### Phase 1: Rough the spine

Load the brain-dump, piece.md, and the locked format's planner.

1. **Mine the dump against the angle.** Every block gets a tag: main point, subpoint, combine, or tangent. Silent work; method and worked tagging in `references/brain-dump-mining.md`.
2. **Shape the survivors to the format.** Lay the main points into the planner's body shape (table below). Each main point gets a couple of subpoints that state, in a line, what it actually says.
3. **Show the spine.** Points, subpoints, and the cuts. The creator adds, cuts, merges, reorders. Lock the spine before anything gets built out.

### Phase 2: Build out the plan

Load `knowledge/parable-decision-matrix.md`. Query one bank only when a point calls for a specific block; never load the banks up front.

1. **Order the locked spine** per the judgment above.
2. **Lock all four per point** to the bar above. This is the phase the writers count on; a half-built plan here becomes a re-interview there.
3. **Show the built plan.** The creator locks or adjusts a point. No prose.

### Phase 3: Write it down

1. **Write script.md** per `assets/script-skeleton-template.md`: intro stub, one body section per point, ending stub, `## To build`, CUTS comment.
2. **Update piece.md** with the fields listed above.
3. **Confirm in one line:** format, point count, which point pays off the title, blocks to build, handed to `vid-intro`.

Worked sessions (clean run, re-structure, format mismatch): `references/structure-conversation-examples.md`.

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

If the mined material clearly does not fit the locked format (eleven separate lessons, but the format is case study, which is one story), surface it and propose a switch. The creator says yes or no. Never force-fit, and never re-ask the format from scratch.

## Rules (and why)

- **Never fabricate.** No invented stories, numbers, results, or bank entries. Empty banks mean a named gap, not an invented block.
- **Cuts are logged, never dropped silent.** In the spine, and in the CUTS comment so re-structure runs do not re-propose them. The creator may know a cut is the real gold, which means the angle is wrong.
- **Never pad to a count.** Mining yields what it yields. A gap between the points and the format's shape gets surfaced (thin dump routes to `vid-intake`, wrong format to `vid-framing`), never filled with tangents.
- **Machinery stays invisible.** No phase numbers, no "mining complete." The creator sees the spine, then the plan, then the confirm.
