---
type: reference
doc: vault-integration
project: authentic-ai-os
status: active
tags: [reference, vault-integration, contract]
---

# Vault Integration Contract

The shared core every skill that writes to this vault follows: where things live, how they link, how they are tagged and named. Small on purpose.

**Per-artifact schemas are NOT here.** They live with the skills that write them, so a skill loads the contract for the artifact it touches and nothing else.

| You are writing | Load | Who loads it |
|---|---|---|
| A piece (`content/pieces/{slug}/piece.md`) | `knowledge/piece-contract.md` | vid-intake, vid-framing, vid-title, vid-thumbnail, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test, vid-pipeline |
| A bank entry (story, proof, metaphor, testimonial, framework), or pulling one into a script | `knowledge/bank-contract.md` | vid-bank, vid-segment, vid-intro, vid-ending, vid-credibility |
| A foundation doc | this file, "Foundation doc schema" below | vid-avatar, vid-positioning, vid-pillars, vid-credibility, vid-backstory |
| The voice profile or a reference-piece set | `knowledge/voice-profile-schema.md` | vid-voice-capture, vid-voice-update |
| The ideas backlog | `.claude/skills/vid-ideas/assets/ideas-backlog-template.md` | vid-ideas |
| A brain dump | the `brain-dump.md` block in `vid-intake/SKILL.md` | vid-intake |

**Do not grow this file.** A new schema goes in the contract for its artifact, or in the skill that owns it. What belongs here is only what applies to every note in the vault.

## Folder map (the routing table)

**Core, populated as the creator runs the workflow:**

| Folder | What lives here |
|---|---|
| `foundation/` | Creator identity, one concern per file so skills load only the slice they need: iceberg.md (iceberg statement, machinery, content notes, the content pillars), avatar.md (avatar plus the Top 3 perceived problems), credibility.md (the three proof points), backstory.md, offer.md. Plus voice-profile.md, packaging-system.md, and `reference-pieces/` (full polished pieces preserved verbatim for piece-level voice rhythm). |
| `banks/` | Evergreen material the creator builds over time. Stories, proofs, testimonials, metaphors, frameworks, packaging winners, plus single-file banks (title, hook, transition, pattern). |
| `content/pieces/` | Per-video work. One folder per piece: piece.md (all locked decisions), brain-dump.md (raw material), script.md (the deliverable), plus per-platform derivatives. Single newsletters and one-off posts also live here as their own piece folder. |
| `content/ideas/` | Swipe file for not-yet-built content. Raw ideas, hooks, framings the creator wants to come back to. |
| `content/email-sequences/` | Multi-piece email sequences (welcome, nurture, launch, re-engagement). One folder per sequence. |
| `people/` | One file per human in the creator's world. Clients, prospects, partners, community. Frontmatter-typed. |

**Optional, scaffolded as the creator needs them:**

| Folder | When the creator would use it |
|---|---|
| `raw/` | Creator's own raw material (full text). Transcripts, articles, brain dumps waiting to be mined. Staging area, not a permanent home. |
| `references/` | External study material pointers (course names, book titles, podcast episodes the creator is learning from). Pointers and notes only, no full content. |
| `notes/` | Drop-zone for on-the-go brain dumps. Reconciled later through a routing skill. |

**Routing rule:** every piece of incoming material has exactly one home. The optional folders activate on demand.

**Out of scope:** `Daily/`, `Projects/`, `Trainings/`, `companies/`, `Intelligence/`. This vault is content-only. Business workflows live in a separate workspace.

## Wikilink form

Two shapes, decided by what the link points AT:

- **Into a bank:** `bank-dir/slug`, like `[[proof-bank/onboarding-5h-to-1h]]` or `[[story-bank/agency-owner-fired-himself]]`. Never put the `banks/` folder in the path.
- **At a piece or a person:** the bare name, like `[[why-systems-beat-hustle]]` or `[[Sarah Chen]]`.

Never write a wikilink whose target does not exist yet. Verify first. If the target is missing, either create it or flag it to the creator as unresolved. A broken wikilink is worse than plain text because it looks connected and isn't.

Free-form wikilinks in body prose are encouraged when entries relate ("this metaphor lands best paired with [[story-bank/agency-owner-fired-himself]]"). No frontmatter needed for those; Obsidian's backlink pane handles it.

## Tag conventions

Every tag is lowercase, hyphen-separated. No spaces. No capitals.

- Every foundation doc: `foundation`
- Every story: `story`, plus theme slugs
- Every metaphor: `metaphor`, `category-{slug}`, plus theme slugs
- Every proof: `proof`, `{proof-type-slug}`
- Every testimonial: `testimonial`, `source-{slug}`
- Every piece: `piece`, `format-{slug}`, `pillar-{slug}`

**Theme tags** are creator-specific and emerge organically (`automation`, `delegation`, `client-onboarding`, `pricing`, `time-management`). Add them when they will help future retrieval. Do not force one onto every entry, and do not invent a single-use tag.

## File naming and slugs

- Lowercase only
- Hyphen-separated
- Descriptive but short (3 to 6 words)
- No dates in the filename (dates live in frontmatter)
- No redundant prefixes (a file in `story-bank/` does not need `story-` in the name)

Examples: `banks/story-bank/airbnb-photo-swap-booked-3x.md`, `banks/proof-bank/4m-youtube-revenue-2025.md`, `content/pieces/why-systems-beat-hustle/`.

Claude proposes the slug. Creator approves or overrides before saving.

## Foundation doc schema

Location: `foundation/iceberg.md`, `foundation/avatar.md`, `foundation/credibility.md`, `foundation/backstory.md`, `foundation/offer.md`, `foundation/voice-profile.md`, `foundation/packaging-system.md`, `foundation/channel-audit.md`

```yaml
---
type: foundation
doc: iceberg               # or avatar, credibility, backstory, offer, voice-profile, packaging-system, channel-audit
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD            # most recent update. Drives "stale doc" warnings (e.g. voice-profile older than 90 days)
contexts_populated: [youtube-script]  # voice-profile only. Which voice_context reference-piece sets exist under foundation/reference-pieces/. Empty list is valid for fresh profiles.
tags: [foundation, {doc-specific-tags}]
---
```

- `last_refreshed`: on every foundation doc, updated whenever the doc gets edited. Skills warn the creator if a load-bearing doc (voice-profile especially) has not refreshed in 90+ days.
- `contexts_populated`: voice-profile only. Other foundation doc types omit it or set `[]`.

## Callout conventions

Obsidian callouts highlight key information. One or two per entry, maximum.

| Callout | When to use |
|---|---|
| `> [!tip]` | Why this works, what makes it land |
| `> [!warning]` | Sensitivity notes, NDA, client permission status |
| `> [!note]` | Context, source, timing |
| `> [!success]` | A quantifiable outcome in its own block |
| `> [!quote]` | A verbatim client quote (testimonials) |
