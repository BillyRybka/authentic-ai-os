---
name: vid-segment
description: Build one body segment of a video script as a parable then a principle then a transition (emotion brick to show, logic brick to tell, handoff to the next point). Format-aware (deep dive, listicle, case study, short process, news, roast, interview), bank-pulling (story, proof, metaphor, testimonial, framework), and runs an internal two-pass review (structure first, then prose) before saving. Standalone OR invoked by vid-pipeline once per body segment in the script phase. Triggers on "write segment", "draft point", "build the next point", "write point [N]", "expand step [N]", "next body segment", or when an orchestrator asks for one segment of script body.
---

# Video Segment Writer

Build ONE body segment as a parable, then a principle, then a transition. Show, then tell, then hand off to the next point, in the creator's voice, pulling from the evergreen banks. Two passes: structure first (does the segment work as a unit?), prose second (does it sound like the creator?). Save only when both pass.

**Scope boundary:** this skill writes ONE segment at a time. It does not write the intro (`vid-intro`), the ending (`vid-ending`), the title (`vid-title`), or the thumbnail (`vid-thumbnail`). It also does not assemble the full skeleton (`vid-structure`). For a multi-segment body, the creator or the orchestrator runs this skill once per segment.

This skill loads `knowledge/vault-integration.md` at session start for the save contract (entry schemas, the wikilink rule, the "update both sides" rule). The vault's own writing principles live in the vault `CLAUDE.md`; this file is the per-write schema.

## What this produces

The segment's prose appended to `content/pieces/{slug}/script.md` under a heading that names the segment. Frontmatter side-effects on the piece's `piece.md` (`stories_used`, `proofs_used`, `metaphors_used`, `segments_completed`) plus matching `used_in:` updates on every bank entry pulled. When invoked as a sub-skill, the prose string is also returned to the caller so the orchestrator can place it.

## When to run this

- A piece is in script-writing phase and the next body segment needs to be drafted
- The orchestrator (`vid-pipeline`) invokes one segment at a time
- A creator wants to revise or rebuild a single segment without touching the rest of the script
- A previously-written segment failed review and needs a structure-first rebuild

Not for: writing the whole body in one shot (loop the skill per segment), bank capture (route to `vid-capture`), assembling the full script skeleton (`vid-structure`).

## Prerequisites

Hard requirements:

- `foundation/voice-profile.md` exists (the guardrail) and `foundation/reference-pieces/` has at least the default `youtube-script` context (the voice engine these writing skills write from)
- `content/pieces/{slug}/piece.md` exists with at minimum `format`, `goal`, and `pillar`
- `content/pieces/{slug}/brain-dump.md` AND/OR `piece.md` exists with the segment's raw material

Optional but used when present:

- `content/pieces/{slug}/script.md` (so the locked skeleton and prior segments inform the segment shape and transition continuity)
- The relevant bank folders (`banks/story-bank/`, `banks/proof-bank/`, `banks/metaphor-bank/`, `banks/testimonial-bank/`, `banks/framework-bank/`)

If the voice files are missing, hard stop. Tell the creator to run `vid-voice-capture` first.

If `content/pieces/{slug}/brain-dump.md` and `piece.md` are both missing, hard stop. The segment has no source material. Route the creator to `vid-intake` (raw capture) or `vid-framing` (decide angle / format / payoff) first.

## Invocation modes

**Standalone.** Creator invokes directly to write or rebuild one segment. The skill loops the two-pass review with the creator until lock, saves to script.md, updates banks, ends.

