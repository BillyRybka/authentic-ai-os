# Feedback capture map

The reproduction layer for the `aai-feedback` skill. When a creator reports a skill produced bad content, the report has to carry enough to RECREATE the problem, not just describe it. A description gets a sympathetic nod. A reproduction gets a fix. So when feedback fires, the skill looks the skill up here in Phase 1 and works the entry to assemble three captures: a replay case, a fixtures snapshot, and the bad output verbatim.

The bar comes from Billy's eval harness (the `tests/` tree in the source repo). That tree does not ship in the plugin, and this doc spells out the seed shape inline below, so nothing here depends on `tests/` at runtime. For reference: a seed in `tests/corpus/seeds.json` is a frozen, reproducible scenario, and a fixtures vault in `tests/fixtures/shared/` is the state a skill reads. A creator-simulator plays the persona (reveals what is in `reveals`, withholds what is in `withholds`, never invents) so the fabrication test stays honest. A real feedback report is the same thing rebuilt from an actual session: a seed reconstructed from how the creator really responded, plus the creator's real vault files in place of the shared Sam Rivera fixtures.

Read this alongside `references/feedback-submit.md` (the payload and submit contract) and `knowledge/vault-integration.md` (schema for the vault files you snapshot and for the local copy).

## How a reproduction entry reads

Each released skill has one tight entry. Every entry tells you how to fill the same three captures, and they map straight onto three payload fields.

- **reproductionCase.** A `seeds.json`-shaped JSON object rebuilt from the session. Goes in the `reproductionCase` textarea. The fields and how to fill them from a real run:
  - `slug`, `pillar`, `format`, `mode`, `audience_temp`: the run's actual identity. `mode` and `format` and `pillar` come from the skill's dials and the piece state. `audience_temp` is the viewer stage (cold / warm / hot) if the skill tracked one, else omit.
  - `is_adversarial`: true only if the creator was deliberately testing a trap (withholding a number to see if the skill invents it). Usually false.
  - `expected_problem`: the failure in one phrase (`fabricated-receipt`, `wrong-voice`, `off-iceberg-idea`, `broken-wikilink`).
  - `expected_iceberg_aligned`: for skills that run the iceberg fit gate, whether the output should have aligned. Omit for skills with no gate.
  - `seed`: the creator's raw dump text that started this run. What the seed IS differs per skill (see each entry). Verbatim, not summarized.
  - `persona {reveals, withholds, pillar_choice, slug_ok}`: reconstructed from how the creator actually responded. `reveals` is everything the creator told the skill in the conversation. `withholds` is what they were asked for and did not give (or deliberately held back). `pillar_choice` and `slug_ok` are their picks when the skill offered them.
  - `distinctive_phrases`: the creator's exact words that the output had to preserve or honor. Pulled from the conversation.
  - `bank_pulls_allowed`: the bank entries the skill actually pulled, or that the creator cited. By slug.
  - `fabrication_traps`: the numbers, claims, names, or links the creator withheld that the skill must not invent. Fill this when the failure is fabrication; leave empty otherwise.
- **fixturesSnapshot.** The FULL content of the determinative vault files the skill read this run. Goes in the `fixturesSnapshot` textarea. Each file under a `--- path ---` header, then its complete content. This is what makes a replay run against the creator's real state (their real foundation doc, their real voice profile, the specific bank entries cited) instead of the shared fixtures. Each entry below names exactly which files to bundle.
- **badOutputVerbatim.** The produced artifact that was bad, in full, exactly as the skill wrote or showed it. Goes in the `badOutputVerbatim` textarea. The break is almost always in the wording, so never trim or paraphrase.

Also tag `failureMode` (a short label for the kind of break) and `sessionMode` (which mode or dial the skill ran in) when either is obvious. The skill already fills the rest of the metadata: `severity`, `whatHappened`, `whatTheyWanted`, `skillName`, `pluginVersion`, `artifactsTouched`, `runtime`, `creatorName`, `creatorEmail`.

