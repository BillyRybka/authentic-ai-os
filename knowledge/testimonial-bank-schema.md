---
type: reference
doc: testimonial-bank-schema
project: authentic-ai-os
status: active
tags: [reference, testimonial-bank, schema, contract]
---

# Testimonial bank schema

The contract for writing testimonial entries to `banks/testimonial-bank/`. Other people's words about the creator, their work, or their results.

Distinct from proof: proof is the creator's own evidence (numbers, screenshots, credentials), testimonials are what clients, viewers, and partners said in their own voice.

This bank is written by `vid-capture` (Testimonial stage) when that skill ships. Until then, this schema documents the intended contract.

## What qualifies as a testimonial

One file per testimonial. Sources:

- **Comment**: YouTube, Instagram, or LinkedIn public comment
- **DM**: direct message from a client or viewer
- **Email**: client correspondence with specific praise or result language
- **Video**: client video testimonial (link and transcript, asset in `banks/proof-bank/assets/`)

Every testimonial preserves the exact wording. Do not paraphrase into "better" language. The authenticity IS the proof.

## What does NOT qualify

- Stats or numbers the creator cites themselves belong in `banks/proof-bank/`.
- Generic praise without specificity. "This was great" with no before/after or named outcome is not usable.
- Anonymous internet comments from strangers. Testimonials should be from real clients or verified viewers.
- Your own description of what the client said. Get the exact quote or drop it.

## Schema

```yaml
---
type: testimonial
project: authentic-ai-os
source: comment                 # comment | dm | email | video
client: "[[Client Name]]"       # or "Anonymous" if anonymized
anonymized: false               # true if identity removed for public use
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [testimonial, source-{slug}]
used_in: []
---
```

## Naming

`{client-slug}-{topic}.md`. Kebab-case. For example: `sarah-chen-operations.md`, `mark-patel-thumbnails.md`, `anonymous-client-pivot.md`.

## Body sections

1. **The quote (verbatim)**: exact words in blockquote
2. **Source**: screenshot path, DM date, email date, or video URL
3. **Context**: what the client was responding to
4. **Which claim does this back up?**: wikilink to matching `banks/proof-bank/` entry if applicable
5. **When to use it**

## People stub rule

Every testimonial references a real person. If `people/{Client Name}.md` does not exist, the skill auto-creates a stub. Anonymized testimonials skip the People stub but must have `anonymized: true`.

## How entries get used

1. `vid-capture` writes entries at its Testimonial stage.
2. Per-video skills pull testimonials as social proof inside intros and segments.
3. When used, `used_in` updates and `status` flips to `used`.
