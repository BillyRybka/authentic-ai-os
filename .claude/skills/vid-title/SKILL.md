---
name: vid-title
description: Package one video into a title by first naming the video's sharpest claim (the disagreeable true thing it argues), writing titles that make the viewer feel that claim, then leading with the underused on-brand angle competitors are not using (the opportunity), with real competitor proof as the filter. Builds from the creator's `banks/pattern-bank.md`, `banks/title-bank.md`, and `banks/power-words-bank.md`, filtered by the iceberg positioning, grounded in the video's material. Anti-fabrication. Runnable standalone OR invoked by the orchestrator during packaging (after framing, before structure). Triggers on "generate titles", "title options for [video]", "lock the title", "rename this video", "give me angles for this", or when a downstream pipeline needs a locked title.
---

# Video Title Generator

Packages one video into a title. It starts from the single most interesting true thing the video argues (the claim), not the topic. It writes titles that make the viewer feel that claim, explores distinct angle lanes on it, finds the lane that is on-brand AND underused by competitors, and leads with that as the recommendation. The creator picks.

**Scope boundary:** this skill produces THE title. It coordinates with the thumbnail but does not write thumbnail text (that is `vid-thumbnail`), hooks (`vid-intro`), or scripts.

## What this produces

A locked title for one video, saved to `content/pieces/{slug}/piece.md` (the `title:` field), plus the `title_lane:` it came from. The save happens in standalone and pipeline mode. In pipeline mode it also returns the title string to the caller for assembly awareness.

## When to run this

- A video is framed and needs its title locked before structure and scripting
- The creator wants to re-title an existing piece or see fresh angles on it
- `vid-pipeline` invokes during packaging, after framing and before structure

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists with the iceberg, avatar, and Top 3 problems (the iceberg is the filter that finds the on-brand angle)
- `foundation/packaging-system.md` exists with format guidance and packaging defaults
- `content/pieces/{slug}/` exists with at minimum `piece.md` OR a brain-dump / framing artifact explaining what the video is about

If the foundation docs are missing, hard stop. Tell the creator to run `/foundation` first.

If `banks/pattern-bank.md` is missing you cannot do the gap analysis (which lanes are crowded vs underused). Say so, fall back to the `title-bank` patterns plus the BENS framework, and warn that without the competitor data the output will skew safe.

## The engine: the claim first, then differentiation over safety

Two failures make a title flat. The first is describing the topic instead of making a claim: "Claude Cowork Just Dropped Scheduled Agents" announces a product, nobody can disagree with it, so nobody feels anything. The second is reaching for the safe pattern every competitor already runs. This skill fixes both, in that order.

**Idea first, pattern second.** A title is downstream of having something to say. Before any pattern or competitor title is touched, name the video's sharpest claim: the disagreeable true thing it argues. The test is simple, can someone disagree with it? "Scheduled agents dropped in Cowork" is a fact, a label, dead. "Most business owners babysit AI that was built to run without them" is a point of view, alive. Titles get written from the claim. Patterns come in afterward as the filter, never as the seed.

**Quarantine the bank during generation.** Do NOT read `pattern-bank.md`, `title-bank.md`, the power-words bank, or any competitor title until the raw titles are written (Phase 3). The nearest competitor title is gravity: read it early and the output becomes that title with the nouns swapped. Generate cold from the claim, bring the bank in only to pressure-test.

Then, differentiation over safety. The safe title is the one every competitor is already using. The on-brand opposite is the angle that fits the creator's positioning AND that the competitor set underuses, because that is the angle nobody else can run and the one that stands out in the feed.

This is computable, not a vibe, and it happens in Phase 3. Use this order:

