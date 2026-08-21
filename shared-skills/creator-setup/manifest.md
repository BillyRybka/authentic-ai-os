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

Distinct folders to create: `foundation/`, `banks/proof-bank/assets/`, `people/`. Plus `CLAUDE.md` and `.env.example` at the workspace root.

The `people/` row is conditional. If the creator chose a path override during setup (person stubs go to an existing root-level People folder), `creator-setup` skips the local `people/` and records the override in the workspace `CLAUDE.md`.

## Class meanings

- **structure**: an empty directory a released skill writes into. Create if missing, never touch otherwise.
- **env-template**: the `.env.example` scaffold. Create if missing. Never create or read the real `.env`.
- **seed**: a starter bank file copied from a plugin template (the `template` column names a file under `${CLAUDE_PLUGIN_ROOT}/knowledge/`) into the workspace. Copy only if the target file does not already exist. Never overwrite a creator's edited bank. Once copied, the creator owns and grows it. The writing skills read the seeded bank as a supplement to the plugin's pattern libraries, which stay the craft reference; a missing bank is fine.

## Deliberately NOT scaffolded

- `knowledge/`: ships with the plugin, referenced via `${CLAUDE_PLUGIN_ROOT}`. Never copied into the workspace. The one exception is a **seed**-class row, where a single named `knowledge/` template is copied into `banks/` as a starter the creator then owns.
- Any folder a released skill does not write into. New rows get added here only when their owning skill ships.

## Pending (ships with the script-writing skills)

These rows are staged, not live. `creator-setup` acts ONLY on the "Container needs (current release)" table above. When `vid-intro`, `vid-segment`, and `vid-ending` ship, move their rows up into that table and the seeds scaffold on the next setup or additive update. Each seeded file lands as a creator-owned starter bank; the writing skills read it as a supplement to the plugin's pattern libraries (`hook-patterns.md`, `transition-patterns.md`), never a replacement.

| skill | needs in container | class | template | since |
|---|---|---|---|---|
| vid-intro | `banks/hook-bank.md` | seed | `hook-bank-template.md` | pending |
| vid-segment | `banks/transition-bank.md` | seed | `transition-bank-template.md` | pending |
| vid-ending | `banks/transition-bank.md` | seed | `transition-bank-template.md` | pending |

The `banks/transition-bank.md` seed is shared by `vid-segment` and `vid-ending`; the copy is idempotent (skip if the file exists), so listing it twice is safe.
