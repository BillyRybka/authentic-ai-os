# AGENTS.md

Guidance for AI coding agents working in this repository. Read this first.

## Project overview

**Authentic AI OS** is an Obsidian-native AI content system for YouTube creators. It is not a traditional software application — it is a **Claude plugin** made of markdown "skills" plus reference "knowledge" files. An AI agent (Claude Code / Cowork) loads the skills and drives a creator from raw idea to published YouTube video, in the creator's own voice.

- The product is a single plugin: `authentic-ai-os` (see `plugins/authentic-ai-os/.claude-plugin/plugin.json`). There is one install, one update path. Never multiple plugins.
- There is no compiled code, no `package.json`, no `pyproject.toml`. The "build" is packaging the plugin folder into a `.plugin` zip artifact.
- Author: Billy Rybka (private source repo `BillyRybka/authentic-ai-os`; public distribution mirror `BillyRybka/aaios-releases`).

## Repository layout

```
plugins/authentic-ai-os/       THE PLUGIN. Ships as a unit to clients.
  .claude-plugin/plugin.json   Version + manifest (version is bumped by release script only)
  skills/                      RELEASED skills (9): creator-setup, foundation, vid-avatar,
                               vid-positioning, vid-pillars, vid-credibility, vid-backstory,
                               vid-research, aaios-feedback
.claude/skills/                STAGED skills. Active WIP, loaded when working in this repo. Never ships.
.claude/skills-wip/            Deeper WIP, parked. Not loaded, not shipped.
.claude/hooks/vale-fire.js     PostToolUse hook: auto-lints edited markdown against voice rules
knowledge/                     Reference material skills load via ${CLAUDE_PLUGIN_ROOT}/knowledge/
                               (bank schemas, capture guides, format planners in format-planners/)
tests/                         Python test harness for vid-* skills. Never ships (dev-only).
documents/                     Internal docs: DEV-WORKFLOW.md, RELEASE.md, SYSTEM-MAP.md,
                               skill-knowledge-map.md, skill-writing-lessons.md, etc.
plans/                         Planning docs.
scripts/release.ps1            THE release script (PowerShell). Rebuilds main from dev.
.vale/ + .vale.ini             Vale prose-linter config, ProductVoice style
.claude-plugin/marketplace.json  Marketplace entry pointing at the plugin
CLAUDE.md                      Rules for Claude when working in an installed creator vault
dist/                          Built .plugin artifacts (gitignored)
```

A skill **ships if and only if it lives in `plugins/authentic-ai-os/skills/`**. That is the whole rule — there is no allowlist of skill names to maintain.

## Branches and the one rule

- `dev` = the workshop. All work happens here. `git checkout dev` and stay there.
- `main` = the storefront. Rebuilt from scratch by `scripts/release.ps1`. Clients install from main.
- **Never edit `main` by hand.** `main` is only ever written by the release script.

## Build, release, and test commands

### Release (PowerShell, from `dev`, clean working tree)

```powershell
pwsh scripts/release.ps1 -Version 0.3.3            # full release: pushes, publishes GitHub Releases
pwsh scripts/release.ps1 -Version 0.3.3 -DryRun    # rehearse: builds locally, pushes nothing
```

The script: validates skill descriptions (1024-char cap), blocks `DEBUG-TRACE` instrumentation from shipping, rebuilds `main` from an allowlist (`.claude-plugin`, `plugins/authentic-ai-os`, `CLAUDE.md`, `.gitignore`), auto-detects `knowledge/*.md` files referenced by shipped skills and relocates them into `plugins/authentic-ai-os/knowledge/`, bumps `plugin.json`, tags `vX.Y.Z`, builds `dist/authentic-ai-os-vX.Y.Z.plugin`, pushes both branches, and creates GitHub Releases on the private repo and the public mirror. It returns you to `dev` and syncs dev's `plugin.json` forward.

Versioning (semver): PATCH = fix/tweak inside an existing skill; MINOR = a skill graduates or new knowledge/feature; MAJOR = breaking change (rename/remove a skill). When unsure, a new skill is a MINOR.

### Tests (Python 3, stdlib only — no dependencies to install)

```bash
cd tests/skills/<skill>          # e.g. vid-intake
python eval.py                   # Tier A: deterministic gate, scores outputs/case_NN/
```

- Tier A (`eval.py`) is the deterministic "does it work" gate — every error-level check must pass. It imports shared checks from `tests/lib/` (`vale_rules.py`, `check_fabrication.py`, `check_handoff.py`, `tier_a_universal.py`, `frontmatter.py`).
- Tier B (`rubric.md`) is an AI-judge quality score (1–5). Only run it on Tier-A-passing outputs.
- Shared corpus: `tests/corpus/seeds.json` (6 synthetic seeds, 2 adversarial). Frozen upstream states live in `tests/fixtures/`; see `tests/fixtures/MANIFEST.md` for staleness tracking.
- Existing suites: `vid-intake` (pilot), `vid-framing`, `vid-title`, `post-write`. Rollout order and how to add a suite: `tests/README.md`.
- Do NOT modify `eval.py` or `rubric.md` during an optimization loop — they are locked while the skill is being optimized.

### Lint (Vale)

Vale runs automatically on every markdown Edit/Write via the `.claude/hooks/vale-fire.js` PostToolUse hook (configured in `.claude/settings.json`). To run manually:

