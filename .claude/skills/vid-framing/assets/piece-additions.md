---
type: asset-template
loaded_by: vid-framing
purpose: The frontmatter fields and body sections vid-framing appends to content/pieces/{slug}/piece.md
---

# piece.md framing additions

piece.md already exists. Append to it, never create it, and never touch a field another skill owns.

## Frontmatter to add

Insert under the existing lifecycle fields (`slug`, `pillar`, `created`, `status`).

```yaml
# Written by vid-framing
frame: "{the locked Frame, first person and spoken, one direction only. The who is a thing the viewer physically does, the what has a handle they already own, the clause after the verb carries the insight, and the verb is physical. Never a headline, never a description of the contents}"
core_payoff: "{what they walk away able to do, second person, one outcome. Reads clearly to somebody who has not seen the material, and does not give away the conclusion}"
format: short-process | case-study | roast | deep-dive | interview | news | listicle
goal: sales | emails | views
voice_context: youtube-script   # default. Another medium (tutorial | shorts | newsletter | linkedin | twitter | instagram | podcast | casual | talk) only if this piece genuinely is one. A walkthrough is still a YouTube script.
last_updated: {YYYY-MM-DD}
```

Add `format-{format}` to the existing `tags` list.

Do not set `status`. The piece stays `ideating`, and the presence of `frame` is what signals framing is done.

`core_payoff` lives in frontmatter only. It locks with the Frame before the read exists, so there is no second copy anywhere for it to drift against.

It is shown to the creator in second person and it saves in second person, the same words both times. Nothing gets added on the way to disk.

## Body to append

### The Read

Three fields, third person, in the words the creator confirmed at Step 2. 

```markdown
## The Read

**Target:** {who this is for and the situation, as one causal chain: they want something, but this keeps happening, so they end up doing this, which costs them that. No "their goal is / their challenge is" scaffold. The middle of the chain is the move that keeps them stuck, and it comes out of the material or it is not there}

**Transformation:** {they stop doing X and do Y instead, plus what that gets them. Names the same ending as core_payoff}

**Stakes:** {what happens if they keep working the old way, each consequence causing the next, sentences tightening as it escalates, landing back where Target started. Name what they blame instead where the material says so, and leave it out where it does not}
```

Never compress a field away to save space. Target with no cost at the end of it is a demographic. Stakes that do not escalate are one sentence of consequence. A Transformation with no "stop doing X" is a feature description. Each field is what a different downstream skill reads.

Read all three aloud before writing them. Anything the creator would pause and reword gets fixed first: plain nouns where the thing has a name, one image per field rather than three stacked, and the cost put in front of the reader rather than described from a distance.

On a re-frame, replace this section. It describes the current frame rather than a history.

The options that lost stay in the conversation. Nothing reads them later, and their working labels are title shaped, so saving them commits a headline before anything has looked at what already works on this channel.

### Proof gaps

If the creator withheld a number, a client detail or something they have not captured yet, flag it in the body and keep it out of both `frame` and `core_payoff`.

```markdown
> [!todo] Proof gap: {what is missing}, mark it and pull it later. {YYYY-MM-DD}
```

## Append protocol

1. Read the existing piece.md frontmatter. Confirm `type: content-piece` and that the `slug` matches.
2. Insert the framing fields after the last lifecycle field, preserving every existing field untouched.
3. Add `format-{format}` to `tags`.
4. Set `last_updated` to today.
5. Write `## The Read`. On a re-frame, replace the existing section.
6. Add any proof-gap lines to the body.
7. Write the file.

## Hard rules

- Never overwrite frontmatter owned by another skill. The ownership map is in `knowledge/piece-contract.md`.
- Never fabricate. The frame, the read and the payoff trace to the brain-dump, the foundation, or something the creator said in the session. A gap is named rather than invented.
- `frame` carries one direction and the condition that makes this viewer specific. Two benefits joined with a comma means the choice was never made, and a who with no condition is a category rather than a person.
- `core_payoff` holds one outcome, which is not the same as one clause. "Five reasons people don't buy and how to overcome those objections" runs two clauses and delivers a single capability, and that is fine. "You'll have the list, and you'll never think about AI writing the same way again" is two payoffs bolted together, and "and you'll" is the tell. So is a colon that introduces a second thing, and so is a trailing "so" clause that restates the first half in softer words.
- If `core_payoff` keeps coming out as a pile of features, the Frame underneath it is vague. Sharpen the Frame rather than rewriting the payoff.
- `core_payoff` carries no fixed opener. "By the end of this video" is the specific one that keeps growing back.
- Always set `last_updated` to today in YYYY-MM-DD.
