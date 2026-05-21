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
dev   = the workshop. ALL 19 skills, ALL knowledge, internal docs. You work here.
main  = the storefront. Only the 7 shipping skills + the knowledge they use.
        Clients install from main. NEVER edit main by hand.
```

`dev` is your home branch. Stay on it. `git checkout dev` and forget the rest.

`main` is built only by the release script. It is an allowlist: nothing untested, no WIP, no internal docs can reach a client, because the script rebuilds `main` from scratch and copies only the 7 named skills plus the knowledge they reference.

## Which folder do I open Claude in?

- **Building the tool** (editing a skill): open Claude in `authentic-ai-os\`, on the `dev` branch.
- **Using the tool** (making real content): open Claude in `Content Vault\Authentic-AI-OS\`.

Skills use relative paths. `foundation/...` lands wherever you launched Claude. No skill ever points at a machine path.

## Daily loop

1. **Use it:** open Claude in `Content Vault\Authentic-AI-OS\`. Run skills. Your real data piles up there, never in the repo.
2. **Improve it:** open Claude in `authentic-ai-os\` on `dev`. Edit the skill. Commit to `dev`.
3. **Ship it:** cut a release (below). Clients pick it up on their next `/plugin update`.

## Cutting a release

From `dev`, with a clean working tree:

```powershell
pwsh scripts/release.ps1 -Version 0.2.0
```

The script rebuilds `main` from `dev` using the allowlist in the script (`$ShipSkills`), auto-detects the knowledge those skills reference, bumps the version, commits `main`, and returns you to `dev`. It does not push. Review, then:

```
git push origin main
```

**To graduate a WIP skill:** move it from `.claude/skills-wip/` into `.claude/skills/`, add its name to `$ShipSkills` at the top of `scripts/release.ps1`, commit to `dev`, then cut a release. That is the only edit needed.

## What never reaches a client

- Anything not in the release allowlist: WIP skills, unused knowledge, `documents/`, `plans/`, `RELEASE.md`, `DEV-WORKFLOW.md`, `.vale/`, `.obsidian/`, the Vale hook.
- Gitignored personal data: `foundation/`, `banks/` entries, `Content/`, `People/`, `raw/`, `Notes/`, `.env`. (Bank schema READMEs DO ship; bank entries do not.)

## The one rule

Never edit `main` by hand. `main` is only ever written by `scripts/release.ps1`. Everything you do happens on `dev`.

## The one plugin

There is one plugin: `authentic-ai-os`. One install, one `/plugin update`. Never multiple.
