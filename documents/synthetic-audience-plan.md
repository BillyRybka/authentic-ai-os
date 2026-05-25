---
type: plan
doc: synthetic-audience-plan
project: authentic-ai-os
status: active
last_refreshed: 2026-05-25
tags: [plan, audience, synthetic, aud]
---

# Synthetic Audience Subsystem Plan

The `aud-*` skill family. Pre-publish copy review using synthetic avatars built from a creator's real call transcripts and YouTube comments. Independent subsystem inside Authentic AI OS. Reads from the vault, integrates with `Content/pieces/` artifacts produced by the vid-* pipeline, but otherwise stands alone.

## 1. Purpose

The creator needs to know whether a script, email, title+thumbnail, hook, or CTA will land with the actual people who watch the channel, before publishing. The current alternatives are bad. Ship and pray, ask one friend, or skip the test and rely on instinct. All three fail predictably.

This subsystem builds 4 to 6 synthetic avatars from real audience material, validates each against held-out quotes, then runs them as a parallel panel on a draft piece. The output is a verdict, three actionable fixes, median scores, and verbatim dissent. The creator reads the first screen and decides.

The system surfaces what the creator missed. It does not predict performance.

## 2. Source grounding

The mechanism comes from Columbia Business School's Digital Twins Lab. Two papers anchor the design.

| Source | What it provides | Files referencing it |
|---|---|---|
| Toubia, Gui, Peng, Merlau, Li, Chen (2025). *Twin-2K-500.* Marketing Science. | The validated approach: narrative synthesis of survey answers, held-out validation against the same human's later responses, 88% of test-retest ceiling. | `knowledge/synthetic-audience-method.md` |
| Hewitt et al. (2025). *Digital Twins are Funhouse Mirrors.* arxiv 2509.19088. | The five distortions to guard against: majority overweighting, exaggerated agreement, demographic stereotyping, position bias, sycophancy. | `knowledge/synthetic-audience-method.md` |
| Justin Book / Crowd Copy demo (Greg Eisenberg event, January 2026, Mind Studio). Rebuilt on Claude Code by the creator in soptxNjjBVI for a 159K-sub guitar YouTuber. | Practitioner shape: panel review, scoring matrix, copywriter rewrite loop. | Design influence only, no skill loads it. |

**Critical correction to the popular framing.** The "88% accuracy" line in the video is sloppy. The number is 88% of the test-retest reliability ceiling on humans re-answering their own questions 2 weeks later. That ceiling is 0.7-0.8. Absolute accuracy on well-built twins lands closer to 0.6-0.7, and that's with 2.4 hours of dense survey data per person across 2,058 humans. At MVP scale (one creator's calls + comments) we are below this. The system says so out loud in every synthesis.

## 3. The 4 MVP skills

Status legend: ✅ built · 🟡 deferred to Phase 2 · ⬜ not started

| Skill | Status | Owns | Files |
|---|---|---|---|
| `aud-intake` | ✅ | Ingests call transcripts + YouTube comments. Extracts the 5 moment types from calls (I-am, I-tried, I-fear, I-want, I-pushed-back). Runs the contamination scan. Outputs per-call summaries and vocabulary-sample entries. Caps: 5 calls + 100 comments per run. | `.claude/skills/aud-intake/SKILL.md` |
| `aud-avatar-build` | ✅ | Clusters audience-data into 4-6 segments via a bounded interview (max 3 questions per session, 5 quotes per question). Writes held-out files to disk BEFORE drafting avatars. Drafts 4-section avatar profiles (Identity, Top Problems, Top Objections, Vocabulary Bank). | `.claude/skills/aud-avatar-build/SKILL.md` |
| `aud-validate` | ✅ | Three-test gate per avatar. Test 1 (quote attribution, >=7/10), test 2 (objection prediction, >=2/3 substance), test 3 (vocabulary leak, <=15% novel). Tiered outcome: `validated-vocabulary` or `validated-full`. Only consumer of `audience/held-out/`. | `.claude/skills/aud-validate/SKILL.md` |
| `aud-review` | ✅ | Runs validated avatars as a panel against a piece. Each avatar reviews via subagent in randomized order, response written to disk before next subagent runs. Synthesis computed from files on disk: verdict, top 3 fixes, median scores, verbatim dissent. Per-content-type question sets (script, email, title+thumbnail, hook, CTA). | `.claude/skills/aud-review/SKILL.md` |

**Decisions locked during the build:**

