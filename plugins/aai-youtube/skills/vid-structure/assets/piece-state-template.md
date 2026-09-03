---
type: skill-asset
skill: vid-structure
purpose: the structure-owned fields in piece.md
---

# Piece State Template

vid-structure does not create `piece.md` and never touches its body. It updates only these frontmatter fields, preserving every other field byte for byte.

```yaml
status: drafting
segment_purposes:
  - "{exact body heading 1, in the creator's material}"
  - "{exact body heading 2}"
segments_completed: []
tension_plan:
  central_question: "{the question the viewer is holding from the title and thumbnail}"
  title_promise_segment: {1-based index of the section that pays it off}
  threads:
    - "{what one section opens and a later one closes, named by what it is}"
last_updated: {YYYY-MM-DD}
```

## Rules

- `segment_purposes`: one entry per body section, in final order, matching the `script.md` headings exactly. Material-anchored, never `point 1`. The pipeline compares `segments_completed.length` against this list to know when the body is done, so the count is the real count.
- `segments_completed: []` is written only on a first outline when the field is absent. `vid-segment` owns it afterward. Never clear it to make routing convenient.
- `tension_plan`: `central_question` and `title_promise_segment` are read by `vid-segment` and `vid-pressure-test`. `threads` holds one or two, or `[]` when the sections stand alone. Never invent one.
- `status`: advance `ideating` to `drafting`. Never regress a later status.
- `last_updated`: today, `YYYY-MM-DD`.
- On a re-structure, replace `segment_purposes` and `tension_plan`; they describe the current outline, not a history.

Worked example:

```yaml
tension_plan:
  central_question: "Which of the five is quietly keeping you as the bottleneck?"
  title_promise_segment: 3
  threads:
    - "every mistake is a version of it lives in your head; opened at mistake 1, closed at mistake 5"
```
