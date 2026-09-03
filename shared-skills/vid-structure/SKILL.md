---
name: vid-structure
description: Build the body outline for one video from a completed brain dump and locked frame, format, title, and thumbnail. Mines the dump against the frame, lays the survivors into the locked format's body shape, locks each section's parable, principle, material, and proof the way that format uses them, and writes the script.md skeleton plus piece.md state that vid-intro, vid-segment, and vid-ending read. Use to structure or safely re-structure a selected piece. Triggers on "structure this video", "build the outline", "plan the body", "what points should this hit", "outline the script", "build the skeleton", "re-structure this piece". Not for intro, body prose, ending, title, thumbnail, or a new frame.
---

# Video Structure

The body is what the viewer needs in order to reach the core payoff, built from the brain dump and kept true to the locked title and thumbnail. Plan it with the creator, shaped to the locked format, so a writer can draft any section without re-picking a story, re-deriving a lesson, or hunting for proof. `vid-intro` runs next.

Scope is the plan, never the prose. No intro, no segment prose, no ending, no title, no thumbnail, no new frame.

## Core principles

- **The planner owns the shape.** Each format has its own body: one parable then steps, parable and principle at every point, one story arc, three tight news beats. `references/format-plans/{format}.md` is the body plan for the locked format. Read that one file, never the other six.
- **Plan so completely the writers never re-plan.** Every section is locked to the plan lines its format uses: the parable type and the exact material, the principle stated as the lesson itself, the proof linked or flagged. A writer that has to re-pick a block, re-derive a lesson, or hunt for proof is a boundary bug, and the fix is always here.
- **Never fabricate.** No invented stories, numbers, results, sources, or bank entries. Where the banks and the dump have nothing, the plan names the hole and it lands in `## To build`.
- **Cuts are logged, never dropped silent.** The creator may know a cut is the real gold, which means the frame or the format is wrong.
- **Never pad to a count.** Mining yields what it yields. A gap between the material and the format's shape gets surfaced: thin dump back to `vid-braindump`, wrong format back to `vid-framing`. Never filled with tangents.
- **Machinery stays invisible.** No step numbers, no "mining complete." The creator sees the spine, then the built plan, then one confirmation.

## What loads, and when

| File | When | For |
|---|---|---|
| `content/pieces/{slug}/piece.md` | 1 | the locked frame, core payoff, format, goal, title, thumbnail text, `must_not_become`, `## The Read` |
| `content/pieces/{slug}/brain-dump.md` | 1 | the raw material |
| `references/brain-dump-mining.md` | 2 | the four tags and the mining sequence |
| `knowledge/format-planners/{format}.md` | 3 | the body structure and the parable types this format uses. Ignore its packaging, intro, conversion, and upload sections; other skills own those |
| `references/format-plans/{format}.md` | 3 | the body plan: the sections, what each one locks, where the payoff lands |
| `references/source-and-gap-policy.md` | 4 | naming sources, picking a bank entry, deciding what needs proof, what counts as a hole |
| one bank, on demand | 4 | the exact block a section calls for |
| `knowledge/script-tension-architecture.md` | 4 | only when the piece has an unusual arc |
| `references/restructure-safety.md` | any | before changing a piece that already has an outline or prose |
| `assets/script-plan-template.md`, `assets/piece-state-template.md` | 5 | the exact shape of both files this skill writes |

Never bulk-load the banks. Never read another piece.

## 1. Validate the piece

If no piece or slug was selected, ask which video. Do not scan for a likely one.

Confirm `piece.md` has `type: content-piece` and a `slug` matching its folder, `brain-dump.md` exists without a `## Still capturing` marker, and `frame`, `core_payoff`, `format`, `goal`, `title`, and a nonempty `thumbnail_text` are set. The format must be one of `step-by-step`, `success-story`, `list-video`, `review`, `deep-dive`, `interview`, `news`, with a planner on disk.

Route a missing prerequisite to its owner and stop. Do not fill another skill's field. If the pipeline already verified these, do not repeat the check aloud.

If `segment_purposes` or a planned `script.md` already exists, this is a re-structure. Read `references/restructure-safety.md` before proposing anything.

## 2. Mine the dump

