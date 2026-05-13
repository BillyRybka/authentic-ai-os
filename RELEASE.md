# Release Process

How to ship updates from `authentic-ai-os` to Inner Circle clients.

## Versioning

Semver: `MAJOR.MINOR.PATCH`

- **PATCH** (`0.1.0` → `0.1.1`): bug fix, doc edit, prompt tweak inside an existing skill
- **MINOR** (`0.1.0` → `0.2.0`): new skill, new command, new agent, new knowledge file
- **MAJOR** (`0.1.0` → `1.0.0`): breaking change — renaming a skill, restructuring vault, removing functionality

## Workflow

### 1. Work on `dev` branch

```bash
git checkout dev
# make changes
```

Anything in progress that isn't ready: prefix with `_` so it stays gitignored on either branch.

```
.claude/skills/_new-skill-wip/   ← won't ship
.claude/skills/vid-foundation/   ← ships
```

### 2. Test locally before merging

From any test folder, install the plugin from your local path:

```bash
cd ~/test-folder
claude
/plugin marketplace add C:/Users/billr/projects/authentic-ai-os
/plugin install authentic-ai-os@peak-systems
```

Run the affected skills, confirm they work as expected.

### 3. Cut the release

```bash
git checkout main
git merge dev
```

Bump version in TWO places (must match):

- `.claude-plugin/plugin.json` → `version`
- `.claude-plugin/marketplace.json` → `plugins[0].version`

Update `CHANGELOG.md` (create if missing) with what changed.

```bash
git add .
git commit -m "Release v0.2.0 — added vid-thumbnail-v2, fixed voice-capture extraction"
git tag v0.2.0
git push origin main --tags
```

### 4. Notify clients (optional but nice)

Inner Circle clients see the update next time their Cowork/Claude Code refreshes the marketplace. To accelerate or notify:

- Drop a message in the Inner Circle community: "v0.2.0 is live — run `/plugin update authentic-ai-os` to pull the new thumbnail skill."
- Major releases: post a 60-second Loom showing what's new.

## What ships vs what doesn't

### Ships to clients
- `.claude/skills/{skill-name}/` (any skill not prefixed with `_`)
- `.claude/commands/` (when added)
- `.claude/agents/` (when added)
- `knowledge/` — canonical reference docs
- `CLAUDE.md` — operating instructions
- `.claude-plugin/` — manifest

### Stays Billy-only (gitignored)
- `build-plan.md` — strategy doc
- `*.log` — local logs
- `.claude/skills/_*/` — work-in-progress skills
- `_scratch/`, `_strategy/`, `_notes/` — scratch folders
- `foundation/`, `banks/`, `Content/`, `People/`, `Companies/`, `Resources/` — vault scaffolding (not yet ready to ship)

To ship the vault scaffolding later: remove from `.gitignore` and create a `/init` command that copies the structure into clients' folders.

## Rolling back

If a release breaks things for clients:

```bash
git revert <commit>
# bump PATCH version (don't reuse the broken version number)
git tag v0.2.1
git push origin main --tags
```

Clients get the fixed version on next update.
