# Skill Auditor: Locked Design

The design we build the structure auditor from. This is not the skill yet, it is the spec: the mindset, the severity model, the multi-agent pipeline, and the rubric. Every test traces to a lesson in `skill-writing-lessons.md` and was pressure-tested against real skills (old and new vid-structure, vid-intake, and a third-party bio generator) during the session that produced this.

## What it is (and is not)

- **Is:** a white-box auditor. It reads a skill file and its neighbors and checks craft: does it do one job, does every part earn its place, does the workflow hold together, does it load the right things at the right time. Cheap triage across many skills.
- **Is not:** an output-quality judge. Good still means good outputs, and that needs the eval loop (Tier A deterministic plus Tier B judge). The auditor is a pre-filter that catches craft rot before you spend on output evals. A skill can pass every test here and still write garbage, and a skill can fail a test and still work. The auditor never claims otherwise.
- **Distinct from** the old `audit-skill` command (XML/format compliance) and `creative-skill-audit` (judges the creative output). This is the third, and it overlaps neither.

## The mindset (two forces, both true at once)

1. **Relentlessly thorough.** Assume something is wrong. Read every line. Check every claim against the rest of the file and against the neighbors. Never skim. The failure we are preventing is a bad problem that ships.
2. **Brutally honest about severity, and skeptical of itself.** Finding a rule violation is the easy part. The hard part is asking "does this cause a real bad outcome, or am I pattern-matching a rule that does not bite here?" Default a finding to *not a problem* unless you can name the bad thing it causes.

The bar: the auditor finds MORE issues than anyone AND dismisses MORE non-issues than anyone. An auditor that cries "fail" on a harmless script is as useless as one that misses a real bug, because you stop trusting it either way.

## Severity model

- **critical:** breaks the skill, produces bad output, or risks fabrication or safety. Must fix.
- **moderate:** bloat, rigidity, drift risk, or maintainability cost. Should fix.
- **minor:** works fine as-is, only a polish or elegance gain.
- **false-positive:** the rule was matched but does not bite here. Dismissed, and listed openly so the reader sees what was considered and rejected.

Default toward false-positive when unsure. Severity is contextual: the same violation can be minor in one skill and critical in another (a hard-scripted line is minor in a mechanical intake, moderate in a voice-sensitive creative capture).

## The pipeline

Six stages. Multi-agent is load-bearing, not a speed trick: a single agent cannot be calibrated because it cannot adversarially refute its own finding, and it anchors on its first impression and skims fourteen tests. Independence is what buys both thoroughness and calibration.

**0. Load context (orchestrator).** The target is the WHOLE skill directory (SKILL.md plus every reference, asset, and script) plus every knowledge file it points to. Our worst real violations lived outside SKILL.md: the clocks in `digging-deeper.md`, the verbatim scripts in the references, the load-bearing mode logic quarantined in `mode-conversation-examples.md`. An auditor that reads only SKILL.md misses tests 5, 10, and 11 exactly where they bite. Also load what the tests need to be judgeable: the immediate upstream and downstream skills, the authority schema (`knowledge/vault-integration.md` for these skills), and the source canon. The canon is an INPUT to the audit (a path the invoker supplies; for the vid skills it is the Ed Lawrence material in business-os, a different repo, undiscoverable from the skill tree). No canon supplied: test 13 reports "not judgeable, canon not provided," never a silent pass. This matters because a finder and a skeptic without the source reason from the same wrong intuition and confirm each other; that is precisely how the tension collapse almost happened.

**1. Mechanical pre-pass (orchestrator, scripts and grep, no agents).** The deterministic checks run first, cheap and exact, over the whole skill directory (not just SKILL.md): em-dashes and banned words, description length, a `${CLAUDE_PLUGIN_ROOT}` or path that does not resolve, every referenced file both resolves AND is git tracked (a file that exists on disk but is untracked ships as a broken pointer; we almost pushed exactly that with `verify-subagent.md`), repeated headings, presence of the eval, character-limit slots. Spawning an agent to count characters is waste.

