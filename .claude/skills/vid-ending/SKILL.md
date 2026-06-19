---
name: vid-ending
description: Write the close of a YouTube video using Pivot/Gap/Bridge, recap the transformation, reveal the new problem, position the next video as the fix. Format-aware (close differs for roast vs deep-dive vs news vs interview vs case-study vs short-process vs listicle). Auto-rejects banned phrases ("and finally", "thanks for watching", "if you liked this, subscribe", "stay tuned"). Anti-fabrication. Never ends a video, every close pivots to the next problem and points to a real, already-published video. Runnable standalone or invoked by `vid-pipeline` during the SCRIPT phase. Triggers on "write the ending", "close this video", "outro for [video]", "what's the CTA", or when a downstream pipeline needs a locked close.
---

# Video Ending Writer

Writes the close of one video using the 3-Part End Formula: Pivot (recap the transformation in one sentence) → Gap (reveal the new problem they still have) → Bridge (position a specific next video as the fix). Format-aware. CTA placement is decided by goal (sales / emails / views) and format, never bolted on.

**Scope boundary:** this skill produces THE close only. It does not write hooks (`vid-intro`), body points (`vid-segment`), titles (`vid-title`), or thumbnails (`vid-thumbnail`). It does not pick the next video on the channel, it asks the creator. It does not generate end-screen visuals.

## What this produces

A locked ending block, saved as the closing section of `content/pieces/{slug}/script.md`. Updates `content/pieces/{slug}/piece.md` with the ending packet (next-video link, goal, CTA shape). When invoked as a sub-skill by `vid-pipeline`, returns the ending packet to the caller.

## When to run this

- Body of the script is locked. The video has a defined transformation the close can recap.
- Creator wants to re-write an existing close (CTA underperformed, needs a different next video, format changed).
- Orchestrator (vid-pipeline) invokes during the SCRIPT phase after `vid-segment` has produced the body.

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists with the avatar's Top 3 problems (the Gap names one of them, the next one the body lesson points to)
- `content/pieces/{slug}/piece.md` exists with `format`, `goal`, and a `pillar` set
- `content/pieces/{slug}/script.md` has the full body written (every segment) AND a non-stub `## Intro` (the close's Pivot calls back to the intro's Setup contract, so the opening must already be written)

If the body is missing or only partially written, hard stop. Tell the creator: "I need the full body locked first. Run `vid-segment` for every section, then re-invoke." If the `## Intro` section is still a stub (`*To be written by vid-intro...*`), hard stop. Tell the creator: "The intro isn't written yet. Run `vid-intro` first so the close can call back to the opening, then re-invoke."

If `foundation/voice-profile.md` is missing, fall back to core voice rules from `Context/brand.md` and note in the brief: "Voice profile not captured. Using brand defaults. Run `vid-voice-capture` for sharper voice fit."

## Invocation modes

**Standalone:** creator invokes directly. After lock, save the close into `script.md` (replacing any existing close) and update `piece.md`.

**Sub-skill:** the orchestrator (vid-pipeline) invokes it in the script phase, after vid-segment has produced the body, with a context packet. Skip questions the caller has already answered. The save (script.md close + piece.md fields) still happens here, in both modes; also return the ending packet to the caller for assembly awareness.

If invoked with caller context (e.g. "ending for case-study, goal=sales, transformation=client went from 0 to 80k/mo, next video={{slug}}"), skip prerequisite probing and go straight to draft.

## The walkthrough (4 phases)

**This skill is a conversation, not a document.** Keep messages short. Never dump reference content into chat. References are for YOUR thinking. Pull selectively. Same hard rules as `vid-title` and `vid-thumbnail`: no fabrication, specificity wins, pull-from-script-only.

### Phase 1: Load context, decide shape

**Silent loads** (do NOT paste into chat):