Three rules hold for every entry.

1. **Held-out content is never snapshotted.** Any file under `audience/held-out/` is a validation guardrail. Bundling it into `fixturesSnapshot` poisons validation the same way reading it during drafting would: a replay would train on the answers. Never put held-out content in a report, not even summarized as text. Capture counts only (how many quotes the set holds), and only when the count matters to the failure.
2. **Size.** For a genuinely huge bank (a full pattern-bank, a long aggregate file), do not snapshot the entire bank into `fixturesSnapshot`. Snapshot only the cited entries plus the file path. The replay needs the rows the skill actually pulled, not all of them, and the full file already sits on the creator's disk for Billy to open via `artifactsTouched`.
3. **Consent.** `fixturesSnapshot` ships the creator's real foundation and bank content, which is the most personal payload in the system. The Phase 5 preview must name exactly which files are going out (by path) and get a clear yes before any send. If the creator says drop one, drop it and send the rest. `reproductionCase` and `badOutputVerbatim` go in the same preview.

## Released skills (shipped in this plugin)

Released means the skill lives in `shared-skills/` AND is listed for this plugin in `.claude-plugin/plugins-map.json`. Both are required: a skill in `shared-skills/` that no plugin claims never ships. Only solicit or file feedback for a skill the creator actually has in this install. A skill still in `.claude/skills/` does not ship, so a creator on a release cannot have run it, and there is nothing to report. Keep this list matched to the map; when a skill graduates, move its entry up here.

### creator-setup
Scaffolding skill. No seed, no persona. Reproduce from the workspace state and the choices made.

- Reproduction note: capture the workspace STATE and the routing choices that reproduce the bad behavior, not a seed. Into `reproductionCase` as a plain JSON object with: `cwd_structure` (the candidate folders present and what was in each), `step_chosen` (2A flat vs 2B inspect), `target_path` (absolute path the creator picked), `manifest_rows` (count and structure-vs-seed breakdown), `people_override` (none vs the path recorded), `routing_block_appended` (yes/no), `existing_root_claude` (present before the run or not), `foundation_state` (which sections were present at handoff). This is enough to re-run the scaffold against the same starting shape.
- fixturesSnapshot: the CWD `CLAUDE.md` if one existed before the run (full), and whichever foundation files were present under `TARGET/foundation/` (`offer.md`, `avatar.md`, `iceberg.md`, `credibility.md`, `backstory.md`, or a legacy `creator-foundation.md`), each in full, to verify the state check. The starting state is the fixture here.
- badOutputVerbatim: the workspace `CLAUDE.md` as written, the root routing block as appended (check the `TARGET_PATH` substitution), the receipt text, the handoff offer text.

### foundation
Router skill. No seed, no persona. Reproduce from the locked-section state and the routing rule that fired.

- Reproduction note: capture the routing STATE, not a seed. Into `reproductionCase` as a plain JSON object with: `sections_locked` (which of Offer, Avatar, Top 3, Iceberg, Pillars, Credibility, Backstory read as present), `routing_rule_fired` (none-exists / avatar-done / positioning-done / pillars-done / credibility-done / backstory-done), `workspace_scaffolded` (both `foundation/` and `CLAUDE.md` present?), `stop_signal` (text matched, if any), `update_check_result` (newer version found?), `feedback_offer` (fired? creator response?). This reproduces which next-skill the router chose.
- fixturesSnapshot: the five foundation files in full (`foundation/offer.md`, `avatar.md`, `iceberg.md`, `credibility.md`, `backstory.md`), whichever exist; these are what the state check reads. Add the legacy `foundation/creator-foundation.md` if the migration flow fired this run. Add `CLAUDE.md` only if the bad behavior was a misfired scaffolding check.
- badOutputVerbatim: the "here's where you are" summary or the state / error message sent after the check, the sub-skill invocation result (triggered or errored), the feedback offer text if shown, the update notice if shown.

