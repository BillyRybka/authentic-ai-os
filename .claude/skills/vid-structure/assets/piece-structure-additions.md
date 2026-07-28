---
type: asset-template
loaded_by: vid-structure
purpose: The frontmatter fields vid-structure APPENDS to content/pieces/{slug}/piece.md
last_updated: 2026-07-28
---

# piece.md structure additions

vid-structure does not create piece.md. vid-intake created it and vid-framing appended the frame. vid-structure appends the outline decisions without touching another skill's fields.

## Frontmatter fields to add

```yaml
# Written by vid-structure
status: drafting                # advance from ideating. The outline locked, so writing has begun.
segment_purposes: ["{point 1, in the creator's own material}", "{point 2}", "{point 3}"]
segments_completed: []          # initialized empty here; vid-segment appends one label per locked segment
tension_plan: "central question: {what the viewer is holding from the title}; {which point} pays off the title; thread: {the setup one point opens and a later one closes}"
last_updated: {YYYY-MM-DD}
```

### segment_purposes

One entry per body section, in final order, matching script.md's headers. Each entry names the actual lesson in the creator's own material, never a placeholder.

- Right: `["mistake 1: no written steps", "mistake 2: client and team onboarding treated as the same thing"]`
- Wrong: `["point 1", "point 2"]`

The pipeline compares `segments_completed.length` against `segment_purposes.length` to know when the body is done, so the count has to be the real count. Never pad it to match a format's typical shape.

### tension_plan

A single quoted line carrying three things, semicolon-separated:

1. **The central question** the viewer is holding from the title.
2. **Which point pays off the title.**
3. **The thread or threads** (1 or 2, never 3 or more), each named by what it is rather than by number.

Where a piece has no thread worth naming, say so rather than inventing one: `"...; no thread, each item stands alone"`.

Worked examples:

```yaml
tension_plan: "central question: which of the five is quietly keeping you as the bottleneck; mistake 3 (the Marcus story) pays off the title; thread: every mistake is a version of it lives in your head"
```

```yaml
tension_plan: "central question: how did Marcus stop being the bottleneck in six weeks; the outcome (5 hours to 1) pays off the title; thread: it was never a trust problem"
```

vid-segment reads this to know where its segment sits in the arc, and vid-pressure-test audits the script against it. Written vaguely ("keep the tension high"), it gives both of them nothing, and each writer re-derives the arc its own way.

## Append protocol

1. Read the existing piece.md frontmatter. Confirm `type: content-piece` and that the `slug` matches the folder.
2. Add the structure fields. Preserve every existing field untouched.
3. Set `status` to `drafting` and `last_updated` to today.
4. Write the file.

On a re-structure, replace `segment_purposes` and `tension_plan` with the new plan rather than appending a second copy. They describe the current outline, not a history. Leave `segments_completed` alone: it is vid-segment's record of real work, and clearing it would tell the pipeline to rewrite finished segments. If a re-structure cut or renamed a point that vid-segment already wrote, say so in the confirm line and let the creator decide what to re-write.

## Hard rules

- Never overwrite frontmatter fields owned by other skills. The ownership map is in `knowledge/piece-contract.md`.
- Never write a field this skill does not own to unblock yourself. An absent field means its owning skill has not run; route there.
- `segment_purposes` is material-anchored. A placeholder entry means the plan is not finished.
- No body sections. vid-structure's output body is script.md; piece.md gets frontmatter only.
- Always set `last_updated` to today in YYYY-MM-DD.
