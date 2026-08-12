---
name: vid-thumbnail-v2
description: Create exactly three distinct, truthful thumbnail-text tests that complete one locked YouTube title without rewriting the title or reframing the video. Use after vid-title-v2 when a creator asks for thumbnail text, thumbnail copy, three thumbnail options, or a thumbnail package for a selected video. Read the selected piece and source material plus relevant packaging evidence privately, then save all three approved tests to piece.md. Text only, never visual direction.
---

# Write three thumbnail-text tests

Package one locked title. Do not rewrite the title, repair the frame, or expand the video's promise.

Keep evidence gathering, generation, and filtering private. The creator sees three useful tests, not the process.

## Select the locked piece

Require a specific video or `content/pieces/{slug}`. If none is selected, ask which video needs thumbnails without scanning the vault.

Read `content/pieces/{slug}/piece.md`. Require a locked `title`, `frame`, and `core_payoff`. If the title is missing, route to `vid-title-v2`. If the frame or payoff is missing, route to `vid-framing`. Do not fill another skill's field.

Use these locked decisions as boundaries:

- `title`
- `frame` and `core_payoff`
- `goal`
- `## The Read`: Target, Transformation, and Stakes
- any explicit `must_not_become`

Older pieces may lack `goal` or `## The Read`. Continue from the locked fields and source material that exist.

Read the selected complete `script.md` when present. Otherwise read `brain-dump.md`. Read the other only when needed to resolve provenance or a material gap. The script does not override the locked frame.

## Lock factual support privately

List only the claims supported by the selected piece, script, brain dump, or creator-provided context. This includes figures, timeframes, tools, names, results, proof, mechanisms, commands, and belief clashes.

Never invent, round, strengthen, merge, or borrow a fact from an example or bank. Every option must be true and fulfillable by the video.

## Use packaging evidence quietly

When present, inspect `foundation/packaging-system.md` and relevant entries in `banks/packaging-bank/` selectively. Use proven creator patterns before generic judgment. Consult title-bank or pattern-bank evidence only when it helps interpret the locked title's winning shape or find a complementary beat.

Treat bank examples as evidence for structure, never as evidence for this video's facts. Do not show research notes, pattern names, receipts, metrics, or files read unless the creator asks.

If packaging evidence is absent, continue with sound thumbnail judgment. Mention the gap only if it prevents a strong set.

## Generate and filter privately

Generate widely enough to find three different packaging hypotheses. Use `knowledge/thumbnail-text-patterns.md` as private calibration when available.

Make the title and thumbnail work as one package. Each thumbnail must add a compatible second beat, such as proof, consequence, contradiction, mechanism, or a specific unresolved tension. Cut any option that restates the title, repeats its key idea, or competes with its tone.

Keep each option:

- brief enough to read at a glance, usually two to four words and never more than five
- concrete and specific to this video
- focused on one idea
- supported by the factual lock list
- intriguing without pre-delivering the whole payoff
- free of generic hype, vague buzzwords, stacked claims, and visual-dependent language

The three options must test meaningfully different tensions or packaging hypotheses. Cosmetic wording, punctuation, casing, or synonym changes do not count as separate tests. Every video gets three thumbnails because each should produce a different learning signal.

Use compatible shape labels when saving: `cognitive-dissonance`, `number-hero`, `named-system`, `single-word`, or `imperative-command`. Choose the label that best describes the actual test. Distinct hypotheses may share a shape only when they create clearly different learning signals.

If the evidence cannot support three strong hypotheses, do not pad the set. Say briefly what is missing, such as a concrete receipt, a genuine belief clash, or a named mechanism, and what source or creator answer would strengthen it. Do not reframe the video or propose title alternatives.

## Present only the three tests

Show the locked title once, followed by exactly three numbered choices. Add one short practical explanation of what each tests. Recommend an order or test hypothesis only when it helps the creator make a decision.

Use this shape:

> **Title:** "{locked title}"
>
> 1. **"{thumbnail text}"**: Tests whether {brief viewer-facing hypothesis}.
> 2. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 3. **"{thumbnail text}"**: Tests whether {different hypothesis}.

Do not expose rejected drafts, scoring, lock lists, bank research, pattern labels, internal checks, or workflow narration. Do not add title alternatives or visual advice. Ask for approval of the three-option set, not for one winning pick.

## Save all three after approval

After the creator approves the set:

1. Re-read the current `content/pieces/{slug}/piece.md` and confirm the content-piece type and selected slug.
2. Set `thumbnail_text` to exactly the three approved texts, verbatim and in presented order.
3. Set `thumbnail_shape` to exactly three matching shape values in the same order.
4. Set `last_updated` to today's date in `YYYY-MM-DD`.
5. Preserve every other frontmatter field and every body line unchanged.
6. Re-read the saved file and verify that only `thumbnail_text`, `thumbnail_shape`, and `last_updated` changed.

Use aligned YAML arrays:

```yaml
thumbnail_text: ["{option 1}", "{option 2}", "{option 3}"]
thumbnail_shape: [{shape 1}, {shape 2}, {shape 3}]
```

Replace earlier thumbnail arrays if present. Never write rationale, candidates, research, or test results to disk.

After saving, reply only:

> Three thumbnail-text tests saved to piece.md.

Stop. Do not hand off, explain the fields, or add visual direction.
