# Feedback capture map

The reproduction layer for the `aai-feedback` skill. A report has to carry enough to RECREATE the bad run, not just describe it. A description gets a sympathetic nod. A reproduction gets a fix.

Phase 1 of the skill looks the skill up here and assembles three captures: a replay case, a fixtures snapshot, and the output verbatim.

Read alongside `references/feedback-submit.md` (payload and submit contract).

## Is this worth reporting?

Run this before anything else. Most session friction is not a bug, and filing it buries the signal that is.

**Report it.**

| Tag | What it means |
|---|---|
| `fabricated` | The skill invented a number, quote, client, link, or fact the creator never gave |
| `low-quality` | The output was weak or generic enough the creator would not use it |
| `messy` | The output was disorganized, or the creator could not tell what to do with it |
| `slow` | It took far more back and forth than the work deserved |
| `wrong-output` | The skill did something other than what it said it would do |
| `broke` | It errored, stopped cold, wrote to the wrong place, or lost work |
| `wrong-voice` | The output ignored a rule already sitting in `foundation/voice-profile.md`. A reword with no standing rule behind it routes to `vid-voice-update` instead |
| `worked-well` | Something landed. Capture the good artifact, not a compliment |

**Do not report it. Route it instead.**

- **A voice correction, one-off or standing.** "No, say it like this" is `vid-voice-update`'s job. It asks one-off vs permanent rule and writes the answer to the creator's voice profile. That fixes their vault. It is not a defect in the skill. Only tag `wrong-voice` and file when the skill ignored a rule already sitting in `foundation/voice-profile.md`.
- **A single preference tweak.** "Shorter", "use the other example", "swap that opener". Normal editing.
- **The creator changing their mind** about the video, the angle, or the material.

If the session had none of the reportable kinds, say so plainly and do not file an empty report.

## The three captures

- **reproductionCase.** A `seeds.json`-shaped JSON object rebuilt from the session. Fields:
  - `slug`, `pillar`, `format`, `mode`, `audience_temp`: the run's actual identity, from the piece state and the skill's dials. Omit any the skill does not track.
  - `is_adversarial`: true only if the creator was deliberately testing a trap. Usually false.
  - `expected_problem`: the failure in one phrase.
  - `expected_iceberg_aligned`: for skills with the iceberg fit gate. Omit otherwise.
  - `seed`: the raw input that started the run, verbatim, never summarized. What counts as the seed differs per skill, named in each entry below.
  - `persona {reveals, withholds, pillar_choice, slug_ok}`: rebuilt from how the creator actually responded. `reveals` is what they told the skill. `withholds` is what they were asked for and did not give.
  - `distinctive_phrases`: the creator's exact words the output had to preserve.
  - `bank_pulls_allowed`: the bank entries actually pulled or cited, by slug.
  - `fabrication_traps`: what the creator withheld that the skill must not invent. Fill on a `fabricated` tag, leave empty otherwise.
- **fixturesSnapshot.** The FULL content of the determinative vault files the skill read this run, each under a `--- path ---` header. Determinative means it shaped the output. This is what makes a replay run against the creator's real state instead of the shared fixtures.
- **badOutputVerbatim.** The produced artifact, in full, exactly as written or shown. The break is almost always in the wording, so never trim or paraphrase. On a `worked-well` report this field carries the GOOD artifact instead. Same field, and `severity: praise` plus `failureMode: worked-well` tells Billy which way it cuts. A praised output with its seed and its fixtures is a gold for the eval harness, which is the most useful thing a creator can send.

Also tag `failureMode` (from the table above) and `sessionMode` (which mode or dial the skill ran in).

## Three rules, every entry

1. **Held-out content is never snapshotted.** Anything under `audience/held-out/` is a validation guardrail. Bundling it poisons validation. Capture counts only, and only when the count matters.
2. **Size.** Never snapshot a whole bank. Snapshot the cited entries plus the file path, and point `artifactsTouched` at the full file.
3. **Consent.** `fixturesSnapshot` ships the creator's real foundation and bank content. The Phase 5 preview names every file going out by path and gets a clear yes. If they say drop one, drop it and send the rest.

## Defaults every entry inherits

Named here once so the entries stay short. Add these to what each entry names, unless the entry says otherwise.

