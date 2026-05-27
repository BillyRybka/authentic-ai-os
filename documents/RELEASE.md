# Release Process

How to ship updates from `authentic-ai-os` to Inner Circle clients.

## The model: two branches, two repos

- **`dev`** is the workshop. All 19 skills, all knowledge, internal docs. You work here, always.
- **`main`** (in the private source repo) is the lean storefront branch. Only the shipping skills plus the knowledge they reference.
- **`BillyRybka/authentic-ai-os`** is the **private** source repo. Internal records only. Clients never touch it.
- **`BillyRybka/aaios-releases`** is the **public** distribution mirror. Just a README and a Releases page. Every release script run uploads the `.plugin` artifact here. The plugin's update-check fetches `https://api.github.com/repos/BillyRybka/aaios-releases/releases/latest`.

`main` is never edited by hand. It is rebuilt from `dev` by `scripts/release.ps1`, which uses an allowlist: only the named skills and their auto-detected knowledge reach `main`. WIP skills, unused knowledge, and internal docs cannot leak to a client. The script also uploads the resulting `.plugin` to both the private repo's Releases (internal record) and the public mirror's Releases (client-facing).

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
- `CLAUDE.md`, `.gitignore`.

### Never ships

- `.claude/skills-wip/` (WIP skills), unused `knowledge/` files, `.claude/hooks/` + `.claude/settings.json` (the machine-specific Vale hook), `documents/`, `plans/`, `scripts/`, `.vale/`, `.obsidian/`, `templates/`.
- Gitignored personal data: `foundation/`, `banks/`, `content/`, `people/`, `raw/`, `notes/`, `.env`. Bank schemas live in `knowledge/{bank}-schema.md`.

### How clients get a vault

The vault is not shipped. `creator-setup` builds the `Authentic-AI-OS/` container in the client's folder at runtime. `knowledge/` is read from the plugin via `${CLAUDE_PLUGIN_ROOT}`, never copied into a vault.

## Cowork gotchas

Hard-won truths from real shipping. Add to the list whenever a new one bites.

### Line endings: LF only on `.md` files

Cowork's YAML frontmatter parser does not handle CRLF. A `---\r\n` closing delimiter is not recognized, so the entire frontmatter block leaks into the body as raw text. Symptoms: skill shows no description in the Cowork UI, and the body opens with literal `name: my-skill description: ...`.

Fix: `.md` files in the plugin must use LF line endings. `.gitattributes` at `plugins/authentic-ai-os/.gitattributes` enforces this for `*.md` and `*.json`. Do not remove it. If a file is edited on Windows with a tool that re-saves as CRLF, run:

```powershell
$f = 'path\to\file.md'; $t = [IO.File]::ReadAllText($f) -replace "`r`n","`n"; [IO.File]::WriteAllText($f, $t, (New-Object Text.UTF8Encoding $false))
```

### Legacy `commands/` directory

Cowork warns on install if the plugin uses `commands/<name>.md`. Use `skills/<name>/SKILL.md` for everything, even pure slash commands. Skills with a description trigger on both slash invocation and model auto-trigger.

### Hooks do not fire in Cowork

Tested 2026-05-27. A `SessionStart` hook configured via `hooks/hooks.json` does not execute on session start in Cowork. The hook file ships inside the `.plugin`, but Cowork's runtime ignores it.

### Working alternative: skill pre-flight + knowledge doc + WebFetch

Validated 2026-05-27. The shipping update-check pattern:

- `knowledge/update-check.md` holds the full check logic, once-per-session guard, and the blocking flow when an update exists.
- Every skill opens with a `> **STOP. PRE-FLIGHT IS MANDATORY.**` blockquote right after the H1, before the descriptive intro.
- Wording must be unmistakably directive (all-caps "STOP," "non-negotiable," "before any tool use," "do not continue past"). Soft wording is treated as documentation and ignored.

When the check finds a newer version, Claude halts and outputs the notice. The creator either drags in the new `.plugin` or says "continue without updating." Works reliably in Cowork.

### Drag-drop installs work; GitHub-link installs are partial

In testing, installing via Cowork's GitHub URL flow gave a partial install (hooks not fired, possibly other features missing). Drag-drop install of the `.plugin` artifact gives a complete install. For client distribution today, drag-drop is the only reliable path.

### Plugin updates don't propagate

Cowork does not auto-pull marketplace updates the way Claude Code does. Once a client installs a version, they stay on it until they manually drag-drop a newer `.plugin`. No "check for updates" or "refresh marketplace" action exists in the Cowork UI as of 2026-05-27. See `documents/audits/` for outreach to Cowork support if it exists.

## Rolling back

`main` is rebuilt, not merged, so rollback is just another rebuild:

```powershell
git checkout dev
git checkout dev~N -- .   # or check out the dev state you want to ship
pwsh scripts/release.ps1 -Version 0.2.1
git push origin main
```

Or `git revert` the bad release commit on `main` and bump a PATCH version. Clients get the fix on next update.
