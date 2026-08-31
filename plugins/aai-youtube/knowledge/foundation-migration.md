# Foundation migration: single file to split files

Older vaults hold the whole foundation in one file, `foundation/creator-foundation.md`. The current format is five focused files (see `knowledge/foundation-templates.md`). This doc is the one place the migration is defined. `/foundation` and every foundation interview skill run the check below before anything else.

## The check (silent)

1. Does `foundation/creator-foundation.md` exist?
2. Do all five split files exist (`offer.md`, `avatar.md`, `iceberg.md`, `credibility.md`, `backstory.md` under `foundation/`)?

| State | What to do |
|---|---|
| No `creator-foundation.md` | No migration. Run the skill normally. |
| `creator-foundation.md` exists, any split file missing | Old-format foundation. Ask the creator, below. |
| `creator-foundation.md` exists, all five split files exist | The breakup never finished. No ask: carve per the rules below (content lands only in `[pending ...]` sections; populated sections are never touched), verify, delete the original, report in one line, then run the skill normally. |

Every foundation skill uses this same trigger, including the interview skills invoked directly. The old file still existing means the breakup hasn't happened; the delete is what closes it out, so a vault migrates once, completely, instead of piecemeal.

## The ask

Show this once, then wait. Don't start carving or interviewing until the creator picks.

> "Your foundation is in the older single-file format (`creator-foundation.md`). The system now keeps it as five focused files so each skill loads only the slice it needs.
>
> Three ways to get there:
>
> 1. **Upgrade.** I move your existing foundation into the five files, word for word. Fast, nothing rewritten.
> 2. **Enhance.** Same move, then we walk the sections in order and sharpen anything that's drifted since you wrote them.
> 3. **Start fresh.** Full foundation interviews from the top, replacing what's there as we go.
>
> Whichever you pick, your content moves into the five files first, word for word, and the old file is deleted once everything is confirmed there. Which one?"

## Carve, verify, delete

Every path runs the same three steps, whatever the pick, so no content ever exists only in the old file when it goes.

1. **Carve** per the map and rules below.
2. **Verify.** Re-read the five split files and confirm every populated section of the old file is present in its target, moved by this carve or already there. If anything didn't land, stop, keep the old file, and tell the creator exactly what's missing. Never delete on a failed verify.
3. **Delete** `foundation/creator-foundation.md`.

The old file being gone is what marks the migration done, so no skill runs it again, in this session or any later one.

## The carve map

| Section in `creator-foundation.md` | Moves to |
|---|---|
| Offer | `foundation/offer.md` |
| Avatar | `foundation/avatar.md`, Avatar section |
| Top 3 perceived problems | `foundation/avatar.md`, Top 3 section |
| Iceberg Statement (+ Optional longer version) | `foundation/iceberg.md`, statement sections |
| Content pillars (bottom of the iceberg) | `foundation/iceberg.md`, Content pillars section |
| Credibility brags | `foundation/credibility.md` |
| Backstory (+ 3-sentence compressed version) | `foundation/backstory.md` |
| Notes | Template boilerplate is dropped. Anything the creator wrote there moves to `foundation/iceberg.md`'s Content notes section and gets named in the report. |

## Carve rules

- Create each new file from its template in `knowledge/foundation-templates.md`. Set `date` to today; carry the old file's `last_refreshed` forward if it has one, otherwise use today. This carve is the one save that does not bump `last_refreshed`: the content didn't change, only its address.
- Content moves verbatim. The carve is a move, not a rewrite. The creator's wording, numbering, and formatting survive as written.
- **Never overwrite an existing split file or a section holding non-pending content.** Carve only into missing files and `[pending ...]` sections. A split file the creator already has (from a hand migration or an interrupted earlier carve) keeps its content.
- A section that is empty, still `[pending ...]`, or absent from the old file stays pending in the new file. Note which skill fills it.
- The Machinery section of `iceberg.md` (Who / How / What / Tension): lift the four components from the statement `iceberg.md` ends up holding (an already-locked statement in an existing `iceberg.md` wins over the old file's, per the no-overwrite rule). Leave Machinery pending only when no statement is locked anywhere.

## After the pick

Report the migration in one short message: each file created or filled, which sections landed, which are still pending and what skill fills them, and that the original `creator-foundation.md` was deleted after the verify.

Then continue by how the check was reached:

- **Triggered inside a foundation interview skill's pre-check** (the creator invoked `vid-positioning`, `vid-credibility`, etc. directly): after the migration completes, resume that skill's pre-check. The creator asked for that skill; the migration was a detour, not the destination. On **Enhance**, the section they want to sharpen is the one whose skill they invoked; resume it in its refresh path.
- **Triggered from `/foundation`:**
  - **Upgrade:** done. Route normally off the new files; pending sections route to their owning skill.
  - **Enhance:** run the interview chain from `vid-avatar` in refresh mode. Each skill surfaces its locked section and asks "Refresh, keep, or replace?", then auto-advances, so every section gets its walk in order. If the walk is interrupted mid-chain, the creator re-enters it by running any section's skill directly; `/foundation` alone routes by what's pending, not by the unfinished walk.
  - **Start fresh:** invoke `vid-avatar`. The chain runs from the top; each skill surfaces the carried-over section and the creator replaces it through the interview. Replacement happens per section through the interviews, never by blanking files up front.
