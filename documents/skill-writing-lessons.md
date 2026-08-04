# Skill Writing Lessons

A living log of what we learn building, auditing, and rewriting the skills in this vault. Add an entry whenever an audit, rewrite, or eval run teaches something reusable. The point is to improve skills faster by not relearning the same lesson twice.

Each lesson carries one tag. **[creative]** means it is specifically about making creative output good: voice, flow, dynamic phrasing, capture. These are the lessons that matter most for skills like the vid- family. **[structural]** is build hygiene that applies to any skill. **[process]** is how to run the work. One tag per lesson. If it could plausibly be "both," it is structural, the creative tag is reserved for lessons that are actually about the craft of the output.

## How to add a lesson

Each entry has three parts:
- **Principle** in one line.
- **What happened**, the concrete example, before to after. Keep it real and specific.
- **How to apply** next time.

Keep examples grounded in actual skills and actual changes, not abstractions.

---

## Craft and structure

### 1. A leaf skill does one thing. It does not narrate the pipeline. [structural]

**Principle:** A skill should reference only its inputs and its immediate handoff. Orchestration knowledge belongs in the orchestrator.

**What happened (vid-intake, 2026-06-24):** The skill's scope section described what `vid-framing`, `vid-intro`, `vid-segment`, and `vid-ending` each do, and one line enumerated every downstream skill's future frontmatter ("vid-framing appends selected_angle, vid-title appends title, vid-structure appends segment_purposes..."). That content rots every time a downstream skill changes, and it bloats the file.
- Before: a paragraph of pipeline narration plus a full downstream-field enumeration.
- After: "Intake captures only. It does not frame, title, or write. `vid-framing` runs next," plus a one-line pointer to `knowledge/vault-integration.md` for the full schema. The "what handles what" map already lives in `vid-pipeline`.

**How to apply:** When a skill starts explaining other skills, cut it. Keep cross-skill references to prerequisite plus next handoff. Let the orchestrator own the chain.

### 2. Load-bearing logic must live in the always-loaded SKILL.md, not a "fallback" reference. [structural]

**Principle:** If a behavior must run on every invocation, it has to be in the file that is always in context. A reference you tell the model to open "only as a fallback" will not run.

**What happened (vid-intake):** The skill declared 7 intake modes but ran the same 6 phases for all of them. The choreography that actually made the modes different (P-A-O for story-first, the source-invisible contract for inspired-by, the forced pivot for client-win) lived only in `mode-conversation-examples.md`, which the SKILL.md said to "open only as a fallback, when a conversation stalls." So on a normal run the model named the mode and then ran the identical spine. The modes changed nothing.
- Before: one-line mode list in SKILL.md, real per-mode behavior quarantined in a fallback file.
- After: a compact per-mode routing table inline (one row per mode: opening signal plus the one or two distinctive moves), and the examples file demoted to optional depth.

**How to apply:** Ask of any reference file, "does the skill work correctly if the model never opens this?" If no, the load-bearing part belongs in the SKILL.md. References are for depth and calibration, not for the core loop. (Pulling that table inline fixed the immediate problem, but it was not the end of it. Lesson 6 comes back to these same modes and finds they were never really separate jobs at all.)

### 3. Match the house style of your clearest skill. [structural]

**Principle:** Pick the most readable skill you have and conform new and rewritten skills to its shape. A human should scan it once and understand the process.

**What happened (vid-intake, benchmarked against `youtube-pipeline`):** The original was 280 lines of prose, with "the save happens in both modes" stated three times and four overlapping rules sections (Conversational discipline, Hard friction, Soft friction, Principles) that recycled the same handful of ideas.
- Before: 280 lines, paragraph-heavy, repeated ideas.
- After: ~165 lines on the youtube-pipeline pattern, one-line opener, a "What loads, and when" table, a scannable numbered flow, the modes as a table, and one "Rules (and why)" section. Each idea stated once.

**How to apply:** Lead with a one-line opener (what it does, in a sentence). Add a "what loads, and when" block. Make the process a scannable list or table, not multi-paragraph walkthroughs. Collapse repeated rules into one section. State each idea once.

### 4. The description is for triggering, not for documenting behavior. [structural]

**Principle:** The frontmatter description is the trigger mechanism. It should carry what the skill does plus when to fire it, with real example phrases. Move principles and behavior specs to the body.

