---
type: bank-index
bank: framework-bank
project: youtube-content-os
status: active
tags: [bank, framework, index]
---

# Framework Bank

The creator's OWN named frameworks, systems, and mental models. The teachable structures they've built and want to repeat on camera. When a creator says "there are 4 types of X" or "the 3-part system I use" and that structure holds across multiple videos — it belongs here.

## What goes in this bank

One file per framework:

- A named system the creator built (e.g. "The 3-part Onboarding System")
- A categorization the creator uses consistently (e.g. "The 4 types of founder burnout")
- A decision model (e.g. "The Hire-or-Automate matrix")
- A staged process (e.g. "The 5 gates before you scale")
- A mental model the creator coined (e.g. "Owner math vs. Operator math")

If the creator references the same labeled structure in 3+ videos, it should be a framework entry. If they've used it once, it's an idea — keep it in `Content/ideas/content-ideas.md` until tested.

## What does NOT go here

- **Frameworks other people created.** Popular business-coaching frameworks, the Eisenhower Matrix, BENS — those are reference material in `knowledge/` or third-party reference folders with explicit attribution. The framework-bank is creator-owned IP only.
- **Acronyms Claude invents.** Frameworks come from the creator's actual practice, not branding.
- **Stories or anecdotes** → `story-bank/`
- **Single tactics.** "Use a Calendly link" is a tactic, not a framework. Frameworks have multiple parts.
- **Half-baked ideas.** A framework needs (a) a name the creator actually uses, (b) named components/steps, (c) a clear problem it solves.

## Schema

```yaml
---
type: framework
project: youtube-content-os
name: "The 3-part Onboarding System"
framework_type: process         # process | categorization | decision-model | mental-model
problem_it_solves: "short description"
components: ["step-1", "step-2", "step-3"]
maturity: active                # draft | active | retired
captured: YYYY-MM-DD
status: captured
tags: [framework, {framework-type-slug}, {domain-slug}]
used_in: []
---
```

## Naming

`{framework-slug}.md` — kebab-case, captures the framework name. e.g. `3-part-onboarding-system.md`, `hire-or-automate-matrix.md`, `owner-vs-operator-math.md`.

## Body sections

```markdown
# {Framework Name}

## What problem does this solve?
[creator's voice — what specific problem this addresses]

## The components
1. **{Component 1}** — what it is, why it matters
2. **{Component 2}** — same
3. **{Component 3}** — same

## When to use it
- Which video types / pillars
- Which segments of the audience

## Related assets
- Stories: [[story-bank/relevant-story]]
- Metaphors: [[metaphor-bank/relevant-metaphor]]
- Proof: [[proof-bank/relevant-proof]]

## Origin
[where this came from — keeps Claude from later treating it as generic]
```

## How entries get used

1. Currently manual — the creator authors entries when a framework crystallizes
2. `vid-framing` / `vid-structure` pull frameworks when a video is structured around a named system
3. `vid-segment` references frameworks when explaining complex systems, with related stories/metaphors/proof pulled alongside
4. When used, `used_in` updates and `status` flips to `used`

## Note on vid-capture

`vid-capture` currently has 4 stages (Story / Metaphor / Proof / Testimonial). Framework entries are manually created until a Framework stage is added — frameworks tend to crystallize from existing stories/proofs, so they're usually authored deliberately rather than captured on the fly.
