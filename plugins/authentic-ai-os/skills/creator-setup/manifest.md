---
type: reference
doc: creator-setup-manifest
project: authentic-ai-os
status: active
tags: [reference, creator-setup, manifest, contract]
---

# Creator setup manifest

The map from currently released skill to the workspace structure it needs before it can run. `creator-setup` reads this and scaffolds exactly these folders inside the chosen `TARGET` directory. Nothing else.

**Rule:** never add a row for a skill that is not released. Never add structure a released skill does not actually write into. When a new skill ships, add its rows here; that is the only change `creator-setup` needs.

## Container needs (current release)

| skill | needs in container | class | since |
|---|---|---|---|
| vid-avatar | `foundation/` | structure | v1 |
| vid-positioning | `foundation/` | structure | v1 |
| vid-pillars | `foundation/` | structure | v1 |
| vid-credibility | `foundation/` | structure | v1 |
| vid-credibility | `banks/proof-bank/assets/` | structure | v1 |
| vid-credibility | `people/` | structure | v1 |
| vid-backstory | `foundation/` | structure | v1 |
| vid-backstory | `people/` | structure | v1 |

Distinct folders to create: `foundation/`, `banks/proof-bank/assets/`, `people/`. Plus the `_guide.md`, `CLAUDE.md`, and `.env.example` files at the workspace root.

## Class meanings

- **structure**: an empty directory a released skill writes into. Create if missing, never touch otherwise.
- **env-template**: the `.env.example` scaffold. Create if missing. Never create or read the real `.env`.

## Deliberately NOT scaffolded

- `knowledge/`: ships with the plugin, referenced via `${CLAUDE_PLUGIN_ROOT}`. Never copied into the workspace.
- `banks/title-bank.md`, `foundation/packaging-system.md`, `banks/story-bank/`, `banks/testimonial-bank/`, `banks/metaphor-bank/`, `banks/framework-bank/`, `banks/packaging-bank/`: no released skill writes these yet. They get rows here when their owning skills ship.
- `content/`, `notes/`: no released skill writes there.

## Future skills (not yet shipping)

These are in development and will get manifest rows when their skill folders exist:

- `vid-voice-capture`: voice profile authoring.
- `vid-research`: pattern banks and packaging defaults from YouTube evidence.
- `vid-capture`: structured capture of stories, proofs, metaphors, testimonials.
- `vid-packaging`: collapsed 2026-05-19. Its job moved to `vid-research`. Never add a row for it.

Do not add rows for these until their skill folder exists under `.claude/skills/`.
