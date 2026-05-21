# Release Process

How to ship updates from `authentic-ai-os` to Inner Circle clients.

## The model: two branches

- **`dev`** is the workshop. All 19 skills, all knowledge, internal docs. You work here, always.
- **`main`** is the storefront. Only the 7 shipping skills plus the knowledge they reference. Clients install from `main` (the GitHub default branch).

`main` is never edited by hand. It is rebuilt from `dev` by `scripts/release.ps1`, which uses an allowlist: only the named skills and their auto-detected knowledge reach `main`. WIP skills, unused knowledge, and internal docs cannot leak to a client.

## Versioning

Semver `MAJOR.MINOR.PATCH`:

- **PATCH** (`0.1.0` to `0.1.1`): bug fix, doc edit, prompt tweak inside an existing skill.
- **MINOR** (`0.1.0` to `0.2.0`): a skill graduates and ships, new knowledge, new feature.
- **MAJOR** (`0.1.0` to `1.0.0`): breaking change. Renaming a skill, restructuring, removing functionality.

## Workflow

### 1. Work on `dev`

```
git checkout dev
```

All editing happens on `dev`. WIP skills live in `.claude/skills-wip/` (version-controlled, but outside the plugin's discovery path). Shipping skills live in `.claude/skills/`.

### 2. Graduate a skill (when one becomes ready)

1. Move the folder: `.claude/skills-wip/<skill>` to `.claude/skills/<skill>`.
2. Add `<skill>` to the `$ShipSkills` array at the top of `scripts/release.ps1`.
3. If it needs container structure, add a row to `.claude/skills/creator-setup/manifest.md`.
4. Commit to `dev`.

### 3. Cut the release

From `dev`, clean working tree:

```powershell
pwsh scripts/release.ps1 -Version 0.2.0
```

The script switches to `main`, rebuilds it from `dev` per the allowlist, auto-detects the knowledge the shipping skills reference, bumps the version in both manifests, commits `main`, and returns you to `dev`. It does not push.

Review, then publish:

```
git checkout main
git ls-files          # sanity-check the lean tree
git checkout dev
git push origin main
```

Also push `dev` so the workshop is backed up: `git push origin dev`.

### 4. Notify clients (optional)

Clients see the update on their next Cowork/Claude Code marketplace refresh. To accelerate:

- Post in the Inner Circle community: "v0.2.0 is live. Run `/plugin update authentic-ai-os`."
- Major releases: a 60-second Loom of what changed.

## What ships vs what doesn't

### Ships to clients (the `main` allowlist)

- `.claude-plugin/` (manifest). `.claude/skills/` declared via `"skills": "./.claude/skills"`.
- The 7 (and growing) skills named in `$ShipSkills`.
- `knowledge/` files those skills reference (auto-detected by the release script).
- `CLAUDE.md`, `banks/` schema READMEs, `.gitignore`.

### Never ships

- `.claude/skills-wip/` (WIP skills), unused `knowledge/` files, `.claude/hooks/` + `.claude/settings.json` (the machine-specific Vale hook), `documents/`, `plans/`, `scripts/`, `.vale/`, `.obsidian/`, `templates/`.
- Gitignored personal data: `foundation/`, `banks/` entries, `Content/`, `People/`, `raw/`, `Notes/`, `.env`.

### How clients get a vault

The vault is not shipped. `creator-setup` builds the `Authentic-AI-OS/` container in the client's folder at runtime. `knowledge/` is read from the plugin via `${CLAUDE_PLUGIN_ROOT}`, never copied into a vault.

## Rolling back

`main` is rebuilt, not merged, so rollback is just another rebuild:

```powershell
git checkout dev
git checkout dev~N -- .   # or check out the dev state you want to ship
pwsh scripts/release.ps1 -Version 0.2.1
git push origin main
```

Or `git revert` the bad release commit on `main` and bump a PATCH version. Clients get the fix on next update.