1. **The iceberg is the filter.** Read `creator-foundation.md`. An angle that contradicts the creator's positioning is off-brand, no matter how well it performs for someone else. For this creator ("AI should enhance you, not replace you, no slop, you lead"), a pure hype or fake-money angle is off-brand even if it is a proven outlier elsewhere.
2. **The creator's own material leads.** The lock list (below) and any working title from `vid-ideas` come first. Specifics from the video are the raw material every lane is built from.
3. **Competitor data is evidence AND the gap signal.** `banks/pattern-bank.md` records, per pattern, `spread: N of 11 channels`, and per outlier the channel and the view multiplier (xMed). High spread (5+ of 11) means the lane is crowded: proven, but generic, and you blend in. Low spread (1 to 2 of 11) on a lane that still fits the iceberg is the underused angle: the opportunity.

**The target is the lane that is on-brand AND underused. Lead with it.** Mark the crowded lanes as the safe alternative so the creator sees the tradeoff and chooses. Never bury the original angle under the safe ones.

**This skill is a conversation, not a document.** Keep messages short. Do not paste bank contents into chat. The references are what you think with. The creator sees the lane groups and your recommendation.

## Phase 1: Load context, build the lock list, find the claim

**Silent loads** (do NOT paste into chat):

1. `foundation/creator-foundation.md` (iceberg, avatar, Top 3 problems, credibility brags)
2. `foundation/packaging-system.md` (format guidance, packaging defaults)
3. `content/pieces/{slug}/piece.md` (format, goal, pillar, locked angle if framing ran)
4. `content/pieces/{slug}/brain-dump.md` AND/OR `script.md`, whatever exists (the actual material)

**Do NOT open the banks yet.** `pattern-bank.md`, `title-bank.md`, `power-words-bank.md`, and the BENS framework load in Phase 3, as the filter. Reading competitor titles now is what makes the output derivative. Quarantine them.

**Build the lock list.** Every verifiable specific in the material: numbers, dollar figures, percentages, timeframes, AND named methods, tools, products, frameworks, and people. Titles may use only what is on this list. If it is not in the material, it cannot go in a title.

**Find the claim, not the topic.** Read the material and the locked angle from framing, then write three plain-English lines a person would say out loud:

- **The claim:** the single most interesting true thing this video argues. The test is, can someone disagree with it? A fact nobody can argue ("scheduled agents dropped in Cowork") is a label, push past it. A point of view ("most people babysit AI that should run without them") is a claim, keep it.
- **The stake:** what it costs the viewer to not get this. The wound the claim presses on.
- **The belief it challenges:** what the avatar currently does or assumes that the claim cuts against.

These three lines are the seed for every title. Anti-fabrication holds: the claim traces to the material and the framing, it is never invented to sound bigger. If the material has no real claim, only a topic, kick it back to framing rather than dress up a description.

## Phase 2: Write titles from the claim (divergent, bank still closed)

Write 6 to 8 raw titles that each make the viewer FEEL the claim. The bank stays closed. Generate cold, from the claim and the stake, in language the creator would say out loud.

Vary the emotional framing, not the topic. The same claim can be felt as:
- the viewer's problem ("You're still doing X")
- a correction ("Stop doing X")
- a confession ("I did X wrong for years")
- a revelation ("Nobody tells you X")
- a cost ("X is quietly costing you Y")
- an identity line ("Real operators don't do X")

These framings are the lanes. The difference from a flat pattern fill is that each one frames the CLAIM, not the subject. "Why the Babysitting Part of Cowork Is Finally Over" frames the topic and falls flat. "You're Still Babysitting Your AI (You Don't Have To)" frames the claim and opens a wound.

Reach. The point of going wide here is to find the framing that makes the claim land hardest, before any pattern narrows you. The one rule that never relaxes: anti-fabrication. Going wide means trying more real framings, never inventing a number, tool, or name.

## Phase 3: Open the bank, prove the shapes, gap analysis and craft cut (converge)

Now load `pattern-bank.md`, `title-bank.md`, `power-words-bank.md`, and the BENS framework. Group the raw titles into 4 to 5 lanes by their framing. For each lane:

