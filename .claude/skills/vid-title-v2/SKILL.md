---
name: vid-title-v2
description: Package one locked YouTube video into a concise set of strong, truthful title finalists and recommend one. Use after framing when a creator asks for title ideas, title options, a title recommendation, or to lock a title for a selected piece. Read the creator's evidence and relevant title-bank patterns silently, preserve the approved frame, and write only title and last_updated after approval. Not for reframing, thumbnail writing, hooks, outlines, or topic ideation.
---

# Write the video title

Package the locked video. Do not improve, reinterpret, or repair its frame.

Keep research and drafting private. The creator sees strong choices, not a work log.

## 1. Select one locked piece

Require a specific video or `content/pieces/{slug}`. If none is selected, ask which video to title without scanning the vault.

Read silently, when present:

1. `content/pieces/{slug}/piece.md`
2. `content/pieces/{slug}/brain-dump.md`
3. `content/pieces/{slug}/script.md`

Do not title a source explicitly marked as incomplete. Treat these framing decisions as locked:

- `frame`
- `core_payoff`
- `goal`
- `## The Read`: Target, Transformation, and Stakes
- any locked must-deliver obligation or factual direction
- any explicit `must_not_become`

Older pieces may lack `## The Read` or `goal`. Use the locked fields and source material that exist. If `frame` or `core_payoff` is missing, route to `vid-framing`; do not fill the gap. If the frame seems weak, title it faithfully or tell the creator it needs reframing. Never repair it here.

## 2. Lock the frame and facts privately

Use the approved promise, audience, transformation, stakes, goal, core payoff, boundaries, and factual direction as the title's perimeter. Packaging may increase the pull of what is already there. It may not change who the video is for, what it delivers, why it matters, or what it claims.

Build an internal list of what the title may claim. Admit only facts supported by the selected piece, raw material, script, or foundation:

- numbers, prices, timeframes, and results
- people, products, tools, methods, and named concepts
- audience descriptions and audience language
- causal claims, comparisons, proof, and consequences

Do not invent, round, strengthen, combine, or borrow any of these from a bank example. A title-bank row proves a shape, not this video's facts.

Audience language helps explain what matters to the audience; it does not require a literal complaint title. Choose the most interesting truthful expression of the selected source structure's existing click mechanism.

## 3. Select proven structures

Treat `banks/title-bank.md` and `banks/pattern-bank.md` as the authoritative source of proven structures. Read them only as far as needed to find relevant evidence. Search in this order:

1. The creator's own proven winners that fit this promise
2. Direct-niche patterns that fit this promise and audience
3. Adjacent patterns whose structure transfers cleanly

Select several relevant bank-backed structures, generally three to five, that naturally fit the locked promise. Each selected structure must retain a private lineage to one concrete bank source or receipt. Do not require coverage of generic categories or formulas.

For each selected structure, identify privately:

- the exact source title and its receipt
- its central tension
- the question it leaves unresolved
- its sentence shape
- its dominant click mechanism

Treat that engine as the reusable evidence. The source's subject, audience, claims, authority, numbers, results, proof, method, and named payload do not transfer. Do not load or summarize the full banks merely because they exist. Keep titles, channels, metrics, pattern names, lineages, and receipts out of the creator-facing response unless asked.

If `piece.md` contains an `anchor`, use it as a strong seed only when its receipt is complete, its promise still matches the locked frame, and every factual word is supported. Make it compete with the other candidates. It receives no automatic win.

If fewer than three relevant proven structures exist, do not pad the set with generic formulas. Use natural, non-proven title judgment only as a private fallback and never misrepresent it as bank-backed. Mention thin coverage only when it materially lowers confidence in the decision set. Do not turn missing evidence into an error lecture.

## 4. Rebuild the payload inside each lineage

For each selected structure, strip away the source title's payload and rebuild it from the locked video's facts, proof, and audience understanding. Draft multiple native variations within that lineage. Do not noun-swap, imitate the source too closely, or bend the locked promise to fill its slots.

Apply BENS quietly within each selected source structure to identify the strongest truthful click pull. Consult `C:\Users\billr\projects\business-os\Content\banks\power-words-bank.md` to help express that pull, using fitting bank language or stronger natural wording. Respect the bank's fit constraints and do not stack language mechanically. Neither BENS nor power words may choose the structure, force a quota or category, or justify unsupported claims.

Carry forward one strongest natural descendant from each lineage, then compare the three to five lineages. Discard the other drafts privately.

## 5. Filter for truth and clickability

Judge every survivor against these requirements:

- Preserve every locked framing decision and factual boundary.
- Make the strongest truthful tension, implication, proof, consequence, contrast, or desire clear enough to earn a click.
- Open one meaningful question that the video resolves.
- Each title must be between 40-65 characters ideal
- Keep one central pull rather than stacking unrelated mechanisms.
- Read aloud as one natural human thought.
- Use only facts on the internal lock list.
- Leave room for the thumbnail to add a second beat.

Truth and deliverability are gates, not scoring dimensions. Cut noun-swapped bank titles, topic labels, complaint restatements with no further pull, vague benefit claims, stitched fragments, unsupported specificity, borrowed authority, and titles whose wording answers its own question. Prefer a strong native line over visible formula compliance.

## 6. Present only the decision set

Present three to five finalists when the evidence supports them. Give each one a concise reason grounded in the video's true tension, proof, implication, or promise. Recommend one decisively.

Use this shape:

> **My pick: "{title}"**
>
> {One brief reason.}
>
> 1. **"{title}"**: {brief human reason}
> 2. **"{title}"**: {brief human reason}
> 3. **"{title}"**: {brief human reason}

Do not invent audience consensus or behavior such as "everyone knows" or "they all did this." Do not expose BENS, power-word strategy, character counts, receipts, bank research, lineages, rejected candidates, files read, lock lists, or drafting work unless the creator asks. Do not present a research report before the titles.

If the creator proposes an unsupported title, name the unsupported claim briefly and offer the closest truthful version. Otherwise accept their judgment on soft style choices.

## 7. Save only after approval

After the creator approves one title:

1. Re-read the current `content/pieces/{slug}/piece.md`.
2. Confirm it is the selected content piece.
3. Set `title` to the approved wording exactly.
4. Set `last_updated` to today's date in `YYYY-MM-DD`.
5. Preserve every other frontmatter field and every body line unchanged.
6. Re-read the saved file and verify only `title` and `last_updated` changed.

Do not create a titles file. Do not write the receipt, rationale, or candidate list anywhere. After saving, reply only:

> Title locked: "{title}". Saved to piece.md.

Stop. Thumbnail owns three separate tests and does not reopen the title. Hook and structure belong to other skills.
