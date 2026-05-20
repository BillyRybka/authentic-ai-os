---
type: reference
doc: vault-integration
project: authentic-ai-os
status: active
tags: [reference, vault-integration, contract]
---

# Vault Integration Contract

Every skill in authentic-ai-os loads this file. It is the contract that makes the system work end-to-end. Capture once, pull in automatically at script-writing time, with full bidirectional wikilinks so nothing sits in isolation.

**Load this reference at the start of any skill that reads from or writes to the vault.**

## Folder map (the routing table)

**Core, populated as the creator runs the workflow:**

| Folder | What lives here |
|---|---|
| `foundation/` | Creator identity. creator-foundation.md, voice-profile.md, packaging-system.md, and `reference-pieces/` (full polished pieces preserved verbatim for piece-level voice rhythm). |
| `banks/` | Evergreen material the creator builds over time. Stories, proofs, testimonials, metaphors, frameworks, packaging winners, plus single-file banks (title, hook, transition, pattern). |
| `Content/pieces/` | Per-video work. One folder per piece. brain-dump, reference-block, script, thumbnail-brief, pressure-test, per-platform derivatives. Single newsletters and one-off posts also live here as their own piece folder. |
| `Content/ideas/` | Swipe file for not-yet-built content. Raw ideas, hooks, framings the creator wants to come back to. |
| `Content/email-sequences/` | Multi-piece email sequences (welcome, nurture, launch, re-engagement). One folder per sequence. |
| `People/` | One file per human in the creator's world. Clients, prospects, partners, community. Frontmatter-typed. |

**Optional, scaffolded as the creator needs them:**

| Folder | When the creator would use it |
|---|---|
| `raw/` | Creator's own raw material (full text). Transcripts, articles, brain dumps waiting to be mined. Staging area, not a permanent home. |
| `references/` | External study material pointers (course names, book titles, podcast episodes the creator is learning from). Pointers and notes only, no full content. |
| `Notes/` | Drop-zone for on-the-go brain dumps. Reconciled later through a routing skill. |

**Routing rule:** every piece of incoming material has exactly one home. The optional folders activate on demand.

**Out of scope:** `Daily/`, `Projects/`, `Trainings/`, `Companies/`, `Intelligence/`. This vault is content-only. Business workflows live in a separate workspace.

## Why this exists

When the creator sits down to write a video, the skill needs to:
- Find the right story for this video's point (tag plus problem lookup)
- Find the matching proof, metaphor, or testimonial
- Write the script with the story in it
- Update BOTH the script AND the source bank entry to show the connection

If every skill doesn't follow the same conventions, queries fail. Stories sit in banks/story-bank/ invisible to the scripting skill. Scripts pull stories but never link back, so "where did I use this?" is unanswerable. The graph breaks.

This doc is the shared contract that prevents that. Every skill across the workspace honors the same frontmatter discipline, wikilink rules, and tag conventions.

## Frontmatter schemas

Every entry in the system has YAML frontmatter matching one of these schemas. Do not skip fields. Populate everything that applies.

### Foundation docs

Location: `foundation/creator-foundation.md`, `foundation/voice-profile.md`, `foundation/packaging-system.md`, `foundation/channel-audit.md`

```yaml
---
type: foundation
doc: creator-foundation    # or voice-profile, packaging-system, channel-audit
project: authentic-ai-os
status: active
date: YYYY-MM-DD
last_refreshed: YYYY-MM-DD            # most recent update. Drives "stale doc" warnings (e.g. voice-profile older than 90 days)
contexts_populated: [youtube-script]  # voice-profile only. Which voice_context reference-piece sets exist under foundation/reference-pieces/. Empty list is valid for fresh profiles.
tags: [foundation, {doc-specific-tags}]
---
```

**Field notes:**
- `last_refreshed`: every foundation doc. Updated whenever the doc gets edited. Skills warn the creator if a load-bearing doc (voice-profile, especially) hasn't refreshed in 90+ days.
- `contexts_populated`: voice-profile only. The `voice_context` values that have a reference-piece set under `foundation/reference-pieces/`. Other foundation doc types omit this field or set it to `[]`.

### Reference pieces

Location: `foundation/reference-pieces/{voice_context}.md` (one file per populated `voice_context`).

The voice engine. Real passages the creator produced, the generation seed writing skills write from. Curated by `vid-voice-capture`, one file per `voice_context`, with passages inside as `## ` sections. Passages stay **intact** (not trimmed of structure) and verbatim: no restructuring, summarizing, or light edits. A creator-designated improvised moment (a personal beat the creator always delivers live and never wants scripted) is never stored here; it is a refusal in voice-profile.md.

