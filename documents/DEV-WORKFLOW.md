# Dev workflow (read this when confused)

## Three folders. Three jobs. They never mix.

```
C:\Users\billr\projects\
├── authentic-ai-os\        THE TOOL (this repo). Skills, knowledge. Ships as a plugin.
├── Content Vault\
│   └── Authentic-AI-OS\    YOUR CONTENT. foundation, banks, raw/voice-sources. Never ships.
└── business-os\            A different system. Untouched. Ignore it here.
```

## Two branches. Workshop and storefront.

```
dev   = the workshop. Every skill, all knowledge, internal docs. You work here.
main  = the storefront. Rebuilt from dev by the release script. Clients install from main.
        NEVER edit main by hand.
```

`dev` is your home branch. `git checkout dev` and stay there.

`main` is rebuilt, never edited. The release script wipes it and copies the whole plugin tree (`plugins/authentic-ai-os/`) plus the knowledge files those skills reference. Anything outside the plugin folder (WIP skills, internal docs, dev tooling) can never reach a client, because it was never copied.

## Where skills live

```
plugins/authentic-ai-os/skills/   SHIPPING skills. Inside the plugin. These reach clients.
.claude/skills/                   WIP under active test. Loaded when you run Claude in this repo. Never ships.
.claude/skills-wip/               Deeper WIP, parked. Not loaded, not shipped.
```

A skill ships if and only if it sits in `plugins/authentic-ai-os/skills/`. That is the whole rule. The release script ships the entire plugin tree as a unit, so there is no list of skill names to maintain anywhere.

## Which folder do I open Claude in?

- **Building the tool** (editing a skill): open Claude in `authentic-ai-os\`, on `dev`.
- **Using the tool** (making real content): open Claude in `Content Vault\Authentic-AI-OS\`.

Skills use relative paths. `foundation/...` lands wherever you launched Claude. No skill points at a machine path.

## Daily loop

1. **Use it:** open Claude in `Content Vault\Authentic-AI-OS\`. Run skills. Real data piles up there, never in the repo.
2. **Improve it:** open Claude in `authentic-ai-os\` on `dev`. Edit the skill. Commit to `dev`.
3. **Ship it:** cut a release (below). Clients pick it up via the plugin's built-in update check.

## Graduating a WIP skill (making it ship)

1. Move the folder into the plugin: `.claude/skills/<skill>` (or `.claude/skills-wip/<skill>`) to `plugins/authentic-ai-os/skills/<skill>`.
2. Strip dev-only files so they never reach clients: `DECISIONS.md`, `WORKING-NOTES.md`, `scripts/__pycache__/`, any dev-only README.
3. Convert the skill's `.md` files to LF. Cowork's frontmatter parser breaks on CRLF. The plugin `.gitattributes` enforces LF for files under the plugin, but convert explicitly so a Windows re-save does not bite you.
4. Add the update-check pre-flight blockquote right after the frontmatter, matching the sibling skills.
5. Keep the frontmatter `description` at 1024 characters or fewer. The plugin validator rejects the whole plugin if any one skill's description is longer, so a single bloated description blocks every skill from installing. `release.ps1` checks this and fails the release if it finds one over, but write it short to begin with. The foundation skills run 240 to 490 chars; that is the target.
6. Confirm the knowledge files it references exist at repo-root `knowledge/`. The release script relocates them into the plugin automatically.
7. Wire it into the system. Update whatever skill should hand off to this one (the foundation chain offers `vid-research` at its end, for example), and grep every shipping skill plus `README.md` and `CLAUDE.md` for stale references that still call it unreleased ("in development", "coming", "chain ends here", "do NOT mention {skill}"). A graduated skill that nothing points to, or that siblings still call work-in-progress, is a silent dead end. This is the step most often missed.
8. Commit on `dev`. No allowlist to touch; a skill ships by living in the plugin folder.

## Cutting a release

Easiest path: the `peak-release` skill orchestrates graduation plus the release script. Or run the script directly.

From `dev`, with a clean working tree:

```powershell
pwsh scripts/release.ps1 -Version 0.3.1            # add -DryRun to rehearse: builds locally, pushes nothing
```

The script switches to `main`, wipes it, copies the plugin tree, auto-detects and relocates the knowledge the skills reference, bumps the version in `plugin.json`, commits `main`, tags `vX.Y.Z`, builds the `.plugin` artifact in `dist/`, then:

- pushes `main` (with the tag) and `dev`,
- creates a GitHub Release on the private source repo (internal record),
- creates a GitHub Release on the public mirror `BillyRybka/aaios-releases` and uploads the `.plugin` (this is what clients install from),
- syncs `dev`'s `plugin.json` forward so dev never lags main.

It returns you to `dev`. With `-DryRun` it does all the local build steps and pushes nothing.

## Versioning (semver MAJOR.MINOR.PATCH)

- **PATCH** (0.3.0 to 0.3.1): bug fix, doc edit, prompt tweak inside an existing skill.
- **MINOR** (0.3.0 to 0.4.0): a skill graduates and ships, new knowledge, a new feature.
- **MAJOR** (0.3.0 to 1.0.0): breaking change. Renaming or removing a skill, restructuring.

When unsure, a new skill is a MINOR. v0.3.0 shipped vid-research and aaios-feedback.

## Rolling back

`main` is rebuilt, not merged, so a rollback is just another release from an earlier `dev` state.

> Warning: the `-DryRun` output prints a rollback line ending in `git reset --hard origin/dev`. That is only safe when `dev` has no unpushed commits beyond the auto-generated sync commit. If you have real unpushed work on `dev`, that reset destroys it. Reset to the specific commit you want instead, or just push the build you already have.

## What never reaches a client

- Anything outside `plugins/authentic-ai-os/`: WIP skills in `.claude/`, `documents/`, `plans/`, `scripts/`, `.vale/`, `.obsidian/`, the Vale hook.
- Gitignored personal data: `foundation/`, `banks/`, `content/`, `people/`, `raw/`, `notes/`, `.env`. Bank schemas live in `knowledge/{bank}-schema.md`; the bank folders are creator content and never ship.

## The one rule

Never edit `main` by hand. `main` is only ever written by `scripts/release.ps1`. Everything you do happens on `dev`.

## The one plugin

There is one plugin: `authentic-ai-os`. One install, one update path. Never multiple.
