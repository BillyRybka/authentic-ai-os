---
type: reference
scope: skill-local
loaded_by: [vid-research]
status: active
tags: [reference, vid-research, curation, theory-of-one]
---

# Theory of One Curation

The Phase 5 conversation pattern. Every AI-extracted pattern gets surfaced to the creator with full context, and the creator hits Keep / Drop / Modify. Examples-first contrastive. Worked dialogues showing how each decision plays out, plus near-misses showing what curation failure looks like.

## Why this exists

AI does the data heavy lifting. Theory of One is the irreplaceable human filter: does this pattern fit MY audience's expectations of me, even if it works on every other channel in the space? The creator's answer can't be predicted by the data. AI structures the question; the creator owns the decision.

Skipping this step (or rubber-stamping every AI proposal) pollutes the bank with patterns the creator's audience won't actually engage with. The Theory of One filter is what separates a useful pattern bank from a generic outlier database.

But do not over-filter. The bank is a signal library of what works in the space, not a brand-purity set. A pattern that clearly works, even one borrowed from an adjacent niche or an off-lane theme, is a signal worth keeping; it gets adapted into the creator's voice at title-making time (Modify), not dropped here. Drop is for true noise, not for adaptable signals. When in doubt on a real signal, Keep or Modify.

## The conversation shape

For each draft pattern surfaced from extraction, the AI presents a short structured panel:

```
> Pattern: `{template}`  (pattern_id: {slug})
> 
> Spread: {N} of {M} channels{, own-channel proven if true}
> 
> Worked examples (from your research session):
> 1. "{example 1}", {channel}, {views}
> 2. "{example 2}", {channel}, {views}
> 3. ...
> 
> Theory of One check:
> Your iceberg: "{iceberg statement from foundation/iceberg.md}"
> Your audience expects: {brief audience expectation summary}
> {off-positioning note, only when it applies: "This prints views but leans off your lane (e.g. {off-lane theme}). It is still a real signal. Lean toward Keep or Modify (adapt it to your lane), not Drop, unless it is true noise."}
> 
> Does this pattern fit YOUR audience's expectations of you?
> 
> [Keep] [Drop] [Modify]
```

Creator hits one of three options. AI captures the decision and rationale.

## The three decisions

### Keep

The creator wants this pattern in the bank as-is. Future vid-framing, vid-title, vid-thumbnail can pull from it.

**When Keep is the right call:**
- Pattern aligns clearly with the audience's existing expectations of the creator
- Pattern matches the creator's tone and voice (won't feel forced)
- Pattern is concrete enough to actually apply (not vague generic principle)
- Spread ≥ 3 of M channels (or own-channel-proven) and Theory of One filter passes

**Worked Keep dialogue:**

```
> Pattern: `Why I [reversal action] [specific subject] After [time/quantity]` (pattern_id: authority-reversal)
> Spread: 4 of 5 niche channels
> Worked examples:
> 1. "Why I Cut My Squat 20% After Coaching 100+ Lifters", @CoachX, 145k views
> 2. "Why I Stopped Running 5x a Week After 12 Years", @CoachY, 92k views
> 3. "Why I Quit Tracking Macros After 8 Years", @CoachZ, 124k views
> 
> Theory of One check:
> Your iceberg: "I help intermediate-to-advanced lifters program training that fits their lives."
> Your audience expects: authority + opinion changes backed by experience
> 
> Does this fit your audience? Keep / Drop / Modify?

Creator: Keep. This is exactly the energy my audience comes back for.

Skill: Locked as pattern_id `authority-reversal` in title-bank.md. Status: curated.
```

### Drop

The creator rejects this pattern. Future runs should NOT re-surface it.

**When Drop is the right call:**
- Pattern works on other channels but doesn't fit the creator's audience
- Pattern's tone or implication doesn't match the creator's brand
- Pattern feels manipulative, gimmicky, or chasing trend rather than serving audience
- Creator has already tested a similar pattern and it flopped on their channel

