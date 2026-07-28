---
type: asset-template
loaded_by: vid-framing
purpose: The frontmatter fields + body section vid-framing APPENDS to content/pieces/{slug}/piece.md
---

# piece.md framing additions

vid-framing does NOT create piece.md. vid-intake created it. vid-framing appends its framing decisions to the existing file without touching another skill's fields.

## Frontmatter fields to add

Insert under the existing frontmatter (after the lifecycle fields `slug`, `pillar`, `created`, `status`). Do not touch fields owned by other skills.

```yaml
# Written by vid-framing
selected_angle: "{one clean sentence naming what the video argues, in the creator's voice. Argument-shaped, not headline-shaped: it says what is true and what it costs, it does not sell the click. No explanation clause, no colon-summary, no TODO text inside}"
core_payoff: "{the deliverable: what the viewer will have, know, or be able to do after watching. One or two sentences: 'By the end of this video, coaches will have a discovery call structure that surfaces the real objection while the prospect is still on the line.' Not a diagnosis of their problem, not a thesis. Identical to the Core payoff field in the body's ## The Read}"
format: short-process | case-study | roast | deep-dive | interview | news | listicle
goal: sales | emails | views
voice_context: youtube-script   # default. Set to another medium (tutorial | shorts | newsletter | linkedin | twitter | instagram | podcast | casual | talk) only if this piece genuinely is one. Drives which foundation/reference-pieces/{voice_context}.md the writing skills load.
last_updated: {YYYY-MM-DD}
```

vid-framing does not set a status. The piece stays `status: ideating` until vid-structure moves it to `drafting`. The orchestrator knows framing is done because `selected_angle` is present.

## Body sections to append

The read goes on disk, all four fields, in the words the creator confirmed and in third person. vid-title presses on the Stakes, vid-intro mines them for hooks, and vid-structure builds toward the Transformation. If it only lives in the conversation it is gone by the next session.

```markdown
## The Read

**Core payoff:** {"By the end of this video you'll have [the one concrete thing], [and what that means you stop doing]." Second person, one deliverable, plain words. Identical to the `core_payoff` frontmatter value}

**Target:** {who this is for and the situation, as one causal chain: they want something, but this keeps happening, so they end up doing this, which costs them that. No "their goal is / their challenge is" scaffold. Blind spot only when the material has one}

**Transformation:** {they stop doing X and do Y instead, plus what that gets them}

**Stakes:** {"if they keep working the old way," then each consequence causing the next, sentences tightening as it escalates, the misattribution named near the end, landing back where Target started}
```

Never compress a field away to save space. Target with no cost at the end of it is a demographic, Stakes that do not escalate are a single sentence of consequence, and a Transformation with no "stop doing X" is a feature description. Each field is what a different downstream skill reads.

Before writing the section, read all four fields aloud. Anything the creator would pause and reword gets rewritten first: plain nouns where the thing has a name, one image per field rather than three stacked, and the cost put in front of the reader rather than described from a distance. A read that is structurally perfect and unsayable hands the writing skills nothing.

On a re-frame, replace this section rather than appending a second copy. It describes the current frame, not a history.

```markdown
## Considered + Dropped Angles

> [!quote] Angle: {dropped angle}
> Why: {one line, e.g. "didn't match the brain-dump material", "wrong audience", "weaker than the pick"}
> Date: {YYYY-MM-DD}
```

Sticky. A re-frame must not resurface these unless the creator asks.

If the creator withheld proof (a number, a client detail, a bank entry they have not captured), add a one-line TODO in the body so the gap is flagged. Keep it OUT of `selected_angle` and `core_payoff`:

```markdown
> [!todo] Proof gap: {what is missing}, mark it and pull it later. {YYYY-MM-DD}
```

## Append protocol

1. Read the existing piece.md frontmatter. Confirm `type: content-piece` and the `slug` match.
2. Insert the framing frontmatter fields after the last lifecycle field. Preserve every existing field untouched.
3. Set `last_updated` to today.
4. Write `## The Read` to the body. On a re-frame, replace the existing section.
5. Append `## Considered + Dropped Angles` to the body. On a re-frame, keep the section append-only (never delete previous drops). Add any proof-gap `> [!todo]` lines here too.
6. Write the file.

## Hard rules

- Never overwrite frontmatter fields owned by other skills. The field-ownership map lives in `knowledge/piece-contract.md`.
- Never delete previous "Considered + Dropped" entries. Append only. `## The Read` is the one section that gets replaced instead.
- Never fabricate. The angle, the read, and the payoff trace to the brain-dump and foundation; a gap is named, never invented.
- Keep `selected_angle` and `core_payoff` clean, no embedded TODOs. Withheld proof goes in a body `> [!todo]`.
- `core_payoff` and the read's Core payoff field are the same sentence. If they drift, the frontmatter is what downstream skills load, so fix the body to match it.
- `selected_angle` is never a title. If it reads like one, rewrite it as the argument underneath and let vid-title do the selling.
- Always set `last_updated` to today in YYYY-MM-DD.
