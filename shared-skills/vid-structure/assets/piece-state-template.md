---
type: skill-asset
skill: vid-structure-v2
purpose: canonical structure-owned state for piece.md
---

# Piece State Template

Vid-structure-v2 updates existing frontmatter only. It does not create `piece.md` and does not change the piece body.

```yaml
status: drafting
segment_purposes:
  - "{exact material-anchored body heading}"
  - "{exact next body heading}"
segments_completed: []
tension_plan:
  central_question: "{main question raised by the locked title and thumbnail package}"
  reason_to_continue: "{what remains meaningfully unresolved as the body advances}"
  payoff_section: "{exact section label that fulfills the package's central promise}"
  threads:
    - name: "{only when a real cross-section dependency exists}"
      opens: "{exact section label}"
      closes: "{exact later section label}"
last_updated: {YYYY-MM-DD}
```

Use `threads: []` when no cross-section thread helps the piece.

## Ownership and write rules

- V2 owns `segment_purposes` and `tension_plan`.
- V2 advances `status` from `ideating` to `drafting`. It never regresses a later status.
- V2 initializes `segments_completed: []` only on the first outline when the field is absent. `vid-segment` owns later additions.
- `last_updated` is shared and moves to today after a successful write.
- Preserve every other frontmatter field and the complete body byte for byte.
- Never write bank-use arrays during planning.

Every `segment_purposes` entry must exactly match one body heading, in order. Every `payoff_section`, `opens`, and `closes` value must exactly match one of those entries. Threads are optional, but their boundaries are not.

The only exception is a re-structure of completed V1 prose whose protected completion identifiers already differ from headings. Follow `references/restructure-safety.md`; never use the exception for new sections.