- **Foundation slice.** Whichever of `foundation/iceberg.md`, `foundation/avatar.md`, `foundation/credibility.md`, `foundation/backstory.md`, `foundation/offer.md` the skill actually read this run. In full.
- **Voice.** `foundation/voice-profile.md` in full when it exists, plus the matched `foundation/reference-pieces/{voice_context}.md` for any skill that writes prose.
- **Piece state.** For any per-video skill, `content/pieces/{slug}/piece.md` in full. It carries every locked field the skill read.
- **artifactsTouched.** Every path the skill wrote or was about to write, comma separated.
- **Plugin material is not a fixture.** Knowledge files, format planners, and skill-local references ship with the plugin. Name them in `artifactsTouched` when they were the break. Never snapshot them.

## Setup and routing

### creator-setup
Scaffolds the workspace. No seed, no persona.

- **seed**: not applicable. Build `reproductionCase` as a plain object: `cwd_structure`, `step_chosen` (2A flat vs 2B inspect), `target_path`, `manifest_rows`, `people_override`, `routing_block_appended`, `existing_root_claude`, `foundation_state`.
- **fixtures**: the CWD `CLAUDE.md` if one existed before the run, and whichever foundation files were present under the target. The starting state is the fixture.
- **bad output**: the workspace `CLAUDE.md` as written, the root routing block as appended (check the `TARGET_PATH` substitution), the receipt, the handoff offer.

### foundation
Router for the five identity skills. No seed, no persona.

- **seed**: not applicable. Build `reproductionCase` as: `sections_locked`, `routing_rule_fired`, `workspace_scaffolded`, `stop_signal`, `update_check_result`, `feedback_offer`.
- **fixtures**: the five foundation files, whichever exist. Add `CLAUDE.md` only if a misfired scaffolding check was the break.
- **bad output**: the "here's where you are" summary, the sub-skill invocation result, the feedback offer text if shown.

### vid-pipeline
Thin orchestrator. Routes to the next skill for a piece. No seed, no persona.

- **seed**: not applicable. Build `reproductionCase` as: `slug`, `files_present` (which of brain-dump / piece / script existed), `piece_fields_read` (the locked fields it routed on), `skill_routed_to`, `expected_skill` (what should have fired).
- **fixtures**: `piece.md` in full and a file listing of `content/pieces/{slug}/`. The routing decision is a pure function of these.
- **bad output**: the routing message and the skill it invoked. If the wrong skill ran, that skill's output is context, and its own entry governs a separate report.

## Foundation identity

### vid-avatar
Locks the Offer into `offer.md` and the Avatar plus Top 3 into `avatar.md`.

- **seed**: the creator's raw description of their viewer and their offer.
- **fixtures**: `foundation/offer.md`, `foundation/avatar.md`.
- **bad output**: the full Offer paragraph, the full Avatar description, all three problems, as saved.
- **traps**: any avatar detail or offer claim the creator never said.

### vid-positioning
Drafts the Iceberg Statement into `iceberg.md`.

- **seed**: the creator's raw talk about their enemy, their angle, what they refuse to do.
- **fixtures**: `foundation/offer.md`, `foundation/avatar.md`.
- **bad output**: both candidate statements shown, the locked statement, and the paraphrased foundation sections from the absorb step.
- **note**: `distinctive_phrases` must carry the creator's literal enemy phrase. Paraphrasing it is the classic break.

### vid-pillars
Locks 8 to 12 pillars into `iceberg.md`.

- **seed**: the creator's keep / drop / replace / add reactions to the starter list, plus any through-line they stated.
- **fixtures**: `foundation/iceberg.md`, `foundation/avatar.md`.
- **bad output**: the locked pillars list exactly as saved, including any label over 4 words or written in marketing language.
- **note**: set `expected_iceberg_aligned` to whether each pillar should have passed the root-cause test.

### vid-credibility
Locks three brags into `credibility.md`, banks leftovers, creates people stubs.

- **seed**: the creator's raw proof answers as they landed.
- **fixtures**: `foundation/avatar.md`, `foundation/iceberg.md`, the specific `banks/proof-bank/{slug}.md` entries cited or written, any `people/{Full Name}.md` touched.
- **bad output**: the three brags verbatim, plus every proof-bank entry and people stub created or updated, in full with frontmatter.
- **traps**: this is the highest-risk fabrication skill. Any number, client name, or result the creator withheld.

### vid-backstory
Locks the Problem-Action-Outcome backstory into `backstory.md`.

- **seed**: the creator's four interview answers (Problem, trigger moment, Action list, Outcome).
- **fixtures**: `foundation/avatar.md`, `foundation/iceberg.md`, any `people/{Full Name}.md` if a client was named.
- **bad output**: the draft shown before save, the creator's reworded version if they changed anything.
- **traps**: any detail the creator said they could not recall. The skill must leave the gap, not fill it.