**What happened (vid-intake):** The description was ~135 words and smuggled in body content: the verbatim-voice principle, "Anti-fabrication. Adaptive drilling. Target 5-10 minutes, never an interrogation," and the iceberg-fit and save-path mechanics. None of that helps the model decide whether to fire the skill.
- Before: ~135 words, half of it behavior specs.
- After: ~95 words, what it does plus the 8 example trigger phrases ("I want to make a video about X", "here's a transcript I want to turn into a video", "I saw this competitor video and want my own take"...). Everything else moved to the body.

**How to apply:** The long part of a description should be trigger phrases, not prose. Per skill-creator, varied example phrasings (formal, casual, "even if they don't say the skill name") earn their length. Behavior, principles, and mechanics go in the body.

### 5. The output should only hold what a later skill actually reads. [structural]

**Principle:** A field or section in your output earns its spot only if something later reads it. Looking useful is not the same as being used. Before you keep it, go find who reads it.

**What happened (vid-intake, 2026-06-25):** We went through the brain-dump file and found three kinds of dead weight. Every one of them looked fine until we checked who actually used it.
- **A section nobody read.** `## Strongest raw lines` was just the best lines copied back out of the raw dump. We searched every vid- skill, and the only place it showed up was vid-intake's own file. Nothing downstream ever read it. Cut it.
- **A gate nobody guards.** `iceberg_aligned` showed up in vid-framing and vid-structure, but only ever in a "this should exist" checklist, never in an actual if-this-then-that. A flag that nothing acts on does not gate anything. And it is `true` on almost every video, so it tells you nothing. The only interesting case would be the rare exception, and nothing reads that either.
- **Work that gets redone anyway.** vid-structure re-reads the raw dump from scratch and re-sorts it against the locked angle (`brain-dump-mining.md`). So intake's neat little Lessons, Stories, and Proof piles just get tossed and rebuilt. Sorting them at intake was wasted effort.

**How to apply:** Before you keep a field or section, search the later skills for who reads it, and notice the difference between "it is listed somewhere" and "something actually acts on it." Cut what nothing reads. Do not pre-sort material that a later skill is going to re-sort anyway. And do not keep a flag that is almost always the same value just in case something reads it one day; add it when the thing that reads it actually exists. If another skill writes the same field too, pulling it is a decision across both skills, not a quiet local cut.

### 6. A list of the things people can hand you is not a list of different jobs. [structural]

**Principle:** When a skill takes different kinds of input, that is a list of what someone can bring you, not a list of separate jobs to do. A good model already adjusts on its own once it sees what came in. The only structure worth keeping is the handful of things it would otherwise get wrong.

**What happened (vid-intake):** This is where the modes from lesson 2 finally got sorted out, and it took three passes to see it clearly.
1. First, the seven modes were named in the skill, but the real behavior for each one lived in a fallback file nobody opened, so every mode ran the same way. That was lesson 2.
2. We fixed that by pulling a mode table inline, so the differences actually ran.
3. Then we looked harder and found the real problem: the seven were never seven different jobs. They were three different questions jammed into one list. How did it arrive (talked out loud, or pasted)? What kind of thing is it (a story, a client win)? And what does the creator want to make from it? "Idea" was just the normal case with no twist.

