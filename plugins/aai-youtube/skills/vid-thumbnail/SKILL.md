---
name: vid-thumbnail
description: Present exactly ten strong, distinct thumbnail-text options for one selected YouTube video, then let the creator choose exactly three tests to approve and lock. Use after the title, frame, and core payoff are set when a creator asks for thumbnail text, thumbnail copy, options, or a text-only thumbnail package. Read the selected piece, source material, and relevant packaging evidence privately; keep upstream decisions closed; then save the three chosen texts with aligned measurement labels in piece.md. Never provide visual direction.
---

# Choose three thumbnail-text tests from ten

Create a decision set of exactly ten strong options for one locked title. Let the creator choose exactly three tests to save. Keep the title, frame, audience, and promise closed. Do not repair packaging by rewriting an upstream decision.

Keep research, generation, and filtering private. The creator sees the locked title once, ten options, and a short reason each option is worth considering.

## How a thumbnail earns the click

The viewer has not watched the video yet. They may know the creator. They may have seen every video on the channel. It does not matter. All they have is the title and these words, read as one package in under a second. Anything that needs the video to make sense is an inside joke. A metaphor, an example, a story beat, or a phrase from inside the script is not a thumbnail until the title alone makes it land. The only job of the text is to make the right viewer think what, why, or how. Sharp, direct, and clear. If it does not do that, nothing else about it matters.

Every title leaves a gap. Write what the title says. Then write what it withholds, the thing the viewer would have to click to find out. The thumbnail works that gap and never restates what the title already carries. The pairings that work:

- The title states the result. The thumbnail flips the belief behind it or raises the question. "How I Got 481% Faster" with "23:07 to 19:42."
- The title asks the question everyone is asking. The thumbnail gives the answer nobody expects. "Should You Buy a House?" with "DO NOT BUY A HOUSE."
- The title teases that something exists. The thumbnail names it. "The One Rule That Killed My Procrastination" with "THE 15-SECOND RULE."
- The title diagnoses. The thumbnail promises the fix without revealing it. "95% of People STILL Prompt ChatGPT Wrong" with "DO THIS INSTEAD."

The first move to try on any channel is cognitive dissonance: name what the viewer has been told or assumes, and say the opposite, because this video backs it up. "LOOK POOR" on a finance channel. "WORK LESS" on a productivity channel. "DON'T HIRE A VA" on an operations channel. The belief is in the material. Every video argues against something: the advice the viewer keeps hearing, the thing they assume, the move they were about to make. Find that in the script or brain dump and reverse it. The viewer has to resolve the contradiction, and the only way to resolve it is to watch. It is the first thing to try, not the only thing. Result, comparison, curiosity, and social hacking each win when the material carries them, and the ten must show that range.

Specificity is credibility. "$712,921.88" beats "$700K." "-30% IN 6 WEEKS" beats "REVENUE DROPPED." Cents matter. The number that would feel made up if it were not true is the one to use. A number that is not in the material does not exist.

Strong verbs pull. STOP, FIX, DELETE, COPY, DON'T, QUIT. Soft verbs die. CONSIDER, TRY, LEARN, EXPLORE.

The words must belong to this video. Ask whether they would fit a hundred other videos in the niche. "BOTTLENECK" fits every founder video. "BACKWARDS" only fits the one where the steps were done in the wrong order. Signal this story, not the channel's theme. Belonging to this video is not the same as coming from inside it. "BACKWARDS" works because the title explains what went backwards. "HALF A RECIPE" does not, because nothing in the title says what the recipe is for.

Bold is allowed. Provocation is allowed. The bar is not whether the text sounds safe. The bar is whether the video honors what the text implies. "STOP DELEGATING" works on a video that shows what to do before you delegate. It fails on a video that says delegate more.

## What great looks like

Real thumbnail text that worked, grouped by the strategy it ran. Copy the shape and the energy. A phrase from this list is allowed only when this video's own material produces it.