**2. Find (fan out by LENS, not by assertion).** A handful of agents, each taking a coherent group of tests, each reading the WHOLE skill. Atomizing to one-agent-per-rule loses the cross-cutting view (some tests need the whole file at once). The lenses:
- **Scope and references** (tests 1-3)
- **Loads and contract** (tests 4-8)
- **Flow and voice** (tests 9-11, interactive/creative skills only)
- **Description and style** (tests 12-15)

**3. Verify (one skeptic per candidate finding).** Each finding goes to an independent refuter, a different agent from the finder, whose job is to break it. False positives die. Severity gets re-graded honestly. This is the pass that kills the auditor's own noise.

**4. Sweep (one or two completeness critics).** Fresh agents through diverse lenses, whose only job is "what did everyone miss." This is the pass that catches what the find agents skimmed past.

**5. Verify criticals by hand (orchestrator, no agent).** Any finding graded critical gets checked against the actual files by the main loop. Never escalate a critical you have not confirmed yourself.

**6. Synthesize (orchestrator).** Dedup overlapping findings, group by severity (critical, then moderate, then minor), each with file:line evidence and the concrete outcome, plus the dismissed false positives listed openly.

**Scale the fleet to the skill.** A tiny or low-stakes skill does not need eight agents. A large or load-bearing one warrants the full pass plus extra sweep lenses.

## Agent structure at a glance

| Agent | Count | Purpose | Reads |
|---|---|---|---|
| Lens finder | ~4 | hunt one lens deep, whole-file | target + neighbors |
| Skeptic | 1 per finding | refute one claim, re-grade severity | target + the finding |
| Completeness critic | 1-2 | find what the finders missed | target + neighbors |
| Orchestrator (main loop) | 1 | mechanical pre-pass, verify criticals, synthesize | everything |

## The rubric (15 tests)

Each test: the check, a right example (a real good instance, never the absence of the wrong one), a wrong example, the default severity, and whether it is mechanical or judgment. Nine apply to every skill; tests 9-11 fire only on interactive or creative skills.

### Lens A: Scope and references

**1. One job = one output.** [judgment] The skill produces one artifact a single skill could own. Several internal steps are fine; several output artifacts are not.
- Right: vid-structure's four steps (mine, shape, order, plan blocks) produce one artifact, the outline.
- Wrong: a skill whose output is both the outline and the finished prose.
- Default: moderate (scope creep), critical if the two jobs actively fight.

**2. Cross-skill refs do work.** [judgment] Every mention of another skill is a redirect on a missing input or the handoff to the output consumer. No section that only catalogs relationships or narrates what other skills do.
- Right: the only mentions are "no brain-dump, run vid-intake" (prereq) and the script.md stubs naming vid-segment as the filler.
- Wrong: a "Related skills" section restating the prereqs as facts, or a scope line enumerating every sibling's job.
- Default: minor to moderate (bloat, rot risk).

**3. Modes are jobs, not inputs.** [judgment] Two-part check. First: does each branch run materially different steps? Identical flows differing by one skipped question are fake modes. Second, and this is the one that survives the first check: are the modes different JOBS, or different things someone can hand you? A list of input kinds (talked vs pasted, story vs client win) is not a list of jobs, even when each gets a distinctive move or two. One job plus a watch-list of gotchas beats a mode table. The middle version of vid-intake passed the first check (each mode had its distinctive moves inline) and was still wrong, because the seven modes were three questions jammed into one list.
- Right: "already outlined? refine the spine or rebuild it," a real fork in what the skill does, as a one-line conditional.
- Wrong: Standalone vs Sub-skill modes running the identical flow; or seven input-type modes each with a token distinctive move, dressed up as seven jobs.
- Default: moderate (fake structure).

### Lens B: Loads and contract

**4. Required context vs step context.** [judgment, partly mechanical] Required context (shapes two or more steps or the whole output) loads up front. Step context (used at one step) loads lazily and is named only at that step. The gate: can you name the one step it is used at? Then it is step context. A step-specific file in the always-load block is a misclassification.
- Right: the format planner loads at the shape step; the save schema loads up front.
- Wrong: all five banks loaded up front when each is used at one point; voice-profile loaded in a skill that writes no prose.
- Default: moderate (premature loading), critical if a required-context load silently fails (a wrong path that then gets claimed as loaded).