```yaml
---
type: reference-pieces
project: authentic-ai-os
voice_context: youtube-script
captured: YYYY-MM-DD
last_refreshed: YYYY-MM-DD
sources: ["{source filename}", ...]
tags: [voice, reference-pieces, context-{voice_context}]
---
```

Body holds a short intro line plus each passage as a `## ` section. Each section opens with a `> Demonstrates:` line (plain-language description of the mode and energy that passage shows, derived from the creator) then the verbatim passage.

**How writing skills use them:** per the contract in [[voice-profile-schema]], a writing skill loads `voice-profile.md` (the thin guardrail) always, plus `foundation/reference-pieces/{voice_context}.md` matching the piece's `voice_context` (default `youtube-script`) as the seed. Voice only, not structure: the passages carry cadence, word choice, register, signature moves. The writing skill's spec (hook arc, segment shape, Pivot-Gap-Bridge ending) owns the architecture. If a passage's structural arc conflicts with the spec, follow the spec. Rhythm is judged by ear against the passages, never against stored numbers.

### Story entries

Location: `banks/story-bank/{slug}.md`

```yaml
---
type: story
project: authentic-ai-os
story_type: client              # client | own | viewer
problem_illustrated: 1          # 1 | 2 | 3 | general (from creator-foundation top 3 problems)
client: "[[Client Name]]"       # wikilink to People/ profile, only for client stories
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [story, problem-{n}, {theme-slug}]
used_in: []                     # populated by writing skills with [[piece-slug]] entries
---
```

### Metaphor entries

Location: `banks/metaphor-bank/{slug}.md`

```yaml
---
type: metaphor
project: authentic-ai-os
concept: "short concept name"   # what the metaphor is clarifying
category: everyday              # food | cars | clothes | sports | travel | other
visual: false                   # true if the metaphor depends on a prop/graphic to land, false if pure speech works
problem_illustrated: 2          # 1 | 2 | 3 | general
captured: YYYY-MM-DD
status: captured
tags: [metaphor, category-{slug}, visual-metaphor OR non-visual-metaphor, {theme-slug}]
used_in: []
---
```

### Proof entries

Location: `banks/proof-bank/{slug}.md`

`proof_type` is about **who the result belongs to** (creator or client). How the proof is presented (static screenshot, before-after pairing, live video clip, inline stat) is captured separately in the body's "Presentation format" section. A single proof can have multiple formats.

```yaml
---
type: proof
project: authentic-ai-os
proof_type: client-win          # personal-result | client-win
client: "[[Client Name]]"       # wikilink, only if client proof
captured: YYYY-MM-DD
status: captured
tags: [proof, {proof-type-slug}]
asset_path: "banks/proof-bank/assets/{file}.png"   # optional, for screenshots/videos
used_in: []
---
```

### Testimonial entries

Location: `banks/testimonial-bank/{slug}.md` (separate top-level bank. Testimonials are other people's words, distinct from proof which is the creator's own evidence)

```yaml
---
type: testimonial
project: authentic-ai-os
source: comment                 # comment | dm | email | video
client: "[[Client Name]]"       # or "Anonymous" if anonymized
anonymized: false               # true if client identity removed
captured: YYYY-MM-DD
status: captured
tags: [testimonial, source-{slug}]
used_in: []
---
```

### Framework entries

Location: `banks/framework-bank/{slug}.md`

Frameworks are the creator's OWN named systems/structures/mental models. The teachable patterns they repeat across videos. See `banks/framework-bank/README.md` for what belongs here and what doesn't (in particular, third-party frameworks like BENS or the Gift Framework do NOT go here. Those live in `knowledge/` or `Resources/references/` with attribution).

```yaml
---
type: framework
project: authentic-ai-os
name: "The 3-part Onboarding System"
framework_type: process         # process | categorization | decision-model | mental-model
problem_it_solves: "short description of the problem this framework addresses"
components: ["step-1", "step-2", "step-3"]
maturity: active                # draft | active | retired
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [framework, {framework-type-slug}, {domain-slug}]
used_in: []                     # populated by writing skills
---
```

### Per-video pieces

Location: `Content/pieces/{slug}/piece.md`

