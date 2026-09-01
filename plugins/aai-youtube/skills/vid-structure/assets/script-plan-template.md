---
type: skill-asset
skill: vid-structure
purpose: canonical first-write shape for script.md
---

# Script Plan Template

Use this only for the first structure write. A re-structure with existing prose follows `references/restructure-safety.md`.

```markdown
---
type: script
piece: "[[content/pieces/{piece-slug}/piece|{piece-slug}]]"
status: outlined
tier: 1
last_refreshed: {YYYY-MM-DD}
---

# {locked title}

> Writer-ready plan. vid-intro fills Intro, vid-segment writes each body section, and vid-ending fills Ending.

## Intro
*vid-intro fills this.*

## {material-anchored section label}
**Job:** {what this section must accomplish}
**Sources:**
- {exact source and anchor}
**Takeaway:** {what the viewer understands, feels, decides, or does}
**{Optional decision}:** {only when useful: Story, Example, Demonstration, Metaphor, Framework, Evidence, Action, Dependency, Story beat, Diagnosis, Fix, Known context, Target story, Target insight, Follow-up trigger, Claim source, Point of view, Arc}

## {next section label}
{same shared core, with only useful optional decisions}

## Ending
*vid-ending fills this. CTA follows piece.md goal.*

## To build
- (empty: no critical planning gaps remain)

## Production follow-ups
- [ ] {known acquisition task that cannot change the prose plan}

<!--
CUTS (sticky across re-structure runs):
- {material anchor}: {reason} [repeated / off-angle / unsupported / off-format / merged]
-->
```

## Rules

- V2 owns this frontmatter only on first write. Once another skill has written prose, re-structure preserves it until the shared contract assigns later ownership.
- Each body heading must exactly match its `segment_purposes` entry. The **Job** line carries the fuller purpose.
- The `piece` wikilink must target the selected piece file that was already validated. Do not write a bare slug link unless that vault resolves it to the same file.
- **Job**, **Sources**, and **Takeaway** are required. Optional lines are omitted when unused.
- Use a source list when a section draws from more than one place. Do not write a vague source such as `the dump` or `a bank story`.
- `## To build` must be empty at writer-ready handoff. A critical planning gap blocks the save.
- First-write verification must confirm both the `## Intro` and `## Ending` stubs remain present.
- Omit `## Production follow-ups` when none exist.
- Keep planning fields concise. Do not write body prose in them.
- Do not add inline tension notes to every section. Cross-section state lives once in `piece.md`. Use an **Arc** line only when the section opens or closes a stored thread or fulfills the package payoff.