## Voice

### vid-voice-capture
Writes `reference-pieces/` (verbatim passages) and `voice-profile.md` (thin guardrail).

- **seed**: the creator's source passages, verbatim, plus which sources they pointed at.
- **fixtures**: the source material under `raw/voice-sources/` that was actually read, and the existing `foundation/voice-profile.md` on a refresh.
- **bad output**: every `foundation/reference-pieces/{voice_context}.md` written and `foundation/voice-profile.md` after the run, in full.
- **note**: the classic break is a reference piece that got cleaned up instead of copied. Snapshot the source next to the output so the diff is visible.

### vid-voice-audit
Returns a findings list against a script. Writes no file.

- **seed**: the script audited, in full.
- **fixtures**: `content/pieces/{slug}/script.md`, `foundation/voice-profile.md`, and the matched `reference-pieces/`.
- **bad output**: the full findings list (severity, location, quote, suggested rewrite) and the per-beat verdict map.
- **note**: report a miss (a line the creator would reword that passed) as much as a false flag.

### vid-voice-update
Appends a permanent rule to `voice-profile.md`, or rewrites one line and saves nothing.

- **seed**: the creator's exact trigger phrase, never paraphrased, plus the flagged line it was about.
- **fixtures**: `foundation/voice-profile.md` before the append.
- **bad output**: `foundation/voice-profile.md` after the append, plus the signal type it tagged (permanent rule vs one-time edit).
- **note**: the break worth reporting is misclassification. A one-off saved as a standing rule poisons every future draft, and a standing rule dropped as a one-off means the creator has to say it again.

## Research and banks

### vid-research
Builds the pattern, title, and power-words banks plus `packaging-system.md`.

- **seed**: the creator's research inputs: channel handle, the niche and adjacent channels named, the window, the floor adjustments, and every Keep / Drop / Modify call.
- **fixtures**: `foundation/iceberg.md`, `foundation/avatar.md`. For the banks, only the broken entries under their bank path headers, never the full bank. Add `foundation/packaging-system.md` in full if packaging defaults were the break.
- **bad output**: the specific wrong entries, any Keep / Drop / Modify exchange, the confirmation message.
- **traps**: critical here. Every outlier title and view count must trace to a real API pull. An invented receipt is the worst failure this skill has.

### vid-bank
Saves a story, metaphor, proof, testimonial, or framework to the evergreen banks.

- **seed**: the raw material as the creator gave it, verbatim.
- **fixtures**: `foundation/iceberg.md`, `foundation/avatar.md`, plus any existing bank entries the dedup check surfaced as candidates.
- **bad output**: the saved bank entry in full with frontmatter, any `people/{Full Name}.md` stub created with its backlink, and the session-close report.
- **traps**: any detail added that was not in what the creator said.

## Per video

### vid-braindump
Captures raw material into `brain-dump.md` in the creator's exact words, then probes the holes.

- **seed**: the creator's full dump (conversation, pasted outline, transcript, or story). This IS the seed.
- **fixtures**: `foundation/iceberg.md` (the fit check), plus any bank entries the dump wikilinks to, to reproduce link resolution.
- **bad output**: `content/pieces/{slug}/brain-dump.md` in full and `piece.md` frontmatter in full.
- **note**: the product is the creator's words surviving intact. The break is almost always tidying, summarizing, or a sentence of the skill's own prose landing in the file. Capture it whole and consent-gate it.
- **traps**: anything in the dump file that was not in what the creator said.

### vid-framing
Locks one frame, core payoff, format, goal, and the `## The Read` section.

- **seed**: `brain-dump.md` in full plus the creator's reactions to the framing options and their pick.
- **fixtures**: `brain-dump.md`, the foundation slice read, `foundation/voice-profile.md` (the refusals list is determinative here).
- **bad output**: the full batch of framing options as shown, the recommendation, the `## The Read` body written, and the dropped-angles section.
- **note**: `expected_iceberg_aligned` applies. A frame that drifts off the iceberg is the failure to catch.

### vid-title
Writes and recommends title options against the locked frame.

- **seed**: the creator's reactions to the title batch (keep / kill / reword) and any title they wrote themselves.
- **fixtures**: `brain-dump.md`, the foundation slice, plus the CITED rows from `banks/title-bank.md`, `banks/power-words-bank.md`, and the cited outlier notes. Never the whole bank.
- **bad output**: the full batch as shown, the recommendation, and the title saved to `piece.md`.
- **traps**: any number or claim in a title that the brain dump does not contain verbatim.

