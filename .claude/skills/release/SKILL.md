---
name: release
description: Orchestrates the dev-to-main release pipeline for authentic-ai-os. Handles the file-moving work when a WIP skill graduates (move folder, flip the map, update the manifest, commit) and then drives `scripts/release.ps1` to rebuild the lean `main` branch. Routine releases (no graduation) just bump the version and run the script. Dev-only; never ships to clients. Triggers on "cut a release", "ship a release", "release v0.X.Y", "graduate {skill}", "graduate {skill} and release", "park {skill}", "demote {skill}", "/release", or whenever the creator wants to publish updates from `dev` to `main`.
---

# Release

The dev-to-main pipeline orchestrator. The release script (`scripts/release.ps1`) is the dumb-but-correct file curator. This skill is the brain: it handles the things humans miss (folder moves, map flips, manifest rows, commit messages) and then hands off to the script for the actual rebuild.

## Source of truth

`documents/skill-knowledge-map.md` is the only place that decides what ships. Each skill is tagged ` ``SHIPPED`` ` or ` ``WIP`` ` on a line starting with `**<name>**`. The release script reads this file directly; never edit any other ship-list anywhere.

## Three modes

**Routine release.** No skill is graduating or being parked. The shipping set stays the same. Just bump the version and rebuild `main`. Triggers: "cut a release", "release v0.X.Y", "ship a release", "/release".

**Graduation release.** A WIP skill is ready for clients. Move it from `skills-wip/` into `skills/`, flip its map tag to `SHIPPED`, add container rows to `creator-setup/manifest.md` if it needs folders in the client's vault, commit, then run the release. Triggers: "graduate {skill}", "graduate {skill} and release", "promote {skill}".

**Park (demote).** A SHIPPED skill needs to come off the storefront (regression, doc rewrite, scope change). Move it from `skills/` into `skills-wip/`, flip the map tag to `WIP`, remove its rows from the manifest, commit. No release runs unless the creator also asks for one. Triggers: "park {skill}", "demote {skill}", "pull {skill} from shipping".

## Pre-flight (every mode)

Run these silently first. If any fails, stop and report the exact failure.

1. Current branch is `dev`. If not, refuse and tell the creator to `git checkout dev`.
2. Working tree is clean (`git status --porcelain` empty). If not, list the dirty files and refuse.
3. `documents/skill-knowledge-map.md` exists and contains at least one `SHIPPED` row.
4. Every `SHIPPED` skill in the map has a real folder at `.claude/skills/<name>/SKILL.md`. If any are missing, refuse and report which.

## Mode A: routine release

1. Read the current version from `.claude-plugin/plugin.json`.
2. Read the map. List the SHIPPED set so the creator can see what will ship.
3. Ask the creator for the new version. Recommend the bump based on what changed since the last release tag (run `git log` quickly; if only doc/typo edits, suggest PATCH; if a new skill, suggest MINOR). Validate semver format.
4. Run the script: `pwsh scripts/release.ps1 -Version <new>`.
5. Parse the script's output. Confirm the "Skills:" line matches the map's SHIPPED set. If not, panic, tell the creator something is wrong, do not proceed.
6. Report what shipped (count and names) and what stayed parked (the WIP set). Give the exact `git push origin main` command for review.

## Mode B: graduation release

1. The creator named a skill (e.g. "graduate vid-capture"). Confirm the name back to them.
2. Verify `.claude/skills-wip/<name>/SKILL.md` exists. If not, refuse with "no WIP folder for {name}; check the name".
3. Verify the map has `**<name>** ` `` `WIP` `` ` on a line. If it already shows SHIPPED, ask whether to proceed anyway (the file probably just needs moving).
4. Move the folder: `git mv .claude/skills-wip/<name> .claude/skills/<name>`.
5. Flip the map: in `documents/skill-knowledge-map.md`, change the line `**<name>** ` `` `WIP` `` ` to `**<name>** ` `` `SHIPPED` `` `. Make exactly that edit; do not touch the rest of the map. If the skill's knowledge-deps section needs review, surface it to the creator as a follow-up but do not block the release.
6. Container check. Read `<name>/SKILL.md` and any `references/` and `assets/` for folder paths the skill writes into (patterns like `foundation/`, `banks/<bank>/`, `people/`, `content/...`, etc., relative to the creator's vault). If any are not already covered by `.claude/skills/creator-setup/manifest.md`, ask the creator: "vid-X writes to {paths}. Add these to creator-setup/manifest.md so a fresh `creator-setup` run scaffolds them?" If yes, append rows in the manifest's table with class `structure` and since-version equal to the upcoming release.
7. Commit on `dev`: `git add -A; git commit -m "Graduate <name>: WIP -> SHIPPED"`.
8. Continue into Mode A from step 1 (version selection through release).

## Mode C: park / demote

1. The creator named a skill. Confirm the name.
2. Verify `.claude/skills/<name>/SKILL.md` exists.
3. Verify the map has `**<name>** ` `` `SHIPPED` `` `.
4. Move the folder: `git mv .claude/skills/<name> .claude/skills-wip/<name>`.
5. Flip the map: `SHIPPED` to `WIP` on that line only.
6. Remove the skill's rows from `creator-setup/manifest.md` if present (the manifest may have multiple rows for one skill; remove all of its rows).
7. Commit on `dev`: `git add -A; git commit -m "Park <name>: SHIPPED -> WIP"`.
8. Ask the creator: "park complete. Cut a release now to remove {name} from clients?" If yes, continue into Mode A. If no, stop.

## Safety rules

- **Never edit `main` directly.** Only `scripts/release.ps1` touches `main`.
- **Never commit a graduation on `main`.** All graduation work happens on `dev`. The script then rebuilds `main`.
- **Never edit the map's structure.** Only flip the ` ``SHIPPED`` ` / ` ``WIP`` ` tag on a single line; never reorder, never add or remove rows, never touch headings.
- **Never invent a skill name.** If the named skill doesn't exist in either `skills/` or `skills-wip/`, refuse with "no skill named {name}". Don't guess.
- **Never bump the version backwards.** Reject a -Version older than the current.
- **Refuse if drift exists.** If a map SHIPPED line points at a folder that isn't in `.claude/skills/`, or vice versa, stop. Tell the creator which row mismatches reality and let them resolve.

## What this skill does NOT do

- It does not write or update `CHANGELOG.md`. (No changelog file exists yet; if/when one is added, that becomes a follow-up.)
- It does not push to `origin`. Push is the creator's review gate. The skill ends with the exact push command printed.
- It does not modify the knowledge auto-detect logic in the script. The script greps the shipped skills' files for `knowledge/X.md` references; that stays automatic.
- It does not ship to clients on its own. Push to `origin/main` is the only step that exposes the release.

## After every release

Print a clean receipt:

```
Released v<version>.
Shipped (<n> skills): <comma list>
Knowledge shipped (<n>): <comma list>
Parked WIP (<n>): <comma list>

Review:  git checkout main; git ls-files; git checkout dev
Publish: git push origin main; git push origin dev
```

That is the whole loop.