**Sub-skill.** The orchestrator (`vid-pipeline`) invokes it mid-pipeline, once per segment. The caller passes a context packet (segment's purpose, format, prior-segment closing line, locked title and intro). Skip questions the caller has already answered. Return the locked prose string plus the packet of bank wikilinks pulled.

If invoked with a caller packet that already names the format, segment purpose, and any locked banks to pull, skip Phase 1 questions and go straight to Phase 2 (structure pass).

## The walkthrough (4 phases)

This skill is a conversation, not a document. Keep messages short. Never paste reference content into chat. References are for YOUR thinking. The two-pass review is the spine: lock the structure first with the creator, then write the prose, then run the voice check, then save.

### Phase 1: Load context and frame the segment

**Silent loads** (do NOT paste into chat):

1. `knowledge/vault-integration.md` (the save schema, wikilink contract, "update both sides" rule, failure modes)
2. `foundation/voice-profile.md` (the thin guardrail: fingerprint, signature phrases, refusals, POV/energy. Always loaded. See `knowledge/voice-profile-schema.md` for the load contract)
3. `foundation/reference-pieces/{voice_context}.md` (the voice engine: real intact passages to write from, as `## ` sections in one file matched to piece.md `voice_context`, default `youtube-script`. If absent, seed from the guardrail fingerprint and note the gap). **Voice only, not structure:** the passages carry cadence, word choice, register, and signature moves. Segment architecture (parable then principle then transition, the format-planner shape) is fixed by THIS skill's spec and the format planner. If a passage's structural arc conflicts, follow the spec.
4. `knowledge/format-planners/{format}.md` (matched to `piece.md` `format:`. The one planner for THIS piece's format, not the others)
5. `knowledge/voice-rhythm.md` (the lens for hearing rhythm in the reference pieces and the draft; no stored numbers)
6. `knowledge/voice-pressure-test.md` (the in-skill voice check run before save; this is the lightweight read-aloud + guardrail check, NOT the multi-agent `vid-pressure-test` skill)
7. `content/pieces/{slug}/piece.md` (format, goal, pillar, voice_context, locked title, prior `stories_used` / `proofs_used` / `metaphors_used`)
8. `content/pieces/{slug}/brain-dump.md` (the segment's raw material: locked angle, core payoff, point list, the creator's actual words)
9. `content/pieces/{slug}/script.md` (if it exists: the locked skeleton section this segment fills, the prior-segment closing line for transition continuity, and the `## Blocks to capture` list so you know which open blocks this segment still owes)
10. Skill-local references: `references/parable-principle-shapes.md`, `references/framework-shapes.md` (this skill's runtime decision logic). Plus shared craft knowledge, each loaded only when its block type is in play: `knowledge/parable-decision-matrix.md`, `knowledge/story-pulling-criteria.md`, `knowledge/proof-placement-rules.md`, `knowledge/metaphor-integration.md`, `knowledge/framework-builder.md` (inline framework crafting when the principle is a framework and no bank match exists), `knowledge/visual-demo-builder.md` (inline visual demo crafting when the parable is a Visual Demo, since there is no Visual Demo bank)
11. `knowledge/visual-proof-callouts.md` (the canonical `> [!important] Visual proof needed` callout convention. Load when the principle makes a numbered, named, or before/after claim the editor must put on screen)
12. `banks/transition-bank.md` (Section 2 segment-to-segment patterns plus Section 4 banned phrases for the segment's outbound transition)
13. The bank folders for the block types this segment pulls (`banks/story-bank/`, `banks/proof-bank/`, `banks/metaphor-bank/`, `banks/testimonial-bank/`, `banks/framework-bank/`), plus the matching capture guide only if a capture is triggered (`story-capture-guide.md` / `proof-capture-guide.md` / `metaphor-builder.md` / `testimonial-capture.md`)
14. `content/pieces/{slug}/async-block-notes.md` (if it exists: a jot pad for ideas about OTHER segments that surfaced during prior writing. Check it for notes tagged with this segment's purpose before brainstorming from scratch)

**Frame the segment.** Pull the segment's job from the locked skeleton in `script.md` and the angle in `piece.md` (e.g. "step 1 of 5", "point 3 of 7", "the case-study Action beat", "the news 'why it matters' beat"). Confirm with the creator in one short message:

> "Segment job: {one-line restatement}. Format: {format}. This segment's payoff: {core payoff fragment}. Sound right? Anything to sharpen before I draft the structure?"

Wait. Lock segment job. If the creator sharpens, update the framing then continue.

**Read the shape, don't re-derive it.** vid-structure already wrote a format-specific skeleton section for this segment (its material anchors, block candidates, and tension role). Read that section. The `knowledge/format-planners/{format}.md` you loaded defines how THIS format weights the two bricks: most formats run a full parable then principle per point, short-process steps run lean (principle-only, add a parable inside a step only when it is hard or the viewer won't believe it), and a case study runs the whole body as one parable with the principle landing at the end. Apply the planner's shape for this format. Do not recite or compare the other formats.

If the format planner conflicts with the segment job the creator just confirmed, surface the conflict. Don't silently override either.

### Phase 2: Structure pass (FIRST internal review)

Goal: the segment works AS A UNIT before any prose gets written. If the structure is broken, no amount of voice polish saves it.

**Draft the segment structure.** A structure draft is bullets and slot fills, not prose. The parable, the principle, the transition:

1. **Parable (the show).** The emotional open: how this segment shows the problem, the transformation, or the proof. Visual demo / story / metaphor / contrast / breakdown. Use the parable decision matrix in `knowledge/parable-decision-matrix.md` to pick the type. The parable IS the open; it carries what the viewer feels before the lesson arrives. Pulls from brain-dump phrasing and the segment's own material. (Lean steps can skip the parable and run principle-only, per the format shape.)
2. **Principle (the tell).** The lesson the viewer can action: the framework and its components, the proof shown AFTER the framework lands, and the one sharp takeaway line they walk away with.
3. **Transition (the handoff).** The forward-hook into the next point (per `banks/transition-bank.md` Section 2), or the body-to-ending bridge if this is the final body segment. This is the segment's contribution to the script's tension, the little setup that pulls the viewer forward. Whether this segment carries the title-promise payoff or opens/closes a thread is set in vid-structure and recorded in piece.md; read it, don't re-derive it.

**Bank-pulling logic** (the differentiator of this skill). Given the segment's job, query the banks:

- **Story.** Query `banks/story-bank/*.md` by `illustrates` line and theme tags. Filter to entries whose `illustrates` lesson maps to the segment's point. Surface 0-3 candidates (not more; choice paralysis kills the flow).
- **Proof.** Query `banks/proof-bank/*.md` by `proof_type` and theme tags. Filter to entries whose "What it proves" sentence backs the segment's framework or claim. Surface 0-2 candidates.
- **Metaphor.** Query `banks/metaphor-bank/*.md` by `concept:` field and theme tags. Filter to entries that clarify an abstract piece in the segment's logic. Surface 0-2 candidates.
- **Testimonial.** Query `banks/testimonial-bank/*.md` for entries that match the claim being made. Use sparingly. Testimonials work best as social proof inside a segment, not as the segment's spine.
- **Framework.** Query `banks/framework-bank/*.md` for the creator's named system the segment is teaching. If the segment is built around a creator-owned framework, name it explicitly in the structure draft.
- **Visual Demo.** No bank to query. If the parable is Visual Demo (per the parable decision matrix), load `knowledge/visual-demo-builder.md` and run the 3-step brainstorm inline (name the point, pick sub-type, generate 2-3 candidate demo concepts, creator picks). The demo lands directly in the prose. No save target.

For each pulled candidate, surface to the creator with: slug + one-line summary + WHY this candidate matches the segment's job. Use `knowledge/story-pulling-criteria.md`, `knowledge/proof-placement-rules.md`, `knowledge/metaphor-integration.md` to filter. They teach contrastive examples of what lands vs. what misses.

**The "no fabrication" gate** (same as `vid-title` and `vid-thumbnail`): if a story / proof / metaphor / testimonial / framework isn't in the banks, the skill does NOT invent it. Three options when banks come up empty:

1. Route to `vid-capture` mid-skill (sub-skill mode) to capture the missing entry, then return with the new wikilink and continue. For Framework, this means: load `knowledge/framework-builder.md`, walk the creator through the 5-step build inline (dump, result, top 3, shape, name), route to vid-capture Stage F to save the locked framework, then return with the wikilink and continue. The creator never leaves vid-segment's flow.
2. Tell the creator the bank is empty for this slot, ask if they want to skip the block (use a different block type) or pause to capture material first.
3. For Visual Demo specifically: there's no bank to capture into. Always run the inline 3-step brainstorm using `knowledge/visual-demo-builder.md`.

**Clearing the gap manifest.** vid-structure may have written open rows into the `## Blocks to capture` list at the bottom of script.md (the inline-later path). Before brainstorming a block from scratch, check that list for a row tagged to this segment. If there is one, it names exactly what to capture. When you capture it (option 1) or consciously cut it (option 2), delete its row from `## Blocks to capture` and replace the section's "no match" placeholder with the real `[[wikilink]]`. If the creator chose batch capture at the structure seam, the list is already empty and this is a no-op.

Never invent client names, numbers, results, or specific phrasings. The brain dump is the only allowed source of new specifics, and only because the creator wrote it.

**Async-block-notes (ideas for OTHER segments mid-write).** If an idea pops up for a different segment while writing this one, DON'T break flow to capture it. Jot a one-line note in `content/pieces/{slug}/async-block-notes.md` (create the file lazily on first note). Format: `- [Segment M, block type]: quick idea`. When this skill later writes that segment, it scans the file in Phase 1 and surfaces relevant notes during the brainstorm.

**Surface the structure draft.** Format:

```
SEGMENT: {short label, e.g. "Step 2: Refactor your week"}

PARABLE (the show): {Visual Demo (Show-the-Problem | Contrast | Breakdown) | Story | Metaphor | none for a lean step}
  - Bank candidates: [[story-slug-1]] (theme: scheduling) | [[story-slug-2]] (theme: deep-work)
PRINCIPLE (the tell): {framework move + proof position + the one-line takeaway}
  - Framework: [[framework-slug]] (or "no framework, single lesson")
  - Proof candidates: [[proof-slug]] (client-win) | [[proof-slug-2]] (personal-result)
TRANSITION (the handoff): {one of the Section 2 patterns from transition-bank, slot-filled with this segment's takeaway}
```

Then ask:

> "Structure check. Does this segment do its job? Pick one: lock structure, swap the block (story to metaphor / etc.), pull a different bank candidate, sharpen the payoff, scrap and start over."

Wait. Loop until structure locks. **Do not write prose until structure locks.** This is the core architectural decision of the skill: structure dictates voice, not the other way around.

### Phase 3: Prose pass (SECOND internal review)

Now write the segment in the creator's voice. The structure is locked; this phase preserves it while solving for voice rhythm and word-level fidelity.

**Voice anchoring.** Three sources, in order:

1. **Brain dump phrasing.** If the brain dump contains the creator's actual words for this segment's idea, use those words. Don't polish into "better" prose. The brain dump IS the voice.
2. **Reference pieces (the seed).** Load `foundation/reference-pieces/{voice_context}.md` matching this piece's `voice_context` (default `youtube-script`). Read all the `## ` sections together to internalize the creator's combined cadence (sentence-length variation, paragraph shape, opener move; use `voice-rhythm.md` as the lens). When the beat you are writing matches what a section's `> Demonstrates:` line describes, let that section weight the cadence most, by feel. Write fresh prose from the brain dump in that grain; never echo a section's words. The set is voice grain only, not a structural template.
3. **Guardrail (constraint only).** From `voice-profile.md`: refusal anti-patterns and creator hard rules are hard rejects, words-avoided are soft rejects with auto-swap, a signature phrase surfacing once or twice in long-form is a healthy signal (never pad to hit it).

**Per-block writing.**

- **Parable prose (the show).** The segment opens on the parable. Pull verbatim from the brain dump where possible. If the creator wrote "I was staring at my inbox at 2am wondering when this stopped being fun," that line goes in. Match the opener move the reference pieces use (declaration / question / anecdote / contrarian). For visual demos, the bank entry's body gives you both layers: the spoken layer goes in script, the shown layer goes in a `> [!note] visual:` callout for the production team. For stories, follow the bank entry's Problem-Action-Outcome verbatim. For metaphors, drop the metaphor in clean (no "let me give you an analogy" announcement; just say it), then use the bank's pivot phrase to bridge to the principle. Lean steps skip the parable and open straight on the principle. The open runs short: 1-3 sentences for tight formats (news, short process), 3-6 for listicle/deep-dive.

- **Principle prose (the tell).** Name the framework, walk the components, then immediately drop in the proof candidate selected.

- **Claim-proof callouts.** When the principle contains a CLAIM (number, named outcome, before/after, volume signal, named person), drop a `> [!important] Visual proof needed` callout immediately AFTER the line carrying the claim, naming what the editor must put on screen. Follow the canonical convention in `knowledge/visual-proof-callouts.md` so vid-intro and vid-pressure-test audit against the same shape. Production-only instructions (visual demo prop setup, metaphor staging, on-screen text overlays) use `> [!note] visual:`. Keep the two distinct.

- **Takeaway (closes the principle).** One clear sentence of takeaway, the "what they walk away with." Match the punch-out the reference pieces use (often a short sentence after a longer one; hear it via `voice-rhythm.md` short-short-long, snap back).

- **Transition prose (the handoff).** Pull the slot-filled Section 2 pattern from Phase 2's structure draft. Verify against Section 4 banned phrases. If the candidate trips a banned phrase ("anyway, moving on" / "let's dive in" / etc.), regenerate from a different Section 2 pattern.

**Anti-fabrication discipline.** Every number, name, claim, story moment, or specific phrasing in the prose MUST trace to one of: brain dump, piece.md, or a bank entry pulled in Phase 2. If a sentence has a number, the number is verifiable. If a sentence claims a result, the result is in the bank. No "imagine you" framing if the brain dump used a real example. No "$10K to $100K" if the bank says "$8,400 to $74,000". Use the real one.

**Voice check inline.** Run `knowledge/voice-pressure-test.md` Pass 1 (the guardrail check) silently as you write. This is the in-skill voice check, not the multi-agent `vid-pressure-test` skill:

- Anti-patterns or creator hard rules from the guardrail present? Hard reject; rewrite.
- Words-avoided present? Soft reject; auto-swap to the paired replacement.
- POV and energy holding against the guardrail defaults?
- Signature phrase echoed at least once in long-form? If zero, voice signal is weak. Fold one in only if the brain dump supports it; never pad to hit a count.
- Writing from the reference pieces, not from rules: the passages are the seed, the guardrail only constrains.

**Surface the prose draft to the creator.** Format:

```
{SEGMENT LABEL}

{Parable paragraph(s): the show. Visual notes in callouts where applicable}

{Principle paragraph(s): the tell, framework then proof}

{Takeaway sentence}

{Transition out (one sentence)}
```

Then ask:

> "Read this aloud. Anything you'd reword? Or want me to adjust rhythm, swap a word, pull a different bank entry, or rewrite the block from a different angle?"

Wait. The read-aloud test is the final voice gate. Loop until the creator confirms.

**Sibling handoff to `vid-voice-update`.** If the creator's reword reads like a permanent rule (signals like "never use X", "I'd never write that", "swap Y for Z", "I hate that word", "drop X from my voice"), hand the trigger off to `vid-voice-update` before applying the rewrite. That skill triages the signal, appends to `foundation/voice-profile.md` refusals when permanent, and returns. Then apply the rewrite to this segment. If the signal reads local ("this line specifically", "doesn't fit this segment"), just apply the rewrite. Do not invoke `vid-voice-update` for one-time edits.

### Phase 4: Voice check, save, update banks

**Voice check full pass.** Run `knowledge/voice-pressure-test.md` Pass 2 (the grain check) against the locked prose: read a representative `## ` section from `foundation/reference-pieces/{voice_context}.md` aloud, then the prose aloud right after, and judge by ear whether sentence variation, paragraph shape, opener, and energy come from the same person in the same mode. If no file exists for this `voice_context`, skip Pass 2 and note the gap. Log result tier (pass / soft-warn / soft-reject / hard-reject). Hard-reject means a guardrail anti-pattern, a creator hard rule, or POV violation. Restructure, do not save.

**Save the prose.** Append to `content/pieces/{slug}/script.md` under a heading naming the segment (e.g. `## Step 2: Refactor your week`). Preserve any prior segments. Do NOT overwrite.

**Update piece.md.** Append the new bank wikilinks to `stories_used:`, `proofs_used:`, `metaphors_used:`, plus `frameworks_used:` if used. Wikilink format: `[[bank-slug]]`.

**Mark the segment done.** Append this segment's label (the heading you saved under) to `segments_completed:` in piece.md, and bump `last_updated:` to today. This is the pipeline's body-progress counter: when `segments_completed` length reaches `segment_purposes` length, the body is finished and the orchestrator routes to vid-ending. This write happens in both standalone and pipeline mode.

**Update each bank entry's `used_in:`.** Per the vault-integration "update both sides" rule. For every bank entry pulled in Phase 2 and surviving Phase 3, open the entry, append `[[piece-slug]]` to its `used_in:` array, and flip `status:` from `captured` to `used` if it was still `captured`.

**Log visual proofs called out in piece.md.** Per the canonical schema in `knowledge/visual-proof-callouts.md`. For every `> [!important] Visual proof needed` callout written in this segment, append an entry to `visual_proofs_called_out:` so the proof can be tracked to filming:

```yaml
visual_proofs_called_out:
  - line: "MRR went from $42k to $74k in 9 weeks"
    proof_needed: "Stripe screenshot or revenue dashboard showing the 9-week arc"
    bank_link: "[[steve-9-weeks-to-2-week-vacation]]"   # null if proof exists in script but no bank link yet
```

If `bank_link: null` for any callout (claim is real but no bank asset is linked), surface it to the creator at save time so they can decide whether to capture the proof before filming or rephrase the claim.

**Log the voice-check result in piece.md.** Per the `voice-pressure-test.md` schema (`voice_pressure_test:` block: date, result, pass1_guardrail, voice_context, pass2_grain, flags, read_aloud_confirmed). This log feeds vid-voice-capture drift detection.

**If sub-skill mode**, return to the caller a `segment_packet` (segment_label, prose string, banks_pulled wikilinks, voice_check result, outbound_transition_pattern). The script.md append, the `segments_completed` mark, and the bank updates already happened here in both modes. The packet is for the orchestrator's awareness, not a handoff of the write.

**STOP.** Do not write the next segment. The creator (or orchestrator) re-invokes for the next one.

## Failure-mode behaviors

From `vault-integration.md` failure modes. Never silent inconsistency.

- **Voice files missing:** hard stop. Tell the creator to run `vid-voice-capture`.
- **brain-dump and piece.md both missing:** hard stop. Route to `vid-intake` or `vid-framing`.
- **Format planner missing or unrecognized:** hard stop. Show the `piece.md` `format:` value and the list of valid format slugs.
- **Bank query returns nothing for a needed block:** offer the creator three options: invoke `vid-capture` mid-skill, swap to a different block type that has bank coverage, or skip the block (rare; flag it in the segment notes).
- **Structure pass keeps failing (3+ rounds without lock):** stop and ask the creator if the segment's job in `piece.md` is wrong. The skill is pulling from a broken framing. Route back to `vid-framing` if needed.
- **Primary write succeeds, secondary write fails (script.md saved but a bank's `used_in:` update fails):** retry once, then surface visibly. "Segment saved to script.md. Could not update [[bank-slug]] used_in. Manually add `[[piece-slug]]` to its frontmatter to close the graph."
- **Person stub missing for a client mentioned in a pulled bank entry:** create the stub immediately per the vault CLAUDE.md people rule. If creation fails, do NOT save the segment with an unresolved `[[Client Name]]` wikilink. Surface the failure.
- **Voice check hard-reject:** restructure the segment from the brain dump's actual phrasing. Do not save. Do not auto-fix.

## Principles

- **Conversation, not document.** Short messages. Never dump reference content into chat. References are for YOUR thinking.
- **Structure dictates voice, not the other way around.** Structure pass FIRST. If the segment doesn't work as a unit, no amount of voice polish saves it.
- **Creator drives, Claude structures.** The brain dump IS the voice. Banks ARE the proof. Claude doesn't invent claims, stories, numbers, or metaphors to make a segment land better.
- **Banks first, fabrication never.** Every story / proof / metaphor / testimonial in the prose traces to a bank entry or the brain dump. If banks come up empty, route to `vid-capture` or change the block type.
- **Update both sides.** When a bank entry gets used, both `piece.md` and the bank entry's `used_in:` get updated. Non-negotiable.
- **Read-aloud is the final gate.** The voice check catches drift. The creator's mouth catches what the check misses.
- **One segment per invocation.** Multi-segment requests get looped, not batched. Quality drops at scale.

## Reference index

| File | Why |
|---|---|
| `knowledge/vault-integration.md` | Save schema, wikilink contract, "update both sides" rule, failure modes |
| `knowledge/format-planners/{format}.md` | The shape for THIS piece's format and its parable/principle weighting |
| `knowledge/voice-rhythm.md` | Sentence-length variation, paragraph ratio, opener pattern, punctuation, energy |
| `knowledge/voice-pressure-test.md` | The in-skill two-pass voice check before save (not the agent skill) |
| `knowledge/story-capture-guide.md` | What stories look like, P-A-O structure, the 6 prompts |
| `knowledge/proof-capture-guide.md` | Proof types, presentation formats, placement-after-framework rule |
| `knowledge/metaphor-builder.md` | 3-step builder, visual vs non-visual, pivot phrases |
| `knowledge/testimonial-capture.md` | Verbatim preservation, source tagging, anonymization |
| `knowledge/visual-proof-callouts.md` | The `> [!important] Visual proof needed` convention + `visual_proofs_called_out:` schema. Shared with vid-intro. |
| `knowledge/parable-decision-matrix.md` | Which block type for which problem (visual demo / story / metaphor / contrast). Shared with vid-intro and vid-ending. |
| `knowledge/story-pulling-criteria.md` | How to pick the right story from N candidates. Shared with vid-intro and vid-ending. |
| `knowledge/proof-placement-rules.md` | Where proof goes, multi-format presentation. Shared with vid-intro and vid-ending. |
| `knowledge/metaphor-integration.md` | How to drop a metaphor in clean and bridge to the principle. Shared with vid-intro and vid-ending. |
| `foundation/voice-profile.md` | The thin guardrail (fingerprint, signature phrases, refusals, POV/energy) |
| `foundation/reference-pieces/{voice_context}.md` | The voice engine (voice only, not structure): real intact passages as `## ` sections |
| `content/pieces/{slug}/piece.md` | Format, voice_context, goal, pillar, locked title, prior banks pulled |
| `content/pieces/{slug}/brain-dump.md` | The segment's actual creator-voice raw material |
| `content/pieces/{slug}/script.md` | The locked skeleton section + prior segments (continuity for transitions) |
| `banks/story-bank/*.md` | Story candidates by what they illustrate and theme |
| `banks/proof-bank/*.md` | Proof candidates by proof_type and theme |
| `banks/metaphor-bank/*.md` | Metaphor candidates by concept and category |
| `banks/testimonial-bank/*.md` | Verbatim social proof candidates |
| `banks/framework-bank/*.md` | Creator's named systems |
| `banks/transition-bank.md` | Section 2 segment-to-segment patterns + Section 4 banned phrases |
| `references/parable-principle-shapes.md` | Per-format parable + principle shapes, contrastive examples (skill-local) |
| `references/framework-shapes.md` | Arrows / pyramids / cycles / Venns / funnels: when to use each (skill-local) |
| `assets/segment-scaffold-template.md` | The structure-draft skeleton for Phase 2 |

## Related skills

- `vid-voice-capture` produces voice-profile.md and reference-pieces/
- `vid-capture` produces bank entries this skill reads and may be invoked mid-skill if a bank gap blocks the segment
- `vid-intake` produces brain-dump.md
- `vid-framing` produces piece.md
- `vid-structure` assembles the skeleton this skill fills, once per body section
- `vid-intro` writes the intro segment (different shape: 6-part architecture, not parable + principle)
- `vid-ending` writes the ending segment (different shape: body-to-ending bridge plus CTA)
- `vid-pipeline` orchestrates the full per-video pipeline and runs the segment loop in the script phase
- `vid-pressure-test` runs the multi-agent adversarial review across the full script after segments are assembled (distinct from this skill's in-skill voice check)
