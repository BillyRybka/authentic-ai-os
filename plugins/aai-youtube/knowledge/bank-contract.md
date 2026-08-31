---
type: reference
doc: bank-contract
project: authentic-ai-os
status: active
tags: [reference, banks, schema, contract]
---

# Bank contract

The contract for the five evergreen banks: how entries are written, how a writing skill pulls one into a script, and what to do when something breaks.

Load this if you create bank entries or pull them into a piece. Shared vault rules (folder map, wikilink form, tags, naming, callouts) are in [[vault-integration]]. The piece side of a pull is in [[piece-contract]].

## Why the reciprocal write matters

When the creator sits down to write a video, the skill has to find the right story for this video's point, find the matching proof or metaphor, write the script with it in, and update BOTH the script AND the source bank entry to show the connection.

Skip the second write and stories sit in `banks/story-bank/` invisible to the query that needed them, scripts pull material but never link back, and "where did I use this?" becomes unanswerable. The graph is the product. That is what this contract protects.

## Frontmatter schemas

Every entry carries frontmatter matching one of these. Populate everything that applies.

### Story

Location: `banks/story-bank/{slug}.md`

```yaml
---
type: story
project: authentic-ai-os
story_type: client              # client | own | viewer
illustrates: without systems and delegation, you drown in client work and never get time to grow
themes: [delegation, systems, time]    # open vocabulary, the angles this lesson touches
client: "[[Client Name]]"       # wikilink to people/ profile, only for client stories
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [story, {theme-slug}]
used_in: []                     # populated by writing skills with [[piece-slug]] entries
---
```

### Metaphor

Location: `banks/metaphor-bank/{slug}.md`

```yaml
---
type: metaphor
project: authentic-ai-os
concept: "short concept name"   # what the metaphor is clarifying (the metaphor's matching key)
category: everyday              # food | cars | clothes | sports | travel | other
visual: false                   # true if the metaphor depends on a prop/graphic to land, false if pure speech works
themes: [delegation, systems]   # open vocabulary, the angles this metaphor touches
captured: YYYY-MM-DD
status: captured
tags: [metaphor, category-{slug}, visual-metaphor OR non-visual-metaphor, {theme-slug}]
used_in: []
---
```

### Proof

Location: `banks/proof-bank/{slug}.md`

`proof_type` is about **who the result belongs to** (creator or client). How the proof is presented (static screenshot, before-after pairing, live video clip, inline stat) is captured separately in the body's "Presentation format" section. A single proof can carry multiple formats. What qualifies as proof, and what belongs in another bank instead, is in [[proof-bank-schema]].

```yaml
---
type: proof
project: authentic-ai-os
proof_type: client-win          # personal-result | client-win
illustrates: delegating one task gave back a full day every week
themes: [delegation, time]      # open vocabulary, the angles this proof backs
client: "[[Client Name]]"       # wikilink, only if client proof
captured: YYYY-MM-DD
status: captured
tags: [proof, {proof-type-slug}]
asset_path: "banks/proof-bank/assets/{file}.png"   # optional, for screenshots/videos
used_in: []
---
```

### Testimonial

Location: `banks/testimonial-bank/{slug}.md`. A separate top-level bank: testimonials are other people's words, distinct from proof, which is the creator's own evidence.

```yaml
---
type: testimonial
project: authentic-ai-os
source: comment                 # comment | dm | email | video
illustrates: the system kept running after the client stepped back
themes: [delegation, systems]   # open vocabulary, the angles this quote backs
client: "[[Client Name]]"       # or "Anonymous" if anonymized
anonymized: false               # true if client identity removed
captured: YYYY-MM-DD
status: captured
tags: [testimonial, source-{slug}]
used_in: []
---
```

### Framework

Location: `banks/framework-bank/{slug}.md`

Frameworks are the creator's OWN named systems, structures, and mental models. The teachable patterns they repeat across videos. Third-party frameworks do NOT go here; they live in `knowledge/` or `resources/references/` with attribution.

```yaml
---
type: framework
project: authentic-ai-os
name: "The 3-part Onboarding System"
framework_type: process         # process | categorization | decision-model | mental-model
problem_it_solves: "short description of the problem this framework addresses"
themes: [onboarding, delegation]   # open vocabulary, the angles this framework touches
components: ["step-1", "step-2", "step-3"]
maturity: active                # draft | active | retired
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [framework, {framework-type-slug}, {domain-slug}]
used_in: []                     # populated by writing skills
---
```

## What an entry illustrates

Story, proof, and testimonial entries carry an `illustrates:` line: the lesson the entry proves, as plain cause and effect, in the creator's voice (`illustrates: without systems and delegation, you drown in client work and never get time to grow`). Metaphors use `concept:` and frameworks use `problem_it_solves:` for the same matching role.

Write it the way the creator would say it out loud, unquoted unless a colon forces quotes. Add open `themes:` for indexing. There are no fixed problem categories: an entry surfaces for any segment whose point it fits, and the same entry can be reused across many.

## The update-both-sides rule

**Non-negotiable.** When a writing skill uses a story (or proof, metaphor, testimonial, framework):

1. Write the content into the script, in the creator's voice, via vid-intro / vid-segment / vid-ending
2. In the piece's `piece.md`, append the wikilink: `stories_used: ["[[story-bank/airbnb-photo-swap]]"]`
3. In the entry's frontmatter, append the piece wikilink: `used_in: ["[[video-slug]]"]`
4. In the entry's frontmatter, set `status: used`