### vid-thumbnail
Presents ten thumbnail-text options, locks three.

- **seed**: the locked title and the creator's picks and rejections from the ten.
- **fixtures**: `script.md` if complete else `brain-dump.md`, plus `foundation/packaging-system.md` and any `banks/packaging-bank/` entries cited.
- **bad output**: all ten options as shown and the locked `thumbnail_text` picks written to `piece.md`.
- **traps**: any number or claim not stated verbatim in the script or dump.

### vid-structure
Co-plans the body into a `script.md` skeleton.

- **seed**: `brain-dump.md` plus the locked frame, and the creator's calls during the outline pass.
- **fixtures**: `brain-dump.md`, plus the cited entries from any evidence bank the outline pulled from.
- **bad output**: the full outline proposal as shown and the `script.md` skeleton with its `## To build` list.
- **note**: name the format planner in `artifactsTouched` when the break was planner-shaped. It ships with the plugin, so do not snapshot it.

### vid-intro
Writes `## Intro`.

- **seed**: the locked title and thumbnail (the questions the intro has to answer) plus the creator's reactions to the drafts.
- **fixtures**: `brain-dump.md`, `script.md` as it stood before the write, the foundation slice, `foundation/voice-profile.md`, the matched `reference-pieces/`, plus the cited entries from `banks/hook-bank.md` and any proof, story, or metaphor bank the credibility weave pulled.
- **bad output**: `## Intro` in full as written, plus every rejected draft the creator saw.
- **traps**: any proof or number woven in that is not in the dump or a cited bank entry.

### vid-segment
Writes one body section.

- **seed**: the section's line from the `## To build` list plus the source material in the dump for that point.
- **fixtures**: `brain-dump.md`, `script.md` (the outline plus the sections already written, since the segment has to follow them), the foundation slice, `foundation/voice-profile.md`, the matched `reference-pieces/`, the cited rows from `banks/transition-bank.md` and the evidence banks.
- **bad output**: the section as written in full, plus its transition in and out.
- **note**: set `sessionMode` to which segment number this was. A break that only shows up on segment 4 is a different bug than one on segment 1.

### vid-ending
Writes `## Ending` with Pivot/Gap/Bridge.

- **seed**: the full assembled body plus the `## Intro` verbatim (the ending has to close what the intro opened) and the published video the bridge points at.
- **fixtures**: `script.md` in full, the foundation slice, `foundation/voice-profile.md`, the matched `reference-pieces/`, cited `banks/transition-bank.md` rows.
- **bad output**: `## Ending` in full.
- **traps**: the bridge must point at a real published video the creator named. A recommended video that does not exist is a fabrication.

### vid-pressure-test
Runs four adversarial reviewers against the assembled script.

- **seed**: the assembled `script.md` in full plus the creator's accept / reject calls on each issue raised.
- **fixtures**: `script.md`, `brain-dump.md` (claim traceability is the whole point), the foundation slice, `foundation/voice-profile.md`.
- **bad output**: the issues each of the four reviewers returned, the rejected rewrites with the creator's reasoning, the read-aloud exchange, and the audit block written to `piece.md`.
- **note**: a miss matters more than a false flag here. If the script shipped with a problem all four reviewers passed, that is the report.

## aai-feedback

The feedback channel itself. A creator rarely reports a problem with the feedback skill through the feedback skill. Use the default principle below in the rare case it comes up.

## Default principle (any unmapped skill)

If the skill has no entry above, do not invent a fingerprint. Reconstruct best effort.

1. **Name the skill and confirm it ships.** If it is not listed for this plugin in the map, the creator never ran it, so do not file for it.
2. **Rebuild a reproductionCase.** The raw input as `seed`, the creator's real responses as `persona.reveals`, what they were asked for and did not give as `persona.withholds`, their load-bearing words as `distinctive_phrases`, the dials as mode / format / pillar, and `fabrication_traps` if the break was an invented fact. Omit what you cannot reconstruct rather than padding it.
3. **Snapshot only the determinative files.** The vault files that shaped the output, in full, each under a `--- path ---` header. Never the whole vault.
4. **Capture the output whole.** Verbatim and untrimmed. For a huge artifact, capture the broken portion and point `artifactsTouched` at the file.

Never snapshot held-out content. The Phase 5 consent gate still applies, naming every file in the snapshot.
