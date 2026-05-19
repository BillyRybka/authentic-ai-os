---
name: creator-setup
description: One-time installer that scaffolds the Authentic AI OS vault container so the foundation skills have somewhere to write. Creates the Authentic-AI-OS/ folder with the minimal structure the currently released skills need, scaffolds a .env.example for the vid-research API key, and is safe to re-run after every plugin update (additive, never destroys the creator's work). Use when a creator just installed the plugin, is setting up for the first time, or needs to refresh the vault structure after an update. Triggers on "set up Authentic AI OS", "install Authentic AI OS", "scaffold my vault", "first time setup", "I just installed the plugin", "set up my vault", "run creator setup".
---

# Creator setup

The installer. Establishes the vault container the foundation skills write into, then hands off to `vid-foundation`. It does not interview the creator. It does not write any identity content. It scaffolds structure and gets out of the way.

This skill is manifest-driven. `manifest.md` lists every currently released skill and the container folders it needs. Scaffold only what the manifest says. Never scaffold for a skill that is not released. When a new skill ships, the maintainer adds a row to `manifest.md`; this skill needs no other change.

## The container

Everything lives under one top folder so it never collides with other systems (business-os, peak-os) and is self-evident in a fresh folder:

```
Authentic-AI-OS/
├── _guide.md                    # what this is, what to run next
├── .env.example                 # YT_API_KEY= line for vid-research
├── foundation/                  # empty; the foundation skills fill it
├── banks/
│   └── proof-bank/
│       └── assets/              # vid-credibility writes proof entries + assets here
└── People/                      # vid-credibility / vid-backstory write person stubs here
```

That is the entire minimal set the released skills touch before they run. No `knowledge/` (it ships with the plugin and is referenced from there). No `title-bank.md` and no `packaging-system.md` (`vid-research` authors those from real evidence when it runs; do not pre-create them). No story/testimonial/metaphor/framework banks (no released skill writes them yet; they arrive when `vid-capture` and its kin ship and get manifest rows).

## How this skill runs

### Step 1: Pre-flight

Check the current working directory ONLY for an existing `Authentic-AI-OS/` folder. Do not search parent or child directories. Do not touch anything outside `Authentic-AI-OS/`.

- **No container** → fresh build (Step 2).
- **Container exists** → additive update (Step 3).

### Step 2: Fresh build

Read `manifest.md`. Create `Authentic-AI-OS/` and every folder listed in the manifest's container-needs column. Then write:

- `Authentic-AI-OS/_guide.md` from `references/README-container.md`.
- `Authentic-AI-OS/.env.example` containing exactly:

  ```
  # Authentic AI OS environment.
  # Copy this file to .env and paste your keys. .env is never committed.
  # YouTube Data API key for vid-research (see vid-research/assets/api-key-setup-guide.md).
  YT_API_KEY=
  ```

Never create `.env` itself. Never put a real key anywhere. The creator copies `.env.example` to `.env` and pastes their own key when they reach `vid-research`.

Then go to Step 4.

### Step 3: Additive update

Read `manifest.md`. For every folder the manifest now lists that does not yet exist in the container, create it. If `_guide.md` or `.env.example` is missing, write it from the reference. Never read, modify, overwrite, or delete anything the creator authored (`foundation/*`, bank entries, `People/*`, their `.env`). This skill only ever adds missing structure.

### Step 4: Receipt and handoff

Report plainly:

- What was created vs already present.
- Anything new this release added.
- The next move:

  > "Vault ready at `Authentic-AI-OS/`. Work inside that folder from here.
  >
  > Run `vid-foundation` to start. It walks you through avatar, positioning, pillars, credibility, and backstory, one focused session each.
  >
  > Later, `vid-voice-capture` needs your source material, and `vid-research` needs a YouTube API key in `Authentic-AI-OS/.env` (copy `.env.example`). Both are manual starts."

## Safety rules

- Only ever create or write inside `Authentic-AI-OS/`. Never a sibling `People/`, `Notes/`, or `foundation/` belonging to another system.
- Creator content is untouchable. This skill scaffolds empty structure only.
- If any write fails, stop and report the exact path. Do not continue blindly.
- Never fabricate a key, a value, or a foundation section.

## What this skill is NOT

- An interview. It asks the creator nothing about their identity. That is `vid-foundation` and its sub-skills.
- A knowledge copier. `knowledge/` reference files ship with the plugin and are referenced from there; they never get copied into the vault.
- A packaging guesser. `packaging-system.md` is authored by `vid-research` from evidence, never pre-seeded here.

## Maintenance contract

When a new skill is released and it needs container structure before it runs, add one row to `manifest.md` (skill, needed folder, class, since-version). If the new skill introduces a new bank, its schema doc goes into the plugin `knowledge/` folder (referenced via the dual-context rule), not into the vault. No code in this SKILL.md changes. The creator re-runs `creator-setup` after the plugin update; Step 3 adds the new folder and nothing else.
