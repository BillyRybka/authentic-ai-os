# Release Process

How to ship updates from `authentic-ai-os` to Inner Circle clients.

## The model: two branches, two repos

- **`dev`** is the workshop. Every skill, all knowledge, internal docs. You work here, always.
- **`main`** (in the private source repo) is the lean storefront branch. It carries the whole plugin tree (`plugins/authentic-ai-os/`) plus the knowledge files those skills reference, nothing else.
- **`BillyRybka/authentic-ai-os`** is the **private** source repo. Internal records only. Clients never touch it.
- **`BillyRybka/aaios-releases`** is the **public** distribution mirror. Just a README and a Releases page. Every release script run uploads the `.plugin` artifact here. The plugin's update-check fetches `https://api.github.com/repos/BillyRybka/aaios-releases/releases/latest`.

`main` is never edited by hand. It is rebuilt from `dev` by `scripts/release.ps1`, which wipes `main` and copies the whole plugin tree plus the knowledge the skills reference (auto-detected). A skill reaches clients only by living in `plugins/authentic-ai-os/skills/`. WIP skills in `.claude/`, unused knowledge, and internal docs sit outside the plugin folder, so they cannot leak to a client. The script also uploads the resulting `.plugin` to both the private repo's Releases (internal record) and the public mirror's Releases (client-facing).

## Versioning

Semver `MAJOR.MINOR.PATCH`:

- **PATCH** (`0.3.0` to `0.3.1`): bug fix, doc edit, prompt tweak inside an existing skill.
- **MINOR** (`0.3.0` to `0.4.0`): a skill graduates and ships, new knowledge, new feature.
- **MAJOR** (`0.3.0` to `1.0.0`): breaking change. Renaming a skill, restructuring, removing functionality.

When unsure, a new skill is a MINOR. The current released version is v0.3.0 (shipped vid-research and aaios-feedback).

## Workflow

### 1. Work on `dev`

```
git checkout dev
```

All editing happens on `dev`. Shipping skills live in `plugins/authentic-ai-os/skills/`. WIP under active test lives in `.claude/skills/` (loaded when you run Claude in the repo, never shipped). Deeper WIP is parked in `.claude/skills-wip/`.

### 2. Graduate a skill (when one becomes ready)

1. Move the folder into the plugin: `.claude/skills/<skill>` (or `.claude/skills-wip/<skill>`) to `plugins/authentic-ai-os/skills/<skill>`.
2. Strip dev-only files so they never reach clients: `DECISIONS.md`, `WORKING-NOTES.md`, `scripts/__pycache__/`, any dev-only README. Also delete any `DEBUG-TRACE` blocks (temporary builder tracing); `release.ps1` hard-stops the release if any survive into the plugin tree.
3. Convert the skill's `.md` files to LF (see the Cowork line-endings gotcha below).
4. Add the update-check pre-flight blockquote after the frontmatter, matching the sibling skills.
5. Keep the frontmatter `description` at 1024 characters or fewer (hard plugin-validator limit; see the gotcha below). `release.ps1` enforces it.
6. If it needs container structure in the client's vault, add a row to `creator-setup`'s manifest.
7. Wire it into the system. Update whatever skill should hand off to this one (the foundation chain offers `vid-research` at its end, for example), and grep every shipping skill plus `README.md` and `CLAUDE.md` for stale references that still call it unreleased ("in development", "coming", "chain ends here", "do NOT mention {skill}"). A graduated skill that nothing points to, or that siblings still call work-in-progress, is a silent dead end. This is the step most often missed.
8. Regenerate the two maps. A skill changing roots (or any edit to its knowledge references) makes `documents/skill-knowledge-map.md` and `documents/SYSTEM-MAP.md` stale: their tier labels, counts, diagrams, and handoff notes drift from reality. Re-grep all three roots per each map's section-7 procedure, re-tier every skill that moved, fix any handoff/NEXT lines you changed in step 7, and bump the "Built" date. They never ship, but they are the packaging contract (which `knowledge/` file each skill needs), so a stale map is how a knowledge file gets forgotten at release time.
9. Commit to `dev`. There is no allowlist array to edit; the whole plugin tree ships.

### 3. Cut the release

Easiest path: the `peak-release` skill drives graduation plus the script. Or run the script directly. From `dev`, clean working tree:

```powershell
pwsh scripts/release.ps1 -Version 0.3.1            # add -DryRun to rehearse: builds locally, pushes nothing
```

A real run (no `-DryRun`) does everything end to end:

- switches to `main`, wipes it, copies the plugin tree, relocates the referenced knowledge,
- bumps the version in `plugin.json`, commits `main`, tags `vX.Y.Z`, builds `dist/authentic-ai-os-vX.Y.Z.plugin`,
- pushes `main` (with the tag) and `dev`,
- creates the GitHub Release on the private repo and on the public mirror, uploading the `.plugin` to both,
- syncs `dev`'s `plugin.json` forward, and returns you to `dev`.

To rehearse first, run with `-DryRun`. It builds `main` and the artifact locally and pushes nothing, then prints inspect and rollback lines. Read the rollback warning under "Rolling back" before using it.

### 4. Notify clients (optional)

Clients get notified by the plugin's built-in update check on their next session, then install the new `.plugin`. To accelerate:

- Post in the Inner Circle community: "v0.3.1 is live."
- Major releases: a 60-second Loom of what changed.

## What ships vs what doesn't

### Ships to clients