**5. The inline/reference split is right, both directions.** [judgment] Direction one: if the model never opens a reference, does the skill still run correctly? Core loop inline. Direction two: is there depth sitting inline that belongs in a reference? Re-teaching domain theory in SKILL.md is the same misclassification mirrored; old vid-structure re-taught tension theory at length that the shared reference already owned, and "drop the reteaching" was the creator's first complaint. Test 14 will not catch it (the theory is stated once), so this test owns it.
- Right: the mining tags live in SKILL.md, the worked example and the theory in the reference.
- Wrong: the per-mode behavior only in a "fallback" file the model never opens; or three paragraphs re-teaching setup/payoff theory inline when a one-line why plus a pointer does it.
- Default: moderate to critical for missing core loop (the skill silently does not do the thing); moderate for inline re-teaching (bloat, drift from the owning reference).

**6. No dead output.** [judgment, needs downstream] Every output field or section has a reader. Includes not pre-sorting what a later skill re-derives.
- Right: `segment_purposes` (the pipeline counts it), `tension_plan` (vid-segment reads it).
- Wrong: a "strongest raw lines" section nothing reads; intake pre-sorting piles vid-structure re-mines.
- Default: minor to moderate (dead weight, wasted work).

**7. No gap in the handoff.** [judgment, needs downstream] The output is complete enough that the next skill does not re-plan or re-interview.
- Right: vid-structure hands over picked blocks, so vid-segment just writes.
- Wrong: a half-outline that makes vid-segment re-pick and re-confirm every segment.
- Default: moderate (redundant downstream interview).

**8. Contract verified: skill vs schema, eval vs both.** [partly mechanical] Two layers. First, eval or no eval: the skill's declared output fields match the authority schema directly. Most vid skills have no eval yet, and the `captured` vs `created` drift lived in four places at once; the schema comparison cannot wait for an eval to exist. Second: an eval exists and passes; deterministic constraints (character limits, no fabricated numbers) get a MECHANICAL check, not model self-attestation; the eval's fields match the authority schema; for a conversational skill it drives a withholding simulator against a fresh judge.
- Right: output frontmatter matching `vault-integration.md` field for field; a Tier A `eval.py` checking char limits plus a Tier B rubric judge.
- Wrong: a skill writing `captured` while the schema says `created`; no eval; a "check" that is just the model counting its own characters; an eval asserting a field the skill renamed.
- Default: moderate for a skill/schema mismatch (contract drift). Missing eval: minor for a terminal creative skill, moderate for a conversational skill with no simulator, because our worst bugs (fabrication under withholding, the permission handshake) were only ever caught by simulation, never by reading.

### Lens C: Flow and voice (interactive/creative only)

**9. Machinery invisible.** [judgment] The user never sees internal scaffolding (step or phase numbers, mode names, slugs).
- Right: the user sees "here are the points," never "Phase 1.2 complete."
- Wrong: "Mode 1, idea dump. Sound right?"
- Default: minor to moderate (UX friction).

**10. Intent, not script (creative surface only).** [judgment] The check applies to the creative and interview surface: the questions that pull material, anything shaping the words the creator will speak. There, a verbatim script reads rigid and a dynamic line fit to what came up is better. It does NOT apply to process gates: a save confirmation, a "pick 1 or 2," a hard-rule kickback. A scripted gate is not a finding; do not report it. Before flagging any scripted line, name which surface it is; if you cannot show it shapes the creative output or an interview pull, it is a gate and it passes.
- Right: "in your own words, tell them to dump everything raw" (creative pull, intent form); a scripted "Intro locked, saved to script.md" (gate, fine as-is).
- Wrong: a fenced block of exact words for a voice-sensitive creative capture or an interview question set.
- Default: not-a-finding for a process gate; minor for mechanical info-gathering; moderate for a scripted creative or interview pull.