**Cognitive dissonance.** "DO NOT BUY A HOUSE" (real estate). "LOOK POOR" (finance). "YOU DON'T NEED SUBSCRIBERS" (YouTube growth). "WORK LESS" (productivity). "POST EVERY DAY" beside a title about introverts. "MAKE BORING VIDEOS" beside "YouTube's Hard, Until Businesses Do This." "SOCIAL MEDIA IS A TRAP" beside "I QUIT social media & grew my business a better way." Each one names the specific belief the audience holds and reverses it.

**Result.** "$712,921.88." "481% FASTER." "-30% IN 6 WEEKS." "AGE 32." "29 DAYS." "TUTORIAL 1.2M" beside a title about making viral AI videos in 11 minutes. "10x FASTER" beside "You've Been Using AI the Hard Way." "THE 90 MINUTE RULE" and "THE 15-SECOND RULE," where the name itself asks a question. The receipt, the timeframe, or the named method is the hook.

**Comparison.** "275 to 175." "23:07 to 19:42." "DAY 1 to DAY 7." Two real states from the material, and the distance between them is the argument.

**Curiosity.** "LIAR." "DELETE THIS." "QUIT EVERYTHING." "BACKWARDS." "WEAK LEGS?" "DO THIS INSTEAD." "It's easy" beside a title promising twelve ways to use Claude. One idea that demands an answer, with the answer inside the video.

**Social hacking.** A name, brand, or tool the audience already trusts, attached to a claim it is genuinely relevant to. Rare, and never two videos in a row.

What fails, from the same channels: "WRONG ORDER. WRONG OUTCOME." (a paradox that names nothing). "THE 12-SOP RULE" (a label, the number carries no question). "SOPs BEFORE PEOPLE" (the lesson, stated, so there is no reason to click). "MY METHOD" (says nothing). "MIND BLOWN" (dead on arrival).

## 1. Start from one locked video

Require a selected video or `content/pieces/{slug}`. If none is selected, ask which video needs thumbnail text without scanning the vault.

Read `content/pieces/{slug}/piece.md`. Require `title`, `frame`, and `core_payoff`.

- If `title` is missing, route to `vid-title`, the current Title V3 handoff.
- If `frame` or `core_payoff` is missing, route to `vid-framing`.
- Never fill another skill's field to unblock this one.

Use the locked title, frame, core payoff, goal, `## The Read`, and `must_not_become` as boundaries. Older pieces may lack some newer fields; continue from the locked material that exists.

Read a complete `script.md` when present. Use it as evidence for what the video actually says and can deliver, but never let it override the locked framing. Read `brain-dump.md` when no complete script exists and whenever factual provenance, omitted source material, or a material gap needs checking. Creator-provided context and directly linked source material may also support a claim. Bank entries the brain dump links, including the names the creator gave them, are the creator's material. Read them when they exist.

## 2. Establish support privately

Write the gap. What the title says, and what it withholds.

Then pull every asset the material holds: exact figures, timeframes, names, tools, results, receipts, mechanisms, commands, consequences, the belief the audience holds that this video reverses, and the single most dramatic moment in the story.

Every fact must trace to the selected video's material. Numbers land verbatim. Never invent, round, merge, or borrow a fact from a bank or example. A script can demonstrate delivery; use the brain dump or source material when provenance is uncertain.

## 3. Calibrate before drafting

Before generating any candidates, read `references/title-thumbnail-calibration.md` in full on every run. Treat it as read-only source material and never edit it during normal thumbnail work. Use it to calibrate the relationship, length, and viewer response. Do not copy wording, force a formula, or treat an example as evidence for this video.

Treat every example in this skill and its references as structural evidence only. It never supplies facts for this video. Do not reveal sources, receipts, pattern names, metrics, files read, or research notes.

## 4. Generate wide and filter hard

Draft a larger private pool before choosing the ten options. Start from the gap and the belief this video reverses. Then work the dramatic moment, the receipts, the mechanism, and the viewer's own situation. Push past obvious paraphrases and do not stop when the first ten viable phrases appear. Find strong phrases before naming their strategy.

Make one concrete-element pass through the evidence. Look for an exact command, artifact, interface, file, template, tool, receipt, or named thing the viewer could recognize, use, or take away. When one exists and the title makes it meaningful, explore its exact natural form as well as written variations. This is a conditional opportunity, not a required type. Never invent or force one.