- **No orchestrator.** A 5th skill (`aud-foundation`) was cut after UX review. Linear dependencies are encoded in each skill's pre-check. Saves one layer of indirection.
- **Calls and comments are different evidence types.** Calls produce full `audience-data` entries. Comments produce `vocabulary-sample` entries that may ONLY be cited in an avatar's Vocabulary Bank section, never in Identity, Problems, or Objections. Structural guardrail in `aud-avatar-build`.
- **4-6 avatars, not 8-12.** The video's number assumes survey-depth data. Calls + comments at MVP scale supports fewer, deeper avatars.
- **Held-out separation lives on disk.** `audience/held-out/{segment}.md` is written before any avatar prose exists. Avatar drafting is forbidden from reading the folder. Working-memory promises don't survive context boundaries.
- **Subagent isolation per avatar.** Real isolation by spawning a subagent per avatar review with only that avatar's profile + the piece. Cross-avatar contamination minimized, not eliminated.
- **Median + dissent, never mean.** Outliers carry information. A single skeptic should not get averaged out.
- **Banned vocabulary list.** Statistical jargon never appears in creator-facing output. Translated to plain English.

## 4. Knowledge layer

Two files. Both load-bearing.

| File | What it encodes | Loaded by |
|---|---|---|
| `knowledge/synthetic-audience-method.md` | Research grounding, contamination checklist (8 tells + 4 worked examples), 5 moment types, held-out protocol, novel-word definition, validation thresholds, scoring dimensions, trigger rules, rotating disclaimer variants, calibration check, banned vocabulary. | All 4 aud-* skills load at session start. |
| `knowledge/common-english.txt` | ~1,000 most-common English words. Filter for test 3 (vocabulary leak). Grows over time as needed. | `aud-validate` only. |

`knowledge/vault-integration.md` is updated with 7 new frontmatter schemas (audience-data, vocabulary-sample, audience-segment, avatar, held-out, avatar-validation, avatar-review, panel-synthesis). The contract file remains the single source of truth for schema across the whole vault.

## 5. Data flow

```
inbox/audience/
  calls/{anything}.txt           Raw drop-in. Billy puts files here.
  comments/{video-slug}.csv      Raw drop-in.
        ↓
   aud-intake
        ↓                        Processes one call at a time. Batches comments.
banks/audience-data/             Contamination scan, batched table on completion.
  calls/{call-slug}.md           Per-call summary with 5 moment-type quote units.
  comments/{video}/{id}.md       Vocabulary samples. Low-trust evidence.
        ↓
   aud-avatar-build              Bounded interview. 3 questions max per session.
        ↓                        State saved to audience/state.md for resumption.
audience/
  segments/{segment-slug}.md     Named by creator, NOT by Claude.
  held-out/{segment-slug}.md     Written BEFORE avatar drafts exist.
  avatars/{avatar-slug}.md       4-section profile. status: draft.
        ↓
   aud-validate                  Three tests. Only consumer of held-out/.
        ↓                        Avatar frontmatter flips to validated-*.
audience/avatars/
  {slug}-validation-{date}.md    Billy-readable. No statistics jargon.
        ↓                        Avatars with status validated-* are usable.
   aud-review                    Subagent per avatar, randomized, isolated.
        ↓                        Each response written to file before next runs.
Content/pieces/{piece-slug}/reviews/{N}/
  {avatar-slug}.md               Per-avatar response. iteration N.
  synthesis.md                   Verdict + 3 fixes + median + dissent + links.
```

## 6. Phase 2 skills (deferred, not built)

Listed so future-me knows what was considered and intentionally deferred. Each gets its own plan when MVP usage exposes the need.

| Skill | What it would own | Triggered by |
|---|---|---|
| `aud-cluster` | Segmentation as a dedicated skill. Currently folded into `aud-avatar-build` Phase 1. Split out when audience-data variety grows enough that clustering deserves its own interview. | Bank > 20 calls or 3+ distinct source types. |
| `aud-panel-config` | Per-content-type avatar selection rules. Which avatars review thumbnails vs CTAs vs scripts. Currently hardcoded in `aud-review`. Split out when the creator wants explicit panel composition control. | Creator requests differentiated panels. |
| `aud-synthesize` | Scoring and consensus split out of `aud-review`. Currently folded into Phase 2 of that skill. Split out when scoring logic grows past ~150 lines or when the creator wants synthesis without re-running reviews. | Synthesis logic complexity outgrows aud-review. |
| `aud-feedback-loop` | Post-publish ingestion of real metrics (CTR, retention, conversion, comments). Per-avatar calibration scoring over 10+ pieces. Drift detection. Auto-retires avatars trending below 0.5 calibration. | Hooks into vid-measurement when that skill ships. Independent until then. |
| `aud-survey-design` | When the creator wants to collect first-party survey data. Designs the survey, writes it to a form tool, processes the responses into audience-data entries. | Creator decides to add surveys as a data source. |