**Do not pre-drop money or results patterns on positioning alone.** When a creator's positioning leans on trust or authenticity, it is tempting to drop revenue, money, or result-claim patterns (e.g. "How I Hit [Number] in [Time]") on reflex. Resist that. For many audiences, results and money are among the strongest reasons they watch. The guard is not removing the pattern, it is anchoring the claim to a real, defensible number the creator can stand behind. Surface it with Modify framing ("Keep the result hook, swap the placeholder for a number you can prove"), and only Drop it if the creator says it genuinely does not fit. This holds across niches, whether the number is a client weight cut, a revenue figure, or a measured outcome in any field.

**Drop ALWAYS captures a one-line rationale.** This is critical for sticky-curation. Without rationale, future quarterly refreshes will re-surface the same pattern and the creator will have to drop it again. With rationale, the AI knows why and skips it next time.

**Worked Drop dialogue:**

```
> Pattern: `I Tested [Famous Person]'s [Method/Routine] for 30 Days` (pattern_id: celebrity-test)
> Spread: 3 of 5 niche channels
> Worked examples:
> 1. "I Tested Hormozi's Sales Script for 30 Days", @CoachW, 380k views
> 2. "I Tried David Goggins' Workout for 30 Days", @CoachQ, 245k views
> 3. "I Followed Cal Newport's Schedule for 30 Days", @CoachP, 180k views
> 
> Theory of One check: 
> Your iceberg: "I help intermediate-to-advanced lifters program training that fits their lives."
> Your audience expects: programming you've validated yourself, not borrowed authority
> 
> Does this fit your audience? Keep / Drop / Modify?

Creator: Drop. My audience expects me to be the authority, not test someone else's. This pattern feels like chasing.

Skill: Captured rationale: "celebrity-test framing conflicts with creator's authority positioning; audience expects original method, not borrowed."

Pattern `celebrity-test` moved to ## Considered + dropped. Won't re-surface in quarterly refresh.
```

**Drop rationales worth capturing (examples):**

- "Doesn't match my audience's expected tone."
- "Tested similar pattern in past, flopped on my channel."
- "Feels generic/manipulative for my brand."
- "Off-brand for the iceberg I've built."
- "Audience too sophisticated for this hook style."
- "Format doesn't fit my production constraints."

### Modify

The pattern has signal but needs reframing for the creator's audience. Creator rewrites the pattern in their own framing, then it gets banked as the modified version.

**When Modify is the right call:**
- The structural pattern works but the specific phrasing doesn't fit the creator's voice
- Pattern is close but needs to dial up specificity for a sophisticated audience
- Pattern needs to drop a power word the creator avoids and substitute one they use
- Pattern's spread is wide but Theory of One says "almost yes, but..."

**Worked Modify dialogue:**

```
> Pattern: power word "STOP" as a title opener (pattern_id: power-stop)
> Spread: 6 of the niche channels
> Worked examples:
> 1. "STOP Following This Outdated Programming Advice", @CoachX, 145k
> 2. "STOP Resting 3 Minutes Between Sets", @CoachY, 88k
> 
> Theory of One check:
> Your audience expects: nuanced authority, not screaming
> 
> Does this fit? Keep / Drop / Modify?

Creator: Modify. "STOP" feels too aggressive for my audience. They respect authority but not yelling. I'd reframe as "Why You Should Stop X", softer, more authoritative. Same pattern, different tone.

Skill: Locked modified pattern. Logged as:
- Original pattern (rejected): "STOP [common practice]", direct command
- Modified pattern (accepted): "Why You Should Stop [common practice]", analytical authority frame
- Reasoning: matches sophisticated audience tone preference