So we collapsed it. One way in (the creator's own material, talked or pasted), plus a short watch-list of things to handle when you spot them: a story, get the moment before the lesson; a client win, push to the principle; a claim with no proof, mark a TODO. `intake_mode` stayed only as a label on the saved file, not a switch that sends the conversation down a different path. And the last piece: you find out what someone wants by asking, not by guessing from the file they pasted. A transcript could be a remake, a reaction, or just raw notes, so you ask what they want to make. You do not see a transcript and assume "run the transcript path."

**How to apply:** Keep "what someone can hand you" separate from "what the skill does." When you are staring at a pile of modes, check whether they are actually different jobs or just different things to bring. Usually it is one job plus a short list of gotchas. Trust the model to adjust from what it sees, and only spell out the parts it would miss on its own.

### 7. Cut to the one real thing, but don't cut the parts that are actually working. [structural]

**Principle:** Most of what looks like structure in a skill is bloat wearing a costume. Modes, sections, rules, and branches that each look like they do something, but really all lead to the same place. The job is to cut hard toward the one thing the skill actually does, while leaving the parts a reader or a later skill genuinely needs. The hard part is telling those two apart.

**What happened (vid-intake):** Almost every cut in this audit was the same move, and the clearest tell was this: when a set of "options" all end up in the same place, they are not options, they are one thing dressed up. The seven modes all ran the same flow, so they were one flow. The schema had sections and a flag that nothing ever read, so they were filler. The skill narrated the whole pipeline and said the same rule three times, so most of it was repetition. Every step had a time budget that just added noise. All cut.

But we did not cut everything. The verbatim raw dump stayed, the fabrication TODOs stayed, the ownership check on a pasted transcript stayed, the fit conversation stayed, because a reader or a later skill actually leans on each of those. And the inspired-by route, a real feature that just was not needed yet, we moved to a v2 plan instead of deleting it. Cutting bloat is not the same as cutting scope.

The last pass was making whatever survived read like a person talking instead of a spec sheet: plain words, jargon only where it earns its keep, and reading it back out loud to catch anything stiff.

**How to apply:** When you see a pile of variations, ask "do these actually end somewhere different, or do they all lead to the same place?" Same place means it is one thing in a costume, so cut it down. Before you cut, ask the other question too: "if I remove this, does a reader or a later skill lose something they need?" If yes, it is real, keep it. If it is real but not needed yet, park it in a plan doc, do not delete it. Then say what is left the way you would say it out loud.

### 17. An incomplete handoff shows up downstream as a redundant interview. [structural]

**Principle:** If a downstream skill re-plans work an upstream skill was supposed to hand it, the handoff is incomplete. Fix the upstream output, not the downstream skill.

**What happened (vid-structure, 2026-07-01):** vid-structure handed vid-segment a half-finished outline: the points were named, but the parable and principle were left as "candidates to pick later." So vid-segment re-queried the banks, re-picked the blocks, and re-confirmed the structure with the creator one segment at a time. That per-segment structure interview felt broken because it was re-doing planning that should have happened once. The fix was to make vid-structure lock the complete plan (parable type plus the specific block, principle plus proof, per point), so vid-segment just writes.

**How to apply:** When a downstream skill re-interviews the user or re-derives a decision, look upstream. The prior skill's output is incomplete. Complete the plan in the planner. A writer that re-plans is a boundary bug, not a feature.

### 19. Never argue for an instruction. The argument is what plants the doubt. [structural]

**Principle:** State the instruction and stop. A sentence defending it against an objection nobody raised introduces the exact idea it is trying to rule out.

**What happened (vid-framing, 2026-08-04):** After a cleanup pass, seven lines had grown a defense of themselves. The clearest:

> **Arguing:** For one video idea, as many genuinely different framing options as the material supports. No target number: a count makes you pad to reach it, and three real angles beat five where two are filler. Say how many survived, in a clause.
>
> **Instructing:** For one video idea, as many genuinely different framing options as the material supports.

Nothing in the first sentence makes a reader think about counting until the second sentence starts arguing against it. The defense created the problem it was defending against. The trailing "say how many survived" was worse: it had been carried over from a version with a visible screen-and-cut step, so in this skill it counted nothing.

Most of the seven were defending an edit against a version the reader never saw, which is changelog written into the skill:

> **Arguing:** Read the register off those pairs rather than off a list of approved words.
>
> **Instructing:** Read the register off those pairs.

The list of approved words had been deleted two commits earlier. The only reader who needed that clause was me.

Same shape in the other five: "This is the only validation pass, run it once" guarded against duplicate checklists that no longer existed. "Whether a frame lands on the audience is Step 2's job and it has already been done" explained which criteria had been removed. "Two tests... vague variety instructions produce the same video in four outfits" argued with the guard they replaced.
- Before: 14,409 characters, seven instructions each trailed by its own defense.
- After: 12,601 characters, same instructions.

**How to apply:** After writing a rule, read the sentence that follows it. If it exists to justify the rule rather than to change what gets done, cut it. Two tests that separate the cases. **Does the reader know about the alternative?** If the instruction is the only thing they have seen, warning them off the alternative introduces it. **Would they do the wrong thing without this sentence?** A why earns its place when it changes behavior in a case the rule does not cover (keep "state the format, do not ask, because a question here spends attention on a call you can already make"). It does not earn its place when it defends the rule's existence. Above all, never write the diff into the file: the reader did not see the old version, and explaining what you removed is the surest way to put it back in their head.

---

## Flow and voice (creative skills)

### 8. Keep the internal machinery invisible to the user. [creative]

**Principle:** Mode detection, fit checks, slugs, and confirmations are plumbing. The user should never feel them. The product is flow state.

**What happened (vid-intake):** The skill announced "Mode 1, idea dump. Sound right?" to the creator, then ran fit, pillar, slug, and save as four separate confirmation turns. That jargon and that checklist dragged the capture experience.
- Before: mode announced out loud; four end confirmations.
- After: silent routing (the creator never hears a mode number), fit and pillar confirmed in one move, slug folded into the save line.
- Result: the judge's `capture_without_interrogation` score moved 4.4 to 4.67 with voice fidelity held.

**How to apply:** Route internal branches silently. Bundle confirmations. If a step exists for the skill's bookkeeping and not the user's decision, do not surface it.

### 9. Offer to go deeper once, then flow. Do not re-ask permission. [creative]

**Principle:** A strong capture helps every downstream step, so mining is good when the user is willing. The thing that breaks flow is the permission-handshake and ignoring a stop, not the questions themselves.

**What happened (vid-intake, Billy's framing):** Phase 5 said "if they go, ask one pointed question at a time," and in testing the skill re-asked permission before each question and pushed again after the creator had said "save what I have and I'll come back." Billy: "it does feel goofy to essentially be like, okay can I ask you another question? It's like you just freaking asked me a question... but we don't want to just endlessly mine."
- Before: "offer one deeper pass... ask one pointed question at a time," plus a soft stop list.
- After: "Offer once. If they say go, just ask the questions in flow. Do not re-ask permission before each one. Keep pulling while they stay engaged and the answers keep coming back richer. Stop the moment they signal done, do not reopen a spot they closed, and never push one spot more than twice."

**How to apply:** Make the offer once, then read engagement instead of asking permission. No hard question cap; the stop signal is the cap. The instant they say "save it / I'll come back / that's it," stop and mark a TODO.

### 10. Test interactive skills by simulation, with isolation, and lean on adversarial cases. [creative]

**Principle:** A conversational skill cannot be tested on a static input. It needs a simulated counterpart that holds the line on what the user would withhold, plus a separate fresh judge.

**What happened (vid-intake):** Each test ran the skill against a `creator-simulator` persona built from a seed, with `reveals` (answer if asked) and `withholds` (never volunteer, never invent). The adversarial seeds (a client named but numbers withheld, a thin dump with no story) are what proved fabrication resistance: the skill marked TODOs and created a people stub instead of inventing a revenue figure. A separate judge with no knowledge of the rewrite scored against a locked rubric.

**How to apply:** For any skill that converses, build a persona that withholds realistically and an isolated judge. The withholds are the real test; a skill looks fine until the user does not hand it what it wants.

---

### 11. Describe the intent of a line. Do not script it verbatim. [creative]

**Principle:** Tell the skill what a message should accomplish and what to uncover, then trust the model to write the sharp, context-fit line. Verbatim scripts read rigid.

**What happened (vid-intake):** Drafts scripted the skill's exact words, the open-the-door line and the drill questions ("Tell me the moment, not the lesson", "Where's that number from?"). Billy: "claude is smart enough to come up with its own brief sentence, why script it like that?" and "we want sharp pointed questions that uncover more; scripting verbatim makes it seem rigid."
- Before: `Open the door: "Go ahead, dump everything on this, raw."`
- After: `Open the door: in your own words, tell them to dump everything raw and to say if they want help digging in.`

We swept both the SKILL.md flow and `digging-deeper.md` (then named `push-vs-pause-rules.md`) to this style: keep the creator-side situations as illustration, drop the skill's locked quotes.

**How to apply:** Describe the move's goal and the gap it targets, not the literal sentence. Examples should show the situation (the creator's gap) and the why, not a script for the skill to read. An illustrative line is fine only if labeled as register, not a quote to paste.

**The boundary (added 2026-07-04, vid-intro audit).** This rule is not absolute, and the first version over-generalized it. It governs the creative and interview surface, the questions that pull material, anything shaping the words the creator will speak. There, scripting reads rigid and a dynamic line fit to what just came up is better. It does NOT govern process gates: a save confirmation, a "pick 1 or 2," a hard-rule kickback. Billy: "Scripted questions aren't bad, this seems fine. If it's an interview I'd prefer it to have some guidance but be dynamic based on what's needed." So: interview and capture moments get guidance plus room to adapt; mechanical gates can stay scripted. When an audit flags a scripted line, first ask which surface it is. A scripted gate is not a finding.

### 12. Don't put a clock on a creative conversation. [creative]

**Principle:** Putting a time on a creative back-and-forth ("under 5 minutes," "30 seconds," "10 seconds") makes the skill feel rushed and robotic, and it tells the model to stop for the wrong reason. What should tell you when to stop is whether the person is still giving you good stuff, not how many minutes have gone by.

**What happened (vid-intake):** The skill and its references were full of little clocks: "Thirty seconds" on the reflect-back, "under five minutes" and "fifteen minutes" in the pacing notes, "10 seconds" on the fit check, "60 seconds" to grab the proof. Billy: "don't put a time on it." We cut all of them. The "when to bail" rule went from "if you are still drilling at fifteen minutes" to "if you keep drilling and nothing new is coming up." The times inside the example dialogues that are actually the creator's content ("12 weeks," "5am") stayed, because those are material, not a clock on the conversation.

**How to apply:** Never put a stopwatch on the conversation itself. Read the person instead: still engaged and the answers keep getting richer, keep going; answers thinning out, wrap it up. Cues about being concise are fine ("one line," "one question at a time"). Anything counted in seconds or minutes is not.

---

## Evals and verification

### 13. The skill is the source of truth. The eval measures it. [structural]

**Principle:** When a skill fails its own eval, do not change the skill to make the eval pass. Find the schema or spec authority, then fix whichever side is actually wrong. The goal is the eval being correct, not the eval passing.

**What happened (vid-intake):** Tier A failed on piece.md frontmatter, and the first instinct was to change the skill's schema to satisfy `eval.py`. Billy: "we want it the other way around." The schema authority (`knowledge/vault-integration.md`) and the skill both used `created` and `last_updated`; the eval was stale, still requiring the old `captured` field. The skill was right.
- Fix: updated `eval.py`, `check_handoff.py`, and the three `validate_billy` scripts to match the skill, and left the skill alone.

**How to apply:** On an eval failure, check the authority doc first. If the skill matches it, fix the eval and any stale fixtures. Never bend the product to the instrument.

### 14. Run the eval after a rewrite, even for "just wording." It surfaces drift you cannot see by reading. [structural]

**Principle:** Contract drift hides across files. Reading one file will not show it. Running the corpus will.

**What happened (vid-intake):** The `captured` vs `created`/`last_updated` mismatch on piece.md existed in four places at once (the skill, the authority doc, the eval, and the baseline fixtures) and had drifted before this session's rewrite even started. It was invisible reading any single file. The corpus re-run exposed it immediately (6/6 fail on `piece_frontmatter`).

**How to apply:** Re-run evals after any rewrite. A clean pass is not the only value; the failures catch latent contract bugs the rewrite did not cause but did reveal.

---

## Process

### 15. When the user is skeptical, audit the artifact yourself. Do not rubber-stamp a subagent's summary. [process]

**Principle:** Subagent summaries can cheerlead. If the user doubts a skill, read the skill yourself before forming a view.

**What happened (vid-intake):** The first exploration agents came back defending the skill ("complexity justified? YES"). Billy's instinct was the opposite, that the modes did not do much. Reading the SKILL.md directly confirmed Billy: the modes did not change behavior on a normal run. The agents had described the structure without testing the skeptical claim.

**How to apply:** Delegate breadth, but verify the load-bearing claim by reading the actual file. Especially when the user is the one raising the doubt.

### 16. Checkpoint before a rewrite. Respect parallel sessions. Look at untracked files. [process]

**Principle:** Commit a clean baseline before refactoring, stage deliberately, and inspect what is untracked.

**What happened (vid-intake):** Before the rewrite we pushed a checkpoint, staged everything except an accidental `SYSTEM-MAP copy.md`, and caught that `verify-subagent.md` was untracked. The skill referenced that file, so the committed tree pointed at a file that did not exist in the repo, a real distribution bug we would have shipped.

**How to apply:** Commit a baseline first so the rewrite is a clean diff. Inspect untracked files before staging; a referenced-but-untracked file is a shipping bug, and a stray "copy" file is junk to leave out. Billy runs parallel sessions, so stage only your paths.

### 18. Verify against the source before collapsing two concepts into one. [process]

**Principle:** When a rewrite hinges on "these two things are the same," read the domain source before you merge them. Assumed synonyms are where canon gets quietly corrupted.

**What happened (vid-structure, 2026-07-01):** I argued we should kill the word "tension" because it was just "setup and payoff" renamed, and told Billy to cut it. Billy sent the source (Ed Lawrence's `naming-untangle.md`) and said not to jump to conclusions. The source is explicit: setup/payoff is the mechanism you plan, tension is the meter (the curiosity gauge) that mechanism moves, and they are NOT the same axis. Collapsing them would have corrupted the model. The real fix was to rename the artifact from "tension" to "setup and payoff" (the thing you actually plan) and keep tension as the meter, referenced once as the why.

**How to apply:** Before collapsing or renaming a concept, read the authority. If the rewrite depends on two labels meaning the same thing, prove it from the source first. When the user says "don't jump to conclusions" and hands you a doc, the doc usually contradicts the shortcut you were about to take.
