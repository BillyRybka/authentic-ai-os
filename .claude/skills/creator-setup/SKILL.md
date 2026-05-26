---
name: creator-setup
description: One-time installer that scaffolds the Authentic AI OS workspace so the foundation skills have somewhere to write. Looks at the current folder, figures out what kind of vault it is (fresh, an existing organizational structure with departments/areas/silos/etc., or something else), proposes a sensible landing spot, asks when unclear, writes a `CLAUDE.md` so Claude knows the rules, and is safe to re-run after every plugin update (additive, never destroys the creator's work). Use when a creator just installed the plugin, is setting up for the first time, or needs to refresh the workspace structure after an update. Triggers on "set up Authentic AI OS", "install Authentic AI OS", "scaffold my vault", "first time setup", "I just installed the plugin", "set up my vault", "run creator setup".
---

# Creator setup

The installer. Establishes the workspace the foundation skills write into, then hands off to `vid-foundation`. It does not interview the creator. It does not write any identity content. It scaffolds structure and gets out of the way.

This skill is manifest-driven. `manifest.md` lists every currently released skill and the container folders it needs. Scaffold only what the manifest says. Never scaffold for a skill that is not released. When a new skill ships, the maintainer adds a row to `manifest.md`; this skill needs no other change.

## What gets scaffolded

The folders the released foundation skills need:

- `foundation/` (empty; the foundation skills fill it)
- `banks/proof-bank/assets/` (where `vid-credibility` writes proof entries and their screenshots)
- `people/` (where `vid-credibility` and `vid-backstory` write person stubs)

Plus three files at the workspace root:

- `_guide.md` (human-readable orientation; written from `assets/_guide.md`)
- `CLAUDE.md` (Claude's rules for working in the workspace; written from `assets/CLAUDE.md`)
- `.env.example` (placeholder for API keys future skills will need)

No `knowledge/` (it ships with the plugin and is referenced from there). No `title-bank.md`, no `story-bank/`, no `packaging-system.md`. Those arrive when their skills ship and get manifest rows.

## How this skill runs

### Step 1: Look at the folder

Check ONLY the current working directory. Never search parent or child directories.

**First, check for an existing container.** If an `Authentic-AI-OS/` folder exists at CWD, OR the CWD itself already contains a `foundation/` folder (signals a previous flat scaffold), → go to **Step 3 (additive update)**.

**Otherwise, read what's there.** List the top-level folders and files. Look for:

- A `claude.md` or `CLAUDE.md` at the root. Signals an existing vault with its own constitution.
- Folder names that suggest organizational structure: `departments`, `areas`, `silos`, `categories`, `divisions`, `teams`, `pillars`, etc. (any plural label that groups work).
- Folder names that suggest content already has a home: `content`, `marketing`, `creative`, `media`, anywhere inside an organizational folder or at the root.
- Any other vault-like signals: `projects/`, `people/`, a `.obsidian/` folder, etc.

**Use judgment about what you see.** This is not a rule-based detection. The skill looks, reasons about the structure, and proposes the most sensible landing spot. If the vault is unfamiliar or the structure is ambiguous, ask.

Then route to one of two paths:

- **Empty or near-empty CWD** (no organizational signals, maybe just an empty folder): → **Step 2A (flat scaffold)**.
- **Existing vault** (anything else, including the cases above): → **Step 2B (locate, propose, ask if unclear)**.

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

### Step 2B: Existing vault, locate the right landing spot

Based on what Step 1 found, decide where Authentic AI OS should live. The principle: **fit the creator's existing structure, do not impose ours.**

**Reasoning the skill follows (in order):**

1. **Is there already a content-style home inside an organizational folder?** Examples: `departments/content/`, `areas/content/`, `silos/creative/`, `categories/marketing/`. If yes, that's the likely target. Propose nesting Authentic AI OS inside it. Show the proposed path, confirm with the creator before writing.

2. **Is there an organizational folder but no content-style sub-folder inside it?** Examples: `departments/` exists, but no `content/` inside. Ask: "I see `<org-folder>/`. Should I create `<org-folder>/content/` for this work, place it somewhere else, or cancel?" Respect the answer.

3. **Is there a vault but no organizational folder at all?** Examples: a flat vault with `projects/`, `people/`, a root `claude.md`, but no department-style grouping. Ask: "I see an existing vault. Where should Authentic AI OS live? At the vault root as `Authentic-AI-OS/`, a custom path you pick, or cancel?"

4. **Structure looks novel or you cannot tell?** Always fall back to asking. List the top-level folders you found, propose your best guess, let the creator override.

**Collision check before writing:** Whatever the chosen `TARGET` is, if it already exists AND contains files (anything beyond a possible `_guide.md`), stop and ask:
> "There's already content at `<TARGET>`. Do you want to (a) nest Authentic AI OS inside it, (b) pick a different path, or (c) cancel?"

**Once the creator confirms a `TARGET`:**

1. Read `manifest.md`. Create every folder listed inside `TARGET`.
2. Write `assets/_guide.md` → `TARGET/_guide.md`.
3. Write `assets/CLAUDE.md` → `TARGET/CLAUDE.md`.
4. Write `TARGET/.env.example` (same content as Step 2A).
5. **Root routing block (only if a root `claude.md`/`CLAUDE.md` exists).** Read it. Check whether it already contains a `## Content work` section pointing at Authentic AI OS. If absent:
   - Read `assets/root-routing-block.md`.
   - Substitute `{TARGET_PATH}` with the relative path to `TARGET` from the root.
   - Show the creator the exact block to be appended and ask yes/no.
   - On yes: append the block to the end of the root file. Never overwrite existing content.
   - On no: skip the append, note it in the receipt.
6. **Never create index files inside folders you didn't create.** If the creator's vault uses a convention like `departments/content/content.md` as an index, that's their convention to maintain. Stay inside `TARGET`.

Go to **Step 4**.

### Step 3: Additive update

Read `manifest.md`. For every folder the manifest now lists that does not yet exist in the container, create it. If `_guide.md` or `CLAUDE.md` or `.env.example` is missing at the container root, write it from `assets/`. Never read, modify, overwrite, or delete anything the creator authored (`foundation/*`, bank entries, `people/*`, their `.env`).

Go to **Step 4**.

### Step 4: Receipt and handoff

Report plainly:

- The path where the workspace landed.
- What was created vs already present.
- Anything new this release added (Step 3 only).
- Whether a routing block was appended to the client's root `claude.md` (Step 2B only).

**Then tailor the handoff to what's already in the workspace.** Read `TARGET/foundation/creator-foundation.md` if it exists and check which sections (Offer, Avatar, Top 3, Iceberg, Pillars, Credibility, Backstory) are filled vs `[to fill]`.

- **Foundation is empty or missing:** offer, don't direct. Phrase as a choice:
  > "Want me to start `vid-foundation` now? It walks you through avatar, positioning, pillars, credibility, and backstory, one focused session each. Or come back to it when you're ready."

  If the creator says yes, invoke `vid-foundation` via the Skill tool. If they say not now, stop with a friendly close.

- **Foundation is partially filled:** acknowledge what's locked, offer to resume.
  > "Looks like your foundation is partway through. You have `[list locked sections in plain language]`. Want me to pick up with `vid-foundation` from where you left off? Or come back later."

- **Foundation is complete (all sections filled):** do not suggest `vid-foundation`. Their identity is locked. Close with a status line:
  > "Workspace is current. Your foundation is locked. More skills are in development; you'll get them on the next plugin update."

  If Step 3 added new folders, name them. If nothing was added, say "Nothing new to add."

Do NOT mention skills that have not shipped (no `vid-voice-capture`, `vid-research`, `vid-capture`). The end-of-foundation handoff lives inside `vid-foundation`, not here. The principle: facilitate, do not prescribe. The creator's state determines the offer.

## Safety rules

- Only ever create or write inside the chosen `TARGET`. Never a sibling `people/`, `notes/`, or `foundation/` belonging to another system.
- Creator content is untouchable. This skill scaffolds empty structure only.
- The client's existing root `claude.md` is never overwritten. Only additively appended, and only with explicit confirmation.
- If any write fails, stop and report the exact path. Do not continue blindly.
- Never fabricate a key, a value, or a foundation section.

## What this skill is NOT

- An interview. It asks the creator nothing about their identity. That is `vid-foundation` and its sub-skills.
- A knowledge copier. `knowledge/` reference files ship with the plugin and are referenced from there; they never get copied into the workspace.

## Maintenance contract

When a new skill is released and it needs container structure before it runs, add one row to `manifest.md` (skill, needed folder, class, since-version). If the new skill introduces a new bank, its schema doc goes into the plugin `knowledge/` folder, not into the workspace. No code in this SKILL.md changes. The creator re-runs `creator-setup` after the plugin update; Step 3 adds the new folder and nothing else.
