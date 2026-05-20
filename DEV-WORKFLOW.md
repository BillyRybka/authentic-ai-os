# Dev workflow (read this when confused)

Three folders. Three jobs. They never mix.

```
C:\Users\billr\projects\
├── authentic-ai-os\        THE TOOL (this repo). Skills, knowledge, docs. Ships as a plugin.
├── Content Vault\
│   └── Authentic-AI-OS\    YOUR CONTENT. foundation, banks, raw/voice-sources. Never ships.
└── business-os\            A different system. Untouched. Ignore it here.
```

## Which folder do I open Claude in?

- **Building the tool** (editing a skill, fixing a bug): open Claude in `authentic-ai-os\`.
- **Using the tool** (making real content, testing): open Claude in `Content Vault\Authentic-AI-OS\`.

The skills use relative paths. `foundation/...` lands wherever you launched Claude. That is the whole trick. No skill ever points at a machine path.

## Daily loop

1. **Use it:** open Claude in `Content Vault\Authentic-AI-OS\`. Run skills. Your real data piles up there, safe, never in the repo.
2. **Improve it:** open Claude in `authentic-ai-os\`. Edit the skill. `/plugin update` to pull it into your vault.
3. **Ship it:** from `authentic-ai-os\`, you commit and push. Only the tool goes. Your content was never there.

## Git rule

You own git. You commit and push, on `main`, your rhythm. Claude does not run git commands unless you explicitly ask in that moment. One person at the git index. This is what stops the collisions.

## What never ships (gitignored)

`foundation/`, `banks/`, `Content/`, `People/`, `raw/`, `Notes/`, `.env`, `*WORKING-NOTES.md`, `Authentic-AI-OS/`. Your content and dev scratch. The product is the plugin: skills + `knowledge/` + manifests + docs.

## Bank schemas

A bank has two halves. The **schema** (what an entry looks like) ships, and lives in `knowledge/{bank}-schema.md` (done: `proof-bank-schema.md`). Your **entries** never ship and live in `Content Vault\...\banks\`. When a new bank's skill ships, its schema moves into `knowledge/` then, per the manifest contract in `creator-setup/manifest.md`.

## The one plugin

There is one plugin: `authentic-ai-os`. One install, one `/plugin update`. Never multiple. If updating ever feels like juggling, something is wrong, re-read this file.
