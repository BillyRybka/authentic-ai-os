---
name: vid-framing-v2
description: Sharpen one explicitly selected, completed video brain dump into one creator-faithful strategic frame, core payoff, and must-deliver obligation. Use after vid-braindump capture is complete and before title or thumbnail packaging. After a specific piece is selected, reads its full dump and context, asks only for missing creator-intent decisions, and can update only its documented piece fields. Not for capture, title generation, thumbnail ideation, structure, or batches of alternate video concepts.
---

# Video Framing V2 Candidate

This is an isolated behavior-test candidate. It is not the live `vid-framing` skill and is not wired into routing.

## The gold standard

Given a creator who says, "The client agrees on the kickoff call, then acts like we never decided anything," do not invent ten angles or turn that phrase into a title. Sharpen the direction they already brought:

> **Frame:** I want to show freelance designers who lose hours to reopened kickoff decisions how to make those decisions stick before they turn into another revision round.
>
> **Core payoff:** You can build a one-page record from a kickoff call, get the client to confirm it, and use it when a settled decision reopens.
>
> **Must deliver:** Show a realistic kickoff excerpt, build the one-page decision log from it, send the exact confirmation request, then use the confirmed log to handle one later request that reopens a settled decision.

The frame is a first-person, spoken strategic promise. Lead with the relief or transformation the creator's person wants. The mechanism is the vehicle and satisfying answer, not the headline promise. The core payoff is the one concrete capability the viewer leaves with. The must-deliver statement is the evidence and instruction the video owes that promise.

Read `references/sharpening-examples.md` for the full example and blocker examples.

## 1. Select the video before reading

If the creator has not explicitly supplied or selected a specific piece or video in the current conversation, ask only:

> What video do you want to frame?

Stop there. Do not inspect the vault, infer a likely piece, summarize files, or begin framing before the creator answers.

Once the video is selected, read the complete files, not excerpts or summaries:

1. `content/pieces/{slug}/brain-dump.md`
2. `content/pieces/{slug}/piece.md`
3. `foundation/avatar.md` and `foundation/iceberg.md` when present

The brain dump is read-only provenance for this skill. Never clean it up or add framing answers to it.

Do not frame a dump explicitly marked as still capturing. For a completed dump, identify internally:

- the single direction the creator is already trying to make
- the specific audience and recognizable person
- that person's current situation or other struggle
- the desired viewer outcome
- the video's stated goal, if present
- the creator's stated boundary

Do not announce what files were read, narrate capture state, describe this process, or explain what the skill will replace. Do not reduce "one person" to a broad market label.

## 2. Ask only for missing intent

Treat an input as known only when the dump, existing piece fields, or creator has established it clearly:

1. **Specific audience:** one recognizable person, not a broad segment.
2. **Audience situation:** what that person is doing, noticing, or repeatedly struggling with now.
3. **Viewer outcome:** what becomes possible for them after watching.
4. **Video goal:** `sales`, `emails`, or `views`.
5. **Must not become:** the creator's boundary for this video.

Ask only for inputs that cannot be grounded from the selected piece. Use one short creator-facing question at a time, or a compact set when the missing decisions are tightly related. Ground each question in the creator's language where useful. If all five inputs are known, ask nothing and sharpen the frame.

When goal is absent, ask directly: "Is this video mainly meant to drive sales, collect emails, or earn views?" Goal is required before lock. Never replace this decision with a general statement about channel fit.

Do not announce a question count, invite skipping, expose internal reasoning labels, or explain why each question is being asked. Do not ask for an "angle."

Do not ask about platform details, installation or handoff readiness, build work, demonstrations, proof capture, closing packaging, or other production choices during intent discovery. Consider those only after the five intent inputs are clear, and surface one only if it directly prevents the requested promise from being honest.

Treat sequential parts of one transformation as one video. Giving someone a tool and showing them how to use it is one promise when both serve the same viewer outcome. Never announce a fork or declare that the creator has two videos. Only when the creator's own material contains genuinely independent transformations or incompatible endings, ask a focused outcome clarification in natural language.

## 3. Sharpen one direction

Produce exactly one proposal:

- **Frame:** first person, natural to say aloud, and one sentence where possible. It leads with one recognizable person's current behavior/problem and promised relief. It may imply the mechanism, but does not have to name it when that would turn the vehicle into the headline. It is not a title, hook, summary, or list of benefits.
- **Core payoff:** second person and one outcome. It states what the viewer can actually do, decide, or produce after watching. It may reveal the mechanism as the satisfying answer, provided that capability fulfills the frame's promised relief rather than adding a second outcome. It must remain honest without hidden prerequisites.
- **Must deliver:** a short obligation naming the instruction, proof, story, or demo that has to appear for the frame to be true. This is a lock-time check, not a `piece.md` field.

Preserve the creator's existing direction. Do not generate a batch, present competing videos, or silently substitute a more clickable topic. When the direction is weak, make the smallest sharpening move that preserves its subject, evidence, and intended change.

Choose one compatible `format`: `short-process`, `case-study`, `deep-dive`, `roast`, `listicle`, `news`, or `interview`. Use the established `goal`; never infer it from channel fit. Format is an implementation choice after the promise is clear, not a new angle.

## 4. Check deliverability after intent is clear

Build Must deliver only after the five intent inputs are established. Put ordinary demonstration, handoff, build, and proof-capture work in Must deliver rather than turning it into interview questions or blockers.

Interrupt the proposal only when:

- the requested transformation depends on evidence, a story, or a demonstration the available material cannot honestly support
- the creator's requested transformation conflicts with the established `must_not_become` boundary

Do not rubber-stamp an unsupported claim. Missing optional production polish is not a blocker.

Speak naturally, give the smallest honest fix, and ask one focused question. Do not expose internal labels:

```text
I can't honestly promise {specific transformation} from what is here yet. The smallest fix is {one reduction, artifact, fact, or choice}. {one focused question}
```

Do not lock or write the frame until the blocker is resolved. If the creator cannot supply the missing material, narrow the promise rather than fabricate support.

## 5. Validate and lock

Before showing the proposal, verify:

- It remains the creator's video, not a substitute direction.
- It promises one video to one recognizable person in a current situation.
- Audience, situation, viewer outcome, goal, and boundary are all established.
- The core payoff gives the viewer one usable capability that fulfills the frame's promised transformation. It may be more concrete than the frame by naming the vehicle, but cannot change or expand the promise.
- The available material can fulfill the must-deliver obligation.
- It respects `must_not_become`.
- No creator fact, fear, proof, quote, or result was invented.
- It is strategic promise language, not title or thumbnail packaging.

Show:

```text
Frame: {first-person strategic promise}
Core payoff: {second-person one outcome}
Must deliver: {concrete obligation}
Format: {format}
Goal: {goal}

Lock this frame?
```

When the creator asks for a correction, revise the one proposal. Do not branch into options.

## 6. Write only after lock

Read `assets/piece-additions.md` and follow its append/replace protocol. This candidate owns only:

- `frame`
- `core_payoff`
- `format`
- `goal`
- `voice_context`
- `must_not_become`, when explicitly present in the selected piece or confirmed by the creator
- `last_updated`
- the `format-{format}` tag
- `## The Read` with `Target`, `Transformation`, and `Stakes`

Never write `title`, `thumbnail`, `status`, capture provenance, or another skill's fields. Never modify `brain-dump.md`.