After drafting, read `references/thumbnail-strategy-lens.md` in full. Use it to classify and judge the directions already on the table.

Read the title and each candidate as one package. Keep a candidate only when the package makes the right viewer think what, why, or how, and the video can pay that off. Kill it when:

- it needs the video to make sense: a metaphor, example, story beat, or phrase from inside the script that the title alone does not explain
- it restates the title's idea, so the pair says one thing twice
- it runs past four words. Count them
- it states the lesson so plainly there is no reason to click
- it just names a fact, a tool, a role, a setting, or a caveat, with no question attached
- it would fit a hundred other videos in this niche
- it uses a number, name, or claim the material does not hold
- it promises a different video than the title does
- it leans on a decoration word (ROADMAP, UNLOCK, JOURNEY), a hedge, stock hype (INSANE, GAME-CHANGER), or open-mouth language (MIND BLOWN)

Shared words with the title are fine when they add clarity or force. Judge the meaning of the pair, not word overlap.

The ten options must create meaningfully different learning signals and span at least three strategies from the lens when the material can carry them. The three saved tests teach which strategy this audience responds to, so range across strategies is the point. Cosmetic rewrites, punctuation changes, casing changes, or synonyms do not count as separate options.

Before presenting, verify each option one last time against the script when complete and the video's evidence when provenance matters. If the material cannot yet support ten strong options, do not pad. Briefly name the missing kind of evidence and ask one focused question before presenting the set. Do not show fewer than ten as the decision set.

## 5. Present exactly ten options

Show the locked title once, followed by exactly ten numbered options. Give each one a single concise clause describing the viewer response or package hypothesis it tests. Do not defend or over-explain an option.

> **Title:** "{locked title}"
>
> 1. **"{thumbnail text}"**: Tests whether {brief viewer-facing hypothesis}.
> 2. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 3. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 4. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 5. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 6. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 7. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 8. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 9. **"{thumbnail text}"**: Tests whether {different hypothesis}.
> 10. **"{thumbnail text}"**: Tests whether {different hypothesis}.

Do not show rejected drafts, scoring, pattern labels, factual lock lists, workflow narration, title alternatives, or visual advice. Ask the creator to choose exactly three options by number.

If the creator wants a replacement before choosing, revise only the affected option or options and present the complete ten-option set again. After one focused revision pass, if the same weakness remains, ask for the one missing fact or clarify the package tension preventing a strong replacement. Never reopen the title or frame.

## 6. Save the chosen three

Treat the creator's explicit selection of exactly three option numbers as approval to save those tests. Before writing, verify that each chosen option remains truthful, distinct from the other two, and deliverable by the video. If one fails, explain the specific conflict briefly and ask for a replacement choice from the remaining options. When two of the three run the same strategy, say so in one line, then save their choice.

After three options are approved:

1. Re-read `content/pieces/{slug}/piece.md` and confirm `type: content-piece` plus the selected slug.
2. Set `thumbnail_text` to exactly the three chosen texts, verbatim and in the creator's selected order.
3. Set `thumbnail_shape` to exactly three aligned measurement labels in the same order.
4. Set `last_updated` to today's date in `YYYY-MM-DD`.
5. Preserve every other frontmatter field and every body line unchanged.
6. Re-read the saved file and verify that only `thumbnail_text`, `thumbnail_shape`, and `last_updated` changed.

Set each `thumbnail_shape` label to the strategy the selected test runs: `cognitive-dissonance`, `comparison`, `result`, `social-hacking`, or `curiosity`. These are the same names the research bank tags outliers with, so a winner can be matched back to the bank. They are measurement metadata, not creator-facing patterns.

Use aligned YAML arrays:

```yaml
thumbnail_text: ["{option 1}", "{option 2}", "{option 3}"]
thumbnail_shape: [{shape 1}, {shape 2}, {shape 3}]
```

Replace earlier thumbnail arrays if present. Never save rationale, drafts, research, or test results.

After saving, reply only:

> Three thumbnail-text tests saved to piece.md.

Stop. Do not add visual direction or reopen the package.