### vid-avatar
Locks the Offer into foundation/offer.md and the Avatar description plus Top 3 perceived problems into foundation/avatar.md.

- reproductionCase: `seed` is the creator's raw description of their viewer and offer from the interview. `persona.reveals` is what they told you about who the viewer is, what they sell, and the problems they named; `persona.withholds` is anything you asked for and they could not give. `mode` is fresh / resume / refresh. `pillar` omit (avatar is pre-pillar). `distinctive_phrases` is the creator's exact wording for the Offer, the Avatar, and each problem (the voice that should have been mirrored). `expected_problem` (e.g. `expert-framed-problems`, `structured-not-narrative`, `paraphrased-voice`). `bank_pulls_allowed` empty. `fabrication_traps` only if the skill invented an avatar detail the creator never said.
- fixturesSnapshot: `foundation/offer.md` and `foundation/avatar.md` (full, the in-progress docs) and `foundation/voice-profile.md` (full, if it exists). The avatar-guide reference is plugin material, not a fixture; cite it in `artifactsTouched` only if voice rules were the break.
- badOutputVerbatim: the full Offer paragraph as saved, the full Avatar description as saved, the full Top 3 problems list as saved (all three).

### vid-positioning
Drafts the Iceberg Statement (WHO + WHAT + HOW + TENSION) into foundation/iceberg.md.

- reproductionCase: `seed` is the creator's raw talk about their enemy, their angle, and what they refuse to do. `persona.reveals` is the WHO / WHAT / HOW / TENSION signals they gave and their reaction to the draft pair; `persona.withholds` is any component they never supplied. `mode` is fresh / refresh / replace, plus the tension type offered (named-enemy / refused-axis / specific-stakes). `distinctive_phrases` is the creator's literal enemy phrase and any term they paused on (these must be preserved verbatim, never paraphrased). `expected_problem` (e.g. `bland-statement`, `paraphrased-enemy`, `missing-component`). `bank_pulls_allowed` empty. `fabrication_traps` rarely applies.
- fixturesSnapshot: `foundation/offer.md` and `foundation/avatar.md` (full, since positioning reads the locked Offer / Avatar / Top 3 from them) and `foundation/voice-profile.md` (full, if it exists).
- badOutputVerbatim: the two candidate Iceberg Statements shown, the final locked statement if saved, and the paraphrased foundation sections from the absorb-first step.

### vid-pillars
Locks 8 to 12 content pillars (1 to 4 word labels) into foundation/iceberg.md.

- reproductionCase: `seed` is the creator's reactions to the starter pillar list (keep / drop / replace / add) plus any through-line they stated. `persona.reveals` is those reactions and the through-line; `persona.withholds` is rare here. `mode` is fresh / refresh-keep-replace, plus the count of pillars. `pillar` omit (this skill makes pillars). `distinctive_phrases` is the through-line text and any pillar wording the creator insisted on. `expected_problem` (e.g. `tactic-as-pillar`, `niche-repeated-back`, `marketing-language-label`). `expected_iceberg_aligned` is whether each locked pillar should pass the root-cause test against the Iceberg. `bank_pulls_allowed` empty.
- fixturesSnapshot: `foundation/iceberg.md` and `foundation/avatar.md` (full, the Iceberg / Avatar / Top 3 / Content pillars sections are all determinative) and `foundation/voice-profile.md` (full, if it exists).
- badOutputVerbatim: the final locked pillars list exactly as saved (the Content pillars section), and any marketing-language or multi-sentence label that should have been trimmed to 1 to 4 words.

### vid-credibility
Locks three brags (Big, Specific, Personal) into foundation/credibility.md, banks leftovers, creates people stubs.

