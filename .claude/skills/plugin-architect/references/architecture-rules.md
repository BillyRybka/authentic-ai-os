# Architecture Invariants

Read before the first change in a session. Every rule here exists because something broke or would have. Each states the rule, then what happens when it is violated.

## Contents
1. Generated vs source
2. The two manifests move together
3. Plugin names are namespaces
4. Line endings
5. Knowledge files must be committed, not just present
6. Skill folder name is the skill name
7. Description length kills the whole plugin
8. Version lives in marketplace.json
9. Resist new plugins
10. main is an allowlist rebuild

## 1. Generated vs source
`plugins/` is deleted and rebuilt by `scripts/generate-plugins.mjs` on every run. A hand edit there survives until the next generate and then vanishes, usually without anyone noticing which change was lost. Edit `shared-skills/` and the manifests. Nothing else.

## 2. The two manifests move together
`.claude-plugin/marketplace.json` holds metadata and version. `.claude-plugin/plugins-map.json` holds composition. A plugin in one and not the other is a broken listing: clients see an entry pointing at a folder that does not exist, or a folder is built that nothing lists. The generator hard-fails on either. Do not work around it, fix the manifest.

## 3. Plugin names are namespaces
Skills invoke as `<plugin>:<skill>`. The namespace is the plugin name, not the marketplace name, so two plugins named `marketing` from two different marketplaces collide on the same machine. Billy runs BenAI's plugins, which already include `marketing`, `youtube`, `design`, `content`, `seo`, `ads`, `obsidian`, and `meta`. Prefix every new plugin (`aai-`) and check the name against the installed set before proposing it.

The original plugin was renamed `authentic-ai-os` to `aai-youtube` in August 2026, while the install base was a handful of testers. That window is closed: every rename from here orphans real client installs, so a name has to be right before it ships.

## 4. Line endings
`core.autocrlf` is true in this repo. Any file without an explicit `eol=lf` rule is checked out with CRLF. Cowork's YAML frontmatter parser rejects CRLF and silently leaks the entire frontmatter block into the body of the skill, so the skill still loads and behaves wrong rather than failing loudly.

Two defences, keep both:
- The repo-root `.gitattributes` forces LF on `.md`, `.json`, `.yaml`, `.py`, `.sh`, and friends, repo-wide. It is repo-wide on purpose: the rule used to live only inside `plugins/authentic-ai-os/`, which meant skills lost protection the moment they moved to `shared-skills/`.
- `generate-plugins.mjs` normalizes text files as it writes, detecting binary by NUL byte. So a bad checkout still cannot ship.

The QA gate blocks on any CRLF in `plugins/`.

## 5. Knowledge files must be committed, not just present
Skills reference `${CLAUDE_PLUGIN_ROOT}/knowledge/<file>.md`. The generator copies those in automatically by scanning skill markdown. But it reads the working tree, so a file that exists on disk and was never committed passes every local check and then does not reach the release branch.

This already shipped once: `vid-credibility` referenced `knowledge/bank-contract.md`, the file was committed on a feature branch only, and v0.3.2 went out with a skill pointing at a file no client had.

The gate checks `git cat-file` against the release ref for exactly this. Do not disable it with `--no-git` before a release.

## 6. Skill folder name is the skill name
`shared-skills/<id>/SKILL.md` must declare `name: <id>`. A mismatch silently fails to resolve. The gate blocks on it.

## 7. Description length kills the whole plugin
Over 1024 characters in a skill's frontmatter `description` and the plugin validator rejects the **entire plugin**, not just that skill. One long description takes down every skill shipping alongside it. Both the generator and the gate block on it.

## 8. Version lives in marketplace.json
Each plugin's `version` is a field on its `marketplace.json` entry. The generator writes it into the built `plugin.json`. Do not edit a version in `plugins/`, it is overwritten.

Two plugins on independent versions cannot share a `v1.2.3` git tag, so source-repo tags are prefixed per plugin (`aai-youtube-v0.3.3`).

Distribution is the public marketplace repo. Clients add it once and pull new versions on marketplace refresh. Refresh is automatic ONLY if the client enabled auto-update for this marketplace (`/plugin` > Marketplaces tab; third-party marketplaces are off by default), and even then it runs after session start with up to a 10-minute delay. Otherwise `/plugin marketplace update authentic-ai`. Cowork sources plugins from the claude.ai-synced Customize configuration, not `~/.claude`, so it has its own state and its own refresh. There are no per-plugin mirror repos, no `releases/latest` update path, and no in-skill update check. That machinery existed for the private-repo era and was deleted; do not reintroduce a "check for updates" step in any skill.

## 9. Resist new plugins
The failure mode to avoid is not too few plugins, it is too many overlapping ones. BenAI's marketplace has `marketing`, `benai-marketing`, `content`, and `marketing-os` all overlapping, plus `obsidian`, `agentic-os`, `aios`, and `vault-os`. His CLAUDE.md now carries defensive paragraphs explaining boundaries that stopped being obvious.

A plugin is justified only when you can name in one sentence who installs it and why, and that sentence does not describe a plugin that already exists. Otherwise it is a skill inside an existing plugin.

## 10. main is an allowlist rebuild
`main` is the client-facing storefront and is rebuilt from scratch each release from an allowlist. Everything else on `dev` (the vault, `Intelligence/`, `documents/`, `plans/`, WIP skills in `.claude/skills/`) stays off it by construction, not by remembering to exclude it.

Consequence: `main` must always carry **every** shipping plugin. Releasing one plugin with a single-plugin allowlist would delete the others from `main` and break those installs. Release selects which plugin versions and publishes, never which plugins exist.
