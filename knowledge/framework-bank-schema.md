---
type: reference
doc: framework-bank-schema
project: authentic-ai-os
status: active
tags: [reference, framework-bank, schema, contract]
---

# Framework bank schema

The contract for writing framework entries to `banks/framework-bank/`. The creator's OWN named frameworks, systems, and mental models. The teachable structures they have built and want to repeat on camera.

When a creator says "there are 4 types of X" or "the 3-part system I use" and that structure holds across multiple videos, it belongs here.

This bank is written by `vid-capture` (Framework stage) when that skill ships. Until then, this schema documents the intended contract. The companion build flow lives in `knowledge/framework-builder.md` (the 5-step process: dump points, ask result, circle top 3, pick shape, name it).

## What qualifies as a framework

One file per framework:

- A named system the creator built (e.g. "The 3-part Onboarding System")
- A categorization the creator uses consistently (e.g. "The 4 types of founder burnout")
- A decision model (e.g. "The Hire-or-Automate matrix")
- A staged process (e.g. "The 5 gates before you scale")
- A mental model the creator coined (e.g. "Owner math vs. Operator math")

If the creator references the same labeled structure in 3+ videos, it should be a framework entry. If they have used it once, it is an idea (keep in `content/ideas/` until tested).

## What does NOT qualify

- Frameworks other people created (Eisenhower Matrix, BENS, popular business-coaching frameworks). Those are reference material in `knowledge/` with explicit attribution. The framework-bank is creator-owned IP only.
- Acronyms Claude invents. Frameworks come from the creator's actual practice, not branding.
- Stories or anecdotes belong in `banks/story-bank/`.
- Single tactics. "Use a Calendly link" is a tactic, not a framework. Frameworks have multiple parts.
- Half-baked ideas. A framework needs (a) a name the creator actually uses, (b) named components/steps, and (c) a clear problem it solves.

## Schema

```yaml
---
type: framework
project: authentic-ai-os
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

`{framework-slug}.md`. Kebab-case, captures the framework name. For example: `3-part-onboarding-system.md`, `hire-or-automate-matrix.md`, `owner-vs-operator-math.md`.

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
- Stories: [[banks/story-bank/relevant-story]]
- Metaphors: [[banks/metaphor-bank/relevant-metaphor]]
- Proof: [[banks/proof-bank/relevant-proof]]

## Origin
[where this came from. Keeps Claude from later treating it as generic]
```

## How entries get used

1. `vid-capture` Stage F (Log path) saves frameworks when they crystallize. Standalone invocation: "I have a system called X, save it." Sub-skill invocation: per-video skills route here after inline crafting.
2. Per-video skills query this bank when a segment's principle is a framework. If a match exists, the bank entry locks the structure for that segment. If no match exists, they load `knowledge/framework-builder.md` and walk the 5-step build inline, then offer to save the result.

## Where the craft flow lives

The actual building of a framework (the 5-step process: dump points, ask result, circle top 3, pick shape, name it) lives in `knowledge/framework-builder.md`. That file is loaded inline by per-video skills when mid-write framework crafting is needed, and by `vid-capture` Stage F for shape selection and naming guidance during a Log capture.

`vid-capture` Stage F is the SAVE path only. The craft path lives in the knowledge file so the creator never has to context-switch into a sub-skill mid-write to build a framework.
