---
name: creator-setup
description: Scaffolds the Authentic AI OS workspace inside the creator's chosen content folder. Inspects the vault, surfaces candidate folders, lets the creator pick. Writes a workspace CLAUDE.md and offers a routing block at the root. Safe to re-run after plugin updates. Triggers on "set up Authentic AI OS", "scaffold my vault", or "run creator setup".
---

> 🔄 **Pre-flight (mandatory).** Before doing anything else, read `${CLAUDE_PLUGIN_ROOT}/knowledge/update-check.md` and follow it. If a newer version exists, halt and tell the creator. If you're up to date, continue with the skill below.

# Creator setup

The installer. Establishes the workspace the foundation skills write into, then offers a handoff. It does not interview the creator about their identity. It scaffolds structure, writes Claude's rules for that folder, and gets out of the way.

This skill is manifest-driven. `manifest.md` lists every currently released skill and the container folders it needs. Scaffold only what the manifest says. Never scaffold for a skill that is not released. When a new skill ships, the maintainer adds a row to `manifest.md`; this skill needs no other change.

**Core principle: the workspace IS the content folder.** Whatever folder the creator designates as their content home (a fresh folder, an existing `content/` inside a department, a root-level `content/`, or anything else), the skill scaffolds directly inside it. No `Authentic-AI-OS/` wrapper subfolder. The workspace and the content folder are the same thing.

## Response format

Keep responses scannable. The creator should be able to skim and know what you're saying.

Break by idea. A new thought gets a new paragraph with a blank line above it. Walls of text don't get read.

Plain language. If the creator wouldn't say a word out loud, don't write it. Default to how they talk.

Lists go in bullets, not comma-separated runs inside a sentence.

### Bad

> "Your business is structured around a hybrid model combining consulting engagements with productized services, which creates revenue volatility because consulting hours fluctuate while productized commitments compound, and that's compounded by your team being optimized for delivery rather than acquisition, so even when leads come in there's no dedicated handler, meaning the funnel leaks at the top."

### Good

> "Your business mixes consulting with productized services.
>
> Consulting hours swing month to month. Productized work piles up. That makes revenue lumpy.
>
> The team is built to deliver, not to win new work. When leads show up, no one's handling them, so they fall out at the top.
>
> Where do you want to start?"

Same content. Broken by idea. Plain words. The creator can scan it in three seconds.

## What gets scaffolded

The folders the released foundation skills need:

- `foundation/` (empty; the foundation skills fill it)
- `banks/proof-bank/assets/` (where `vid-credibility` writes proof entries and their screenshots)
- `people/` (where `vid-credibility` and `vid-backstory` write person stubs by default. Skipped if the creator chose a path override; see "Path overrides" below.)

Plus two files at the workspace root:

