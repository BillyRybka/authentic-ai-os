---
name: vid-thumbnail
description: Present exactly ten strong, distinct thumbnail-text options for one selected YouTube video, then let the creator choose exactly three tests to approve and lock. Use after the title, frame, and core payoff are set when a creator asks for thumbnail text, thumbnail copy, options, or a text-only thumbnail package. Read the selected piece, source material, and relevant packaging evidence privately; keep upstream decisions closed; then save the three chosen texts with aligned measurement labels in piece.md. Never provide visual direction.
---

# Choose three thumbnail-text tests from ten

Create a decision set of exactly ten strong options for one locked title. Let the creator choose exactly three tests to save. Keep the title, frame, audience, and promise closed. Do not repair packaging by rewriting an upstream decision.

Keep research, generation, and filtering private. The creator sees the locked title once, ten options, and a short reason each option is worth considering.

## 1. Start from one locked video

Require a selected video or `content/pieces/{slug}`. If none is selected, ask which video needs thumbnail text without scanning the vault.

Read `content/pieces/{slug}/piece.md`. Require `title`, `frame`, and `core_payoff`.

- If `title` is missing, route to `vid-title`, the current Title V3 handoff.
- If `frame` or `core_payoff` is missing, route to `vid-framing`.
- Never fill another skill's field to unblock this one.

Use the locked title, frame, core payoff, goal, `## The Read`, `must_not_become`, and any must-deliver obligation as boundaries. Older pieces may lack some newer fields; continue from the locked material that exists.

Read a complete `script.md` when present. Use it as evidence for what the video actually says and can deliver, but never let it override the locked framing. Read `brain-dump.md` when no complete script exists and whenever factual provenance, omitted source material, or a material gap needs checking. Creator-provided context and directly linked source material may also support a claim.

## 2. Establish support privately

Identify the locked title's main hook, the question it plants, and its tone. Then identify factual material the thumbnail may use: exact figures, timeframes, names, tools, results, proof, mechanisms, commands, consequences, and genuine belief clashes.

Every claim must trace to the selected video's material. Never invent, round, strengthen, merge, or borrow a fact from a bank or example. A script can demonstrate delivery; use the brain dump or source material when provenance is uncertain.

## 3. Calibrate, then use packaging evidence selectively

Before generating any candidates, read `references/title-thumbnail-calibration.md` in full on every run. Treat it as read-only source material and never edit it during normal thumbnail work. Use the recorded pairs to calibrate how a title and thumbnail create a stronger package together, not to copy wording or force a formula. In addition, notice the length, and emotional response it would create together with the title. 

Treat every example as structural evidence only. It never supplies facts for this video. Do not reveal sources, receipts, pattern names, metrics, files read, or research notes.

## 4. Generate wide and filter hard

Draft widely enough in private to find exactly ten meaningfully different options. Each option must add a useful second beat to the title, such as proof, consequence, contradiction, mechanism, specificity, or unresolved tension. The main goal is to create a mental itch that would make someone want to click. We need to create a curiousity gap.

Keep every survivor:

- truthful and deliverable by the video
- specific to this video rather than generic to the niche
- focused on one idea and readable at a glance, usually one to four words and never more than five
- compatible with the title's hook and tone, whether matching or productively contrasting
- curious or provocative without pre-delivering the full payoff
- free of vague hype, stacked claims, filler, and language that needs visual direction to make sense

Read the title and each candidate as one package. Cut a candidate when the pair merely repeats itself, fights the locked promise, feels generic enough for many unrelated videos, or removes the reason to watch.

Apply a private package-reaction gate to every survivor. Read the locked title and thumbnail text as one semantic unit. Keep the option only when that pair creates a distinct, compelling reaction, question, tension, or expectation. A true detail is not enough by itself. Reject options that merely name a fact, tool, setup detail, warning, exception, generic problem, implementation caveat, or standalone label. Also reject unsupported scarcity and unexplained tool names. A detail from any of those categories may survive only when the complete title-plus-thumbnail pair creates a clear hook the video can deliver.

Judge the package by meaning, not literal word overlap. Shared words remain allowed when they strengthen clarity, curiosity, or force.

The ten options must create meaningfully different learning signals. Cosmetic rewrites, punctuation changes, casing changes, or synonyms do not count as separate options.

Before presenting, verify each option one last time against the script when complete and the video's evidence when provenance matters. If the material cannot yet support ten strong options, do not pad. Briefly name the missing kind of evidence and ask one focused question before presenting the set. Do not show fewer than ten as the decision set.

## 5. Present exactly ten options

Show the locked title once, followed by exactly ten numbered options. Give each one short, practical description of the viewer response or package hypothesis it tests.

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

Treat the creator's explicit selection of exactly three option numbers as approval to save those tests. Before writing, verify that each chosen option remains truthful, distinct from the other two, and deliverable by the video. If one fails, explain the specific conflict briefly and ask for a replacement choice from the remaining options.

After three options are approved:

1. Re-read `content/pieces/{slug}/piece.md` and confirm `type: content-piece` plus the selected slug.
2. Set `thumbnail_text` to exactly the three chosen texts, verbatim and in the creator's selected order.
3. Set `thumbnail_shape` to exactly three aligned measurement labels in the same order.
4. Set `last_updated` to today's date in `YYYY-MM-DD`.
5. Preserve every other frontmatter field and every body line unchanged.
6. Re-read the saved file and verify that only `thumbnail_text`, `thumbnail_shape`, and `last_updated` changed.

Choose each `thumbnail_shape` label privately to describe what the selected test is measuring. Use a simple accurate category such as `belief-clash`, `proof`, `consequence`, `mechanism`, `number`, `command`, `curiosity`, `named-method`, or `other`. These labels are measurement metadata, not creator-facing patterns, and they do not need to cover different categories when the actual hypotheses differ.

Use aligned YAML arrays:

```yaml
thumbnail_text: ["{option 1}", "{option 2}", "{option 3}"]
thumbnail_shape: [{shape 1}, {shape 2}, {shape 3}]
```

Replace earlier thumbnail arrays if present. Never save rationale, drafts, research, or test results.

After saving, reply only:

> Three thumbnail-text tests saved to piece.md.

Stop. Do not add visual direction or reopen the package.