```yaml
---
type: content-piece
project: authentic-ai-os
slug: video-slug
pillar: {pillar-slug}           # creator's content pillar
format: short-process           # from the 7 formats: short-process | case-study | roast | deep-dive | interview | news | listicle
voice_context: youtube-script   # delivery medium for voice: youtube-script (default) | tutorial | shorts | newsletter | linkedin | twitter | podcast | casual | talk. Orthogonal to format. Set by vid-framing. Drives which foundation/reference-pieces/{voice_context}.md a writing skill loads.
goal: sales                     # sales | emails | views (ONE only)
status: ideating                # ideating | drafting | filming-ready | filmed | editing | published
captured: YYYY-MM-DD
published: null                 # YYYY-MM-DD when published
stories_used: []                # [[story-slug]] wikilinks added when writing skills use them
metaphors_used: []
proofs_used: []
tags: [piece, format-{slug}, pillar-{slug}, {other-tags}]
---
```

## Wikilink patterns

### When a story (or proof, or testimonial) mentions a client by name

1. In frontmatter: `client: "[[Client Name]]"`
2. In body prose: reference as `[[Client Name]]` at first mention
3. Check `People/{Client Name}.md`. If missing, create a stub per CLAUDE.md rule 20:

```markdown
---
type: person
bucket: active-client           # or former-client, prospect, community-network, etc.
status: active
tags: [person, client]
---
# Client Name

> [!note] Stub created automatically when mentioned in [[story-slug|a story]]. Flesh out when needed.
```

Never mention a client without creating the People profile.

### When an entry illustrates one of the top 3 problems

The top 3 problems are defined in `foundation/creator-foundation.md` under the Avatar section.

1. Frontmatter: `problem_illustrated: 1` (or 2, 3, or "general")
2. Body prose (optional, for readability): `This illustrates [[creator-foundation#Top 3 problems|problem 1]]. "I'm drowning in emails..."`

### When a writing skill USES a story (or proof, or metaphor)

**The "update both sides" rule. Non-negotiable.**

