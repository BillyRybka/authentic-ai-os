---
name: vid-structure
description: Co-plan the writer-ready body of one video from a completed brain dump and locked frame, payoff, format, goal, title, and thumbnail package. Use to structure or safely re-structure a selected piece without writing its intro, body prose, or ending. Adapts the plan to the material and format, resolves critical gaps, writes a sourced script skeleton, and updates structure-owned piece state after creator approval.
---

# Video Structure V2

The core payoff is what the viewer walks away with. The body is what they need in order to get there, built from the brain dump and kept true to the title and thumbnail.

Build the body plan with the creator. Finish when the section order, jobs, source material, takeaways, and any useful supporting devices are approved and a writer can draft without needing to choose the structure, interview/mine stories, metaphors, examples again.

Scope is the plan, not the prose. Do not write the intro, body prose, ending, title, thumbnail, or a new frame.

## Operating rules

- Preserve the locked package and the creator's stated boundaries. A format planner is a strong starting shape, not a cage.
- Require only three things for every body section: its job, exact source material or provenance, and intended viewer takeaway.
- Add a story, example, demonstration, metaphor, framework, evidence item, setup or payoff responsibility, or cross-section thread only when it helps that section do its job.
- Keep a meaningful unresolved reason to continue through the body. Do not delay an answer by rule. Let the package, material, format, and next useful question determine where each payoff belongs.
- Never fabricate a story, fact, result, quotation, source, bank entry, or link. Never pad a count.
- Recommend one supporting device when the fit is clear. Surface alternatives only when the creative decision is genuinely close.
- Log cuts with a reason. A cut the creator restores may expose a frame or format problem.
- Keep private analysis private. The creator sees a concise map when it needs a decision, then one complete plan for approval.

## 1. Validate the selected piece

If no piece or slug was selected, ask which video. Do not scan for a likely one.

Read the selected `piece.md` and `brain-dump.md`. Confirm:

- `piece.md` has `type: content-piece` and its `slug` matches the folder.
- `brain-dump.md` exists and has no `## Still capturing` marker.
- `frame`, `core_payoff`, `format`, `goal`, `title`, and nonempty `thumbnail_text` exist.
- The locked format is one of: `short-process`, `case-study`, `roast`, `deep-dive`, `interview`, `news`, `listicle`.
- `knowledge/format-planners/{format}.md` exists.

Also read `must_not_become` and `## The Read` when present. Read only source files directly supplied or linked for this piece. Do not scan unrelated content or banks.

Route a missing or unfinished prerequisite to its owner. Do not fill another skill's field. If the pipeline already verified a prerequisite, do not narrate or repeat the check.

If `segment_purposes` or a planned `script.md` already exists, this is re-structure mode. Read [references/restructure-safety.md](references/restructure-safety.md) before proposing a change.

## 2. Map the body privately

Read the selected format planner's body structure and the matching section in [references/format-plans.md](references/format-plans.md). Ignore its packaging, upload, and promotion guidance.

Map the material against the locked package:

- must include: required to fulfill the frame, payoff, title, thumbnail promise, or approved transformation
- support: strengthens another section but does not need its own section
- combine: overlaps material that becomes stronger together
- cut: off-angle, repeated, unsupported, or wrong for this video
- missing: a fact, story beat, demonstration, answer, or evidence item needed to write honestly

Check whether the locked format still fits. When it does not, show the conflict before building a plan. Offer the smallest real choices: customize the format, narrow the material to fit, or return to framing. The creator decides.

Choose the lightest creator gate that protects a real decision:

- Show a separate section map when membership, grouping, order, cuts, or format fit is meaningfully contestable.
- For a simple piece with an obvious shape, combine the section map and complete plan into one proposal.

Never call either proposal a step, pass, mining result, or workflow stage.

## 3. Build the writer-ready plan

For every body section, decide:

