---
name: vid-title
description: Write, sharpen, and recommend truthful YouTube title options for one selected video whose frame and core payoff are already locked. Use after framing when a creator asks for title ideas, finalists, a recommendation, or to approve and save a title. Study relevant title, pattern, and power-word bank evidence privately, keep the approved frame closed, and write only title and last_updated after approval. Not for reframing, thumbnails, hooks, outlines, other platforms, or topic ideation.
---

# Write the video title

Package one locked YouTube video into a short choice set. Find the most compelling natural expression of what the video truly delivers. Keep the creative work private.

## Start from one locked video

Require a selected video or `content/pieces/{slug}`. If none is selected, ask which video to title without scanning the vault.

Read these selected-piece files silently when present:

1. `content/pieces/{slug}/piece.md`
2. `content/pieces/{slug}/brain-dump.md`
3. `content/pieces/{slug}/script.md`

Do not title material marked as incomplete. Require `frame` and `core_payoff`; route missing fields to `vid-framing`. Once they exist, framing is closed. Do not reinterpret, repair, or reopen it.

Treat the frame, core payoff, goal, `## The Read`, `must_not_become`, and factual direction as the boundary. Older pieces may lack some newer fields; continue from the locked material that exists.

## Find the title material

Privately identify the video's core value and its usable ingredients: the viewer, promised change, stakes, distinctive idea, proof, facts, and language the creator can honestly say. A title may intensify the pull of those ingredients, but may not change the audience, delivery, or claim.

Use only supported names, numbers, timeframes, results, comparisons, authority, methods, and causal claims. Never invent facts. 

Study only relevant evidence in:

- `banks/title-bank.md` for proven structures and examples
- `banks/pattern-bank.md` for the outlier evidence behind them
- `banks/power-words-bank.md` for fitting vocabulary and its use constraints

Learn why an example works, then write for this video. For example, a bank row may teach "direct challenge plus a replacement." Use that relationship only when the locked video supports it. Filling a proven shape with this video's real subject is a legitimate move when the claim holds.

Banks are evidence, not a quota. Do not require exact wording, lineage, receipts, one candidate per pattern, or coverage of any pattern set. Original candidates compete equally.

Apply BENS quietly as a clickability lens. One useful driver can be enough. Use the power-word bank actively when a word makes the title stronger and more natural. Neither creates a quota or permits a larger claim.

## Write wide, then sharpen

Draft enough private candidates to discover the strongest line. Explore bank-informed and original wording. If no relevant bank structure helps, work from the video's strongest truthful tension, implication, contrast, consequence, proof, desire, or novelty. These are prompts for judgment, not categories to fill.

For example, if the selected material proves that five revisions made an intro worse, "Why Your Fifth Rewrite Makes the Intro Worse" explores consequence and contrast. The number and result are usable only because the hypothetical source supports both.

Cut weak drafts, then compare the best on:

- truth and delivery fit
- clear value plus a meaningful unanswered question
- one strong central pull
- natural spoken language
- concise wording, with 40 to 65 characters as the usual target
- room for the thumbnail to add a second beat

Reject topic labels, vague benefits, stitched phrases, unsupported specificity, borrowed authority, and lines that reveal the whole payoff. Do not write thumbnail text. `vid-thumbnail-v2` owns its three tests.

## Present the choice

Show three to five strong finalists when the evidence supports them. Recommend one decisively and give each option one short, viewer-facing reason.

> **My pick: "{title}"**
>
> {One brief reason.}
>
> 1. **"{title}"**: {brief reason}
> 2. **"{title}"**: {brief reason}
> 3. **"{title}"**: {brief reason}

Do not show character counts, BENS, pattern names, source titles, receipts, bank coverage, rejected drafts, files read, factual lock lists, or work logs. If the creator proposes an unsupported title, name the unsupported claim briefly and offer the closest truthful version. Otherwise respect their style choice.

## Save only after approval

After the creator approves one title:

1. Re-read the current selected `piece.md` and confirm its content-piece identity and slug.
2. Set `title` to the approved wording exactly.
3. Set `last_updated` to today's date in `YYYY-MM-DD`.
4. Preserve every other frontmatter field and body line.
5. Re-read the saved file and verify that only `title` and `last_updated` changed.

Do not create a titles file or save candidates, rationale, research, or process notes. Reply only:

> Title locked: "{title}". Saved to piece.md.

Stop. Thumbnail work belongs to `vid-thumbnail-v2` and never reopens the title.