- reproductionCase: `seed` is the creator's raw proof answers (personal result, client win, authority, volume, belief-breaker) as they landed. `persona.reveals` is every proof point given; `persona.withholds` is any number or client name they would not share. `mode` is fresh / refresh, plus MVP flag if a new creator. `distinctive_phrases` is the creator's wording for the brags. `expected_problem` (e.g. `anti-proof-framing`, `generic-credential`, `name-drop-not-result`, `irrelevant-to-avatar`). `bank_pulls_allowed` is any proof-bank entry the creator cited. `fabrication_traps` is the key one: any number, client name, or result the creator withheld that the skill must not invent into a brag.
- fixturesSnapshot: `foundation/avatar.md` and `foundation/iceberg.md` (full, for Avatar / Top 3 / Iceberg), plus the specific `banks/proof-bank/{slug}.md` entries cited or written this run (full, each under its own path header), plus any `people/{Full Name}.md` stub touched (full). Do not snapshot the whole proof-bank, only the cited entries.
- badOutputVerbatim: the three locked brags verbatim as they appear in foundation/credibility.md, any proof-bank entries created or updated (full, with frontmatter), any people stubs created or updated (full, with frontmatter and backlinks).

### vid-backstory
Locks the Problem-Action-Outcome backstory (full plus 3-sentence compressed) into foundation/backstory.md.

- reproductionCase: `seed` is the creator's four interview answers (Problem, trigger moment, Action list, Outcome). `persona.reveals` is those answers and their specificity; `persona.withholds` is any number or detail they could not recall (which the skill must omit, not invent). `mode` is fresh / refresh, plus own-story vs client-story attribution. `distinctive_phrases` is the creator's voice rhythms the draft had to keep. `expected_problem` (e.g. `summary-language-action`, `corporate-tone`, `vague-problem`, `fabricated-detail`). `bank_pulls_allowed` empty. `fabrication_traps` is any detail the creator said they could not recall (the skill must not fill the gap).
- fixturesSnapshot: `foundation/avatar.md` and `foundation/iceberg.md` (full, for Avatar and Iceberg), `foundation/voice-profile.md` (full, if it exists), and `people/{Full Name}.md` (full, if a client was named).
- badOutputVerbatim: the exact backstory draft shown before save (the blockquote), the creator's reworded version if they changed anything, and any draft the skill rejected internally if it is informative.

### vid-research
Builds or refreshes the pattern, title, and power-words banks plus packaging-system.md from YouTube research.

- reproductionCase: `seed` is the creator's research inputs: channel handle, the niche channels named, the adjacent channels named, the window, the floor adjustments, and the Keep/Drop/Modify calls during curation. `persona.reveals` is those inputs and curation decisions; `persona.withholds` is rare (this skill pulls from the API, not from withheld creator facts). `mode` is 1 first-build / 2 refresh / 3 single-add. `distinctive_phrases` is any wording the creator insisted patterns honor. `expected_problem` (e.g. `fabricated-outlier`, `adjacent-topic-leak`, `confidence-rank-stored`, `re-surfaced-dropped`). `bank_pulls_allowed` empty (research builds banks, it does not pull from them). `fabrication_traps` is critical: any outlier title or view count the skill must not invent (every receipt must trace to a real API pull).
- fixturesSnapshot: `foundation/iceberg.md` and `foundation/avatar.md` (full, for iceberg, audience, and niche match) and `foundation/voice-profile.md` (full, if it exists). For the banks, snapshot only the broken entries (the flagged patterns, the bad title templates) under their bank path headers, never the full bank. Snapshot `foundation/packaging-system.md` in full if the packaging defaults were the break.
- badOutputVerbatim: the specific wrong entries (flagged patterns, off title candidates, bad packaging defaults), any Keep/Drop/Modify exchange, the Phase 5 or 6 confirmation message. Point `artifactsTouched` at the full bank files.

### vid-pipeline
Router skill. No seed, no persona. Reproduce from the piece state and the routing decision.

