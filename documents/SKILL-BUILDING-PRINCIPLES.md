---
type: principles
project: authentic-ai-os
date: 2026-08-12
status: living
last_updated: 2026-08-12
tags: [skill-building, skill-design, verification]
---

# Skill-building principles

The standing decisions for building and rebuilding skills in Authentic AI OS. These are product rules, not suggestions. Add to them when real use exposes a new failure pattern.

## How to use this document

Read this before rebuilding a skill. Use it to set the skill's boundary, interaction, write contract, and behavioral tests before polishing instructions. When a real run teaches a reusable lesson, update this file with the smallest clear rule that would have prevented the failure. Keep the concrete history in [[skill-writing-lessons]] or [[skill-wiring-lessons]] when it needs more detail.

## Boundaries and ownership

### Give each skill one job

Name the decision or artifact the skill owns. Name what it receives from upstream and what downstream can treat as locked. If a downstream skill must repeat an interview, repair a decision, or derive missing work, the upstream handoff is incomplete.

Do not let a leaf skill narrate or manage the full pipeline. It should know its prerequisites, its own job, and its immediate handoff.

Keep these jobs separate:

- **Framing** locks the audience, stakes, transformation, goal, strategic promise, and honest delivery boundary.
- **Title** packages that locked promise and locks one title. It does not repair the frame.
- **Thumbnail text** tests exactly three distinct packaging hypotheses against the locked title. It does not choose one winner, rewrite the title, or add visual direction.
- **Structure** plans how the video fulfills the locked promise and package. It does not reopen packaging.

### Gate decisions that downstream work depends on

Use an explicit confirmation gate for any decision another skill will inherit. A confident read is still a proposal until the creator confirms it. Present confirmed and proposed fields as separate, plainly labeled values so the creator can correct one without reopening everything.

Answer local corrections locally. If the creator changes one field, revise that field first. Do not regenerate the whole package unless the change actually invalidates it.

## Keep the product simple

The creator should see decisions, useful options, and focused questions. Research, source checks, bank shopping, drafting, filtering, scoring, and routing stay internal.

Do not expose file lists, process logs, internal labels, framework scores, rejected drafts, or verification narration unless the creator asks. After a save, confirm the result in one short line. Do not append a handoff speech or a summary of checks performed.

## Truth and source discipline

Use real material only. Never invent or strengthen proof, quotes, numbers, results, audience language, fears, causal claims, or credibility. Narrow a claim or ask for the missing source.

Treat banks as pattern evidence, not fact evidence. A bank can prove that a title shape, tension, or packaging move has worked. It cannot prove that this video's creator achieved a result or that this audience used a phrase.

Quote only exact language from one identifiable source. Do not stitch fragments from different places into a Frankenstein quote. Paraphrase openly when exact wording is not available.

Load references selectively. Start with the selected piece and its direct sources. Search only the bank entries or reference sections needed for the current decision, then stop. Never load or dump every bank because it exists.

## Writing standard

Write in language the audience would naturally use. Lead with the tension, consequence, or desired outcome they recognize. Prefer concrete nouns and named handles they can picture or repeat.

Do not hide a clear idea behind vague internal language such as "system," "framework," "layer," or "guard." A proposed name is allowed when it gives the audience a useful handle, but label it as proposed and let the creator correct it.

Examples are executable behavior. Models copy their moves, sequence, tone, and assumptions. Update examples whenever a live rule changes. Remove examples that teach behavior the skill now forbids. Forward test the changed behavior against real material, including thin or adversarial material, instead of trusting a clean read-through.

## State writes

Write only the fields the skill owns. Re-read the current file immediately before saving, preserve every other field and body line, then verify the exact diff. Never let one skill quietly clean up, reorder, or reinterpret another skill's state.

Conversation-only material stays in the conversation unless a named downstream consumer needs it. Do not save research notes, candidate piles, rationales, or process artifacts just because they were useful internally.

## Candidates, promotion, and validation

Build a candidate beside the current skill. Preserve the original while the candidate is being judged. Promote only after the candidate survives realistic use and its ownership, interaction, source discipline, and write behavior are proven.

Validate behavior, not only syntax. Frontmatter, paths, line endings, and schemas must pass, but a structurally valid skill can still ask the wrong questions, expose internal work, invent support, overwrite state, or fail its handoff. Test the choices it makes and the files it changes.

Follow [[DEV-WORKFLOW]] when a candidate graduates. Promotion includes wiring, stale-reference checks, maps, and release hygiene. It is not a folder rename alone.

## Revision process

1. Observe a real failure in use or forward testing.
2. Name the behavioral rule the failure violated or revealed.
3. Make the smallest coherent change that fixes the behavior at its owner.
4. Update examples in the same pass so they teach the live rule.
5. Validate syntax, contracts, owned-field writes, and downstream handoff.
6. Test again on real material. Include the case that failed and at least one different case that could expose overfitting.
7. Add the reusable decision here. Put the longer incident record in the relevant lessons document.

Do not write the history of old alternatives into the skill. The live skill should state what to do. This document and the lesson logs hold why the rule exists.

## Open decisions

These are unresolved. Do not treat them as settled contracts.

- Whether `must_deliver` remains a framing-owned field, changes shape, moves to structure, or is removed after downstream consumers are traced.
- Whether `must_not_become` should be a durable piece field, a conditional boundary used only when the creator states one, or removed when no downstream gate acts on it.
- Whether the framing skill should retain both concepts, retain one, or replace them with a tighter delivery-boundary contract.

Resolve each decision by tracing named consumers, testing the behavior on real pieces, and updating the owner, examples, schema authority, and downstream readers together.
