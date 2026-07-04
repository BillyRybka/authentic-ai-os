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
selected_angle: "{the picked angle, one sentence in the creator's voice}"
core_payoff: "{what the viewer walks away able to do, one sentence}"
format: short-process | case-study | roast | deep-dive | interview | news | listicle
goal: sales | emails | views
voice_context: youtube-script   # default. Set to another medium (tutorial | shorts | newsletter | linkedin | twitter | instagram | podcast | casual | talk) only if this piece genuinely is one. Drives which foundation/reference-pieces/{voice_context}.md the writing skills load.
last_updated: {YYYY-MM-DD}
```

vid-framing does not set a status. The piece stays `status: ideating` until vid-structure moves it to `drafting`. The orchestrator knows framing is done because `selected_angle` is present.

## Body section to append

```markdown
## Considered + Dropped Angles

> [!quote] Angle: {dropped angle}
> Why: {one line, e.g. "didn't match the brain-dump material", "wrong audience", "weaker than the pick"}
> Date: {YYYY-MM-DD}
```

Sticky. A re-frame must not resurface these unless the creator asks.

## Append protocol

1. Read the existing piece.md frontmatter. Confirm `type: content-piece` and the `slug` match.
2. Insert the framing frontmatter fields after the last lifecycle field. Preserve every existing field untouched.
3. Set `last_updated` to today.
4. Append `## Considered + Dropped Angles` to the body. On a re-frame, keep the section append-only (never delete previous drops).
5. Write the file.

## Hard rules

- Never overwrite frontmatter fields owned by other skills. The field-ownership map lives in `knowledge/vault-integration.md`.
- Never delete previous "Considered + Dropped" entries. Append only.
- Never fabricate. The angle and payoff trace to the brain-dump and foundation; a gap is named, never invented.
- Always set `last_updated` to today in YYYY-MM-DD.