## 7. Integration with the vid-* pipeline

The two subsystems are intentionally independent. The integration surface is a single file path.

`aud-review` reads `Content/pieces/{piece-slug}/{file}.md` artifacts produced by the vid-* writing pipeline (`vid-intake`, `vid-structure`, `vid-segment`, `vid-intro`, `vid-ending`, `vid-title`, `vid-thumbnail`). It writes its outputs into `Content/pieces/{piece-slug}/reviews/{N}/`, alongside but never inside the piece artifacts the vid-* skills wrote.

No vid-* skill reads anything from the aud-* subsystem. No vid-* skill changes when aud-* changes. The audience pipeline can be installed, run, retired, or rebuilt without touching the writing pipeline.

If `aud-feedback-loop` ships in Phase 2, it will hook into the future `vid-measurement` skill. That's the only planned cross-pipeline coupling.

## 8. Verification path

End-to-end test, run once after MVP build, re-run when any skill changes.

1. Drop 3 sample call transcripts + 50 sample comments in `inbox/audience/`. Run `aud-intake`. Verify per-call summaries land in `banks/audience-data/calls/`, vocabulary-samples in `banks/audience-data/comments/`, contamination scan flags AI-style entries in a single batched table.
2. Run `aud-avatar-build`. Verify max 3 clustering questions per session, max 5 quotes shown per question, held-out files written to `audience/held-out/` BEFORE avatar drafts exist, 4-section avatars with citations from calls (comments only in Vocabulary Bank).
3. Run `aud-validate`. Verify tiered status (validated-vocabulary or validated-full), Billy-readable report (no statistics jargon), failed avatars stay draft.
4. Run `aud-review` on a sample script. Verify subagent invoked per avatar (each response file written before next subagent runs), synthesis structured verdict→3 fixes→scores→dissent→links→disclaimer, dissent quotes pulled verbatim from avatar files.
5. Run `aud-review` on a deliberately weak piece. Verify REWRITE verdict, scores drop, dissent block populates.
6. Cross-avatar identity check (monthly maintenance): show avatar A a held-out quote from avatar B. If A says "that's me," one avatar retires (mode collapse).
7. Voice check across all aud-* skill outputs: zero em-dashes, zero banned words ("ship" as publish, "flatten", "developer" as foil), zero phrasal hyphens.

## 9. Honest limits

**The system can:** flag vocabulary mismatches, surface objections the creator forgot, score friction points, identify tone-deaf framing, generate evidence-grounded rewrite briefs.

**The system cannot:** predict view counts, replace customer calls, score independently of source data depth, stay accurate without ongoing real human input. Comments-derived avatars are weakest for behavioral predictions and should never be trusted for them.

Realistic accuracy floor at MVP scale: directionally useful, well below Twin-2K-500's ceiling. Useful as a fast critic, not as an oracle.

Required disclaimer encoded in every synthesis output. Three rotating variants. Calibration check appended every 10th run OR when `banks/audience-data/calls/` last-modified is > 60 days old.

## 10. Work log

- 2026-05-24. **MVP shipped.** 4 skills built: aud-intake, aud-avatar-build, aud-validate, aud-review. 2 knowledge files added (synthetic-audience-method.md, common-english.txt). vault-integration.md gained 7 new frontmatter schemas. CLAUDE.md folder structure + routing table updated. Plan went through one UX critique round before build (cut orchestrator, shrank avatar profile from 8 to 4 sections, tiered validation, file-system-enforced held-out, subagent isolation). Original plan archived at `C:\Users\billr\.claude\plans\can-we-build-a-mighty-flute.md`.
- 2026-05-25. **Wordlist rename.** `knowledge/common-english-5k.txt` renamed to `knowledge/common-english.txt`. The "5k" suffix promised 5,000 words; the file contained ~940. Name now matches reality. References updated in `synthetic-audience-method.md` and `aud-validate/SKILL.md`. List grows over time as needed.
- 2026-05-25. **This plan doc created.** Separate from `documents/build-plan.md` so the audience subsystem has its own accountable surface.