- Reproduction note: into `reproductionCase` as a plain JSON object: `piece_slug`, `status` at entry, which piece.md fields read as present (title, thumbnail_text, segment_purposes, segments_completed vs purposes, intro_locked, ending_locked, pressure_test_status), `skill_invoked`, and the creator's ask verbatim. This reproduces which next skill the router chose.
- fixturesSnapshot: the routed piece's `piece.md` in full. Nothing else is determinative.
- badOutputVerbatim: the "where you are" message and the invocation result (right skill, wrong skill, or error).

### vid-braindump
Captures one video's raw material verbatim into brain-dump.md, creates piece.md.

- reproductionCase: `seed` is the creator's raw material as it arrived (talk, pasted notes, transcript), verbatim. `persona.reveals` is what surfaced across the capture passes; `persona.withholds` is gaps left open at close. `mode` is fresh / resume. `distinctive_phrases` is wording that had to survive into the file unpolished. `expected_problem` (e.g. `over-polished-voice`, `fabricated-content`, `lost-material`, `wrong-piece-resumed`). `fabrication_traps` is anything in the file that was not said.
- fixturesSnapshot: on resume, the prior `brain-dump.md` in full. Fresh runs have no determinative fixtures.
- badOutputVerbatim: the full `brain-dump.md` as saved and the `piece.md` frontmatter as created. The break is whether the creator's words survived.

### vid-framing
Locks frame, core_payoff, must_not_become, format, goal, voice_context, and The viewer section into piece.md.

- reproductionCase: `seed` is the brain dump the frame was built from plus the creator's interview answers. `persona.reveals` is their intent answers and reactions to the proposed frame; `persona.withholds` is any question they skipped. `distinctive_phrases` is their spoken frame wording (the frame must be first person and spoken, never a headline). `expected_problem` (e.g. `headline-not-spoken`, `invented-frame`, `wrong-format`, `reopened-locked-field`).
- fixturesSnapshot: `brain-dump.md` and `piece.md` (full), `foundation/avatar.md` (full), and any audience-language sources the creator supplied.
- badOutputVerbatim: every framing field as written plus the The viewer section.

### vid-title
Writes truthful title options against the locked frame, saves the pick to piece.md.

- reproductionCase: `seed` is the locked frame, core_payoff, and anchor from piece.md plus the creator's reactions per round. `persona.reveals` is their picks and pushes; `distinctive_phrases` is wording they insisted on. `expected_problem` (e.g. `payoff-leaked`, `frame-drift`, `claim-not-in-material`, `bland-finalists`). `bank_pulls_allowed` is the title/pattern/power-word rows cited. `fabrication_traps` is any claim or number not in the material.
- fixturesSnapshot: `piece.md` (full) and the specific bank rows cited, never the full banks.
- badOutputVerbatim: every candidate shown and the locked title as saved.

### vid-thumbnail
Presents ten thumbnail texts, locks three with measurement shapes into piece.md.

- reproductionCase: `seed` is the locked title plus the numbers, paradoxes, and named systems mined from the piece's own material. `persona.reveals` is the three picks and reactions; `expected_problem` (e.g. `restates-title`, `invented-number`, `payoff-leaked`, `fewer-than-ten-distinct`). `fabrication_traps` is any number or claim not present in the material verbatim.
- fixturesSnapshot: `piece.md` and `brain-dump.md` (or `script.md` when it exists), full, since the mined numbers must trace there.
- badOutputVerbatim: all ten options plus the three locked `thumbnail_text` and `thumbnail_shape` values as saved.

### vid-structure
Plans the writer-ready body: segment_purposes, tension_plan, script.md skeleton.