1. Write the story content into the script (in the creator's voice, via vid-segment or vid-intro)
2. In the piece's `piece.md`, add the wikilink: `stories_used: ["[[airbnb-photo-swap]]"]`
3. In the story's frontmatter, add the piece wikilink: `used_in: ["[[video-slug]]"]`
4. In the story's frontmatter, update `status: used`

Both sides. Always. This is what makes "which videos used this story?" answerable. It's also what makes the Obsidian graph view show real connections.

Same rule for metaphors (`metaphors_used` in piece, `used_in` in metaphor) and proofs (`proofs_used` in piece, `used_in` in proof).

### Cross-references between bank entries

Free-form wikilinks in body prose are encouraged when entries relate:

- A metaphor that pairs with a specific story: "This metaphor lands best when paired with [[story-slug]]."
- A proof that backs up a story: "Screenshot proof lives at [[proof-slug]]."

No frontmatter required for these. Obsidian's backlink pane handles it.

## Tag conventions

Every tag is lowercase, hyphen-separated. No spaces. No capitals.

### Required tags per entry type

- Every foundation doc: `foundation`
- Every story: `story`, `problem-{n}`, plus theme slugs
- Every metaphor: `metaphor`, `category-{slug}`, `problem-{n}` (if illustrates one)
- Every proof: `proof`, `{proof-type-slug}`
- Every testimonial: `testimonial`, `source-{slug}`
- Every piece: `piece`, `format-{slug}`, `pillar-{slug}`

### Theme tags

Theme tags are creator-specific and emerge organically. Examples for a systems/automation channel:

- `automation`
- `delegation`
- `client-onboarding`
- `pricing`
- `time-management`

Add theme tags when they'll help future retrieval. Don't force every entry to have one.

### Problem slugs

From creator-foundation.md top 3 problems:
- `problem-1`
- `problem-2`
- `problem-3`
- `problem-general` (applies to all or none specifically)

### Proof type slugs

- `personal-result`
- `client-win`

Presentation formats (static-screenshot / before-after-pairing / live-clip / inline-stat-or-quote) live in the body's "Presentation format" section, not as proof types. A single proof can carry multiple presentation formats, its proof type doesn't change.

### Metaphor category slugs

- `category-food`
- `category-cars`
- `category-clothes`
- `category-sports`
- `category-travel`
- `category-other`

## File naming / slug rules

- Lowercase only
- Hyphen-separated
- Descriptive but short (3-6 words)
- No dates in the filename (dates live in frontmatter)
- No redundant prefixes (a file in `story-bank/` doesn't need `story-` in the name)

Examples:

- `banks/story-bank/airbnb-photo-swap-booked-3x.md`
- `banks/metaphor-bank/wine-tasting-early-dating.md`
- `banks/proof-bank/4m-youtube-revenue-2025.md`
- `banks/testimonial-bank/sarah-50k-ad-spend.md`
- `Content/pieces/why-systems-beat-hustle/`

Claude proposes the slug. Creator approves or overrides before saving.

## Callout conventions

Use Obsidian callouts to highlight key information. Don't overuse. One or two per entry max.

| Callout | When to use | Example |
|---------|-------------|---------|
| `> [!tip]` | Why this works / what makes it land | `> [!tip] The specific dollar amount is what made this story land.` |
| `> [!warning]` | Sensitivity notes, NDA, client permission status | `> [!warning] Client consented to stats only, no name.` |
| `> [!note]` | Context, source, timing | `> [!note] Captured after a Zoom call, 2026-04-15.` |
| `> [!success]` | Quantifiable outcome in its own block | `> [!success] Booked 3× within a week.` |
| `> [!quote]` | Verbatim client quote (testimonials) | `> [!quote] "I finally have my evenings back." Sarah, email 2026-03-20` |

## Body structure guidelines

Every entry body has clear sections, not just frontmatter. Readable in both source and preview mode.

### Story body template

```markdown
# [Story title, short, descriptive]

## Problem
[1-3 sentences in creator's voice. Specific. Emotional.]

## Action
[Concrete moves. Verbs. 1-3 sentences.]

## Outcome
[Specific result. Numbers where possible.]

> [!tip] Why this story lands
> [1-2 sentence note on what makes it work. The specific detail, the unexpected turn, etc.]

## Notes
- Captured: {date}
- Source: {how it was captured. Conversation, past video, client email, etc.}
- Related: [[related-story-or-metaphor]] (optional)
```

### Metaphor body template

```markdown
# [Metaphor name, short]

## Concept being clarified
[What abstract or confusing idea this metaphor makes clear.]

## The metaphor
[The actual comparison language, in the creator's voice. Ready to drop into a script.]

## When it lands best
[Which audiences or situations it works for.]

> [!tip] The pivot phrase
> ["So what does that actually mean for you?" or whatever transition brings it back to logic.]

## Notes
- Captured: {date}
- Everyday source: {category. Food, cars, etc.}
```

### Proof body template

```markdown
# [Proof name, what it proves]

## What it proves
[1 sentence. The claim this backs up.]

## The asset
[Path to screenshot/video/file OR inline description if not a visual.]

## Context
[When, where, who. Enough for the creator to remember.]

> [!warning] Usage rules
> [NDA status, client permission, anonymization needs. If any]

## Notes
- Captured: {date}
- Client: [[Client Name]] (if applicable)
```

### Testimonial body template

```markdown
# [Testimonial slug, client plus topic]

> [!quote] {client name or "Anonymous"}, {source} {date}
> [Verbatim quote, preserved exactly]

## Context
[What the client was responding to. Link to the piece or moment that triggered it.]

## Anonymization
{Applied / Not applied / Permissions granted}

## Notes
- Captured: {date}
- Source: [[Client Name]] (if named) via {comment/dm/email/video}
```

### Piece piece.md template

See `Content/pieces/{slug}/piece.md` (templates live in the relevant skill's assets/).

## People profile stub rule

When ANY entry mentions a client, customer, or external person by name:

1. Check `People/{Full Name}.md`
2. If missing, create a stub immediately:

```markdown
---
type: person
bucket: active-client             # or former-client, prospect, community-network, key-relationship, etc.
status: active
tags: [person, client]
---
# Full Name

> [!note] Stub created automatically when mentioned in [[source-entry|a bank entry]]. Flesh out when needed. This is the second brain pattern.
```

3. Link to the profile in the source entry: `client: "[[Full Name]]"` in frontmatter AND `[[Full Name]]` at first mention in body prose.

No exceptions. Per CLAUDE.md rule 20.

## The read-aloud test

Every entry that captures creator voice (stories, metaphor text, testimonials) must pass the read-aloud test:

**Read the entry out loud. Would the creator reword any of it?**

If yes, the entry hasn't preserved their voice correctly. Re-edit to match their actual phrasing. Claude structures, Claude never polishes the creator's words into generic prose.

## Graph view check

After any significant capture or write session, the creator should be able to:

1. Open any story entry and see backlinks to the pieces that used it
2. Open any piece's piece.md and see wikilinks to stories/metaphors/proofs used
3. Open any client's People profile and see backlinks to every story/proof/piece that mentions them
4. Filter the graph by tag (`problem-1`, `automation`, etc.) and see a meaningful cluster

If any of these don't work, something upstream broke the contract. Fix it in the skill that produced the broken entry.

## Common mistakes to avoid

- **Saving an entry without frontmatter.** Breaks every downstream query.
- **Mentioning a client without creating a People stub.** Orphan mentions don't connect to the graph.
- **Writing the script but forgetting to update the story's `used_in`.** Breaks the "where did I use this?" lookup.
- **Inventing tags per entry.** Stick to the schema, invent theme tags only when they'll be reused.
- **Over-polishing creator's voice.** Preserve phrasing. The read-aloud test is the quality bar.
- **Skipping the People profile stub because it's a hassle.** It's the connective tissue for the whole second brain. Don't skip.

## Failure modes and the update contract

The "update both sides" rule is the load-bearing mechanism of this system. When a writing skill uses a bank entry, both the piece and the bank entry must reflect that connection. The failure modes below tell a skill how to behave when something goes wrong, because silent inconsistency is worse than loud failure.

### Core principle

Never leave the graph in a silently-inconsistent state. If a write fails, the creator must know.

### What's authoritative when things conflict

- **Piece's `stories_used` / `metaphors_used` / `proofs_used`**: authoritative for "what this piece used." Primary write.
- **Bank entry's `used_in`**: reflective. It mirrors which pieces consumed this entry. Secondary write.
- **Bank entry's `status`**: reflective. Updates from `captured` to `used` when first consumed.

This means: when a writing skill uses a story, it writes the piece FIRST (primary), then updates the story's `used_in` (secondary). If the secondary write fails, the script still works. The graph just has a gap that needs manual fix.

### Failure cases

**1. Target bank entry not found by query**

The writing skill asks for a story about problem 2, bank returns nothing.

- Do NOT fabricate a story.
- Tell the creator: "No story in your bank illustrates problem 2. Do you want to capture one now, or skip this and use a different tension tool?"
- Route to vid-capture if creator wants to capture.

**2. Bank entry frontmatter malformed or missing required fields**

Skill opens a story entry, `problem_illustrated` is missing or malformed.

- Do NOT auto-fix.
- Show the creator what was found vs. what the schema expects.
- Ask: "Want me to skip this entry, or pause so you can fix it?"
- If creator picks skip, move on. If fix, pause and let creator edit.

**3. Primary write succeeds, secondary write fails**

Piece's `stories_used` updated correctly. Story's `used_in` failed to update (permission error, file lock, etc.).

- Retry the secondary write once.
- If still fails: visibly report to creator. "Script saved and piece updated. Could not update [[story-slug]]'s used_in field. You'll want to manually add `[[piece-slug]]` to its frontmatter. Graph has a gap until this is fixed."
- Never silently continue.

**4. Expected file missing**

- Piece's `piece.md` doesn't exist: create it from the piece template, proceed.
- Story/metaphor/proof bank folder doesn't exist: create the folder, proceed.
- `foundation/creator-foundation.md` missing: hard stop. Tell creator to run vid-foundation first.

**5. People profile missing when a bank entry mentions a client**

Per CLAUDE.md rule 20 and this document's People profile stub rule.

- Create the stub automatically.
- If stub creation fails (permission error on `People/` folder, etc.): report visibly and ask creator to create the profile manually before proceeding. Do NOT save the bank entry with an unresolved `[[Client Name]]` wikilink.

**6. Wikilink target doesn't exist yet**

A piece's `stories_used` contains `[[story-slug]]`, but `banks/story-bank/story-slug.md` doesn't exist.

- Verify wikilink targets BEFORE writing them. If target is missing, either:
  - Route to capture (if the intent was to create it), or
  - Flag to creator as an unresolved reference
- Do NOT write broken wikilinks silently.

**7. Bank entry was manually renamed or moved outside the skill**

Piece's `stories_used: [[old-slug]]` but file is now `new-slug.md`.

- Out of skill scope. This is a vault hygiene concern.
- If a skill encounters an unresolved wikilink during read, report it and ask creator how to resolve.
- Obsidian's built-in rename updates wikilinks if the creator uses it. Manual file renames outside Obsidian break links.

### The visibility rule

Every failure the skill encounters must surface to the creator before the session ends. A summary at session close that lists:

- Entries not found (with suggestion to capture)
- Writes that partially failed (with manual-fix instructions)
- Unresolved wikilinks (with the orphan targets listed)
- Malformed entries the creator may want to fix

No silent swallowing. The graph is the product, visibility into graph-breaking events is how we maintain it.

## How to load this reference

Every skill's SKILL.md should state near the top:

> This skill loads `knowledge/vault-integration.md` at session start. Every entry it creates must match that contract.

The skill's workflow should explicitly reference the schema it's writing (e.g., "produce a story entry per the story schema in vault-integration.md").
