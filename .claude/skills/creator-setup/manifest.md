---
type: reference
doc: creator-setup-manifest
project: authentic-ai-os
status: active
tags: [reference, creator-setup, manifest, contract]
---

# Creator setup manifest

The map from currently released skill to the container structure it needs before it can run. `creator-setup` reads this and scaffolds exactly these folders inside `Authentic-AI-OS/`. Nothing else.

**Rule:** never add a row for a skill that is not released. Never add structure a released skill does not actually write into. When a new skill ships, add its rows here; that is the only change `creator-setup` needs.

## Container needs (current release)

| skill | needs in container | class | since |
|---|---|---|---|
| vid-avatar | `foundation/` | structure | v1 |
| vid-positioning | `foundation/` | structure | v1 |
| vid-pillars | `foundation/` | structure | v1 |
| vid-credibility | `foundation/` | structure | v1 |
| vid-credibility | `banks/proof-bank/assets/` | structure | v1 |
| vid-credibility | `People/` | structure | v1 |
| vid-backstory | `foundation/` | structure | v1 |
| vid-backstory | `People/` | structure | v1 |
| vid-voice-capture | `foundation/` | structure | v1 |
| vid-research | `.env.example` | env-template | v1 |

Distinct folders to create: `foundation/`, `banks/proof-bank/assets/`, `People/`. Plus the `_guide.md` and `.env.example` files at the container root.

## Class meanings

- **structure**: an empty directory a released skill writes into. Create if missing, never touch otherwise.
- **env-template**: the `.env.example` scaffold. Create if missing. Never create or read the real `.env`.

## Deliberately NOT scaffolded

- `knowledge/`: ships with the plugin, referenced via `${CLAUDE_PLUGIN_ROOT}` (dual-context rule). Never copied into the vault.
- `banks/title-bank.md`, `foundation/packaging-system.md`: authored by `vid-research` Phase 7 from real evidence. Pre-creating them would seed a guess.
- `banks/story-bank/`, `banks/testimonial-bank/`, `banks/metaphor-bank/`, `banks/framework-bank/`, `banks/packaging-bank/`: no released skill writes these yet. They get rows here when `vid-capture` (and kin) ship.
- `Content/`, `Notes/`: no released skill writes there.

## Not in scope this release

- `vid-packaging`: collapsed 2026-05-19. Its packaging-defaults job moved to `vid-research` Phase 7. Never add a row for it.