- reproductionCase: `seed` is the brain dump plus the locked package (title, thumbnail_text, format, goal). `persona.reveals` is gap answers and approval calls on the proposed skeleton; `persona.withholds` is critical gaps left unresolved. `expected_problem` (e.g. `early-payoff-plan`, `section-without-source`, `invented-material`, `re-structure-clobbered-completed-section`).
- fixturesSnapshot: `brain-dump.md` and `piece.md` in full. The format planner is plugin material, cite it in `artifactsTouched`.
- badOutputVerbatim: the proposed outline, the `script.md` skeleton as written, and `segment_purposes` plus `tension_plan` as saved.

### vid-intro
Writes the opening against the questions the locked title and thumbnail raised.

- reproductionCase: `seed` is the locked title, thumbnail_text, and the material the hook pulls from, plus the creator's confirmation of the Top 3 viewer questions. `persona.reveals` is their reactions per candidate round. `distinctive_phrases` is their voice the intro had to keep. `expected_problem` (e.g. `question-never-raised`, `credibility-misplaced`, `off-voice`, `payoff-leaked`).
- fixturesSnapshot: `piece.md`, `brain-dump.md`, `foundation/credibility.md`, `foundation/voice-profile.md`, and the matched `foundation/reference-pieces/` file, each full.
- badOutputVerbatim: the assembled intro plus the rejected candidates for the failed phase.

### vid-segment
Writes one body segment from its locked plan slot.

- reproductionCase: `seed` is the segment's plan slot (job, sources, takeaway from script.md) plus its material anchors. `persona.reveals` is approval and correction beats; `distinctive_phrases` is creator wording the prose had to carry. `expected_problem` (e.g. `claim-without-source`, `off-voice`, `closed-the-open-thread`, `payoff-early`). `bank_pulls_allowed` is entries pulled this segment. `fabrication_traps` is any claim not in the dump or a cited bank entry.
- fixturesSnapshot: `script.md`, `piece.md`, `foundation/voice-profile.md`, the matched reference-pieces file, and the pulled bank entries, each full.
- badOutputVerbatim: the full segment prose as written.

### vid-ending
Writes the Pivot/Gap/Bridge close, points at a real published video.

- reproductionCase: `seed` is the script body being closed plus the goal. `persona.reveals` is the next-video choice and reactions; `expected_problem` (e.g. `announced-the-ending`, `invented-next-video`, `wrong-goal-pivot`, `off-voice`). `fabrication_traps` is a `next_video` that does not exist as a published piece.
- fixturesSnapshot: `script.md`, `piece.md`, `foundation/voice-profile.md`, and cited bank entries, full.
- badOutputVerbatim: both draft candidates and the locked close plus `next_video` as saved.

### vid-pressure-test
Four adversarial reviewers plus the interactive fix loop and read-aloud gate.

- reproductionCase: `seed` is the assembled script plus the piece.md fields the reviewers read (format, goal, tension_plan, viewer_questions). `persona.reveals` is the approve/deny/skip calls per issue and the read-aloud rewords. `expected_problem` (e.g. `missed-fabrication`, `false-positive-voice-flag`, `early-payoff-not-caught`, `rewrite-broke-voice`).
- fixturesSnapshot: `script.md`, `brain-dump.md`, `piece.md`, `foundation/voice-profile.md`, and the bank entries the traceability reviewer checked, full.
- badOutputVerbatim: the findings lists, the rewrites the creator rejected with their reasoning, and the audit block written to piece.md.

### vid-bank
Captures stories, metaphors, proof, testimonials, and frameworks into the evergreen banks.

- reproductionCase: `seed` is the raw material as the creator dropped it. `persona.reveals` is answers to the capture walk; `persona.withholds` is details they could not give (which must stay absent). `expected_problem` (e.g. `duplicate-entry`, `invented-detail`, `wrong-bank`, `missing-person-stub`). `fabrication_traps` is anything in the entry the creator never said.
- fixturesSnapshot: `foundation/iceberg.md`, `foundation/avatar.md`, any dedup-candidate entries checked, and any `people/` stub touched, full.
- badOutputVerbatim: the saved bank entry in full with frontmatter, plus the session-close report.