```bash
vale path/to/file.md
```

## Code style and conventions

### Skill authoring

- Each skill is a folder with a `SKILL.md` carrying YAML frontmatter (`name`, `description`). The `description` must be **1024 characters or fewer** — the plugin validator rejects the entire plugin otherwise (the release script checks this; target 240–490 chars like the foundation skills).
- Shipping skills carry an update-check pre-flight blockquote right after the frontmatter (read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` first). Match the sibling skills.
- Skills reference knowledge via `knowledge/<file>.md`. In the repo those live at root `knowledge/`; the release script relocates them into the plugin. `documents/skill-knowledge-map.md` is the source of truth for which knowledge files each skill requires.
- Skills use **relative paths only** — no machine-specific absolute paths. `foundation/...` resolves wherever the agent was launched.
- `DEBUG-TRACE` blocks are dev-only instrumentation; they must never enter `plugins/authentic-ai-os/` (the release script hard-fails on them).

### Markdown / voice rules (enforced by Vale, `.vale/styles/ProductVoice/`)

- No em-dashes or en-dashes. No banned words, AI-isms, or hedge words (see the `.yml` rule files). `tests/lib/vale_rules.py` mirrors these rules at eval time — keep the two in sync.
- Obsidian-flavored markdown throughout: internal references are always `[[wikilinks]]`, never `[markdown](links)` or plain-text entity names. Callouts `> [!tip]`, highlights `==text==`, frontmatter `tags: [a, b]`.
- Frontmatter on every note a skill creates. `knowledge/vault-integration.md` holds the shared conventions and indexes the per-artifact schemas (`knowledge/piece-contract.md`, `knowledge/bank-contract.md`, `knowledge/voice-profile-schema.md`).
- Plain, spoken language. "Read aloud is the voice test" — if the creator would reword it when speaking, it is wrong.
- Vale skips: frontmatter blocks, wikilinks, and the paths excluded in `.vale.ini` (creator-side output, scratch dirs). Rule-documentation meta files (e.g. `CLAUDE.md`) may contain banned words.

### Line endings and files

- Plugin files must be **LF**, not CRLF — Cowork's frontmatter parser breaks on CRLF. `plugins/authentic-ai-os/.gitattributes` enforces this, but convert explicitly when graduating a skill.
- Dev-only files never graduate: `DECISIONS.md`, `WORKING-NOTES.md`, `scripts/__pycache__/`, dev-only READMEs (also gitignored).

### Graduating a WIP skill (making it ship)

Full checklist in `documents/DEV-WORKFLOW.md`. In short: move the folder to `plugins/authentic-ai-os/skills/`, strip dev-only files, convert to LF, add the update-check pre-flight, verify description length, verify referenced knowledge exists at root `knowledge/`, **wire it in** (update the skill that hands off to it, and grep all shipping skills + `README.md` + `CLAUDE.md` for stale "in development" references — the step most often missed), regenerate `documents/skill-knowledge-map.md` and `documents/SYSTEM-MAP.md`, then commit on `dev`.

## Behavioral rules when editing skills/content

These come from `CLAUDE.md` and apply to anything the skills produce:

1. **Never fabricate** positioning, avatar details, stories, numbers, testimonials, or metaphors. If the creator did not say it, do not invent it. (This is also the anti-fabrication spine of the test harness: `tests/lib/check_fabrication.py`.)
2. **Ask before scanning.** Do not pre-load foundation docs, banks, or content pieces at session start; read silently only when a specific task requires it.
3. Wikilinks everywhere, bidirectional for people; people get `people/{Full Name}.md` stubs.
4. Auto-save meaningful info immediately and report what was saved; never ask permission to save.
5. Do not duplicate content across banks — check for existing entries first.

## Security considerations

- Never commit secrets. `.env`, `*.pem`, `*.key`, and `secrets/` are gitignored.
- Creator/vault content (`foundation/`, `banks/`, `content/`, `people/`, `raw/`, `notes/`) is gitignored and **never ships**. Test fixtures intentionally mirror these folder names and are re-included via `!tests/` negations in `.gitignore` — do not "fix" those patterns.
- `tests/`, `documents/`, `plans/`, `scripts/`, `.vale/`, and `.claude/` never reach clients; the release script copies only its allowlist. Do not widen the allowlist in `scripts/release.ps1` without understanding that everything on it ships.
- The release script pushes branches and creates public GitHub Releases; use `-DryRun` first when unsure. Beware its printed rollback line (`git reset --hard origin/dev`) — it destroys unpushed dev work.
- The Vale hook hard-codes a Vale binary path for the author's machine (`C:\Users\billr\.local\bin\vale.exe`); adjust locally if Vale lives elsewhere on yours.

## Key reference documents

- `documents/DEV-WORKFLOW.md` — daily loop, graduation checklist, release, versioning, rollback. Read this when confused.
- `documents/RELEASE.md` — detailed release process.
- `documents/skill-knowledge-map.md` — skill-to-knowledge packaging contract (regenerate when skills move tiers).
- `documents/SYSTEM-MAP.md` — full system map.
- `documents/skill-writing-lessons.md`, `documents/skill-wiring-lessons.md` — hard-won conventions.
- `tests/README.md` — testing strategy, rollout order, how to add a skill suite.