Both sides. Always. Same rule for all five types: `metaphors_used`, `proofs_used`, `testimonials_used`, `frameworks_used` each get the piece-side append AND the bank-side `used_in`.

**Write order and authority.** The piece is the primary write, the bank entry is reflective:

- Piece's `*_used` arrays: authoritative for "what this piece used." Write first.
- Bank entry's `used_in`: mirrors which pieces consumed the entry. Write second.
- Bank entry's `status`: reflective. Moves from `captured` to `used` on first consumption.

If the secondary write fails, the script still works and the graph has a gap that needs a manual fix. That is why the order is fixed, and why a failed secondary write is reported rather than swallowed.

## Person stubs

**Stubs are created at bank-capture time, never at intake.**

`vid-intake` captures names exactly as the creator said them, in plain prose, with no wikilink and no stub. A name in a raw dump is material, not yet an entity: the creator names people who never become entries, and a wikilink written before its target exists is a broken link. The moment that material becomes a bank entry, the skill writing that entry creates the profile.

So: when ANY bank entry names a client, customer, or external person:

1. Check `people/{Full Name}.md`
2. If missing, create the stub immediately:

```markdown
---
type: person
bucket: active-client             # or former-client, prospect, community-network, key-relationship, etc.
status: active
tags: [person, client]
---
# Full Name

> [!note] Stub created automatically when mentioned in [[source-entry|a bank entry]]. Flesh out when needed.
```

3. Link both ways: `client: "[[Full Name]]"` in the entry's frontmatter AND `[[Full Name]]` at first mention in body prose.

Never save a bank entry with an unresolved `[[Client Name]]` wikilink. Default path is `people/{Full Name}.md`; if the workspace `CLAUDE.md` defines a `## Path overrides` entry for person stubs, follow that override instead.

## Body structure

Every entry body has clear sections, not just frontmatter. Readable in source and preview mode.

### Story

```markdown
# [Story title, short, descriptive]

## Problem
[1-3 sentences in creator's voice. Specific. Emotional.]

## Action
[Concrete moves. Verbs. 1-3 sentences.]

## Outcome
[Specific result. Numbers where possible.]

> [!tip] Why this story lands
> [1-2 sentences on what makes it work. The specific detail, the unexpected turn.]

## Notes
- Captured: {date}
- Source: {how it was captured. Conversation, past video, client email.}
- Related: [[story-bank/related-slug]] (optional)
```

### Metaphor

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

### Proof

```markdown
# [Proof name, what it proves]

## What it proves
[1 sentence. The claim this backs up.]

## The asset
[Path to screenshot/video/file OR inline description if not a visual.]

## Context
[When, where, who. Enough for the creator to remember.]

> [!warning] Usage rules
> [NDA status, client permission, anonymization needs. If any.]

## Notes
- Captured: {date}
- Client: [[Client Name]] (if applicable)
```

### Testimonial

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

## Failure modes

Never leave the graph in a silently inconsistent state. If a write fails, the creator must know.

**1. No bank entry matches the query.** The skill asks for a story illustrating this segment's point and the bank returns nothing.
- Do NOT fabricate one.
- Tell the creator: "No story in your bank illustrates this point yet. Want to capture one now, or skip this and use a different tension tool?"
- Route to `vid-bank` if they want to capture.

**2. Entry frontmatter malformed or missing required fields.**
- Do NOT auto-fix.
- Show the creator what was found against what the schema expects.
- Ask whether to skip the entry or pause so they can fix it.

**3. Primary write succeeds, secondary write fails.** The piece's `stories_used` updated, the entry's `used_in` did not (permission error, file lock).
- Retry the secondary write once.
- If it still fails, report visibly: "Script saved and piece updated. Could not update [[story-bank/slug]]'s used_in field. Add `[[piece-slug]]` to its frontmatter manually. The graph has a gap until then."
- Never silently continue.

**4. Expected file missing.**
- A bank folder does not exist: create the folder, proceed.
- `content/pieces/{slug}/piece.md` does not exist: create it per [[piece-contract]], proceed.
- `foundation/iceberg.md` or `foundation/avatar.md` missing: hard stop. Tell the creator to run `/foundation` first.

**5. Person stub creation fails** (permission error on `people/`).
- Report visibly and ask the creator to create the profile manually before proceeding.
- Do NOT save the entry with an unresolved `[[Client Name]]` wikilink.

**6. Wikilink target does not exist yet.** A piece's `stories_used` names an entry with no file behind it.
- Verify targets BEFORE writing them. If missing, either route to capture (if creating it was the intent) or flag it as unresolved.
- Do NOT write broken wikilinks silently.

**7. Entry renamed or moved outside the skill.** The piece points at `[[story-bank/old-slug]]`, the file is now `new-slug.md`.
- Out of skill scope; this is vault hygiene. Report the unresolved link and ask the creator how to resolve.
- Obsidian's built-in rename updates wikilinks. Manual renames outside Obsidian break them.

### The visibility rule

Every failure surfaces to the creator before the session ends. At session close, list entries not found (with a capture suggestion), partial writes (with manual-fix instructions), unresolved wikilinks (with the orphan targets), and malformed entries worth fixing.

No silent swallowing.