- `CLAUDE.md` (Claude's scoped rules for this workspace; written from `assets/CLAUDE.md`). **Mandatory. Always written. Never skipped.** See "Why CLAUDE.md is mandatory" below.
- `.env.example` (placeholder for API keys future skills will need)

No `_guide.md` (deprecated; CLAUDE.md serves both Claude and the creator). No `knowledge/` (it ships with the plugin and is referenced from there). No `title-bank.md`, no `story-bank/`, no `packaging-system.md`. Those arrive when their skills ship and get manifest rows.

## Why CLAUDE.md is mandatory

Per Claude Code's documented [CLAUDE.md cascade](https://docs.claude.com/en/docs/claude-code/memory), when a creator is working inside the workspace folder, Claude Code loads:

- The root vault `CLAUDE.md` (if it exists), AND
- The workspace `CLAUDE.md` (the one this skill writes)

Both **concatenate** into context. They do not conflict. The cascade is the documented mechanism for scoping instructions to a sub-tree.

The workspace `CLAUDE.md` is the only place Authentic AI OS rules apply in that folder. Without it, the foundation skills have no scoped guardrails when they run there. Skipping it defeats the entire skill.

**Never skip writing the workspace CLAUDE.md.** If the creator already has a root `CLAUDE.md`, that one stays as-is. The workspace one sits alongside, in the workspace folder, and applies on top.

## How this skill runs

### Step 1: Look at the folder

Check ONLY the current working directory. Never search parent or child directories.

**First, check for an existing workspace.** If the CWD itself contains a `foundation/` folder AND a workspace `CLAUDE.md`, this is already an AAI OS workspace, → go to **Step 3 (additive update)**.

**Otherwise, inspect what's there.** List the top-level folders and files with `ls`. Look for:

- A `claude.md` or `CLAUDE.md` at the root. Signals an existing vault with its own constitution.
- Any folder whose name suggests it could be a content home: `content`, `Content`, `creative`, `media`, `marketing`. Both at the vault root AND inside organizational folders (`departments/`, `areas/`, `silos/`, `teams/`, `divisions/`, etc.).
- Other vault-like signals: `projects/`, `people/`, `People/`, `.obsidian/`.

**Critical: inspect, do not pattern-match.** First-match-wins is the failure mode of this skill. If multiple folders could plausibly be content homes, do not lock in on the first one. List each candidate with `ls`, see what's actually inside, and surface them all to the creator with context.

Then route:

- **Empty or near-empty CWD** (no organizational or vault signals): → **Step 2A (flat scaffold)**.
- **Existing vault** (any signal found): → **Step 2B (inspect candidates, propose, ask)**.

### Step 2A: Empty CWD, flat scaffold

Read `manifest.md`. Create every folder listed at CWD.

Then write:
- `assets/CLAUDE.md` → `./CLAUDE.md`
- `./.env.example` containing exactly:

  ```
  # Authentic AI OS environment.
  # Copy this file to .env and paste your keys. .env is never committed.
  # Future skills will document the keys they need.
  ```

In Step 2A, the workspace CLAUDE.md ships with the default Path overrides section (none set, since there's no surrounding vault to integrate with).

Go to **Step 4**.

### Step 2B: Existing vault, inspect candidates and let the creator pick

**This is the failure-prone step. Follow the discipline below.**

#### Decision discipline

Two rules that override everything below. The earlier failure mode was Claude ignoring its own rules and asking the creator about settled decisions. Don't.

**Rule 1: Obey the defaults. Never re-ask them.**

Some choices are already settled by this skill. Do NOT surface them as creator decisions. Not via the form tool, not via plain question, not via casual mention. They are settled:

- **Existing root claude.md handling.** Always leave it alone. Always write the workspace CLAUDE.md alongside. The [Claude Code cascade](https://docs.claude.com/en/docs/claude-code/memory) concatenates both files when working inside the workspace folder. There is no creator decision to make. Do not ask.
- **Writing the workspace CLAUDE.md.** Always yes. Mandatory per "Why CLAUDE.md is mandatory" above. Do not ask.
- **What folders to scaffold.** `manifest.md` is the source of truth. Read it, create what's listed, done.

The one exception is the root routing block append (B.6.4 below). Asked because we're touching the creator's authored root file. Everything else above defaults silently.

**Rule 2: Propose, never just present.**

When you do ask, lead with your recommendation and reasoning. Never hand the creator a flat list with no opinion. The creator's time is the resource; lazy "what do you want?" asks waste it.

- In a form: mark one option as "(Recommended)" with a short reason in the description.
- In a plain message: name your pick and why in the first sentence, then list alternates.

> Good: "Best fit: `Projects/content/`. It already has README and ideas folders, so the production work lands there cleanly. Confirm or pick a different location."
>
> Bad: "Where should the workspace go? Options: vault root, Projects/, Resources/, somewhere else."

Think critically before you ask. What does the structure actually suggest? What would a sharp human pick? Lead with that.

#### B.1: Identify ALL candidate content homes

List every folder that could plausibly be the content workspace. Sources:

- Root-level folders with content-style names (e.g., `content/`, `Content/`, `creative/`).
- Folders inside organizational containers (e.g., `departments/content/`, `areas/marketing/`).
- The creator's volunteered preference, if they named one.

Do not stop after finding one match. There may be two or more.

#### B.2: Inspect each candidate

For each candidate folder, run `ls` and look at what's inside. Distinguish ops/strategy folders (SOPs, plans, strategy docs, README.md) from production folders (pieces/, ideas/, sequences/, content artifacts).

#### B.3: Surface candidates to the creator

If there is exactly one candidate and its contents clearly indicate a content production home, propose it: "Best fit based on your structure: `<path>`. It contains `<3-5 things you saw>`. Confirm, or pick a different location."

If there are multiple candidates, name your pick and why first. Then list the alternates:

> "Best fit: `<recommended-path>`. `<one-sentence reason based on what's inside>`.
>
> Alternates I considered:
> - `<other-path-1>` contains `<contents>`. `<one-line read>`.
> - `<other-path-2>` contains `<contents>`. `<one-line read>`.
>
> Confirm the recommendation, or pick a different location."

If no candidate is obvious and the vault has organizational structure, propose creating a new `content/` folder at the vault root: "I don't see an obvious content home. My recommendation: create a new `content/` folder at the vault root and scaffold there. Confirm or pick a different location."

**Do not propose a location until you have inspected the contents of every plausible candidate.** First-match-wins is the documented failure mode of this skill.

#### B.4: Collision check before writing

Let `TARGET` be the folder the creator chose. If `TARGET` already exists and contains files:

- If `TARGET/foundation/` exists, this is an AAI OS workspace already. Switch to Step 3.
- Otherwise, the creator already has content in that folder. Confirm: "The folder `<TARGET>` already contains `<list a few files>`. The scaffold will add `foundation/`, `banks/proof-bank/assets/`, and `people/` alongside what's there. Confirm or pick a different location."

#### B.5: Handle the people/ override

The default behavior creates a local `people/` folder inside `TARGET` for `vid-credibility` and `vid-backstory` to write person stubs.

**Check the vault root for an existing People-style folder** (`people/`, `People/`, `contacts/`, etc.). If none exists, do NOT ask. Default to local `people/` silently. There is no creator choice when only one option exists.

If a root-level People folder DOES exist, propose the recommendation and ask:
> "I see `<root-people-folder>` at the vault root. My recommendation: route person stubs there so all your people live in one place. Confirm, or keep them local to the workspace in `people/`."

- If (a): default behavior. Scaffold local `people/`. No override needed in CLAUDE.md.
- If (b): SKIP scaffolding local `people/`. Record the override path. Include it in the workspace CLAUDE.md "Path overrides" section so foundation skills follow the redirect.

#### B.6: Write

Once `TARGET` and the people/ override (if any) are settled:

1. Read `manifest.md`. Create the listed folders inside `TARGET`. If a people/ override is in effect, skip the `people/` row.
2. Write `assets/CLAUDE.md` → `TARGET/CLAUDE.md`. **Always.** If a people/ override is in effect, fill in the "Path overrides" section in the written CLAUDE.md with the redirect. If no overrides, leave that section empty or note "no overrides."
3. Write `TARGET/.env.example` (same content as Step 2A).
4. **Root routing block.** Read the root `claude.md` or `CLAUDE.md`. Check whether it already contains a `## Content work` (or equivalent) section pointing at this workspace. If absent:
   - Read `assets/root-routing-block.md`.
   - Substitute `{TARGET_PATH}` with the relative path to `TARGET` from the vault root.
   - Show the creator the exact block to be appended and ask yes/no.
   - On yes: append to the end of the root file. Never overwrite existing content.
   - On no: skip the append, note it in the receipt.

   Always offer. Do not skip silently.

5. **Do not create folder index files inside `TARGET`.** If the creator's vault uses a `content.md` or `README.md` index convention, that's theirs to maintain.

Go to **Step 4**.

### Step 3: Additive update

The workspace already exists. Read `manifest.md`. For every folder the manifest now lists that does not yet exist in `TARGET`, create it. If `CLAUDE.md` or `.env.example` is missing at the workspace root, write it from `assets/`.

Never read, modify, overwrite, or delete anything the creator authored (`foundation/*`, bank entries, `people/*`, their `.env`, their CLAUDE.md if they edited it).

Go to **Step 4**.

### Step 4: Receipt and handoff

Report plainly:

- The path where the workspace landed.
- What was created vs already present.
- Anything new this release added (Step 3 only).
- Whether a routing block was appended to the root `claude.md` (Step 2B only).
- Any path overrides recorded in the workspace CLAUDE.md.

**Then tailor the handoff to foundation state.** Read `TARGET/foundation/creator-foundation.md` if it exists and check which sections (Offer, Avatar, Top 3, Iceberg, Pillars, Credibility, Backstory) are filled vs `[to fill]`.

- **Foundation is empty or missing:** offer, don't direct.
  > "Want me to start `vid-foundation` now? It walks you through avatar, positioning, pillars, credibility, and backstory, one focused session each. Or come back to it when you're ready."

  If yes, invoke `vid-foundation` via the Skill tool. If not now, friendly close.

- **Foundation is partially filled:** acknowledge what's locked, offer to resume.
  > "Looks like your foundation is partway through. You have `[list locked sections in plain language]`. Want me to pick up with `vid-foundation` from where you left off? Or come back later."

- **Foundation is complete:** do not suggest `vid-foundation`. Close with a status line:
  > "Workspace is current. Your foundation is locked. More skills are in development; you'll get them on the next plugin update."

  If Step 3 added new folders, name them. If nothing was added, say "Nothing new to add."

Do NOT mention skills that have not shipped (no `vid-voice-capture`, `vid-research`, `vid-capture`). The principle: facilitate, do not prescribe. The creator's state determines the offer.

## Safety rules

- Only ever create or write inside the chosen `TARGET`. Never a sibling `people/`, `notes/`, or `foundation/` belonging to another system.
- Creator content is untouchable. This skill scaffolds empty structure only.
- The client's existing root `claude.md` is never overwritten. Only additively appended, and only with explicit confirmation.
- The workspace CLAUDE.md is always written. No exceptions, no rationalized skips. See "Why CLAUDE.md is mandatory" above.
- If any write fails, stop and report the exact path. Do not continue blindly.
- Never fabricate a key, a value, or a foundation section.
- Never invent new artifact files (no ad-hoc routing files, no sidecar configs). If a piece of information needs to live somewhere, it goes in the workspace CLAUDE.md (the documented vehicle for scoped instructions).

## What this skill is NOT

- An interview. It asks the creator nothing about their identity. That is `vid-foundation` and its sub-skills.
- A knowledge copier. `knowledge/` reference files ship with the plugin and are referenced from there; they never get copied into the workspace.

## Maintenance contract

When a new skill is released and it needs container structure before it runs, add one row to `manifest.md` (skill, needed folder, class, since-version). If the new skill introduces a new bank, its schema doc goes into the plugin `knowledge/` folder, not into the workspace. No code in this SKILL.md changes. The creator re-runs `creator-setup` after the plugin update; Step 3 adds the new folder and nothing else.
