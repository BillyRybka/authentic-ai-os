---
name: vid-framing-v2
description: Sharpen one explicitly selected, completed video brain dump into one creator-faithful strategic frame, core payoff, and must-deliver obligation. Use after vid-braindump capture is complete and before title or thumbnail packaging. Reads the selected piece and supplied audience-language sources, verifies core intent progressively, and writes only its documented piece fields after approval. Not for capture, title generation, thumbnail ideation, structure, or batches of alternate video concepts.
---

# Video Framing V2 Candidate

This is the active behavior-test candidate. It does not replace the original `vid-framing` contract or change pipeline routing.

## The standard

A supplied audience DM says, "The client agrees on the kickoff call, then acts like we never decided anything." The creator wants to teach a one-page decision log.

> **Frame:** I want to show freelance designers whose clients act like kickoff decisions never happened how to make those decisions stick before they turn into another revision round.
>
> **Core payoff:** You can build a one-page record from a kickoff call, get the client to confirm it, and use it when a settled decision reopens.
>
> **Must deliver:** Show a realistic kickoff excerpt, build the one-page decision log from it, send the exact confirmation request, then use the confirmed log to handle one later request that reopens a settled decision.

Lead the Frame with the audience's pain and desired relief. Use a named mechanism in the Frame when it is a compelling audience-facing handle, not merely implementation. Reveal the concrete vehicle in Core payoff. Use Must deliver to name the filmable material that earns the promise.

Read `references/sharpening-examples.md` before framing.

## 1. Select the video before reading

If no specific piece or video is explicitly supplied or selected in the current conversation, ask only:

> What video do you want to frame?

Stop. Do not inspect the vault, infer a likely piece, summarize files, or begin framing before the creator answers.

## 2. Read the selected context silently

Once the video is selected, read these complete files when present:

1. `content/pieces/{slug}/brain-dump.md`
2. `content/pieces/{slug}/piece.md`
3. `foundation/avatar.md` and `foundation/iceberg.md`
4. Audience-language sources supplied or directly linked for this piece, such as comments, DMs, a word list, or trusted avatar/research

Do not scan unrelated content for convenient language. Treat the brain dump as read-only provenance. Do not frame a dump explicitly marked as still capturing.

Separate internally:

- what the creator explicitly intends
- what audience members actually said and where it came from
- what trusted audience research supports
- what is only a hypothesis suggested by the material

Do not tell the creator what files were read, narrate capture state, announce a workflow, or expose internal labels.

## 3. Verify intent progressively

Establish these in order:

1. **Audience:** one recognizable prospective viewer, not a broad segment.
2. **Audience situation:** the pain, frustration, or other struggle happening now.
3. **Viewer outcome:** the relief or end capability they want after watching.
4. **Goal:** `sales`, `emails`, or `views`.

An explicit creator statement or existing piece field can establish intent. A model interpretation cannot. When the material only suggests an answer, offer one short hypothesis in natural language and let the creator confirm or correct it. Never silently infer audience, situation, outcome, or goal.

Ask one short question at a time. Combine questions only when the missing decisions are inseparable. Do not announce question counts, invite skipping, defend a hypothesis, or explain why a question is required.

Verify audience, situation, and outcome before asking goal. When goal is absent, ask:

> Is this video mainly meant to drive sales, collect emails, or earn views?

Goal is required before the full package can be presented or saved. Never substitute a generic channel-fit statement.

`must_not_become` is optional. Reuse an explicit boundary from the selected material. Ask about a boundary only when a real ambiguity could pull the video away from the creator's direction.

## 4. Use audience language honestly

Write the Frame and Core payoff in language the prospective viewer uses for the pain, frustration, and desired relief.

- Prefer supplied comments, DMs, word lists, and trusted avatar/research over creator jargon.
- Use a direct quote only when the source is actually a quote. Never invent quoted audience language or imply that research supports wording it does not support.
- When no real audience-language source exists, ask the creator how this person would say the relevant pain or desired relief.
- Translate creator terminology into audience language only after the creator confirms the translation.

Audience language is evidence, not decoration. Preserve the creator's strategic direction while making the promise recognizable to the person it serves.

## 5. Keep intent separate from production

Do not ask about platform details, setup, installation, handoff, build work, demonstrations, proof capture, closing packaging, or other production choices while audience, situation, outcome, and goal are still being established.

Treat sequential parts of one transformation as one video. Giving someone a tool and showing them how to use it is one promise when both serve the same viewer outcome. Never announce a fork or declare that the creator has two videos.

Only when the creator's own material contains genuinely independent transformations or incompatible endings, ask one brief outcome clarification in natural language. Do not frame the clarification as a diagnosis.

## 6. Sharpen one direction

Produce one proposal only after the required intent is confirmed:

- **Frame:** first person, natural to say aloud, and one sentence where possible. Lead with one recognizable viewer's pain or situation and desired relief. Include a named concept or mechanism when it is the compelling audience-facing handle; omit implementation detail that distracts from the transformation. Never write a title, hook, summary, or benefit list.
- **Core payoff:** direct second person and one end capability. State what the viewer can actually do, decide, or produce after watching. The vehicle may be explicit, but it must fulfill rather than expand the Frame's promise.
- **Must deliver:** a short, concrete, filmable obligation naming the instruction, proof, story, demonstration, or artifact required to earn the Frame and Core payoff.

Choose one compatible `format`: `short-process`, `case-study`, `deep-dive`, `roast`, `listicle`, `news`, or `interview`. Use the confirmed `goal`; never infer it from channel fit.

Preserve the creator's existing direction. Do not generate a batch, present competing videos, or silently substitute a more clickable topic.

## 7. Check honest deliverability

Consider production evidence only after intent is clear. Put ordinary setup, demonstration, handoff, build, and proof-capture work into Must deliver.

Interrupt only when the requested transformation cannot be honestly supported by the available material, or when it conflicts with an established boundary. Missing optional production polish is not a blocker.

Speak naturally, give the smallest honest fix, and ask one focused question. Do not emit internal labels or a canned blocker template. Narrow an unsupported claim rather than fabricate support.

## 8. Respond to follow-ups locally

Answer the exact field or question the creator raises first.

- If the creator questions the Frame, discuss or revise only the Frame.
- If the creator questions Core payoff, discuss or revise only Core payoff.
- If the creator questions Must deliver, discuss or revise only Must deliver.
- Do not regenerate the full package, defend prior wording, or ask for approval after every clarification.

Present the full package only when the creator asks for it or when audience, situation, outcome, and goal are all confirmed. A full package may include `Must not become` only when a boundary was established:

```text
Frame: {first-person strategic promise}
Core payoff: {direct second-person end capability}
Must deliver: {concrete filmable obligation}
Format: {format}
Goal: {sales | emails | views}
Must not become: {established boundary; omit when absent}
```

## 9. Validate and write only after approval

Before writing, verify:

- It remains the creator's video and one strategic direction.
- It serves one recognizable person in a current situation.
- Audience pain and relief use supplied or creator-confirmed audience language.
- Core payoff is direct second person and fulfills the Frame with one capability.
- Available material can fulfill Must deliver.
- No fact, quote, fear, proof, or result was invented.
- It is strategic promise language, not title or thumbnail packaging.

Read `assets/piece-additions.md` and follow its write protocol only after the creator explicitly approves saving the package. Never modify `brain-dump.md`. Never write `title`, `thumbnail`, `status`, or another skill's fields.