- Map its titles to the `title-bank` `pattern_id` they match (or free-form). A raw title that maps to no proven shape is not auto-cut; flag it as untested and let the creator weigh it.
- Pin one real competitor proof from `pattern-bank.md`: the outlier title, the channel, and its xMed multiplier. The proof shows the shape lands in this niche. Prefer proof whose topic is closest to this video; when only a shape match exists, say so, because a multiplier on an unrelated topic proves the shape, not the title.
- Label **crowded or underused** from the pattern `spread` (5+ of 11 crowded, 1 to 2 underused) and **on-brand or off-brand** from the iceberg.

**Name the opportunity.** The lane that is on-brand AND underused is the opportunity. That is the recommendation. If two qualify, prefer the one whose claim is sharpest for this specific video.

Then put every surviving title through the craft gates, in this order:
- **Claim, not label (first gate):** read the title and ask what the viewer's brain fills in. If the answer is "nothing, it just says what the video is about," cut it. A title that only describes the topic is dead no matter how proven its pattern is.
- Lock-list only (no fabrication)
- Aim for 50 characters, 55 hard ceiling. Flag 51 to 55 as over target but allowed; cut over 55 unless it is clearly strongest, and say why
- Hits at least one BENS letter (annotate which)
- Passes the read-aloud test: one continuous thought a person would say out loud, not stitched fragments, not an invented compound noun, not a mid-title period smash-up
- Carries a lock-list specific that makes it impossible to paste onto another video
- **Title and thumbnail unit check:** prefer titles that leave the thumbnail room to add weight (a face, the number, a bold word) instead of saying the same thing the thumbnail will. If the title and the obvious thumbnail would be the same beat twice, sharpen one of them

Trim each lane to its 1 to 2 strongest titles.

## Phase 4: Present, opportunity first

Open with the claim in one line so the creator sees what every title is framing. Then lead with the opportunity lane, marked Recommended, with one or two sentences on why: it fits the positioning, the competitor set underuses it, and here is the proof. Then list the other lanes, each labeled crowded or underused and on-brand or off-brand, each with its proof. Be a creative partner with a point of view, not a stenographer.

Shape:

```
Recommended lane: Confession (on-brand, underused. Your direct competitors lean hype and
money. Almost nobody in the set runs the honest-reckoning angle, so it stands out and only
you can run it credibly.)

  1. "21 AI Content Mistakes I Made So You Don't"   contrarian-correction  B+N  (44)
  2. "I Got AI Content Wrong for 2 Years"           free-form              N+S  (37)
  proof: "Why Growing A Personal Brand Is An AWFUL Idea" (@ed-lawrence, 7.0x) shows the
  contrarian-honesty shape lands in this niche.

Authority lane (on-brand, CROWDED. Proven, but you blend in with every AI-tips channel.)
  3. "21 AI Content Lessons That Actually Work"     better-than-masses     E+B  (43)
  proof: "Master 95% of Claude Design in 17 Minutes" (@brockmesarich, 28x)

Result lane (CROWDED, watch the iceberg. Only with a real, defensible number.)
  4. "The 21 Lessons Behind a $1.3M Channel"        money-proof            B+S  (42)
  proof: "How This Mom Makes $48K/Month With Claude" (@sabrina_ramonov, 17x)
```

Then ask:

> "Which lane feels closest? I can go wider on the opportunity lane, or push a different tension."

If they want changes:
- "Different tension" means rebuild lanes from a different emotional core
- "Go wider" means more options inside the chosen lane
- "Shorter" means re-cut under 40 characters
- "Play it safer" means surface the crowded high-spread lane as the lead instead
- "More specific" means pull more lock-list specifics into the options

**Push back when a pick is weak:**
- A crowded generic pick: name that it blends in, and offer the on-brand underused lane instead
- A fabricated number or claim: refuse and explain. Only lock-list specifics are allowed
- An off-brand hype pick: flag that it contradicts the positioning and will pull the wrong viewer

## Phase 5: Lock and save

