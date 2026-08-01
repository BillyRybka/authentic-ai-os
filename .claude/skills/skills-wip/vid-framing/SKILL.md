---
name: vid-framing
description: Turn a video idea into a decided video. Reads the brain dump and the creator foundation, writes several genuinely different framings of the same idea with a core payoff on each, and recommends one. Once the creator picks, writes the target, transformation and stakes, sets the format and the goal, and saves it all to piece.md before handing to vid-title. Use this whenever a piece needs its direction decided, including when the creator never says the word "frame". Triggers include "frame this video", "pick the angle", "what should this video be about", "what's the angle here", "what part of this do people care about", "re-frame this piece", "I don't know how to position this one", and any point where a creator has an idea but has not decided why anyone would watch it.
---

# Video Framing

A brain dump goes in. Several genuinely different framings come out with a recommendation, the creator picks one, and the piece leaves with its frame, its core payoff, an understanding of the viewer, its format and its goal on disk.

```
Material + avatar → framings + recommendation → pick → the read, format, goal, save
```

Generate first. Do not interview the creator before you have shown them anything.

## Before you start

No `brain-dump.md`, point them at vid-intake. No `creator-foundation.md`, point them at /foundation. If the pipeline invoked this with a slug, do not ask which piece.

If piece.md already has a `frame`, this is a re-frame. Ask whether they want fresh directions or that one sharpened, then run stage 1 or skip to stage 3 with `## The Read` replaced rather than appended.

---

## 1. Generate

**Read:** `references/framing.md` · `references/core-payoff.md` · `content/pieces/{slug}/brain-dump.md` · `foundation/creator-foundation.md` 

Work these out privately. None of it gets shown.

- **Every attempt that did not work**, and what went wrong with each. Somebody who never tried needs what's in the video. Somebody who tried three times needs to know why it keeps failing.
- **What struggle do they think is unique to them?** What would make them feel instantly seen? What shift gives them hope without dismissing the pain?

Now you need to make sure that truly the audience will care about it and that it's written in a way that genuinely speaks to them and uses precise language and puts things in clear relatable terms that would make them understand and identify with it.

Then write the framings. As many as the material genuinely supports, no target number. Each one aimed the audience and coming at it from a different, intriguing angle and would make the audience want to click.

Look at the `references/framing.md` to see real worked examples. It's critical you do this.

One core payoff per framing, third person.

**Screen before you show.** Anything that fails does not get offered and does not get patched, because a framing that needs defending is one the viewer would have to be talked into too.

- The viewer and their failed attempt are identifiable.
- It opens a question the topic alone does not, and a search cannot answer it in a line.
- Something in it makes them feel caught, annoyed, curious or wronged.
- The creator-specific material changes the direction or supplies the proof.
- The mechanism sits where you put it.
- The material can carry the answer with nothing invented.

**Then show it.** Options first, one entry each, blank line between.

1. **{short handle, so they can say "the third one"}**

   {the framing}
   Core payoff: {what they walk away able to do}

Handles never get saved. A handle is title shaped and hands vid-title a headline drafted before it looked at anything.

Say how many you wrote and how many survived, in a clause. Do not list what got cut, because a framing that failed the screen costs attention to read and invites rescuing. The one exception is the creator's own angle: if you cut that, say so and say where it does belong, or they learn to stop offering one.

Then the recommendation and the dial in a separate message: recommend the one with the strongest combination of a real unresolved question, a specific failed attempt, creator-only proof, and a core payoff that changes a decision. Never because it is practical, broad, safe or easy to film. Dial in one line: more, a different direction, sharper, start again.

**If the batch misses**, do not reshuffle. Ask two questions: what had they already tried before this and what kept going wrong, and what angle are they leaning toward. What they tried is almost never in the dump because they solved it and moved on, and their angle carries the phrase they have been using in their own head. Then regenerate. Their angle competes rather than skipping the rotation.

**If everything comes back flat**, that is evidence rather than failure. Say so and give three options: narrow to the part that does have a stake, let a real number carry it, or film it fast knowing the ceiling.

---

## 2. The pick

**Stop. Nothing gets written until they pick.** A clear choice with a reason means it worked. Taking the recommendation with no comment usually means none of them opened anything, so say what you noticed and hand it back rather than deciding for them.

---

## 3. Write the read, set the format, save

**Read:** `references/the-read.md` · `references/format-index.md` · `assets/piece-additions.md`

Ask the cost question first: what does it actually cost them to keep doing it this way. Ask it every time, including when you could write Stakes without it.

Then three fields, third person, one short paragraph each. Target is the loop they are stuck in as a causal chain ending on a cost. Transformation is what they stop doing and do instead. Stakes take that cost and follow what it causes.

State the format and the goal, do not ask. "Short-process, goal emails. Say the word if either is wrong." Format follows the material and the framing. Goal follows how warm the audience is: cold wants views, warm wants emails, hot wants sales. Leave `voice_context` on `youtube-script` unless the piece genuinely is a different medium.

Flip the core payoff to second person. Show the read, then write piece.md, then one line: format, goal, vid-title next.

---

## Before you save

- The saved `frame` is the framing they picked, word for word. If a word changed, say what changed.
- The framing carries one direction, and a viewer under a condition rather than inside a category.
- `core_payoff` names what they can do, decide, diagnose, catch, fix, choose or stop. Second person, one outcome, no second clause bolted on with "and" or "so".
- `core_payoff` reads clearly cold, does not give away the conclusion, and has no fixed opener. "By the end of this video" is the one that grows back.
- Target is a causal chain, not a profile. If "their goal is" or "their pain point is" appears, rewrite it.
- Transformation reaches the same ending as the core payoff.
- Stakes grow out of Target and land back where it started. A wrong diagnosis appears only if the material gives you one.
- Stakes belong to this piece. Put another video's framing on the paragraph, and if it would still be true, replace a consequence.
- Every claim, number and duration traces to the dump, the foundation, or something the creator said. Every gap is a `> [!todo]`.
- `format` is one of the seven and `goal` is set.
- No em-dashes and nothing from the refusals list.

## Never invent

Every framing, core payoff and line of the read traces to the dump, the foundation, or something the creator said in this session. If the material cannot support an angle, it does not get offered, so there is nothing to walk back later. This applies to what you say in conversation, not only what reaches the file. Be most careful with the creator's own history: telling somebody they spent months on something the material never dated asserts a fact about their life back to them.

## Output and handoff

Appends to the piece.md vid-intake created, never touching a field another skill owns. Ownership is in `knowledge/piece-contract.md`, the exact shape in `assets/piece-additions.md`.

Frontmatter: `frame`, `core_payoff`, `mechanism`, `format`, `goal`, `voice_context`, `last_updated`. Body: `## The Read` with Target, Transformation and Stakes, plus any withheld proof as a `> [!todo]`.

Prerequisite: vid-intake. Handoff: vid-title.

| File | When |
|---|---|
| `references/framing.md` | Stage 1 |
| `references/core-payoff.md` | Stage 1 |
| `references/the-read.md` | Stage 3 |
| `references/format-index.md` | Stage 3 |