Pattern P-2 saved in power-words-bank.md as audience-specific modification of the STOP pattern.
```

## Bulk-keep mode for power users

Some patterns are obvious keeps. The creator already trusts AI synthesis and doesn't want a per-pattern review.

**Trigger:** when 5+ patterns in a row are wide-spread AND the creator has been hitting Keep on every one.

**Skill offers:**

```
> 5 wide-spread patterns surfaced so far, all Kept. 
> 12 more wide-spread patterns remaining in this batch.
> 
> Bulk-keep them all and save time? Or continue per-pattern review?
> 
> [Bulk keep all wide-spread] [Continue per-pattern]
```

**On bulk-keep:** all wide-spread patterns get Kept, audit log captures the bulk action, creator returns to per-pattern review for the thinner-spread patterns.

**Why this matters:** the curation pass can have 30+ patterns. Per-pattern feels exhausting at scale. Bulk-keep on obvious wins lets the creator focus attention on the borderline cases where their judgment matters most.

**When NOT to use bulk-keep:** first time the creator is curating (no track record yet, all patterns deserve fresh consideration). Or when the spread signal hasn't been validated against the creator's actual feel for the bank.

## Sticky-curated growth (Mode 2 quarterly refresh)

In quarterly refreshes, patterns from prior sessions are sticky:

- Previously **Kept** patterns stay in the bank with `last_validated: {prior date}` updated to today only if the creator wants to re-validate. By default, Kept patterns just persist and don't get re-surfaced for review.
- Previously **Dropped** patterns are checked against new outlier data. If the dropped pattern shows up again with wider spread (more channels), surface as: "This was dropped 90 days ago for [rationale]. New data shows it appearing in [N] more channels. Reconsider, or stay dropped?"
- Previously **Modified** patterns are honored as the modified version. If new data could refine the modification further, surface for re-review.
- New patterns from this refresh's data go through a fresh Theory of One pass.

The result: the creator's curated taste compounds across sessions instead of restarting each time.

## Drop rationale taxonomy

To help future runs and the creator's own self-awareness, classify drop rationales into broad buckets:

- **Tone mismatch**, pattern works mechanically but conflicts with the creator's voice/brand
- **Audience sophistication**, pattern is too beginner or too aggressive for THIS audience
- **Brand off-axis**, pattern would broaden the channel beyond its committed iceberg
- **Tested + flopped**, creator already tried this on their channel, didn't work
- **Format mismatch**, pattern requires production type the creator doesn't do (e.g., cinematic when channel is webcam)
- **Authority conflict**, pattern requires credibility the creator doesn't have or doesn't want to claim
- **Trend-chasing**, pattern feels like chasing current viral mechanics rather than serving long-term audience
- **Other**, write a custom one-liner

The bucket gets stored alongside the rationale string. Buckets help quarterly refresh decide whether to re-surface (a "tested + flopped" drop should NEVER re-surface; a "tone mismatch" drop might re-surface if the creator's voice has shifted; a "trend-chasing" drop might re-surface if the trend stuck around long enough to become a real pattern).

## Curation completion criteria

Phase 5 ends when:

- Every pattern in the draft set has a Keep / Drop / Modify decision
- Every Drop has a captured rationale
- Every Modify has a captured modified version
- Creator has confirmed final pattern set looks right

Skill saves and moves to Phase 6.

If creator hits friction mid-curation ("I'm tired, save what we have"), bail cleanly:

```
> Saving curation progress.
> 18 of 31 patterns curated this session.
> 13 remain in draft state.
> 
> Resume next session, or skip the remaining drafts and lock in just these 18?
```

Either path is valid. Bail at any time with no work lost, sticky curated entries persist; drafts can be revisited next session.

## Common mistakes

- **Rubber-stamping every Keep without reading the Theory of One panel.** Defeats the purpose. Force at least a 2-second pause per pattern by surfacing the iceberg-and-audience reminder.
- **Dropping without rationale.** Future runs re-surface the same pattern and the creator drops it again. Capture rationale every Drop, no exceptions.
- **Modify-as-rewrite-from-scratch.** Modify is for tweaking the pattern's framing, not inventing new patterns. If the creator wants to rewrite extensively, that's a Drop + a separate creator-supplied pattern (which gets logged as `source: creator-input` in the bank).
- **Surfacing all patterns at once instead of one-at-a-time.** Cognitive overload. Always one pattern per turn (with bulk-keep as opt-in escape).
- **Auto-bulk-keep without creator opt-in.** Theory of One requires conscious choice. Don't bulk-keep unprompted just because the spread is wide.
- **Letting Drop rationales drift to vague.** "I don't like it" isn't a rationale. Push for specificity: "what about it doesn't work for your audience?" Capture the answer.
