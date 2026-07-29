---
type: asset-template
loaded_by: vid-framing
purpose: The frontmatter fields + body sections vid-framing APPENDS to content/pieces/{slug}/piece.md
---

# piece.md framing additions

vid-intake created piece.md. vid-framing appends its decisions to that file and never touches a field another skill owns.

## Frontmatter fields to add

Insert under the existing lifecycle fields (`slug`, `pillar`, `created`, `status`).

```yaml
# Written by vid-framing
frame: "{the chosen video, described in third person: 'A video that shows {who} how to {the change}, {the condition that makes it theirs}.' Never a spoken line, never a headline, never a description of the contents}"
core_payoff: "{the one concrete thing the viewer ends up holding, second person: 'By the end of this video you'll have [the thing], [and what that means you stop doing].' One deliverable, plain words, no bonus asset}"
mechanism: "{what actually produces the result, plus its kind: delivery | draw | qualifier. Delivery stays out of the frame; draw carries it; qualifier narrows it}"
format: short-process | case-study | roast | deep-dive | interview | news | listicle
goal: sales | emails | views
voice_context: youtube-script   # default. Another medium (tutorial | shorts | newsletter | linkedin | twitter | instagram | podcast | casual | talk) only if this piece genuinely is one. Drives which foundation/reference-pieces/{voice_context}.md the writing skills load.
last_updated: {YYYY-MM-DD}
```

vid-framing does not set a status. The piece stays `status: ideating` until vid-structure moves it to `drafting`. The orchestrator knows framing is done because `frame` is present.

`core_payoff` lives in frontmatter only. It is locked with the frame, before the read exists, so there is no second copy for it to drift against.

## Body sections to append

### The Read

Three fields, third person, in the words the creator confirmed. vid-title presses on the Stakes, vid-intro mines them for hooks, vid-structure builds toward the Transformation. Left in the conversation it is gone by the next session.

```markdown
## The Read

**Target:** {who this is for and the situation, as one causal chain: they want something, but this keeps happening, so they end up doing this, which costs them that. No "their goal is / their challenge is" scaffold. The middle of the chain is the move that keeps them stuck, and it comes out of the material or it is not there}

**Transformation:** {they stop doing X and do Y instead, plus what that gets them}

**Stakes:** {"if they keep working the old way," then each consequence causing the next, sentences tightening as it escalates, the misattribution named near the end, landing back where Target started}
```

Never compress a field away to save space. Target with no cost at the end of it is a demographic. Stakes that do not escalate are one sentence of consequence. A Transformation with no "stop doing X" is a feature description. Each field is what a different downstream skill reads.

Read all three aloud before writing them. Anything the creator would pause and reword gets fixed first: plain nouns where the thing has a name, one image per field rather than three stacked, and the cost put in front of the reader rather than described from a distance.

On a re-frame, replace this section. It describes the current frame, not a history.

### Considered + Dropped Angles

The frames that lost, one line each, grouped by the rotation that produced them. Terse: enough to recognise it, enough to know why it is not the video.

```markdown
## Considered + Dropped Angles

> [!quote] Rotated {YYYY-MM-DD}
> - {frame, cut to its distinguishing clause}. {Why it lost, one clause.}
> - {next}. {Why.}
```

Append-only across re-frames, and never re-offered unless the creator asks. Option handles from the conversation are never written here. The frame is what gets recorded, because a handle is title-shaped and vid-title should arrive with nothing pre-written.

### Proof gaps

If the creator withheld a number, a client detail, or a bank entry they have not captured, flag it in the body. Keep it out of `frame` and `core_payoff`:

```markdown
> [!todo] Proof gap: {what is missing}, mark it and pull it later. {YYYY-MM-DD}
```

## Append protocol

1. Read the existing piece.md frontmatter. Confirm `type: content-piece` and that the `slug` matches.
2. Insert the framing fields after the last lifecycle field. Preserve every existing field untouched.
3. Set `last_updated` to today.
4. Write `## The Read`. On a re-frame, replace the existing section.
5. Append to `## Considered + Dropped Angles`, never overwriting earlier entries. Proof-gap `> [!todo]` lines go here too.
6. Write the file.

## Hard rules

- Never overwrite frontmatter owned by another skill. The ownership map is in `knowledge/piece-contract.md`.
- Never delete previous "Considered + Dropped" entries. Append only. `## The Read` is the one section that gets replaced.
- Never fabricate. The frame, the read, and the payoff trace to the brain-dump, the foundation, or something the creator said in the session. A gap is named, never invented.
- Keep `frame` and `core_payoff` clean. No embedded TODOs, no explanation clause, no colon-summary.
- `frame` is never a title and never a spoken line. If it reads like either, rewrite it as the description of the video and let vid-title do the selling.
- `mechanism` carries its kind. Without that word the field cannot be used by anything downstream.
- Always set `last_updated` to today in YYYY-MM-DD.
