---
type: skill-reference
skill: vid-structure
purpose: safe behavior when script.md or completed segments already exist
---

# Re-structure Safety

Use this whenever `segment_purposes` exists or `script.md` contains a prior plan or prose.

## Establish protected state

Read the complete current `piece.md` and `script.md`. Take exact in-memory snapshots before any save.

Treat a body section as completed when either condition is true:

- its label appears in `segments_completed`
- it contains text beyond recognized planning fields, stubs, or unresolved production notes

Use the union. A stale completion list must not expose prose to replacement.

Older pieces may use shortened completion or purpose labels that do not exactly equal their body headings. Preserve those completed identifiers rather than renaming downstream-owned state. Require one unambiguous heading match for each legacy identifier, keep the mapping stable, and use exact heading labels for every new uncompleted section. Do not use this exception on a first V2 outline.

Intro prose belongs to `vid-intro`, body prose to `vid-segment`, and ending prose to `vid-ending`. Preserve it byte for byte unless the creator runs the owning writing skill to revise it.

Once downstream prose exists, preserve the complete `script.md` frontmatter as protected state. V2 does not change its `status`, `tier`, `piece`, or `last_refreshed` during re-structure until shared ownership is defined at promotion.

## Safe changes

When no body prose is completed, V2 may replace the body plan after approval while preserving any existing intro or ending prose. Rebuild `segment_purposes` and `tension_plan` to match.

When body prose is completed, V2 may safely:

- refine or replace plan blocks only in uncompleted sections
- cut, merge, add, rename, or reorder only within the uncompleted suffix
- update cuts, production follow-ups, and tension decisions that do not change a completed section's job or position
- preserve completed section labels, order, prose, and matching `segments_completed` entries exactly

## Changes that require downstream revision

Do not save a supposedly writer-ready re-structure when the approved change would:

- cut, rename, reorder, merge, split, or change the job of a completed section
- move a new section before completed prose
- make an existing intro promise or completed transition false
- change the payoff or thread responsibility of completed prose
- require clearing or rewriting `segments_completed`

Show the affected sections and the smallest revision required. Route each completed body section back through `vid-segment`; route an affected intro or ending to its owner. After those revisions are approved and completion state is reconciled, run structure again to save the new canonical plan.

This is a real stop, not a warning. Vid-structure does not own completed prose or the completion record.

## Lifecycle safety

- First outline from `ideating`: set `status: drafting`.
- Already `drafting`: keep it.
- `filming-ready`, `filmed`, `editing`, or `published`: do not regress status. Explain that structural changes invalidate later work and require an explicit revision path through the owning skills.

## Save protocol

Prepare the complete new script and piece states in memory. Verify that protected prose and fields are unchanged before writing.

Write `script.md`, then `piece.md`, then re-read both. If a write or verification fails, restore both exact snapshots. If `script.md` did not exist before the attempt, remove only the new incomplete file during rollback.

Never clear `segments_completed` to make the pipeline route conveniently. Never leave section count and completion state disagreeing after a successful save.

## Example

Two of five sections are complete. The creator wants to merge sections four and five. That is safe: preserve sections one and two exactly, leave section three's plan intact unless approved otherwise, merge the two untouched plan blocks, and update the ordered purposes.

The same creator wants the new merged section to become section one. That changes the position and handoff of completed prose. Do not move it silently. Identify the affected intro and completed sections and route them for revision first.
