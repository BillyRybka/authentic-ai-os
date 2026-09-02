---
type: asset-template
loaded_by: vid-framing
purpose: Candidate-owned fields and body section written to an existing content piece only after the creator approves one package
---

# piece.md candidate additions

`piece.md` already exists. Update it in place only after validating `type: content-piece` and matching the slug. Preserve every unowned field and body section.

## Owned frontmatter

```yaml
frame: "{approved first-person spoken strategic promise using sourced or creator-confirmed audience language for pain and relief; include a named mechanism only when it is the compelling audience-facing handle}"
core_payoff: "{approved direct second-person end capability; it may name the vehicle that fulfills the frame}"
format: step-by-step | success-story | deep-dive | review | list-video | news | interview
goal: sales | emails | views  # Required explicit creator intent. Never infer from channel fit.
voice_context: youtube-script
must_not_become: "{optional boundary explicitly stated in the selected material or confirmed when a real ambiguity required it}"
last_updated: {YYYY-MM-DD}
```

Add `format-{format}` to the existing `tags` list if it is not already present.

`goal` is required before approval and must come from the selected piece or a direct creator answer. Never infer it from channel fit.

`must_not_become` is optional. Write it only when the selected material establishes a boundary or a real ambiguity led the creator to confirm one. Omit it otherwise; never invent a stock boundary.

`voice_context` defaults to `youtube-script`. Use another established medium value only when the existing piece context clearly says the piece is not a YouTube script.

Do not save `must_deliver`. It is a conversational obligation used after intent is clear to validate that the promise can be filmed and supported.

## Owned body section

Append this section, or replace the existing `## The Read` section on a reframe:

```markdown
## The Read

**Target:** {one recognizable person plus the current situation and behavior that make this video relevant, using sourced or creator-confirmed audience language}

**Transformation:** {what they stop doing, what they can do instead, and the same result named by core_payoff}

**Stakes:** {the audience-grounded cost or fear if the current behavior continues; never invent audience wording or source support}
```

The three fields must trace to the dump, selected piece context, supplied audience-language sources, or creator answers from this framing session. They cannot introduce a broader audience, a second payoff, or a stronger claim than the approved Frame.

## Write protocol

1. Write only after the creator explicitly approves saving the package, then re-read the current `piece.md`.
2. Confirm its content-piece type and slug.
3. Insert or replace only the owned frontmatter fields.
4. Add the one compatible format tag without changing other tags.
5. Append or replace only `## The Read`.
6. Set `last_updated` to today in `YYYY-MM-DD`.
7. Re-read the saved file and verify unowned fields and sections are unchanged.

## Hard boundary

This candidate never writes or removes `title`, `thumbnail`, `status`, `slug`, `created`, or any other skill-owned field. It never writes `brain-dump.md`. It does not create a new `piece.md`.