Silent work. Every block in the dump gets one tag against the frame and `## The Read`: main point, subpoint, combine, or tangent. Pull the material anchor for every keeper: the exact phrasing, number, name, or moment. The method is in `references/brain-dump-mining.md`.

## 3. Shape to the format, then show the spine

Load the planner's body structure and the body plan for the locked format. Lay the surviving main points into that shape: steps, points, reviews, questions, story beats, or news beats, with each subpoint under its parent.

Check the fit before proposing. Eleven separate lessons in a success story, or a full system in a step-by-step, is a mismatch. Surface it and give the creator two routes: return to `vid-framing` for a format that fits, or narrow to the one thing this format carries and log the rest as cuts. They decide. Never force-fit, and never re-ask the format from scratch.

Show the spine: sections in proposed order, one line each in the creator's own material, subpoints under them, cuts with reasons. The creator adds, cuts, merges, reorders. Lock the spine before building anything out.

For a simple piece with an obvious shape, the spine and the built plan can be one proposal.

## 4. Build the plan

**Order.** Withhold what the avatar does not already believe. Front-load what they already know; recognition lands in a line. The locked format sets how late the payoff lands, and the body plan says where. After any payoff, the next section must open something new or the viewer is done.

**Lock every section** to the fields its body plan names. A field is a label line, then the beats under it as bullets: what the parable shows, moment by moment; what the principle says, point by point. As many bullets as the section needs, and no fewer than a writer needs to draft without asking. A field the format does not use in that section is left out, never written as `none`. The common pair:

- **Parable:** the label carries the type, from the planner's own matrix, plus the material: a bank wikilink or the dump anchor, or `to build` where the banks and dump have nothing. The bullets carry the beats of the story, the two sides of the contrast, what the demo shows.
- **Principle:** the bullets carry the lesson as the viewer would repeat it, the reason it is true, and the move. `Proof: [[proof-bank/slug]]` or `Proof: to build` rides the bullet that makes the claim.

Some formats lock different fields. A success story locks story beats and a lesson. A review locks the asset, the problems, and the fix. News locks facts with sources. The body plan for that format is the authority, and its example is the bar.

Source rules, bank selection, proof decisions, and what counts as a hole are in `references/source-and-gap-policy.md`. A hole in material is a `to build` flag. A hole that makes the format impossible, such as a success story with no outcome or a news fact with no source, gets named to the creator before anything saves. They choose: capture it, narrow the claim, cut, or go back.

**Mark the arc.** The central question the viewer is holding from the title, which section pays it off, and one or two threads a section opens and a later one closes. Three or more running at once floods the viewer. Where nothing connects, say so rather than inventing a thread.

**Show the built plan.** Section by section, plan lines only, with one line on why the order changed if it did. The creator locks or adjusts. No prose.

## 5. Save and verify

Read both asset templates. Prepare both complete edits before writing either.

1. Write `script.md`: the Intro stub, one body section per locked section with its fields and beats, the Ending stub, `## To build`, the CUTS comment.
2. Update only structure-owned fields in `piece.md`: `segment_purposes`, `tension_plan`, `segments_completed: []` on a first outline, `status: drafting` when advancing from `ideating`, `last_updated`.
3. Re-read both. Section headings and `segment_purposes` match exactly and in order. Intro and Ending stubs exist. Every `to build` flag has a row in `## To build`. Every wikilink resolves. Non-owned fields are unchanged.
4. If a write or check fails, restore only the files this save touched and report it.

Never regress a later lifecycle status. Planning a bank entry does not count as using it: do not touch `*_used`, `used_in`, or an entry's status.

Confirm in one line: format, section count, which section pays off the title, what still needs building, handed to `vid-intro`.

## Before you save

- The creator locked the spine and the built plan.
- Every section carries the fields its body plan names, each with its beats under it and exact material or a `to build` flag.
- Headings are material-anchored and read the way the creator talks. Never `## Point 3: {placeholder}`.
- The section count is the real count, never padded to the format's typical shape or to a title's number the material cannot support.
- Cuts are logged with reasons.
- `tension_plan` names the central question, the payoff section, and any threads.
- Labels and beats, no prose. A bullet is a note to the writer, not a line of the script.
- No em-dashes.
