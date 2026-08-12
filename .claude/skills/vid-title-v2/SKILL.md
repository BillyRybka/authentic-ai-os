---
name: vid-title-v2
description: Package one locked YouTube video into a concise set of strong, truthful title finalists and recommend one. Use after framing when a creator asks for title ideas, title options, a title recommendation, or to lock a title for a selected piece. Read the creator's evidence and relevant title-bank patterns silently, preserve the approved frame, and write only title and last_updated after approval. Not for reframing, thumbnail writing, hooks, outlines, or topic ideation.
---

# Write the video title

Package the locked video. Do not improve, reinterpret, or repair its frame.

Keep research and drafting private. The creator sees strong choices, not a work log.

Work the six steps below in order.

## Step 1: Select one locked piece

**Lock the promise and limits.** Read the selected video's framing, audience, source material, and factual boundaries. Never reframe it here.

Require a specific video or `content/pieces/{slug}`. If none is selected, ask which video to title without scanning the vault.

Read silently, when present:

1. `content/pieces/{slug}/piece.md`
2. `content/pieces/{slug}/brain-dump.md`
3. `content/pieces/{slug}/script.md`
4. `foundation/avatar.md`
5. `foundation/iceberg.md`
6. `foundation/credibility.md`

Treat these framing decisions as locked:

- `frame`
- `core_payoff`
- `goal`
- `## The Read`: Target, Transformation, and Stakes
- any explicit `must_not_become`

Older pieces may lack `## The Read` or `goal`. Use the locked fields and source material that exist. If `frame` or `core_payoff` is missing, route to `vid-framing`; do not fill the gap. If the frame seems weak, title it faithfully or tell the creator it needs reframing. Never repair it here.

## Step 2: Lock the facts privately

Build an internal list of what the title may claim. Admit only facts supported by the selected piece, raw material, script, or foundation:

- numbers, prices, timeframes, and results
- people, products, tools, methods, and named concepts
- audience descriptions and audience language
- causal claims, comparisons, proof, and consequences

Do not invent, round, strengthen, combine, or borrow any of these from a bank example. A title-bank row proves a shape, not this video's facts.

## Step 3: Shop evidence selectively

**Shop proven structures.** Search creator winners, then direct-niche evidence, then adjacent evidence for the strongest relevant starting structure.

Read `banks/title-bank.md` and `banks/pattern-bank.md` only as far as needed to find relevant evidence. Search in this order:

1. The creator's own proven winners that fit this promise
2. Direct-niche patterns that fit this promise and audience
3. Adjacent patterns whose structure transfers cleanly

Treat these banks as the evidence source for proven and transferable structures. Direct structural reuse is the normal move when a structure fits. **Preserve the engine.** Keep that structure's central tension, emotional pull, and sentence shape as intact as the locked promise permits. Change or abandon it only when preserving it would create an unsupported claim, confuse the right audience, or clash with the title-thumbnail package. Stop when a small set of useful, distinct shapes is clear. Do not load or summarize the full banks merely because they exist. Keep titles, channels, metrics, pattern names, and receipts out of the creator-facing response unless asked.

If `piece.md` contains an `anchor`, use it as a strong seed only when its receipt is complete, its promise still matches the locked frame, and every factual word is supported. Make it compete with the other candidates. It receives no automatic win.

If the banks are absent or have no relevant evidence, continue with natural title judgment. Mention the gap only when it materially lowers confidence in the recommendation. Do not turn missing evidence into an error lecture.

Read `references/title-judgment.md` when bank evidence is thin or the candidate set needs a sharper range of shapes.

## Step 4: Write wide and cut privately

**Rebuild the payload.** Write the claim, proof, specifics, and language from this video's factual lock list and audience. Never settle for swapped nouns.

Identify three to five meaningfully different title shapes. Write enough candidates to discover the strongest language, usually 12 to 20, then discard weak ones privately.

Read `knowledge/BENS-framework.md` before selecting finalists. Use BENS as the core quiet emotional and clickability lens, not the goal or a scorecard. Every finalist needs at least one strong BENS driver; keep one or two and do not stack or maximize all four.

Use its worked titles as valid internal cross-niche examples of emotional engine and sentence shape. For any bank or BENS example, identify privately why it works, such as tension, curiosity, credibility, novelty, ease, desire, or consequence, then rebuild that pull around the locked promise and factual lock list. Do not noun-swap or copy the payload. Never borrow an example's numbers, results, named methods, authorities, audience, or claims. Make the rewrite more specific, relevant, and interesting for this video while keeping it true and coherent.

**Gate and filter privately.** Judge every survivor against these requirements:

- Pass the truth gate: preserve the locked video's promise and audience, use only supported claims, and ensure the video can honestly fulfill the title's implication.
- Title the wound, tension, curiosity, consequence, or desired result. Do not recite the process.
- Give the right viewer a genuine reason to click. Curiosity is common, not required; consequence, desire, contrast, proof, or novelty can carry the click.
- Keep one meaningful central question or tension without opening unrelated loops.
- Use one coherent click mechanism. One or two complementary BENS drivers may support it without adding clutter.
- Read aloud as one natural human thought.
- Use only facts on the internal lock list.
- Leave room for the thumbnail to add a second beat.

After the truth gate, choose by clickability: which title gives this viewer the strongest genuine reason to click? Prefer clear tension over clever wording. Cut labels, vague benefit claims, stitched fragments, stacked mechanisms, unsupported specificity, and titles whose question the wording already answers.

## Step 5: Present only the decision set

**Present and hand off.** Show three to five finalists. Give each one brief, human reasoning tied to its likely effect, not the internal framework. Recommend one decisively.

Use this shape:

> **My pick: "{title}"**
>
> {One brief reason.}
>
> 1. **"{title}"**: {brief human reason}
> 2. **"{title}"**: {brief human reason}
> 3. **"{title}"**: {brief human reason}

Do not expose BENS letters, scores, framework explanations, character counts, receipts, bank research, rejected candidates, kill passes, files read, lock lists, or process narration unless the creator asks. Do not present a research report before the titles.

If the creator proposes an unsupported title, name the unsupported claim briefly and offer the closest truthful version. Otherwise accept their judgment on soft style choices.

## Step 6: Save only after approval

After the creator approves one title:

1. Re-read the current `content/pieces/{slug}/piece.md`.
2. Confirm it is the selected content piece.
3. Set `title` to the approved wording exactly.
4. Set `last_updated` to today's date in `YYYY-MM-DD`.
5. Preserve every other frontmatter field and every body line unchanged.
6. Re-read the saved file and verify only `title` and `last_updated` changed.

Do not create a titles file. Do not write the receipt, rationale, or candidate list anywhere. After saving, reply only:

> Title locked: "{title}". Saved to piece.md.

Stop. Thumbnail, hook, and structure belong to other skills.
