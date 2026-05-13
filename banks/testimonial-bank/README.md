---
type: bank-index
bank: testimonial-bank
project: youtube-content-os
status: active
tags: [bank, testimonial, index]
---

# Testimonial Bank

Other people's words about the creator, their work, or their results. Distinct from proof: proof is the creator's own evidence (numbers, screenshots, credentials), testimonials are what clients, viewers, and partners said in their own voice.

## What goes here

One file per testimonial. Sources:

- **Comment**: YouTube, Instagram, or LinkedIn public comment
- **DM**: direct message from a client or viewer
- **Email**: client correspondence with specific praise or result language
- **Video**: client video testimonial (link and transcript, asset in `banks/proof-bank/assets/`)

Every testimonial preserves the exact wording. Do not paraphrase into "better" language. The authenticity IS the proof.

## What does NOT go here

- Stats or numbers the creator cites themselves → `proof-bank/`
- Generic praise without specificity. "This was great" with no before/after or named outcome is not usable.
- Anonymous internet comments from strangers. Testimonials should be from real clients or verified viewers. Credibility is weak otherwise, and the People stub rule breaks.
- Your own description of what the client said. Get the exact quote or drop it.

## Schema

```yaml
---
type: testimonial
project: youtube-content-os
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

`{client-slug}-{topic}.md`. Kebab-case. E.g. `sarah-chen-operations.md`, `mark-patel-thumbnails.md`, `anonymous-client-pivot.md`.

## Body sections

See `assets/testimonial-entry-template.md` in `vid-capture`. Key sections:

1. **The quote (verbatim)**: exact words in blockquote
2. **Source**: screenshot path, DM date, email date, or video URL
3. **Context**: what the client was responding to
4. **Which claim does this back up?**: wikilink to matching `proof-bank/` entry if applicable
5. **When to use it**

## People stub rule

Every testimonial references a real person. If `People/{Client Name}.md` doesn't exist, the skill auto-creates a stub. Anonymized testimonials skip the People stub but must have `anonymized: true`.

## How entries get used

1. `vid-capture` → Testimonial stage → file written here
2. `vid-intro` may pull a testimonial for credibility
3. `vid-segment` pulls testimonials as social proof inside a segment
4. When used, `used_in` updates and `status` flips to `used`