**11. No clocks.** [mechanical-ish] No time budgets on a creative conversation. Content ratios (payoff at 60-80% of the body) are fine; stopwatch counts on the back-and-forth are not.
- Right: "stop when the answers thin out."
- Wrong: "thirty seconds on the reflect-back."
- Default: minor to moderate (rushes the conversation, wrong stop signal).

### Lens D: Description and style

**12. Description triggers, when-to-use lives only there.** [partly mechanical] The description is what-it-does plus trigger phrases, no behavior specs, and all "when to use" lives ONLY in the description, not duplicated or diverging in a body section.
- Right: what it does plus eight varied trigger phrases, no "When to Activate" body section.
- Wrong: 135 words of behavior specs in the description; or a body "When to Activate" list that diverges from the description, adding triggers the router never sees.
- Default: moderate (triggering drift, bloat).

**13. Naming matches the canon.** [judgment, needs canon] The skill's terms match the source or domain canon; no invented label that fuses or corrupts a concept.
- Right: "setup and payoff" for the plan, "tension" only for the meter, as the source keeps them.
- Wrong: "tension architecture," fusing the meter and the mechanism.
- Default: minor to moderate (confusion, drift from source).

**14. Each idea stated once.** [judgment] No idea restated across multiple overlapping sections; no repeated rules blocks.
- Right: one "Rules (and why)" section, each idea once.
- Wrong: the no-fabrication rule stated four times across Core Principles, Content Guidelines, and Quality Checks; four overlapping rules sections.
- Default: minor to moderate (sync burden, drift risk).

**15. Workflow singular and consistent.** [judgment, partly mechanical] The authoritative description of each step exists once; the stated step or phase count matches the actual content; no summary contradicts its detail; the real procedure is not scattered across un-numbered peer sections.
- Right: three phases described once, in order, header says "three phases."
- Wrong: "## The 2 phases" over three phases; numbered steps stop at Step 2 while the real work lives in un-numbered peer H2 sections.
- Default: moderate (reader and model cannot follow the flow, skip risk).

## Calibration cases

- **Case 1, `social-media-bio-generator` (third-party).** The auditor's first real run. It correctly dismissed a hard-scripted intake as a false positive (test 10, mechanical gathering), downgraded three of the first-pass findings to minor, and the sweep found the one that mattered: a required-context load from the wrong path (`/context` instead of the plugin root's `context/core/`) that the skill then claims to the user it loaded, running blind (tests 4 and 8, critical). Proof that the verify pass kills noise and the sweep pass finds the real bug.
- **Acid test, vid-structure old vs new.** The old version should light up on cross-skill narration (2), unused loads (4), hidden modes (3), the phase-count drift (15), the inline re-teaching of tension theory (5), and the tension/setup-payoff naming fusion (13, canon supplied). The new version should come back clean. If the auditor cannot tell them apart, or catches only the first four, the rubric is not sharp enough and gets fixed before it is trusted on anything else.

## Stated limits (by design, not gaps)

- **Behavior-only bugs stay invisible.** The permission handshake, fabrication resistance under withholding, interrogation feel: white-box reading never caught those, simulation did. The auditor's whole answer to them is test 8 (a conversational skill without a simulator eval is a moderate finding). It never claims to have checked the behavior itself.
- **Readability is not tested here.** "Reads like a person talking" was the closing pass on every rewrite and no lens checks for spec-sheet prose. It belongs to the creative-output side of the house; if it gets a home, that home is `creative-skill-audit`, not this rubric. Until then it is a known blind spot, stated, not hidden.

## Open items before build

- Lock the four find lenses as the agent prompts (each lens gets the whole skill plus the neighbors plus its slice of the rubric).
- Decide where the skill lives and what invokes it (a workflow-backed skill, since the pipeline is inherently multi-agent).
- Wire the mechanical pre-pass to the existing `tests/lib` helpers where they already exist (em-dash, banned words, frontmatter, fabrication).
- Run the acid test and tune.
