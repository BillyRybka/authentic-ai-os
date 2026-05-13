---
type: bank-index
bank: framework-bank
project: youtube-content-os
status: active
tags: [bank, framework, index]
---

# Framework Bank

The creator's OWN named frameworks, systems, and mental models. The teachable structures they've built and want to repeat on camera. When a creator says "there are 4 types of X" or "the 3-part system I use" and that structure holds across multiple videos, it belongs here.

## What goes in this bank

One file per framework:

- A named system the creator built (e.g. "The 3-part Onboarding System")
- A categorization the creator uses consistently (e.g. "The 4 types of founder burnout")
- A decision model (e.g. "The Hire-or-Automate matrix")
- A staged process (e.g. "The 5 gates before you scale")
- A mental model the creator coined (e.g. "Owner math vs. Operator math")

If the creator references the same labeled structure in 3+ videos, it should be a framework entry. If they've used it once, it's an idea. Keep it in `Content/ideas/content-ideas.md` until tested.

## What does NOT go here

- Frameworks other people created. Popular business-coaching frameworks, the Eisenhower Matrix, BENS. Those are reference material in `knowledge/` or third-party reference folders with explicit attribution. The framework-bank is creator-owned IP only.
- Acronyms Claude invents. Frameworks come from the creator's actual practice, not branding.
- Stories or anecdotes → `story-bank/`
- Single tactics. "Use a Calendly link" is a tactic, not a framework. Frameworks have multiple parts.
- Half-baked ideas. A framework needs (a) a name the creator actually uses, (b) named components/steps, and (c) a clear problem it solves.

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

`{framework-slug}.md`. Kebab-case, captures the framework name. E.g. `3-part-onboarding-system.md`, `hire-or-automate-matrix.md`, `owner-vs-operator-math.md`.

## Body sections

```markdown
# {Framework Name}

## What problem does this solve?
[creator's voice. What specific problem this addresses]

## The components
1. **{Component 1}**: what it is, why it matters
2. **{Component 2}**: same
3. **{Component 3}**: same

## When to use it
- Which video types / pillars
- Which segments of the audience

## Related assets
- Stories: [[story-bank/relevant-story]]
- Metaphors: [[metaphor-bank/relevant-metaphor]]
- Proof: [[proof-bank/relevant-proof]]

## Origin
[where this came from. Keeps Claude from later treating it as generic]
```

## How entries get used

1. `vid-capture` Stage F (Log path) saves frameworks when they crystallize. Standalone invocation: "I have a system called X, save it." Sub-skill invocation: vid-segment routes here after inline crafting.
2. `vid-segment` queries this bank when the segment's logic brick is a framework. If a match exists, the bank entry locks the structure for that segment. If no match exists, vid-segment loads `knowledge/framework-builder.md` and walks the 5-step build inline (dump → result → top 3 → shape → name), then offers to save the result via vid-capture Stage F.
3. `vid-framing` may reference frameworks at the angle-locking stage when a video is structured around a named system.
4. When used, `used_in` updates and `status` flips to `used`.

## Where the craft flow lives

The actual building of a framework (the 5-step process: dump points → ask result → circle top 3 → pick shape → name it) lives in `knowledge/framework-builder.md`. That file is loaded inline by vid-segment when mid-write framework crafting is needed, and it's loaded by vid-capture Stage F for shape selection and naming guidance during a Log capture.

vid-capture Stage F is the SAVE path only. The craft path lives in the knowledge file so the creator never has to context-switch into a sub-skill mid-write to build a framework.
