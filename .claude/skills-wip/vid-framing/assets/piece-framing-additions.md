---
type: asset-template
loaded_by: vid-framing
purpose: The frontmatter fields + body sections vid-framing APPENDS to Content/pieces/{slug}/piece.md
---

# piece.md framing additions

vid-framing does NOT create piece.md. The file already exists (created at piece-folder creation by vid-intake or whatever made the folder). vid-framing APPENDS framing decisions to the existing piece.md without overwriting lifecycle fields.

## Frontmatter fields to add

Insert these fields under the existing frontmatter (after lifecycle fields like `slug`, `pillar`, `created`). Do NOT touch fields written by other skills.

```yaml
# Written by vid-framing
selected_angle: "{one-sentence angle in creator's voice}"
core_payoff: "{what the viewer gets in one sentence}"
format: case-study | short-process | deep-dive | listicle | roast | interview | news
voice_context: youtube-script   # delivery medium for voice. Default youtube-script. Set to tutorial | shorts | newsletter | linkedin | twitter | podcast | casual | talk only if this piece is genuinely that medium. Orthogonal to format. Drives which foundation/reference-pieces/{voice_context}.md the writing skills load.
goal: sales | email | views
viewer_stage: cold | warm | hot
outlier_anchor: "{outlier title} (@{channel}, {views})"   # null if experimental angle picked
anchor_confidence: high | medium | low | experimental
framed_at: {YYYY-MM-DD}
```

Update existing field:

```yaml
piece_status: framed
```

## Body sections to append

Append these three sections to the body of piece.md. If piece.md already has content from earlier phases (idea description, intake notes), append AFTER existing content. Do not delete existing body.

```markdown
## Selected Angle

{the selected angle written out in full, 1-3 sentences. Specific, concrete, in the creator's voice.}

## Why This Angle Lands

- **Iceberg fit:** {how this angle ties to creator's iceberg statement}
- **Top 3 fit:** Problem #{1|2|3|outlier}. {why this is the right problem to solve in this video}
- **Outlier evidence:** {specific anchor outlier title + channel + view count + DPV if known. For experimental angles, write "no anchor, creator gut pick" and one-line rationale.}
- **Format fit:** {why {format} is right for this angle, pull from packaging-system rotation rationale}
- **Goal fit:** {why {goal} is the right call given the angle and audience temperature}
- **Temperature fit:** {predicted viewer_stage and the four-choice score that produced it}

## Considered + Dropped Angles

> [!quote] Angle: {dropped angle 1}
> Rationale: {one-line, usually "too broad", "didn't match brain-dump material", "wrong temperature for stated goal", "anchor confidence too low"}
> Date: {YYYY-MM-DD}

> [!quote] Angle: {dropped angle 2}
> Rationale: {one-line}
> Date: {YYYY-MM-DD}

> [!quote] Angle: {dropped angle 3}
> Rationale: {one-line}
> Date: {YYYY-MM-DD}
```

The dropped angles are STICKY, future runs of vid-framing on this piece (re-framing) should NOT re-surface these dropped angles unless the creator explicitly asks.

## Append protocol

1. Read existing piece.md frontmatter. Confirm `type: piece` and `slug` match.
2. Insert framing frontmatter fields after the last lifecycle field. Preserve all existing fields untouched.
3. Update `piece_status: framed`.
4. Append `## Selected Angle`, `## Why This Angle Lands`, `## Considered + Dropped Angles` to the body. If sections already exist (re-framing case), REPLACE them with the new content; keep the dropped angles section APPEND-ONLY (never delete previous drops).
5. Write the file.

## Hard rules

- Never overwrite frontmatter fields owned by other skills (see piece.md schema in build-plan.md for the ownership matrix).
- Never delete previous "Considered + Dropped" entries. Append only.
- Never write `outlier_anchor` as a fabricated outlier. If experimental, write `null`. Real anchors only.
- Always set `framed_at` to today's date in YYYY-MM-DD format.
