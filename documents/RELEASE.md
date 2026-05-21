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

Then, in that test folder: run `creator-setup` (it scaffolds `Authentic-AI-OS/`), open that folder, run `vid-foundation`. Confirm the affected skills resolve their `knowledge/` files via `${CLAUDE_PLUGIN_ROOT}` with no missing-file errors, and that nothing writes outside `Authentic-AI-OS/`.

Note: `/plugin marketplace add` takes the repo path (real repo: `BillyRybka/authentic-ai-os`). `@peak-systems` is the marketplace alias from `marketplace.json`, not the repo owner. They do not need to match.

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
- `.claude/skills/{skill-name}/` (any skill not prefixed with `_`). Declared via `"skills": "./.claude/skills"` in `plugin.json` so an installed plugin discovers them.
- `.claude/commands/`, `.claude/agents/` (when added; declare their paths in `plugin.json` the same way)
- `knowledge/` (canonical reference docs, read by skills via the dual-context `${CLAUDE_PLUGIN_ROOT}` rule)
- `CLAUDE.md` (operating instructions)
- `.claude-plugin/` (manifest)

Hooks are NOT declared in `plugin.json`. The Vale hook stays local-only (its binary path is machine-specific). It runs for Billy via project `.claude/settings.json`, never ships.

### Stays Billy-only (gitignored)
- `build-plan.md` (strategy doc)
- `*.log` (local logs)
- `.claude/skills/_*/` (work-in-progress skills)
- `_scratch/`, `_strategy/`, `_notes/` (scratch folders)
- `foundation/`, `banks/`, `Content/`, `People/`, `Companies/`, `Resources/` (Billy's own vault data; clients never get Billy's content)

### How clients get a vault

The vault is NOT shipped as repo folders. `creator-setup` builds the `Authentic-AI-OS/` container in the client's own folder at runtime, scaffolding only what the released skills need. `knowledge/` is never copied into a vault; skills read it from the plugin via `${CLAUDE_PLUGIN_ROOT}`.

**Maintenance contract.** When a new skill ships and it needs container structure before it runs, add a row to `.claude/skills/creator-setup/manifest.md` (skill, needed folder, class, since-version). If the new skill introduces a new bank, put its schema doc in `knowledge/` (referenced via the dual-context rule), not in the vault. Never add a manifest row for an unreleased skill. No other change is needed; clients re-run `creator-setup` after the update and it adds the new structure additively.

## Rolling back

If a release breaks things for clients:

```bash
git revert <commit>
# bump PATCH version (don't reuse the broken version number)
git tag v0.2.1
git push origin main --tags
```

Clients get the fixed version on next update.