1. `foundation/creator-foundation.md` (avatar, Top 3 problems. The Gap is one of the Top 3, the next one the body lesson points to)
2. `foundation/voice-profile.md` (the thin guardrail, always loaded) and `foundation/reference-pieces/{voice_context}.md` (the voice engine: real intact passages to write the close from, as `## ` sections in one file matched to piece.md `voice_context`, default `youtube-script`. Contract in `knowledge/voice-profile-schema.md`). **Voice only, not structure:** passages carry cadence, word choice, register, and signature moves. Closing architecture (Pivot/Gap/Bridge, CTA, push to next video, sign-off shape) is fixed by THIS skill's spec. If a passage's structural arc conflicts with the spec, follow the spec. Reproduce the grain, not the order of moves.
3. `knowledge/vault-integration.md` (frontmatter schema for the piece.md update)
4. `knowledge/voice-rhythm.md` and `knowledge/voice-pressure-test.md` (line-level voice and end-of-skill validation)
5. `knowledge/format-planners/{format}.md`, load ONLY the planner matching `piece.md`'s `format` field
6. `banks/transition-bank.md` Section 3 (BE-1 through BE-8 patterns) and Section 4 (banned phrases)
7. `references/pivot-gap-bridge-shapes.md` (the 3-Part End Formula examples and contrast)
8. `references/cta-placement-by-format.md` (which goal-and-format combinations work, which tank)
9. `references/ending-anti-patterns.md` (banned phrases and the failure mechanism)
10. `references/end-screen-design.md` (which video to point to and why)
11. `content/pieces/{slug}/piece.md` (format, goal, pillar, locked title)
12. `content/pieces/{slug}/script.md` (the body. Read the `## Intro` section verbatim to lift the Setup contract, viewer-question promises, hook line, and which avatar problem the intro poked. Read the body sections too, to lift the actual transformation language.)
13. `content/pieces/{slug}/piece.md` if it exists (locked angle, core payoff)
14. **Sub-skill mode only:** the intro packet returned by `vid-intro` to the caller. Key fields you read:
    - `setup.text` (literal Setup contract; your Pivot pays this off near-verbatim)
    - `setup.top_3_questions_used` (the three viewer questions your Pivot has to confirm got answered)
    - `problem_result.top_3_problem_anchored` (1, 2, or 3; the problem the intro poked. Your Gap reveals the next logical problem the body exposes, usually a different one of the three, not forced to be this same one)
    - `hook.text` and `hook.type` (so you don't reopen with the same hook lane at the close)
    - `credibility.text` if present (so you don't re-cite the same receipt; reference the lesson, not the receipt)
15. **Conditional shared loads** (load only when the close leans on the relevant material; endings are claim-light by design, so most runs skip these):
    - `knowledge/story-pulling-criteria.md` only if the recap or Gap framing pulls a story from `banks/story-bank/`. Use the 5-criteria filter to pick the right one.
    - `knowledge/proof-placement-rules.md` only if the recap cites proof. Owns PLACEMENT decisions (place receipts AFTER the framework lesson, never before), bank-pulling, and presentation-format selection. Cross-references `knowledge/visual-proof-callouts.md` for callout SYNTAX. Load that one too if the proof needs an on-screen callout (vid-ending is in `loaded_by` for the recap edge case in Case Study / Deep Dive closes).
    - `knowledge/metaphor-integration.md` only if a metaphor frames the transformation. Honor the drop-clean / 3-sentence cap / two-layer rule.
    - `knowledge/parable-decision-matrix.md` rarely needed at the close (the body owns parables); load only if the close opens with a fresh emotional beat (e.g., a story-led roast close where the Pivot replays a contestant's transformation).

**Build the lock list:** every number, dollar figure, percentage, timeframe, named method that actually appears in the script. The Gap reveal and any receipt in the close may ONLY use these. No fabrication.

**Decide format-aware shape.** Each format has a default close pattern. The planner is authoritative. Common defaults:

- **Short Process:** tight Pivot (one sentence recap of the system) → Gap (the next of the Top 3 the system surfaces but doesn't solve) → Bridge to a related process video. CTA per goal.
- **Case Study:** Pivot recaps the transformation in plain language ("That's how Steve went from 0 clients to 80k/mo"). Gap reveals the second-order problem (delivery, retention, scale). Bridge often points to a deep-dive that walks the methodology.
- **Roast:** Pivot recaps the universal lesson across the contestants. Gap = "yours is probably making one of these mistakes too". Bridge = submission CTA + a related fix video. The submission CTA is non-optional for this format.
- **Deep Dive:** Pivot is short (the body did the heavy lift). Gap names the next-stage problem the deep-dive opens up. Bridge close is **aggressive for sales**, the format's audience is the warmest of any format.
- **Interview:** Pivot recaps the GUEST's transformation, not the creator's lesson. Gap names what the viewer's stack still lacks. Bridge points to a video where the CREATOR is the expert (per format planner, host credibility is the whole monetization mechanism here).
- **News:** Pivot is one line ("That's what just happened"). Gap names what the viewer should do or watch for. Bridge points to a non-news evergreen video that demonstrates the channel's value (per format planner).
- **Listicle:** Pivot recaps the cumulative payoff in one phrase. Gap reveals the next-stage problem. Bridge points to a deeper video on the strongest item or a related listicle.

If the planner conflicts with the goal the creator picked, surface the conflict: "Format=interview defaults goal=views or emails. You picked sales. Interviews tank for sales (credibility flows to the guest). Want me to switch to emails or override?"

**Pick the next video first, then derive the Gap from it.** Ed's rule: don't map a perfect chain in advance. Look at what the creator has ALREADY published, especially what converts for this goal (per `references/end-screen-design.md`: the best sales/email/lead converter, or a same-format winner), and pick the one that's the most logical next watch after this video's topic. Then write the Gap as the problem THAT video solves: what they just learned isn't enough on its own, the next thing in their way is what the next video covers. The next problem lands on one of the channel's recurring problems naturally (the catalog orbits them), so you are bridging to a real video, not scanning an abstract list. **Critical:** point only to a video that exists and converts. If nothing the creator has made is a close-enough next step, do NOT invent a problem or promise an unmade video, fall back to a subscribe pointer (Ed's first-video rule). Do not force the Gap to be the same problem the intro poked (Ed's own example pivots a clarity lesson to "your intro doesn't hook people").

**Decide CTA shape from goal:**

- **Sales:** strong direct CTA (or stealth, woven through), top link in description, Bridge to past sales-converting video
- **Emails:** lead magnet directly tied to this video's content, mention 3x (one already in body, one in close), top link in description, Bridge to past email-converting video
- **Views:** NO external links in description, Bridge to evergreen channel asset, focus on retention through the close itself

**Callback rules (intro coordination).** The close has to feel like the same video closing, not a different video starting. Honor these when drafting:

1. **Coherent pivot, not a topic jump.** The Gap can move to a different problem than the intro poked (Ed pivots a clarity lesson to hooks), but it has to read as the logical next step from what this video taught, not a jarring jump to an unrelated topic. The bridge to a real next video is what carries the coherence. Read `problem_result.top_3_problem_anchored` for context on where the viewer started; you are not required to stay on that same problem.
2. **Pay off the Setup contract.** The Pivot recaps the Setup near-verbatim. If the Setup said "I'm going to show you the formula, why it works, and how to use it," the Pivot tracks: "you now know the formula, why it works, and how to use it." Mismatched recap reads as a different video. Read `setup.text` and `setup.top_3_questions_used` to get the language.
3. **Don't reopen with the intro's hook lane.** If the intro opened with a Question Hook, don't re-open the close with another question. Same for Statement, Contrarian, Fact, Credibility. Reusing the lane signals "the video restarted." Read `hook.type` and pick a different shape. The Bridge stays declarative regardless.
4. **Don't re-cite the credibility receipt.** If the intro wove a credibility line (a personal result number, a notable client, a volume stat), the close references the LESSON, not the same receipt. Cold viewers already heard it; re-citing burns trust. Read `credibility.text` and route around its specific number/name.
5. **Echo, don't repeat.** Pivot wording can riff on intro language for resonance ("you now have everything you need to write a hook that stops scrolling" echoing the intro's "I'm going to show you how to write a hook that stops scrolling"). Verbatim repeat is fine if it lands; cosmetic remix that loses meaning is not. Read aloud both lines back-to-back. Does the close feel like the closing beat or a redo?

### Phase 2: Draft the close, present 2 candidates

**Draft 2 close candidates** drawing from:

- BE patterns from `banks/transition-bank.md` Section 3 (fill slots with the video's actual material)
- The format planner's recommended close shape
- The creator's voice profile (energy, opener pattern, sentence rhythm)
- The lock list (every receipt traces to the script)

Each candidate is a complete close: Pivot sentence(s), Gap sentence(s), Bridge sentence(s), CTA. The candidates differ on shape (e.g., one uses BE-3 "you now have everything you need" framing, the other uses BE-6 "here's the thing nobody warns you about"). Same Gap problem, same next video, different rhythm.

Length budget: 30-60 seconds when read aloud. Roughly 60-150 spoken words. Longer than that is a recap (banned). Shorter than that is a bare CTA (banned).

**Hard filters (auto-reject any candidate that hits these):**

1. **Anti-fabrication.** Any number not in the lock list. REJECT and regenerate.
2. **Tier 1 banned phrases (auto-reject, source-explicit):** "And finally" / "Lastly" (source-explicit ban: lesson-11 line 40, "Don't say 'and finally'"). "Thanks for watching" / closes that signal the video is ending at all (source-explicit: "Never end a video," lesson-11 line 40, 52). REJECT and substitute. Tier 2 phrases ("If you liked this please subscribe," "Smash that like button," "Stay tuned," "Without further ado," "Today's video was about") move to Soft friction below.
3. **Recap dump.** Listing all the body lessons in sequence ("So we covered X, then Y, then Z"). REJECT. Pivot is ONE sentence, not a recap of the body.
4. **Bare CTA.** A close that is just "subscribe" or "check the link" with no Pivot or Gap. REJECT.
5. **Em-dashes.** Brand-level hard no. REJECT.
6. **Read-aloud failure.** If the close doesn't flow as continuous spoken speech, REJECT.

**Soft friction (flag and explain, let creator decide):**

7. **Tier 2 banned phrases (derived patterns).** "If you liked this please subscribe," "Smash that like button," "Stay tuned," "Without further ado," "Today's video was about." Each has an override case (see `transition-bank.md` Section 4 Tier 2). Surface the failure mechanism and the override; the creator decides whether their voice or format earns it.

8. **Pivot too long.** If Pivot is 3+ sentences, the close starts to feel like a wind-down. Flag.
9. **Gap with no video behind it.** If the Gap points at a problem the creator has no published video for, flag it, the Bridge needs a real next watch. Either pick a Gap a real converting video solves, or fall back to a subscribe pointer.
10. **Bridge to underperforming video.** If the creator picks a next-video that previously flopped, flag the trade-off.
11. **CTA placement mismatched to goal.** E.g., a sales CTA on a news video. Surface the format-planner's warning.
12. **Hedge words.** "Maybe" / "Possibly" / "I think you should". The Bridge should be confident, not tentative. Flag.

**Present candidates as a numbered list:**

```
1. [Format-aware shape], BE-3 frame, 47s read-aloud, goal=sales
   "You now have everything you need to land your first 3 clients without a website. The next problem is keeping them past month two. I made a video on it. Watch this next."

2. [Format-aware shape], BE-6 frame, 52s read-aloud, goal=sales
   "Here's the thing nobody warns you about getting your first 3 clients: the bottleneck moves to delivery the day client three signs. I'll show you exactly how to handle it next."
```

Each candidate annotated with: BE pattern used, estimated read-aloud time, goal, soft flags if any.

### Phase 3: Pick, refine, lock

Ask:

> "Which one? Or want me to regenerate with a different Gap problem, different next-video, or shorter/longer shape?"

Wait. If they pick, go to Phase 4.

If they want changes:
- "Different Gap" means re-generate around a different next-video (and the problem that video solves)
- "Different next video" means swap the Bridge target, ask which past video and verify it actually exists and converts (per `references/end-screen-design.md` rules)
- "Shorter" means tighten under 40 seconds
- "Different rhythm" means regenerate weighted to the creator's voice profile defaults
- "Aggressive sales" or "softer" means swap CTA shape per `references/cta-placement-by-format.md`

**Push back when picks are weak:**

- They want to point to a video that hasn't been published yet. REJECT and explain (per source-backed rule: never link to a video you haven't made; viewers get confused and don't return).
- They want to point to an underperforming video because it's the most recent. Flag and ask: "This one underperformed. Per the rule, point to one that converted. Want me to ask which past video hit the goal?"
- They want a generic Gap ("there's still more to learn"). Flag: "This is too vague to drive a click. Name the specific problem your next video solves."
- They want to add "thanks for watching". REJECT (Tier 1, source-explicit "Never end a video" rule).
- They want to add "smash that like button" or "if you liked this please subscribe". Surface as Tier 2 soft friction with the failure mechanism and override case from `transition-bank.md` Section 4. The creator decides whether their voice earns the override; don't auto-reject.

**Run the voice pressure test** on the selected close (per `knowledge/voice-pressure-test.md`):

- Pass 1 (guardrail): signature phrase echoed, anti-patterns and creator hard rules absent, words-avoided absent, POV and energy consistent
- Pass 2 (grain): read a `## ` section from `foundation/reference-pieces/{voice_context}.md` aloud, then the close aloud, and judge by ear whether rhythm and the closing move match. No stored numbers. Skip and note the gap if no file for this `voice_context`
- Read-aloud: would the creator reword anything? If yes, drop back to draft.

**Sibling handoff to `vid-voice-update`.** If the creator's reword reads like a permanent rule (signals like "never use X", "I'd never write that", "swap Y for Z", "I hate that word", "drop X from my voice"), hand the trigger off to `vid-voice-update` before applying the rewrite. That skill triages the signal, appends to `foundation/voice-profile.md` refusals when permanent, and returns. Then apply the rewrite to the close. If the signal reads local ("this line specifically", "doesn't fit this ending"), just apply the rewrite. Do not invoke `vid-voice-update` for one-time edits.

### Phase 4: Lock and save

Once locked:

**Always (both modes).** The fields below are how the pipeline knows the ending is done, so they always get written here:
- Read `assets/ending-block-template.md` to get the fillable structure. Fill the bracketed slots ({Pivot}, {Gap}, {CTA}, {Bridge}, {{next-video-slug}}) with the locked content from the picked candidate. If `goal=views`, omit the CTA block entirely per the template's inline note.
- Replace the existing close (if any) in `content/pieces/{slug}/script.md` with the filled template. The close goes at the end of the script. The `## Ending` heading from the template makes it scannable for editors.
- Update `content/pieces/{slug}/piece.md`:
  - `ending_locked: true`
  - `next_video: "[[slug-of-next-video]]"` (wikilink)
  - `cta_shape: sales | emails | views` (matches goal)
  - `ending_be_pattern: BE-N` (which transition pattern was used)
  - `last_updated: today`
- **Update both sides on any bank pull.** If the close pulled a story (story-bank), proof (proof-bank), or testimonial (testimonial-bank) for the recap or Gap framing, update the bank entry's `used_in:` array to include `[[{this-piece-slug}]]`. The script citing the bank entry and the bank entry citing the script must be reciprocal. That is the wikilink contract from `knowledge/vault-integration.md`. Same rule vid-intro and vid-segment honor.
- If the next-video wikilink target doesn't exist, do NOT save a broken link. Ask the creator: "The wikilink target `[[{slug}]]` doesn't resolve. Want me to (a) ask you for the right slug, (b) leave it as plain text and you fix later, or (c) skip the Bridge until the next video is created?"
- Confirm: "Ending locked. Saved to script.md and piece.md. Next-video Bridge points to [[{slug}]]."

**Sub-skill mode also:**
- Return the ending packet to the caller for assembly awareness. Shape (matches the team-standard packet shape vid-intro returns):
  ```yaml
  ending_packet:
    pivot: gap-bridge | result-bridge | submission-bridge | subscribe-pointer
    recap_line: "{the Pivot sentence}"
    new_problem: "{the Gap sentence, names the second-order Top-3 problem}"
    top_3_problem_anchored: 1 | 2 | 3
    next_video_slug: "[[piece-slug]]" | null
    next_video_status: real-published | next-stack-placeholder | none
    cta_type: subscribe | watch-next | lead-magnet | sales-link
    bridge_line: "{the Bridge sentence}"
    be_pattern: BE-N
    voice_pressure_test: pass | warn | fail
    text: "{the full locked close, verbatim, ready to paste under ## Ending}"
  ```
- If `next_video_status: next-stack-placeholder`, the new-problem reveal is a logical second-order problem the creator could plausibly cover next, but no real published piece exists yet. Flag this in `piece.md` so vid-pipeline can retro-link the close to a real piece once it's published.
- The script.md and piece.md writes above still happen here. The packet is for the orchestrator's awareness, not a handoff of the write.

**STOP.** Do not edit the body, do not regenerate the title, do not pre-write the next video's intro. Those are different skills.

## Anti-fabrication discipline

Every receipt, number, named method, or claim in the close MUST trace to the script's body or to foundation docs. If the creator wants a number-driven Pivot and the body doesn't have a usable receipt, kick it back: "The body doesn't have a number to ground the recap. Either drop the number-driven Pivot or add the receipt to the body first."

The Gap problem must come from `creator-foundation.md` Top 3. Inventing a new problem here breaks the signal, viewers were promised the avatar's stack, not a new thread.

The Bridge target must be a real, already-published video. Never link to "I'll make this next", viewers don't return for promised content.

## The golden rule: never end a video

This is the load-bearing principle of the whole skill. Don't say "and finally". Don't recap every lesson. Don't wind down. The goal is a close so smooth viewers don't notice the video is ending, they're already moving to the next one.

If the creator's draft pulls toward "and now to wrap up", that's the signal the close is breaking. Restructure into Pivot → Gap → Bridge.

## Principles

- **Conversation, not document.** Short messages. Never dump references at the creator.
- **Format drives shape.** A roast close differs from a news close differs from a deep-dive close. Read the planner; don't override its defaults silently.
- **Goal drives CTA.** Sales, emails, and views close differently. Pick one and commit.
- **Specificity wins.** Real receipts from the body. Real next-video. Real Gap problem from the Top 3.
- **Never end a video.** Pivot, name the new problem, point to the next video. The viewer should feel pulled forward, not closed off.

## Reference index

| File | Why |
|---|---|
| `references/pivot-gap-bridge-shapes.md` | The 3-Part End Formula with examples and near-misses |
| `references/cta-placement-by-format.md` | Goal-and-format pairings, what works, what tanks |
| `references/ending-anti-patterns.md` | Banned phrases and the failure mechanism behind each |
| `references/end-screen-design.md` | Which video to Bridge to, the two options, the chain-reaction effect |
| `banks/transition-bank.md` Section 3 + Section 4 | BE-1..BE-8 patterns and banned phrases (shared with vid-segment, vid-intro) |
| `knowledge/format-planners/{format}.md` | Format-specific close shape and CTA defaults |
| `knowledge/voice-rhythm.md` | The lens for hearing rhythm in the reference pieces and the draft; no stored numbers |
| `knowledge/voice-pressure-test.md` | End-of-skill validation (Pass 1 guardrail, Pass 2 grain by ear vs reference pieces) |
| `knowledge/vault-integration.md` | Frontmatter schema for piece.md updates |
| `knowledge/story-pulling-criteria.md` (conditional) | Story selection filters when the recap or Gap pulls from story-bank. Shared with vid-intro, vid-segment. |
| `knowledge/proof-placement-rules.md` (conditional) | Receipt-placement rules when the close cites proof. Owns PLACEMENT decisions and bank-pulling. Shared with vid-intro, vid-segment. |
| `knowledge/visual-proof-callouts.md` (rare, pending loaded_by add) | Callout SYNTAX (callout AFTER claim, never before) when a numeric Pivot needs an on-screen callout. Currently `loaded_by: [vid-intro, vid-segment]`; ask team-lead to extend to vid-ending. |
| `knowledge/metaphor-integration.md` (conditional) | Splice rules when a metaphor frames the transformation. Shared with vid-intro, vid-segment. |
| `knowledge/parable-decision-matrix.md` (rare) | Used only if the close opens with a fresh emotional beat. Shared with vid-intro, vid-segment. |
| `foundation/creator-foundation.md` | Avatar Top 3 problems (the Gap names the next logical one) |
| `foundation/voice-profile.md` | The thin guardrail (fingerprint, signature phrases, refusals, POV/energy) |
| `foundation/reference-pieces/{voice_context}.md` | The voice engine (voice only, not structure): real intact passages as `## ` sections, matched to piece.md `voice_context` |
| `content/pieces/{slug}/script.md` + `piece.md` | The video being closed |
| `content/pieces/{slug}/script.md` `## Intro` section | Standalone-mode source for Setup contract, hook lane, and which problem the intro anchored. Drives the callback rules. |
| Intro packet from `vid-intro` (sub-skill mode) | Sub-skill source for the same fields: `setup.text`, `setup.top_3_questions_used`, `problem_result.top_3_problem_anchored`, `hook.text`, `hook.type`, `credibility.text`. Schema in vid-intro SKILL.md "Output packet" section. |
| `assets/ending-block-template.md` | Fillable structure read at lock time, filled with the locked content, then written into script.md |

## Related skills

- `vid-segment` produces the body this skill closes
- `vid-intro` produces the open this skill's Pivot calls back to (echo, don't repeat)
- `vid-title` and `vid-thumbnail` lock the package the close has to honor
- `vid-pipeline` (future) is the orchestrator that calls this skill after vid-segment
- `vid-measurement` (future) does post-publish analysis, logs winning Bridges (which next-video pulls best end-screen click-through) back into the channel's notes
