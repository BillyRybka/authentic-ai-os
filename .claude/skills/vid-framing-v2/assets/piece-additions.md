---
type: asset-template
loaded_by: vid-framing-v2
purpose: Candidate-owned fields and body section written to an existing content piece only after the creator locks one frame
---

# piece.md candidate additions

`piece.md` already exists. Update it in place only after validating `type: content-piece` and matching the slug. Preserve every unowned field and body section.

## Owned frontmatter

```yaml
frame: "{locked first-person spoken strategic promise that leads with the person's desired relief rather than the mechanism}"
core_payoff: "{locked second-person one capability or outcome; it may name the vehicle that fulfills the frame}"
format: short-process | case-study | deep-dive | roast | listicle | news | interview
goal: sales | emails | views  # Required creator intent from the dump, existing piece field, or a direct creator answer. Never infer from channel fit.
voice_context: youtube-script
must_not_become: "{boundary explicitly stated in the dump or piece, or confirmed by the creator before lock}"
last_updated: {YYYY-MM-DD}
```

Add `format-{format}` to the existing `tags` list if it is not already present.

`goal` and `must_not_become` are required before lock. Reuse an explicit value from the selected piece; otherwise ask the creator. Never infer either from general channel fit or a stock boundary.

`voice_context` defaults to `youtube-script`. Use another established medium value only when the existing piece context clearly says the piece is not a YouTube script.

Do not save `must_deliver`. It is a conversational lock-time obligation used to validate the promise. Required missing material triggers a blocker before save.

## Owned body section

Append this section, or replace the existing `## The Read` section on a reframe:

```markdown
## The Read

**Target:** {one recognizable person plus the current situation and behavior that make this video relevant}

**Transformation:** {what they stop doing, what they can do instead, and the same result named by core_payoff}

**Stakes:** {the creator-grounded cost or fear if the current behavior continues}
```

The three fields must trace to the dump, existing piece context, or creator answers from this framing session. They cannot introduce a broader audience, a second payoff, or a stronger claim than the locked frame.

## Write protocol

1. Re-read the current `piece.md` immediately before writing.
2. Confirm its content-piece type and slug.
3. Insert or replace only the owned frontmatter fields.
4. Add the one compatible format tag without changing other tags.
5. Append or replace only `## The Read`.
6. Set `last_updated` to today in `YYYY-MM-DD`.
7. Re-read the saved file and verify unowned fields and sections are unchanged.

## Hard boundary

This candidate never writes or removes `title`, `thumbnail`, `status`, `slug`, `pillar`, `created`, or any other skill-owned field. It never writes `brain-dump.md`. It does not create a new `piece.md`.