- `.claude-plugin/` (marketplace manifest) and the plugin manifest at `plugins/authentic-ai-os/.claude-plugin/plugin.json`.
- The whole `plugins/authentic-ai-os/` tree: every skill in `plugins/authentic-ai-os/skills/`, plus the knowledge files those skills reference (auto-detected and relocated under `plugins/authentic-ai-os/knowledge/` by the release script).
- `CLAUDE.md`, `.gitignore`.

### Never ships

- Everything outside `plugins/authentic-ai-os/`: WIP skills in `.claude/skills/` and `.claude/skills-wip/`, unused `knowledge/` files, `.claude/hooks/` + `.claude/settings.json` (the machine-specific Vale hook), `documents/`, `plans/`, `scripts/`, `.vale/`, `.obsidian/`, `templates/`.
- Gitignored personal data: `foundation/`, `banks/`, `content/`, `people/`, `raw/`, `notes/`, `.env`. Bank schemas live in `knowledge/{bank}-schema.md`.

### How clients get a vault

The vault is not shipped. `creator-setup` builds the `Authentic-AI-OS/` container in the client's folder at runtime. `knowledge/` is read from the plugin via `${CLAUDE_PLUGIN_ROOT}`, never copied into a vault.

## Cowork gotchas

Hard-won truths from real shipping. Add to the list whenever a new one bites.

### Line endings: LF only on `.md` files

Cowork's YAML frontmatter parser does not handle CRLF. A `---\r\n` closing delimiter is not recognized, so the entire frontmatter block leaks into the body as raw text. Symptoms: skill shows no description in the Cowork UI, and the body opens with literal `name: my-skill description: ...`.

Fix: `.md` files in the plugin must use LF line endings. `.gitattributes` at `plugins/authentic-ai-os/.gitattributes` enforces this for `*.md` and `*.json`. Do not remove it. That attribute only covers files under the plugin folder, so a skill authored in `.claude/` is likely CRLF until you graduate it; convert it on the way in. If a file is edited on Windows with a tool that re-saves as CRLF, run:

```powershell
$f = 'path\to\file.md'; $t = [IO.File]::ReadAllText($f) -replace "`r`n","`n"; [IO.File]::WriteAllText($f, $t, (New-Object Text.UTF8Encoding $false))
```

### Description length: 1024-char hard cap

The plugin validator rejects the entire plugin if any skill's frontmatter `description` exceeds 1024 characters (error: `field 'description' in SKILL.md must be at most 1024 characters`). It is the whole plugin that fails, not just that skill, so one long description blocks every skill from installing. v0.3.0 shipped with aaios-feedback at 1280 chars and failed validation; v0.3.1 fixed it. `scripts/release.ps1` now checks every shipping description before it builds and throws if any is over. Keep descriptions tight: what the skill does, when it triggers, a handful of trigger phrases. The foundation skills run 240 to 490 chars; that is the target range.

### Legacy `commands/` directory

Cowork warns on install if the plugin uses `commands/<name>.md`. Use `skills/<name>/SKILL.md` for everything, even pure slash commands. Skills with a description trigger on both slash invocation and model auto-trigger.

### Hooks do not fire in Cowork

Tested 2026-05-27. A `SessionStart` hook configured via `hooks/hooks.json` does not execute on session start in Cowork. The hook file ships inside the `.plugin`, but Cowork's runtime ignores it.

### Working alternative: skill pre-flight + knowledge doc + WebFetch

Validated 2026-05-27. The shipping update-check pattern:

- `knowledge/update-check.md` holds the full check logic, once-per-session guard, and the blocking flow when an update exists.
- Every skill opens with a pre-flight blockquote right after the frontmatter, before the descriptive intro.
- Wording must be unmistakably directive ("mandatory," "before doing anything else," "halt"). Soft wording is treated as documentation and ignored.
- aaios-feedback is the one deliberate exception: it runs mid-session after another skill already checked, so it skips the pre-flight to avoid interrupting a feedback report with an update notice.

When the check finds a newer version, Claude halts and outputs the notice. The creator either drags in the new `.plugin` or says "continue without updating." Works reliably in Cowork.

### Drag-drop installs work; GitHub-link installs are partial

In testing, installing via Cowork's GitHub URL flow gave a partial install (hooks not fired, possibly other features missing). Drag-drop install of the `.plugin` artifact gives a complete install. For client distribution today, drag-drop is the only reliable path.

### Plugin updates don't propagate

Cowork does not auto-pull marketplace updates the way Claude Code does. Once a client installs a version, they stay on it until they manually drag-drop a newer `.plugin`. No "check for updates" or "refresh marketplace" action exists in the Cowork UI as of 2026-05-27. The plugin's built-in update-check (above) is what bridges the gap: it notifies the client and delivers the new `.plugin` to install.

## Rolling back

`main` is rebuilt, not merged, so a rollback is just another release from an earlier `dev` state:

```powershell
git checkout dev
git checkout dev~N -- .   # or check out the dev state you want to ship
pwsh scripts/release.ps1 -Version 0.3.2
```

The script pushes and publishes on its own; no manual `git push origin main` needed.

> Warning about the `-DryRun` rollback line. The dry-run prints `git reset --hard origin/dev` as part of its rollback hint. That is only safe when `dev` has no unpushed commits beyond the auto-generated sync commit. If you have real unpushed work on `dev` (a freshly graduated skill, for instance), that reset destroys it. Reset to the specific commit you want instead, or simply push the build the dry-run already produced.

Or `git revert` the bad release commit on `main` and bump a PATCH version. Clients get the fix on next update.