Once picked, save in BOTH modes (the `title:` field is how the pipeline knows packaging advanced, so the write always happens here):
- Save the title to `content/pieces/{slug}/piece.md` `title:` field
- Save the lane it came from to `title_lane:`
- Bump `piece.md` `last_updated:` to today
- Confirm: "Title locked: '{title}' (from the {lane} lane). Saved to piece.md."

Pipeline mode also returns the title string and BENS letters to the caller for assembly. The piece.md write still happens here.

**Stop.** Do not generate the thumbnail, hook, or script. Those are different skills.

## Anti-fabrication discipline

Every number, name, method, tool, framework, or specific phrase in a title MUST trace to the material or foundation docs. If it is not there, the title cannot claim it, in any lane, including the divergent pass.

If the creator wants a number-driven title and the material has no usable number, kick it back: "The script has no number to ground this. Add the number to the script first, or pick a lane that does not lean on one." A made-up number is the exact slop this brand is built against.

## Title and thumbnail pairing

The title and thumbnail are one unit. They make the same promise and they do not repeat the same words. Two coordination rules:
- In Phase 3, run the unit check: prefer a title that leaves the thumbnail room to add a different beat (a face, the number, a bold word), not one the thumbnail will only echo.
- If `vid-thumbnail` already produced a `thumbnail-brief.md` for this piece, read its picks and avoid repeating their key words in the title.

vid-title runs first, does not wait on the thumbnail, and does not write thumbnail text. If the thumbnail has not run, just lock the title; `vid-thumbnail` will respect the title's words later (the rule lives in `knowledge/thumbnail-text-patterns.md`).

## Principles

- **Claim, not label.** A title that only describes the topic is dead. Make a point someone could disagree with.
- **Generate before you reference.** Write titles from the claim with the bank closed. Bring competitor data in only to pressure-test, never to seed.
- **Differentiation over safety.** The widest-spread pattern is the crowded center. Lead with the on-brand angle the competitor set underuses.
- **Lead with the tension, not the topic.** The viewer feels the frame before they read the words.
- **The iceberg is the filter.** On-brand first. An off-brand outlier is still off-brand.
- **Prove the shape.** Pin a real competitor outlier and its multiplier to every lane, so a recommendation is evidence, not taste.
- **Specificity wins.** Real numbers over round numbers. Named methods over generic verbs. A specific person or situation over "people."
- **Read aloud is the voice test.** If the creator would reword it speaking it, it is wrong.
- **Creator drives, Claude structures.** Never invent a claim to make a title sound bigger.

## Reference index

- `banks/pattern-bank.md`: competitor outliers with spread and xMed multipliers (gap-finder + proof)
- `banks/title-bank.md`: fill-in patterns, each with `pattern_id` and `spread`
- `banks/power-words-bank.md`: words by when-it-lands / when-it-fails
- `references/title-filters.md`: the angle-lane frame menu, the soft-filter catalog, pattern shapes, and craft notes (load on demand)
- `knowledge/BENS-framework.md`: Big / Easy / New / Safe
- `foundation/creator-foundation.md`: iceberg (the on-brand filter), avatar, Top 3
- `foundation/packaging-system.md`: format guidance, packaging defaults
- `content/pieces/{slug}/*`: the video's material

## Related skills

- `/foundation` produces `creator-foundation.md`; `vid-research` produces `packaging-system.md`, `pattern-bank.md`, `title-bank.md`, and `power-words-bank.md`, the files this skill reads
- `vid-framing` runs before this skill and locks the CONTENT angle (the argument). This skill packages that content into a title: it explores PACKAGING lanes, it does not re-argue the video
- `vid-thumbnail` is a separate skill that runs after and writes the thumbnail text. This skill only coordinates with it, it never writes thumbnail text
- `vid-ideas` may have surfaced a provisional working title; treat it as one input, free to beat or discard
- `vid-pipeline` orchestrates and calls this skill during packaging
- `vid-measurement` (future) logs winning titles and their lanes back into the banks
