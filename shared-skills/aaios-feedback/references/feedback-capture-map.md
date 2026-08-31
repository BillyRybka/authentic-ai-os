# Feedback capture map

The reproduction layer for the `aaios-feedback` skill. When a creator reports a skill produced bad content, the report has to carry enough to RECREATE the problem, not just describe it. A description gets a sympathetic nod. A reproduction gets a fix. So when feedback fires, the skill looks the skill up here in Phase 1 and works the entry to assemble three captures: a replay case, a fixtures snapshot, and the bad output verbatim.

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

### aaios-feedback
The feedback channel itself. A creator rarely reports a problem with the feedback skill via the feedback skill, so it carries no special entry. Use the default principle below in the rare case it comes up.

## Staged skills (built in `.claude/skills/`, not yet shipped)

These three have full reproduction entries ready, but they live in `.claude/skills/` and are not listed in the map, so they do not ship to creators. A creator on a release cannot have run them. They move up to Released the moment they graduate into `shared-skills/` and get listed. Until then only Billy's dev environment runs them, and the entries below are pre-built so the move is a copy, not a rewrite.

### vid-research
Builds or refreshes the pattern, title, and power-words banks plus packaging-system.md from YouTube research.

- reproductionCase: `seed` is the creator's research inputs: channel handle, the niche channels named, the adjacent channels named, the window, the floor adjustments, and the Keep/Drop/Modify calls during curation. `persona.reveals` is those inputs and curation decisions; `persona.withholds` is rare (this skill pulls from the API, not from withheld creator facts). `mode` is 1 first-build / 2 refresh / 3 single-add. `distinctive_phrases` is any wording the creator insisted patterns honor. `expected_problem` (e.g. `fabricated-outlier`, `adjacent-topic-leak`, `confidence-rank-stored`, `re-surfaced-dropped`). `bank_pulls_allowed` empty (research builds banks, it does not pull from them). `fabrication_traps` is critical: any outlier title or view count the skill must not invent (every receipt must trace to a real API pull).
- fixturesSnapshot: `foundation/iceberg.md` and `foundation/avatar.md` (full, for iceberg, audience, and niche match) and `foundation/voice-profile.md` (full, if it exists). For the banks, snapshot only the broken entries (the flagged patterns, the bad title templates) under their bank path headers, never the full bank. Snapshot `foundation/packaging-system.md` in full if the packaging defaults were the break.
- badOutputVerbatim: the specific wrong entries (flagged patterns, off title candidates, bad packaging defaults), any Keep/Drop/Modify exchange, the Phase 5 or 6 confirmation message. Point `artifactsTouched` at the full bank files.

### vid-ideas
Surfaces 5 to 6 signal-backed video ideas, saves keepers to ideas-backlog.md, seeds vid-intake.

- reproductionCase: `seed` is the creator's stated focus (pillar / problem / all) and dial turns in sequence. `persona.reveals` is the focus, the dial turns, the pick, and the keep flags; `persona.withholds` is rare. `mode` is the dial posture at the bad batch (more / tighter / wilder / different-pillar / different-problem). `pillar` and the problem tag for the batch. `distinctive_phrases` is the creator's voice the idea lines should mirror. `expected_problem` (e.g. `fabricated-receipt`, `off-iceberg-surfaced`, `transcribed-not-adapted`, `re-proposed-dropped`). `expected_iceberg_aligned` is whether the surfaced ideas should have passed the 2-layer gate. `bank_pulls_allowed` is the pattern-bank entries (by pattern_id) the receipts cite. `fabrication_traps` is any outlier or view count not in the pattern-bank.
- fixturesSnapshot: `foundation/iceberg.md` and `foundation/avatar.md` (full, for Iceberg / Pillars / Avatar / Top 3), `content/ideas-backlog.md` (full, if it exists, to reproduce sticky drops and prior keepers), and the cited `banks/pattern-bank.md` rows. The pattern-bank can be large: snapshot the synthesis sections and the specific cited entries, not every per-outlier row, and point at the full file.
- badOutputVerbatim: the full surfaced batch (all idea lines with receipts), any fabricated or misquoted receipt, any off-voice idea line, the seed packet passed to vid-intake (all required fields), the ideas-backlog.md rows added, the anchors cited.

