---
type: reference
doc: proof-bank-schema
project: authentic-ai-os
status: active
tags: [reference, proof-bank, schema, contract]
---

# Proof bank schema

The contract for writing proof entries to `banks/proof-bank/`. `vid-credibility` loads this when it writes leftover wins that did not make the locked three. `vid-bank` writes the same entry shape at its Proof stage, guided by its own proof-capture-guide.

Proof is tangible evidence the creator can cite: numbers, stats, credentials, before/afters, screenshots, results. Anything that answers "why should I trust this person on this topic?"

## Two proof types

`proof_type` is about **who the result belongs to**:

- **`personal-result`**: the creator's own number, win, or transformation
- **`client-win`**: someone else's result, captured with permission or anonymized

How the proof gets presented (static screenshot, before-after pairing, live video clip, inline stat) is a separate concern, captured in the body's "Presentation format" section. A single proof entry can carry multiple presentation formats. The same client win might be cited as an inline stat in one video and shown as a before-after screenshot in another.

## What qualifies as proof

- Personal results: "I made $4M from YouTube in 2025"
- Client wins: "Sarah's agency went from $50k to $200k months in 9 months"
- Before/afters: "Client's operations went from 80 hours/week to 15"
- Credentials or certifications (only when the viewer specifically cares)
- Volume stats: "I've treated 3,000+ patients in my clinic"
- Screenshots, chart grabs, video clips that function as visual evidence (asset stored in `banks/proof-bank/assets/`, referenced via `asset_path`)

## What does NOT qualify

- Stories. Narrative with tension/resolution belongs in `story-bank/`
- Client testimonials. Quotes from other people belong in `testimonial-bank/`. Proof is what the creator can cite about their own work; a testimonial is what someone else said.
- Metaphors or analogies belong in `metaphor-bank/`
- Generic claims. "I'm good at this" is not proof. Specific number, scope, and timeframe equal proof.
- Hedged claims. "I've helped a lot of people" is not proof.

## Schema

The proof frontmatter block lives in [[bank-contract]], alongside the other four banks. Write it from there; this file does not restate it.

## Naming

`{short-slug}.md`. Kebab-case. For example: `sarah-50k-to-200k.md`, `4m-youtube-2025.md`, `87-percent-under-8-weeks.md`.

## Body sections

1. **The proof in one sentence**: the specific claim
2. **Context**: starting state, what was done, the result
3. **Presentation format**: static screenshot, before-after, live video clip, or inline stat (one or more)
4. **Evidence**: asset reference, link, or data source
5. **When to use it**: which video types this lands in

## People links

If a proof entry names a recognizable person (a client, a guest), create or update a person stub and wikilink the name both ways, per the person-stub rule in [[bank-contract]]. Default path is `people/{Full Name}.md` inside the workspace; if the workspace `CLAUDE.md` defines a `## Path overrides` entry for person stubs, follow that override instead.
