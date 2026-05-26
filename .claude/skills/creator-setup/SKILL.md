---
name: creator-setup
description: One-time installer that scaffolds the Authentic AI OS workspace so the foundation skills have somewhere to write. Detects the current folder shape, lands the workspace in the right place (a fresh folder, a business-os vault under `Departments/Content/`, or a custom path the creator picks), writes a `CLAUDE.md` so Claude knows the rules, and is safe to re-run after every plugin update (additive, never destroys the creator's work). Use when a creator just installed the plugin, is setting up for the first time, or needs to refresh the workspace structure after an update. Triggers on "set up Authentic AI OS", "install Authentic AI OS", "scaffold my vault", "first time setup", "I just installed the plugin", "set up my vault", "run creator setup".
---

# Creator setup

The installer. Establishes the workspace the foundation skills write into, then hands off to `vid-foundation`. It does not interview the creator. It does not write any identity content. It scaffolds structure and gets out of the way.

This skill is manifest-driven. `manifest.md` lists every currently released skill and the container folders it needs. Scaffold only what the manifest says. Never scaffold for a skill that is not released. When a new skill ships, the maintainer adds a row to `manifest.md`; this skill needs no other change.

## What gets scaffolded

The folders the released foundation skills need:

- `foundation/` (empty; the foundation skills fill it)
- `banks/proof-bank/assets/` (where `vid-credibility` writes proof entries and their screenshots)
- `People/` (where `vid-credibility` and `vid-backstory` write person stubs)

Plus three files at the workspace root:

- `_guide.md` (human-readable orientation; written from `assets/_guide.md`)
- `CLAUDE.md` (Claude's rules for working in the workspace; written from `assets/CLAUDE.md`)
- `.env.example` (placeholder for API keys future skills will need)

No `knowledge/` (it ships with the plugin and is referenced from there). No `title-bank.md`, no `story-bank/`, no `packaging-system.md`. Those arrive when their skills ship and get manifest rows.

## How this skill runs

### Step 1: Detect

Check ONLY the current working directory. Never search parent or child directories. Pick the first case that matches.

**Case A. Existing container.** An `Authentic-AI-OS/` folder exists at CWD, OR the CWD itself already contains `foundation/` (signals a previous flat scaffold).
→ Go to **Step 3 (additive update)**.

**Case B. Business-os vault detected.** CWD has a `claude.md` or `CLAUDE.md` with `os-mode:` frontmatter, OR a `Departments/` folder.
→ Go to **Step 2B**.

**Case C. Other existing vault.** CWD has a `claude.md` / `CLAUDE.md` / `Context/` / `Projects/` but none of the business-os signals.
→ Go to **Step 2C**.

**Case D. Empty or near-empty CWD.** None of the above.
→ Go to **Step 2A**.

### Step 2A: Empty CWD, flat scaffold

Read `manifest.md`. Create every folder listed at CWD (no `Authentic-AI-OS/` wrapper).

Then write:
- `assets/_guide.md` → `./_guide.md`
- `assets/CLAUDE.md` → `./CLAUDE.md`
- `./.env.example` containing exactly:

  ```
  # Authentic AI OS environment.
  # Copy this file to .env and paste your keys. .env is never committed.
  # Future skills will document the keys they need.
  ```

Go to **Step 4**.

### Step 2B: Business-os vault detected

Check whether `./Departments/Content/` exists.

- **If it exists with any content** (any files other than `_guide.md`): stop and ask the creator using `AskUserQuestion`:
  > "I found an existing Content department at `Departments/Content/`. Where should Authentic AI OS live?"
  >   - **Nest inside it**: `Departments/Content/Authentic-AI-OS/`
  >   - **Pick a different path**: prompt for a custom path
  >   - **Cancel**: stop without writing anything

- **If it does not exist** (or exists but is empty): propose the default and confirm:
  > "I'll nest Authentic AI OS at `Departments/Content/Authentic-AI-OS/`. Confirm, or pick a different path."

Once the creator confirms a path (let `TARGET` be the chosen absolute or relative directory):

1. Read `manifest.md`. Create every folder listed inside `TARGET`.
2. Write `assets/_guide.md` → `TARGET/_guide.md`.
3. Write `assets/CLAUDE.md` → `TARGET/CLAUDE.md`.
4. Write `TARGET/.env.example` (same content as Step 2A).
5. **Root routing block (additive).** Read the root `claude.md` (or `CLAUDE.md`). Check whether it already contains a `## Content work` section pointing at Authentic AI OS. If absent:
   - Read `assets/root-routing-block.md`.
   - Substitute `{TARGET_PATH}` with the relative path to `TARGET` from the root.
   - Show the creator the exact block to be appended and ask yes/no.
   - On yes: append the block to the end of the root `claude.md`. Never overwrite existing content.
   - On no: skip the append, note it in the receipt.
6. **Do NOT create `Departments/Content/Content.md`.** That index file is business-os's convention to manage. Stay in the chosen `TARGET` directory.

Go to **Step 4**.

### Step 2C: Other existing vault

Ask the creator using `AskUserQuestion`:
> "I see an existing vault but no business-os structure. Where should Authentic AI OS live?"
>   - **At the vault root** as `Authentic-AI-OS/` (default)
>   - **Pick a custom path**: prompt for a path
>   - **Cancel**: stop without writing anything

Once the creator confirms a path (let `TARGET` be the chosen directory):

1. Read `manifest.md`. Create every folder listed inside `TARGET`.
2. Write `assets/_guide.md` → `TARGET/_guide.md`.
3. Write `assets/CLAUDE.md` → `TARGET/CLAUDE.md`.
4. Write `TARGET/.env.example` (same content as Step 2A).
5. **No root routing block.** This case has no recognized root constitution to safely modify.

Go to **Step 4**.

### Step 3: Additive update

Read `manifest.md`. For every folder the manifest now lists that does not yet exist in the container, create it. If `_guide.md` or `CLAUDE.md` or `.env.example` is missing at the container root, write it from `assets/`. Never read, modify, overwrite, or delete anything the creator authored (`foundation/*`, bank entries, `People/*`, their `.env`).

Go to **Step 4**.

### Step 4: Receipt and handoff

Report plainly:

- The path where the workspace landed.
- What was created vs already present.
- Anything new this release added (Step 3 only).
- Whether a routing block was appended to the client's root `claude.md` (Step 2B only).
- The next move:

  > "Workspace ready at `[TARGET]`. Run `vid-foundation` to start. It walks you through avatar, positioning, pillars, credibility, and backstory, one focused session each."

Do NOT mention skills that have not shipped (no `vid-voice-capture`, `vid-research`, `vid-capture`). The end-of-foundation handoff lives inside `vid-foundation`, not here.

## Safety rules

- Only ever create or write inside the chosen `TARGET`. Never a sibling `People/`, `Notes/`, or `foundation/` belonging to another system.
- Creator content is untouchable. This skill scaffolds empty structure only.
- The client's existing root `claude.md` is never overwritten. Only additively appended, and only with explicit confirmation.
- If any write fails, stop and report the exact path. Do not continue blindly.
- Never fabricate a key, a value, or a foundation section.

## What this skill is NOT

- An interview. It asks the creator nothing about their identity. That is `vid-foundation` and its sub-skills.
- A knowledge copier. `knowledge/` reference files ship with the plugin and are referenced from there; they never get copied into the workspace.

## Maintenance contract

When a new skill is released and it needs container structure before it runs, add one row to `manifest.md` (skill, needed folder, class, since-version). If the new skill introduces a new bank, its schema doc goes into the plugin `knowledge/` folder, not into the workspace. No code in this SKILL.md changes. The creator re-runs `creator-setup` after the plugin update; Step 3 adds the new folder and nothing else.