### vid-intake
Captures raw material into brain-dump.md for one video, locks iceberg fit.

- reproductionCase: `seed` is the creator's full brain dump (the conversational dump, pasted outline, transcript, or story). This IS the seed for this skill. `persona.reveals` is the dump plus their answers to drilling and alignment; `persona.withholds` is any detail they marked as a TODO or could not give. `mode` is which of the 7 intake modes was detected. `pillar` from the Phase 6 selection. `audience_temp` if captured. `distinctive_phrases` is the creator's exact phrasing that the brain dump had to preserve verbatim. `expected_problem` (e.g. `over-polished-voice`, `mode-misdetect`, `fabricated-content`, `broken-wikilink`). `expected_iceberg_aligned` is the fit outcome (true if the idea fits the iceberg, false if it does not). `bank_pulls_allowed` is any story / proof / metaphor entry the creator pulled in. `fabrication_traps` is anything added that was not in the dump.
- fixturesSnapshot: `foundation/avatar.md` and `foundation/iceberg.md` (full, for Top 3 and iceberg), `foundation/voice-profile.md` (full, if it exists), and any cited bank entries the dump wikilinks to (full, under their path headers, to reproduce link resolution).
- badOutputVerbatim: the full brain-dump.md as saved and the full piece.md frontmatter as saved. The brain dump is the creator's voice verbatim, so the break is whether their words survived. Capture it whole, then consent-gate it.

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
- **vid-voice-audit:** seed is the script audited; snapshot script.md, voice-profile.md, and the matched reference-pieces; bad output is the full findings list and verdict map (report only, no file).
- **vid-voice-update:** seed is the creator's exact trigger phrase (never paraphrased); snapshot voice-profile.md before the append; bad output is voice-profile.md after the append, plus the signal type tagged (hard rule / one-time / preference shift).
- **vid-bank:** seed is the raw story / metaphor / proof / testimonial / framework; snapshot iceberg.md, avatar.md, and any dedup-candidate entries; bad output is the saved bank entry in full plus the session-close report.
- **vid-voice-capture:** seed is the creator's source passages; snapshot the source materials and the existing voice-profile on refresh; bad output is the reference-pieces and voice-profile written.
- **vid-pressure-test:** seed is the assembled script plus piece.md fields; snapshot script.md, brain-dump.md, voice-profile.md, and cited banks; bad output is the rejected rewrites with the creator's reasoning, the read-aloud exchange, and the piece.md audit block.
- **vid-thumbnail:** seed is the locked title and script numbers; snapshot piece.md, script.md, and packaging-system.md; bad output is the candidate list plus the locked `thumbnail_text` picks written to piece.md. Fabrication trap: any number or claim not stated in the script verbatim.
- **vid-structure:** seed is the brain-dump plus locked angle; snapshot brain-dump.md, piece.md, the foundation slice files the run read, and the format planner; bad output is the full outline proposal and the script.md skeleton.
- **vid-intro:** seed is the brain-dump material plus locked title and thumbnail_text; snapshot piece.md, brain-dump.md, voice-profile.md, and the matched reference-pieces; bad output is the assembled intro plus the rejected candidate list for the failed phase.
- **vid-ending:** seed is the script body it closes; snapshot script.md, piece.md, voice-profile.md, the format planner, and cited banks; bad output is both draft candidates and the locked close.
- **vid-segment:** seed is the segment's outline slot plus its material anchors; snapshot script.md, piece.md, voice-profile.md, and the bank entries pulled; bad output is the full segment prose. Fabrication trap: any claim not in the brain-dump or a cited bank. (Provisional: derived from the pipeline pattern, no fingerprint yet.)
- **vid-framing:** seed is the creator's reaction to the angle candidates; snapshot piece.md, avatar.md, iceberg.md, and cited pattern-bank rows; bad output is all angle candidates and the piece.md framing fields appended.
- **vid-title:** seed is the locked hook and payoff; snapshot piece.md, script.md, and packaging-system.md; bad output is all 5 to 10 candidates and the locked title.
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
