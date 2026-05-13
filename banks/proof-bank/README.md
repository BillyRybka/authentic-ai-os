---
type: bank-index
bank: proof-bank
project: youtube-content-os
status: active
tags: [bank, proof, index]
---

# Proof Bank

Tangible evidence the creator can cite. Numbers, stats, credentials, before/afters, screenshots, results. Anything that answers "why should I trust this person on this topic?"

## Two simple proof types

`proof_type` is about **who the result belongs to**:

- **`personal-result`**: the creator's own number, win, or transformation
- **`client-win`**: someone else's result, captured with permission or anonymized

How the proof gets PRESENTED (static screenshot, before-after pairing, live video clip, inline stat) is a separate concern, captured in the body's "Presentation format" section. A single proof entry can have multiple presentation formats. The same client win might be cited as an inline stat in one video and shown as a before-after screenshot in another.

## What goes in this bank

- Personal results: "I made $4M from YouTube in 2025"
- Client wins: "Sarah's agency went from $50k to $200k months in 9 months"
- Before/afters: "Client's operations went from 80 hours/week to 15"
- Credentials or certifications (only when the viewer specifically cares)
- Volume stats: "I've treated 3,000+ patients in my clinic"
- Screenshots, chart grabs, video clips that function as visual evidence (asset stored in `assets/`, referenced via `asset_path` in frontmatter)

## What does NOT go here

- Stories. Narrative with tension/resolution → `story-bank/`
- Client testimonials. Quotes from other people → `testimonial-bank/` (proof is what YOU can cite about your own work, testimonials are what someone else said)
- Metaphors or analogies → `metaphor-bank/`
- Generic claims. "I'm good at this" isn't proof. Specific number, scope, and timeframe equal proof.
- Hedged claims. "I've helped a lot of people" is not proof.

## Sub-folder

- **`assets/`**: screenshots, charts, video clips referenced by proof entries. Use `asset_path` in the entry frontmatter.

## Schema

```yaml
---
type: proof
project: youtube-content-os
proof_type: client-win          # personal-result | client-win
client: "[[Client Name]]"       # only if proof_type: client-win
captured: YYYY-MM-DD
status: captured                # captured | used | archived
tags: [proof, {proof-type-slug}]
asset_path: "banks/proof-bank/assets/{file}.png"   # optional
used_in: []
---
```

## Naming

`{short-slug}.md`. Kebab-case. E.g. `sarah-50k-to-200k.md`, `4m-youtube-2025.md`, `87-percent-under-8-weeks.md`.

## Body sections

See `assets/proof-entry-template.md` in `vid-capture`. Key sections:

1. **The proof in one sentence**: the specific claim
2. **Context**: starting state, what was done, the result
3. **Presentation format**: static screenshot, before-after, live video clip, or inline stat (one or more)
4. **Evidence**: asset reference, link, or data source
5. **When to use it**: which video types this lands in

## How entries get used

1. `vid-capture` → Proof stage → file written here
2. `vid-intro` pulls proof for the Problem/Proof/Promise intro
3. `vid-segment` pulls proof as evidence inside segments
4. When used, `used_in` updates and `status` flips to `used`
