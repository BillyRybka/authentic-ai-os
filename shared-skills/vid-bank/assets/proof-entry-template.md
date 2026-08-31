---
type: proof
project: authentic-ai-os
proof_type: client-win
illustrates: delegating one task gave back a full day every week
themes: [delegation, time]
client: "[[Client Name]]"
captured: YYYY-MM-DD
status: captured
tags: [proof, client-win, delegation, time]
asset_path: "banks/proof-bank/assets/{file}"
used_in: []
---

# {Proof name, what it proves at a glance}

## What it proves

{One sentence. The claim this proof backs up.}

## The asset

{Path to screenshot, video, or file at `banks/proof-bank/assets/{file}`. OR inline description if the proof is a stat or quote with no separate asset file.}

## Presentation format

{One or more of: static-screenshot / before-after-pairing / live-clip / inline-stat-or-quote. A single proof can have multiple formats. Add new formats over time as you collect them. The proof_type never changes, but the ways of showing it can grow.}

## Context

{When, where, who. Enough for the creator to remember why this matters in six months.}

> [!warning] Usage rules
> {NDA status, client permission, anonymization scope. Omit this callout if there are no restrictions.}

## Notes

- Captured: {date}
- Client: {wikilink to People profile if applicable}
- Related: {optional wikilinks to related stories or testimonials}

---

## Filling instructions (delete this section before save)

**Frontmatter fields:**

- `proof_type`: one of `personal-result` or `client-win` (about who the result belongs to, not how it's presented)
- `illustrates`: one short line for the point this proof backs, plain cause and effect, in the creator's voice. Unquoted unless a colon forces quotes.
- `themes`: open list of the angles this proof backs (e.g., `delegation`, `time`). Multi-value.
- `client`: wikilink to `people/{Full Name}.md`. Only present for proof involving a client. Remove the line for personal-result proof.
- `captured`: ISO date
- `status`: starts `captured`
- `tags`: at minimum `proof` and the proof-type slug (`personal-result` or `client-win`), plus the theme slugs.
- `asset_path`: path to the asset file in `banks/proof-bank/assets/`. Omit if proof is inline.
- `used_in`: starts `[]`

**Body rules:**

- "What it proves" is one sentence. If it takes more, the proof is too vague.
- "The asset" lists the file path OR the inline stat/quote.
- "Context" grounds the proof in a time, place, and person.
- `> [!warning] Usage rules` callout is required if anonymization, NDA, or permission scope applies. Omit if there are none.

**Client mention rule:** if the proof involves a client named, check `people/{Full Name}.md`. If missing, create it using `people-stub-template.md`.

**Anonymization default:** when in doubt, anonymize. Use "Anonymous" in `client:` until permission is verified.
