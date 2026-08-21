---
type: skill-reference
skill: vid-structure-v2
purpose: coordinated changes required before candidate promotion
---

# Promotion Contract

Do not wire this candidate into the live pipeline until the files below change together.

## Shared schema

Update `knowledge/piece-contract.md` to:

- define `tension_plan` as the object in `assets/piece-state-template.md`
- state that vid-structure initializes `segments_completed` on first outline and vid-segment appends afterward
- replace the universal late-payoff wording on `core_payoff` with format-aware package fulfillment
- reconcile the piece-link convention with the actual `content/pieces/{slug}/piece.md` filename; V2 uses an explicit path-targeted link so it cannot silently point at a nonexistent slug-named note

Define shared ownership for `script.md` frontmatter after the first structure write, especially `status` and `last_refreshed`. V2 preserves the complete block during re-structure until that contract exists.

Update `knowledge/script-tension-architecture.md` to:

- make threads optional
- use operational open and close section labels when a thread exists
- remove the universal 60 to 80 percent payoff requirement
- stop requiring duplicate inline tension notes in `script.md`

## Downstream skills

Update `.claude/skills/vid-segment/SKILL.md` and its local references to:

- read required **Job**, **Sources**, and **Takeaway** fields
- read optional format-specific decisions without requiring Parable and Principle on every section
- consume the structured `tension_plan`
- treat `## Production follow-ups` as production work, not a request to choose material
- keep bank use tracking at approved prose save time
- treat a pre-recording Interview section as host-authored framing, question, and follow-up prompts; never draft a guest answer from an elicitation target

Update `.claude/skills/vid-intro/SKILL.md` only where it assumes V1 plan labels. It can keep using the first body section and package promise.

Update `vid-pressure-test` tension checks to read the object and judge whether the stored reason to continue is honored rather than enforcing late payoff.

## Routing and documentation

When promoting, replace the live vid-structure skill or change `.claude/skills/vid-pipeline/SKILL.md` to invoke the promoted name. Do not leave both candidates eligible for the same implicit trigger.

Regenerate:

- `documents/skill-knowledge-map.md`
- `documents/SYSTEM-MAP.md`
- any generated skill map maintained by `scripts/build-skill-map.js`

## Tests

Update the locked vid-structure and vid-segment suites together:

- current package fields: `title`, `thumbnail_text`, and `thumbnail_shape`, not `locked_title`
- all seven format plan shapes
- conditional supporting devices and evidence
- structured tension state with optional threads
- bank-link existence and no use-state mutation during planning
- unfinished-dump and critical-gap stops
- first write and partially completed re-structure safety
- first-write Intro and Ending stub preservation
- completed-section thread changes and label-identity edge cases

The current V1 evaluator requires exactly Parable and Principle lines and treats proof as complete whenever the word is absent. It cannot validate this candidate without a coordinated rubric and evaluator revision.