1. **Job:** what this section must accomplish in the body.
2. **Sources:** the exact dump moment, supplied source, creator-approved session material, or validated bank entry it may use.
3. **Takeaway:** what the viewer should understand, feel, decide, or do when the section lands.

Then add only the useful optional decisions described by the matching format plan. Read [references/source-and-gap-policy.md](references/source-and-gap-policy.md) before selecting a bank entry, external source, or evidence item.

Plan the package arc once for the whole body:

- `central_question`: the main question raised by the approved title and thumbnail package
- `reason_to_continue`: what remains meaningfully unresolved as the body advances
- `payoff_section`: the exact section that fulfills the package's central promise; it may be early, middle, or late
- `threads`: zero or more cross-section dependencies, each with an exact open section and close section

Do not invent a thread for disconnected items. Do not preserve curiosity by withholding information the viewer needs now. A payoff may land early when the next section opens a real new question.

## 4. Resolve gaps before handoff

Classify every missing item:

- **Critical:** the writer cannot make the section true, specific, or complete without it. Resolve it by capturing or sourcing the material, merging, cutting, changing the claim, or changing the plan. Do not save a writer-ready outline while one remains.
- **Production follow-up:** the decision and factual content are complete, but a known asset still needs retrieval or capture, such as exporting an already verified screenshot. Record the exact follow-up without handing the writer a creative decision.

Ask one focused question at a time when creator knowledge is required. When a gap exposes a weak section, recommend the smallest sound repair rather than protecting the old outline.

Name what is missing in plain terms and let the creator decide how to fill it. Missing material is not a reason to change the format. That route exists only for a genuine misfit.

## 5. Approve the complete plan

Show one concise plan in final order. Include each section's job, sources, takeaway, and only the optional decisions that matter. Show the package payoff location, any operational threads, and production follow-ups.

Name a cut only when it costs the video something, such as the last story in the dump or anything the package promised. The rest stay logged in the file.

Ask for one approval or a concrete adjustment. The creator may override the proposed shape. Recheck truth, package fulfillment, source coverage, and format fit after an override.

Do not save before explicit approval.

## 6. Save and verify

Read [assets/script-plan-template.md](assets/script-plan-template.md) and [assets/piece-state-template.md](assets/piece-state-template.md). On first write:

1. Prepare both complete edits before changing either file.
2. Write `script.md` first, then update only structure-owned state in `piece.md`.
3. Re-read both files. Verify the Intro and Ending stubs exist, section order and count agree, all required sources resolve, `## To build` is empty, critical gaps are absent, and non-owned fields are unchanged.
4. If either write or verification fails, restore only the files changed in this save attempt and report the failure.

On re-structure, follow the separate safety reference. Never rebuild a partially written script from the first-write template.

Set `status: drafting` only when advancing from `ideating`. Never regress a later lifecycle state. Initialize `segments_completed: []` only on the first outline when the field is absent.

Planning a bank entry does not count as using it. Do not change `*_used`, `used_in`, or bank entry status.

For a pre-recording Interview, writer-ready means the host's framing, questions, and follow-up prompts are fully planned. `vid-segment` writes those host-authored lines and never invents the guest's answer. Material marked `to elicit in recording` is an intentional production input for this format, not permission to script an answer.

Confirm the saved format, section count, payoff section, production follow-ups, and handoff to `vid-intro` in one short message.

## Before declaring writer-ready

- The creator approved the section membership and final order.
- Every section has a job, exact source provenance, and takeaway.
- Optional devices and evidence appear only where useful.
- Every bank wikilink points to a real, readable, matching entry.
- No critical gap remains.
- Cuts are preserved with reasons.
- On a first write, `segment_purposes`, script headings, and `tension_plan` use the same exact section labels. A legacy re-structure follows the protected-label exception in the safety reference.
- `script.md` contains planning lines, not body prose.
- No downstream writer must choose the section structure or interview the creator for missing content.
