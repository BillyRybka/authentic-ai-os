---
type: reference
doc: thinking-partner-agent-research
project: authentic-ai-os
status: active
tags: [reference, research, thinking-partner, agent-design]
---

# Thinking Partner Agent: Research Base

Evidence base for building an agent that runs a real collaborative thinking session, modeled on recorded calls with a human thinking partner. Domain-general by design: the same conversation should work toward titles, business planning, or anything else.

Researched 2026-08-22. Academic sources are the load-bearing ones. Most popular "prompts that make AI argue with you" content is filler and is not cited here.

## The core risk

A default AI thinking partner feels productive while quietly destroying the thing that makes the conversation valuable.

Nature study (Wharton Mack Institute coverage): ChatGPT-assisted brainstorming raised the creativity of *individual* ideas and significantly reduced the diversity of the idea *set*. 37 of 45 statistical comparisons showed significant diversity drops. In one task 94% of AI-assisted ideas overlapped, and nine participants independently named their invention "Build-a-Breeze Castle." Human-only ideas were entirely unique.

The value of a thinking session is spread, not polish. This is the failure to design against.

## Five design constraints

### 1. The agent must not lead

Controlled study on human-led vs model-led co-creation (arXiv 2510.23324): human-led produced more original work. Model-led lowered cognitive load and homogenized output.

Build rule: open by making the creator generate. Work on what they produced. Never open with "here are five angles." Suggestion-first is the fastest way to collapse the session onto the model's prior.

### 2. Rotate the stance, do not run one voice

arXiv 2504.13868: the homogenization effect is largely an artifact of *uniform deployment*, not inherent to the model. Ten diverse personas generating plots preserved diversity against a human-only baseline. Their framing: treat the model as a configurable partner, not a static tool.

Build rule: one move set, several seats. Example seats: wants the strongest version, wants it killed, wants the weird version, only asks about the audience. Switch seats deliberately within a session and across sessions.

### 3. Sycophancy is structural, not tonal

Interpretability work (arXiv 2604.19117) found models detect that a user's belief is wrong and agree anyway. It is trained in by RLHF, since raters reward agreement. "Be critical, don't just agree with me" in a system prompt does very little.

What actually works:

- Required steelman of the opposing position
- "Assume this fails. Why?" framing rather than open evaluation
- A forced "what I would say if I had no incentive to agree" section
- Scalar over open questions. "Rate this 1 to 10" resists flattery better than "what do you think"
- Avoid asking for balanced pros and cons. Balance reintroduces the agreement bias.

### 4. The judgment layer will fail on v1

arXiv 2509.04871 cloned a voice sales agent from roughly 1,000 real call recordings. Their pipeline:

1. Sample and rank calls by quality (top performers vs average)
2. Derive a job description from about 40 top calls: tasks, responsibilities, conversational style
3. Extract knowledge per sub-topic
4. Distill representative example dialogues per call phase
5. Compose into one system prompt

Their failure report is the useful part. Routine and structured segments transferred cleanly. The hard judgment work (persuasion, objection handling) did not. Named causes: **ambiguous objectives** and **overly cautious behavior**. Fixed by explicit goal-setting and refinement, worth roughly 20% improvement in hard scenarios.

Build rule: expect the mechanical moves to transfer immediately and "knowing when to push" to fail. Build the refinement loop on day one instead of expecting v1 to land.

### 5. It drifts by turn five

Widely documented: custom instructions decay as context fills, and by response five or six the model reverts to generic patterns. A real thinking session runs an hour.

Build rule: the agent needs a re-anchoring mechanism, or it is sharp for ten minutes and mush afterward.

## Confirmed patterns

**One question at a time.** The most consistent recommendation across Socratic and coaching agent implementations. Some go as far as "only one sentence in the reply is a question." Most commonly cited single lever.

**Cross-session continuity must be deliberate.** The practical pattern that works is a structured handoff written at the end of each session and loaded at the start of the next. Without it the move inventory never accumulates and the creator re-explains themselves every time.