### vid-voice-capture
Curates reference pieces plus the guardrail into the voice profile.

- reproductionCase: `seed` is the source passages the creator supplied (what they wrote or said). `persona.reveals` is curation picks and refusals stated; `expected_problem` (e.g. `synthetic-reference-piece`, `guardrail-missed-refusal`, `wrong-context-file`).
- fixturesSnapshot: the source materials supplied and, on refresh, the prior `foundation/voice-profile.md` and reference-pieces files, full.
- badOutputVerbatim: the reference-pieces files and voice-profile as written.

### vid-voice-audit
Reads a finished script against the reference pieces and guardrail, flags every line failing the read-aloud test.

- reproductionCase: `seed` is the script audited. `persona.reveals` is which flags the creator accepted vs rejected. `expected_problem` (e.g. `missed-off-voice-line`, `false-flag`, `rewrite-not-in-voice`, `guardrail-refusal-ignored`).
- fixturesSnapshot: `script.md`, `foundation/voice-profile.md`, and the matched reference-pieces file, full.
- badOutputVerbatim: the full findings list with per-beat verdicts (report only, no file write).

### vid-voice-update
Triages a mid-draft voice signal, appends permanent rules to the profile.

- reproductionCase: `seed` is the creator's exact trigger phrase, never paraphrased. `persona.reveals` is their answer when the skill asked which signal type it was. `expected_problem` (e.g. `one-time-saved-as-rule`, `rule-not-saved`, `wrong-signal-type`).
- fixturesSnapshot: `foundation/voice-profile.md` BEFORE the append, full.
- badOutputVerbatim: the profile after the append plus the signal type tagged (hard rule / one-time / preference shift).

### aai-feedback
The feedback channel itself. A creator rarely reports a problem with the feedback skill via the feedback skill, so it carries no special entry. Use the default principle below in the rare case it comes up.

## Staged skills (built in `.claude/skills/`, not yet shipped)

These live in `.claude/skills/` and are not listed in the map, so they do not ship to creators. A creator on a release cannot have run them. Entries here are pre-built so graduation is a copy, not a rewrite.

### vid-ideas
Surfaces 5 to 6 signal-backed video ideas, saves keepers to ideas-backlog.md, seeds vid-intake.

- reproductionCase: `seed` is the creator's stated focus (pillar / problem / all) and dial turns in sequence. `persona.reveals` is the focus, the dial turns, the pick, and the keep flags; `persona.withholds` is rare. `mode` is the dial posture at the bad batch (more / tighter / wilder / different-pillar / different-problem). `pillar` and the problem tag for the batch. `distinctive_phrases` is the creator's voice the idea lines should mirror. `expected_problem` (e.g. `fabricated-receipt`, `off-iceberg-surfaced`, `transcribed-not-adapted`, `re-proposed-dropped`). `expected_iceberg_aligned` is whether the surfaced ideas should have passed the 2-layer gate. `bank_pulls_allowed` is the pattern-bank entries (by pattern_id) the receipts cite. `fabrication_traps` is any outlier or view count not in the pattern-bank.
- fixturesSnapshot: `foundation/iceberg.md` and `foundation/avatar.md` (full, for Iceberg / Pillars / Avatar / Top 3), `content/ideas-backlog.md` (full, if it exists, to reproduce sticky drops and prior keepers), and the cited `banks/pattern-bank.md` rows. The pattern-bank can be large: snapshot the synthesis sections and the specific cited entries, not every per-outlier row, and point at the full file.
- badOutputVerbatim: the full surfaced batch (all idea lines with receipts), any fabricated or misquoted receipt, any off-voice idea line, the seed packet passed to vid-intake (all required fields), the ideas-backlog.md rows added, the anchors cited.

## Default principle (any unmapped skill)

If the skill that ran has no entry above, do not invent a fingerprint. Reconstruct best-effort along these lines.

