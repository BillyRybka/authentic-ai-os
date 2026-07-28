---
type: asset-template
loaded_by: vid-framing
purpose: The frontmatter fields + body section vid-framing APPENDS to content/pieces/{slug}/piece.md
---

# piece.md framing additions

vid-framing does NOT create piece.md. vid-intake created it. vid-framing appends its framing decisions to the existing file without touching another skill's fields.

## Frontmatter fields to add

Insert under the existing frontmatter (after the lifecycle fields `slug`, `pillar`, `created`, `status`). Do not touch fields owned by other skills.

```yaml
# Written by vid-framing
selected_angle: "{one clean sentence naming what the video argues, in the creator's voice. Argument-shaped, not headline-shaped: it says what is true and what it costs, it does not sell the click. No explanation clause, no colon-summary, no TODO text inside}"
core_payoff: "{a direct instruction spoken to the viewer, second person: 'pick the one task only you can do this week and write the steps down'. Never 'the viewer does X'}"
format: short-process | case-study | roast | deep-dive | interview | news | listicle
goal: sales | emails | views
voice_context: youtube-script   # default. Set to another medium (tutorial | shorts | newsletter | linkedin | twitter | instagram | podcast | casual | talk) only if this piece genuinely is one. Drives which foundation/reference-pieces/{voice_context}.md the writing skills load.
last_updated: {YYYY-MM-DD}
```

vid-framing does not set a status. The piece stays `status: ideating` until vid-structure moves it to `drafting`. The orchestrator knows framing is done because `selected_angle` is present.

## Body sections to append

The read goes on disk. It is the ore vid-title, vid-intro, and vid-structure pull from, and if it only lives in the conversation it is gone by the next session. Four short lines, no prose.

```markdown
## The Read

- **Viewer:** {the one person, localized to this topic, not the generic avatar}
- **Believes:** {what they hold to be true about it, in plain words}
- **Costs them:** {what that belief is costing, or the bill they cannot see yet}
- **Payoff:** {what they walk away able to do, second person}
```

On a re-frame, replace this section rather than appending a second copy. It describes the current frame, not a history.

```markdown
## Considered + Dropped Angles

> [!quote] Angle: {dropped angle}
> Why: {one line, e.g. "didn't match the brain-dump material", "wrong audience", "weaker than the pick"}
> Date: {YYYY-MM-DD}
```

Sticky. A re-frame must not resurface these unless the creator asks.

If the creator withheld proof (a number, a client detail, a bank entry they have not captured), add a one-line TODO in the body so the gap is flagged. Keep it OUT of `selected_angle` and `core_payoff`:

```markdown
> [!todo] Proof gap: {what is missing}, mark it and pull it later. {YYYY-MM-DD}
```

## Append protocol

1. Read the existing piece.md frontmatter. Confirm `type: content-piece` and the `slug` match.
2. Insert the framing frontmatter fields after the last lifecycle field. Preserve every existing field untouched.
3. Set `last_updated` to today.
4. Write `## The Read` to the body. On a re-frame, replace the existing section.
5. Append `## Considered + Dropped Angles` to the body. On a re-frame, keep the section append-only (never delete previous drops). Add any proof-gap `> [!todo]` lines here too.
6. Write the file.

## Hard rules

- Never overwrite frontmatter fields owned by other skills. The field-ownership map lives in `knowledge/piece-contract.md`.
- Never delete previous "Considered + Dropped" entries. Append only. `## The Read` is the one section that gets replaced instead.
- Never fabricate. The angle, the read, and the payoff trace to the brain-dump and foundation; a gap is named, never invented.
- Keep `selected_angle` and `core_payoff` clean: one voiced line each (the payoff in second person), no embedded TODOs. Withheld proof goes in a body `> [!todo]`.
- `selected_angle` is never a title. If it reads like one, rewrite it as the argument underneath and let vid-title do the selling.
- Always set `last_updated` to today in YYYY-MM-DD.