## The unresolved tension

Cloning one person's voice fights the diversity finding. Rotating stances fights the "it feels like him" goal.

Current resolution: clone the **move set** and the **trigger conditions**, since that is the transferable part and it is what the cloning paper actually extracted. Let the **stance rotate**, since that is what protects against the Build-a-Breeze Castle problem. A real partner has a repertoire, not one setting.

## What to extract from a recorded session

Thirteen items. The first nine are the general frame. The last four were forced by the research above.

1. **Move inventory.** Every distinct thing the partner does that changes the state of the creator's thinking, each with a verbatim quote and a note on what it did to the next sentence. This is the whole asset. Twelve real quotes beat any amount of description.
2. **Trigger conditions.** What made them push. Vagueness, an unsupported claim, repetition, or an idea that was working and deserved more. Capture the moments they did *not* push as much as the ones they did. Selectivity is the value.
3. **Rhythm and airtime.** How long before they cut in. Interrupt mid-thought or wait. One question then silence, or a stack.
4. **Divergence vs convergence, and who calls the switch.** Do they generate or only prune. When did it flip from more to pick one, and who flipped it.
5. **How the goal got set,** and how the session got there from catching up. The warmup is not filler. It is what makes the sharp part possible.
6. **Dead ends and the sentence that killed them.** Where the implicit quality bar lives. First thing a normal summary throws away.
7. **The creator's own tells.** Stuck sounds different from cooking. Lets the agent know whether to push or shut up.
8. **What the partner knew that an agent will not.** Business, audience, back catalogue. Tells us exactly what context to load so a move is honest rather than hollow.
9. **Where they added nothing.** Do not clone the whole person.
10. **Initiated vs responded,** every instance. Establishes the real human-led ratio to build against.
11. **Every disagreement, verbatim,** and how it landed without stalling the session. Anti-sycophancy training data that is specific rather than generic.
12. **Distinct stances occupied** across the session, and what triggered each switch.
13. **The arc.** Sharp at minute 50 or faded. Tells us where re-anchoring is needed.

## Two extractions, never one file

A recorded session contains two separate things:

- **The mechanics** (items 1 to 13). This becomes the agent.
- **The content.** The actual decisions and ideas that came out. This is video material and belongs in the vault as material.

Mixing them produces an agent that steers every future conversation back to the original topic.

## n=1 warning

One call gives a strong first draft and a false sense of certainty. The extraction format must be built so a second and third session stack into it, with moves accumulating and trigger conditions getting confirmed or corrected.

## Sources

- ChatGPT Decreases Idea Diversity in Brainstorming (Nature), via Wharton Mack Institute: https://mackinstitute.wharton.upenn.edu/2025/new-in-nature-chatgpt-decreases-idea-diversity-in-brainstorming/
- Partnering with Generative AI: Human-Led and Model-Led Interaction in Co-Creation: https://arxiv.org/pdf/2510.23324
- Diverse AI Personas Can Mitigate the Homogenization Effect in Human-AI Collaborative Ideation: https://arxiv.org/abs/2504.13868
- Cloning a Conversational Voice AI Agent from Call Recording Datasets: https://arxiv.org/html/2509.04871v1
- LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-Lying Circuit: https://arxiv.org/html/2604.19117v1
- Preventing AI Sycophancy, adversarial council prompts: https://www.mindstudio.ai/blog/prevent-ai-sycophancy-adversarial-council-prompts
- Why ChatGPT Keeps Ignoring Custom Instructions: https://resources.opencraftai.com/blog/why-chatgpt-keeps-ignoring-custom-instructions-and-what-actually-works/
- LLM-based Socratic conversational agent, effects study (ScienceDirect): https://www.sciencedirect.com/science/article/abs/pii/S0360131525002623
- Socratic coach prompt pattern: https://thatryanp.medium.com/my-go-to-prompt-for-chatgpt-socratic-coach-7bf0dd2c01ec
- How memory transforms AI agents: https://moveo.ai/blog/ai-memory-agents