1. **Identify the skill that ran, and confirm it shipped.** Name it from the session. If several ran, name the one that prompted the feedback plus the others as context. Fills `skillName`. If the skill is not part of this install (not listed for this plugin in the map), the creator never ran it, so do not file feedback for it.
2. **Reconstruct a reproductionCase from the session.** Build the best `seeds.json`-shaped object you can: the raw input that started the run as `seed`, the creator's real responses as `persona.reveals`, what they were asked for but did not give as `persona.withholds`, their exact load-bearing words as `distinctive_phrases`, the mode and format and pillar from the dials, and `fabrication_traps` if the break was an invented fact. Omit fields you genuinely cannot reconstruct rather than padding them.
3. **Snapshot the determinative files the skill touched.** The full content of the vault files the skill actually read this run, each under a `--- path ---` header, into `fixturesSnapshot`. Determinative means it shaped the output: the foundation doc, the voice profile, the specific bank entries cited. Never the whole vault.
4. **Capture the bad output whole.** The exact text the skill produced or showed that the creator called bad, verbatim and untrimmed, into `badOutputVerbatim`. For a huge artifact, capture the broken portion and point `artifactsTouched` at the file.

Never snapshot held-out content. The Phase 5 consent gate still applies, naming every file in the snapshot.

## WIP appendix (provisional, no full entries yet)

These ship later. If one runs and goes bad, use the default principle. One-line reproduction steers:

- **aud-avatar-build:** seed is the clustering interview answers; snapshot the cited `banks/audience-data/` call summaries and comment samples plus the avatar file produced; bad output is the avatar that displayed bad structure. Never snapshot the held-out file.
- **aud-intake:** seed is the raw call transcript or comment CSV reference; snapshot the generated call summary or vocabulary-sample files; bad output is the bad extraction plus the contamination report.
- **aud-review:** seed is the piece under review plus content type; snapshot the validated avatar files used and the piece; bad output is the full synthesis.md (verdict, top 3 fixes, dissent block, median table).
- **aud-validate:** seed is the draft avatar set; snapshot the avatar files and the validation report; bad output is the report plus the Billy-facing summary. Held-out sets are counts only, never snapshotted.
- **vid-format-plan:** (parked in 0.4.1, untested) seed is the video idea plus format choice and blank-by-blank answers; snapshot the plan file produced; bad output is the filled plan. Never writes piece.md or script.md.
- **post-write:** seed is the batch of raw ideas or the long-form source; snapshot iceberg.md, avatar.md, voice-profile.md, and the matched reference-pieces; bad output is the full post note and the batch summary.

> [!warning] When the aud-* skills graduate
> Held-out quote sets are validation guardrails. Putting one into `fixturesSnapshot` poisons validation the same way reading it during drafting would: the replay trains on the answers. When `aud-avatar-build`, `aud-validate`, and `aud-review` move to released, their full entries must repeat this rule in plain terms. Held-out content is summarized as counts only, never snapshotted, never quoted, period.

## Maintenance

This map is hand-derived from each skill's fingerprint and SKILL.md. When a released skill changes its `consumes`, `produces`, dials, session signals, or failure surface, regenerate that entry so the reproductionCase fields, the fixturesSnapshot file list, and the bad-output target stay matched to the current spec.

Three tiers, by where the skill lives:

- **Released**: in `shared-skills/` and listed in the map. Ships to creators. Feedback can be about these.
- **Staged**: in `.claude/skills/`. Full entries are ready but the skill does not ship yet. On graduation into `shared-skills/` plus a map entry, move it from Staged to Released.
- **WIP appendix**: in `.claude/skills-wip/`. One-line steers only; the default principle covers them if one runs in dev.

The Released list is the source of truth for which skills feedback can be about in a given release. Keep it matched to the map so the shipped plugin never invites feedback on a skill the creator does not have.
