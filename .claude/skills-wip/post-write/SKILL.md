---
name: post-write
description: Turn a batch of raw ideas or a long-form source into individual platform posts, written one at a time in the creator's voice. Two layers stay separate. Post-type is the shape of the idea (mistake, story, framework, checklist, contrarian, warning, comparison, do-this-not-that). Platform is the delivery (LinkedIn, Instagram carousel, Instagram caption). Filters every idea through the creator's iceberg and Top 3 problems, writes from the vault voice system, and runs an anti-slop editorial pass so nothing reads generated. Self-contained, anti-fabrication, one post at a time with an approval beat. Use this skill whenever a creator wants to turn ideas or existing content into social posts. Phrases like "turn these ideas into posts", "write LinkedIn posts from this", "make a carousel from this", "repurpose this video into posts", "I have a batch of ideas, write them up", "spin this into a series", "give me posts for Instagram and LinkedIn", "draft social posts from my script", or any moment raw material needs to become platform-ready posts should fire this skill.
---

# Post Writer

Turns one source into many posts, written one at a time, each in the creator's voice and run through an anti-slop pass before it is shown. The source can be a batch of raw ideas (one lesson per post) or a long-form piece (a script, transcript, brain dump, or article) broken into post-worthy units. v1 writes for LinkedIn and Instagram (carousel and caption). This is the first skill in the `post-` family, the distribution area that takes finished material into platform posts, parallel to the `vid-` video line and the `aud-` audience line.

**Scope boundary:** this skill writes POSTS from material the creator already has. It does NOT invent topics from a blank slate (that is `vid-ideas`), write video scripts (that is `vid-structure` and the segment skills), or render images. A carousel comes out as slide-by-slide copy plus a text visual brief, never a rendered graphic. v1 covers two platforms only: LinkedIn and Instagram. Other platforms are out of scope until a later version.

Two layers never collapse: **post-type is the shape of the idea** (what job it has to do), **platform is the delivery** (how it gets packaged where people read it). The same idea can become a LinkedIn argument and an Instagram carousel, translated for each, never pasted across.

> **Resolving `knowledge/` and skill paths.** Any path written `knowledge/X.md` is a plugin reference file. Load it from `${CLAUDE_PLUGIN_ROOT}/knowledge/X.md` when running as an installed plugin. If `${CLAUDE_PLUGIN_ROOT}` is unset or that path does not exist (running from the source repo during development), load the repo-relative path instead. The same applies to skill references named `.claude/skills.../...` and to this skill's own `references/`.

## What this produces

- For each idea: a platform-agnostic **core piece** that nails the content, plus an **adaptation** for each platform the creator wants (LinkedIn, Instagram carousel, Instagram caption). Written and shown one idea at a time, each settled before the next.
- One note per idea at `content/pieces/{slug}/posts/{idea-slug}.md`, created from `assets/post-note-template.md`. Frontmatter carries wikilink provenance (parent source, pillar, problem, post-type, hook-type). The body holds the core piece and each platform adaptation as `## Publishable` blocks, clean copy: no wikilinks, no markdown links, no em-dashes, ready to paste straight to the platform. Carousels also carry a `## Visual brief` text block.
- A short batch summary at the end: what was produced, where it saved, and a hook-variety check across the batch.

## When to run this

- The creator has a batch of raw ideas or lessons and wants each turned into its own post.
- The creator has a long-form piece (script, transcript, article, brain dump) and wants posts pulled from it.
- The creator wants the same idea written for more than one platform.
- NOT when the creator does not yet know what to make. Send them to `vid-ideas` first.
- NOT when they want a video script. Send them to the script pipeline.

## Prerequisites

Hard requirements:
- `foundation/creator-foundation.md` exists with the Iceberg Statement, Content pillars, Avatar, and Top 3 perceived problems. If missing, hard stop: "No foundation docs. Run `/foundation` first so I know your positioning and audience, otherwise the posts will be generic."
- Source material to work from. Either the creator pastes a batch or names a long-form source, or points at an existing piece folder. If there is no source, hard stop: "Give me the ideas or the source piece. This skill repurposes what you already have, it does not invent topics. For that, run `vid-ideas`."

Soft requirements (loaded if present, graceful fallback if not):
- `foundation/voice-profile.md` plus `foundation/reference-pieces/{voice_context}.md` for the chosen platform (`linkedin` or `instagram`). If absent, fall back to `voice_fingerprint` and `signature_phrases` only, and note the gap in the batch summary so the creator can add voice sources for that context. Follow the load contract in `knowledge/voice-profile-schema.md` exactly.

## Invocation modes

**Standalone:** the creator invokes directly with a batch or a source. Run all phases, write the posts one at a time, save them, give the batch summary.

**Sub-skill:** a downstream pipeline (future `vid-pipeline`) may invoke this after a script is locked to spin derivatives. Same flow. Return the list of saved post paths to the caller instead of giving the standalone summary.

## The 5 phases

### Phase 1: Lean load and frame

**Silent loads** (do NOT paste into chat). Load only these:

1. `knowledge/vault-integration.md`. The frontmatter and wikilink contract for everything this skill saves.
2. `knowledge/voice-profile-schema.md`. The voice load contract. Follow it exactly.
3. `foundation/creator-foundation.md`, but only the **Iceberg Statement**, the **Content pillars** list, the **Avatar** description, and the **Top 3 perceived problems**. Skip offer, credibility, backstory.
4. `foundation/voice-profile.md` if it exists, plus `foundation/reference-pieces/{voice_context}.md` for each platform in play. Graceful fallback per the load contract if absent.
5. `references/format-rubric.md`. The decision tree (idea job to post-type) and the platform adaptation matrix. Your thinking, not chat content.
6. `references/anti-slop.md`. The slop tells, the hook rotation library, and the editorial-pass checklist. This is the quality bar for every post.
7. `references/hooks.md`. The hook standard: face the reader, open a gap. The first line is the whole bet, and this is how you make it land. Strength here, variety in anti-slop.
8. `knowledge/iceberg-and-top-3-alignment.md`. The 2-layer fit gate. Reuse it, do not reinvent it.

**Then ask one short question** to frame the run:

> "Two things. What platform(s) do you want, LinkedIn, Instagram, or both? And is this a batch of separate ideas, or one longer piece you want broken into posts?"

Read the input mode from the answer plus the material. Batch of ideas: each idea is a candidate post. Long-form source: you will split it in Phase 2.

### Phase 2: Split into post-worthy units and fit-filter

**Split.** Break the source into one-idea-per-post units. A unit is one point that can stand alone. For a batch, each idea is usually already one unit. For long-form, find the distinct claims, lessons, stories, and frameworks inside it. Do not cram two ideas into one post, and do not split one idea into two thin posts.

**Preserve the creator's exact phrasing.** The source is the voice. Pull the real words, the real claim, the real example. Never paraphrase a unit into smoother generic prose. If a unit is just a topic with no substance ("a post about pricing"), it is not a unit yet. Flag it and ask the creator for the actual point, or drop it.

**Fit-filter each unit** through the 2-layer iceberg + Top 3 gate from the alignment reference. Iceberg fit, then Top 3 fit, the 4 outcomes. Drop a NO/NO (off-channel) unit, do not write it. Allow a YES/NO unit but tag it `outlier_within_iceberg`. Tag each surviving unit with `problem_addressed` (1, 2, 3, or `outlier_within_iceberg`). Surface the filter result in one line per unit, do not run a debate.

### Phase 3: Classify post-type and pick target platforms

For each surviving unit, using `references/format-rubric.md`:

1. **Post-type (the shape).** Ask what job the idea has to do, then pick the type. Correcting a behavior is a mistake post. A repeatable action is a checklist or workflow. Something that happened is a story. A model is a framework. Challenging a belief is a contrarian. Protecting from a risk is a warning. Two confused things is a comparison. A tactical contrast is do-this-not-that. The rubric is the decision tree. The post-type shapes the core piece you write next, and it is platform-agnostic.
2. **Target platforms.** Note which platforms the creator wants this idea on (LinkedIn, Instagram carousel, Instagram caption). Check the adaptation matrix for fit and flag any weak fit. You do not write per platform yet. You write one core piece, then adapt it.

### Phase 4: Write the core, approve it, then adapt per platform

This is the loop. For the next unit, in order:

1. **Fill the post brief** from `assets/post-brief-template.md`: Format (post-type), Audience, Core belief, Enemy, Proof (the real story, example, or pattern from the source, never invented), Practical takeaway, CTA. Keep it short, it is your scaffolding.
2. **Write the core piece.** Read `references/post-types/{type}.md` for the structure and the good and bad examples. Write the idea fully in that post-type's shape, in the creator's voice, anti-slop. The core is a complete standalone piece. It is NOT formatted for any one platform's quirks. It is the canonical version every platform adapts from. Nail the content once here; the platforms are downstream of an approved core. **Engineer the opening line.** Read `references/hooks.md` and make the first line face the reader and open a gap, not introduce a character or a topic. The hook is a first-class part of the core, not a warm-up to it. A flat, subject-facing opener ("Marcus ran an agency...") is the single most common reason a finished post gets scrolled past, so write the hook deliberately and hold it to the hook test. Even a story opens on the reader's tension first, then brings the character in as proof.
3. **Run the anti-slop pass on the core** from `references/anti-slop.md`: strip the AI tells, run the hedging test from `knowledge/ai-hedging.md` (strip the soft phrase, keep it only if a committed claim remains), run the hook test from `references/hooks.md` on the first line (faces the reader, opens a gap, earns line two), confirm one clear idea and real specificity, no invented numbers anywhere (not even in a CTA or an aside, see the invented-numbers rule in `references/anti-slop.md`), and read it aloud per `knowledge/voice-pressure-test.md`.
4. **Show the core ALONE and lock it.** Present just the core piece. Offer the beat: "Is this good? Tweak it, switch the type, or drop it." Do NOT write any platform version until the creator approves the core. This is the gate: the content gets locked before any platform effort, so you never adapt a piece the creator is about to change.
5. **Once the core is approved, adapt it to each target platform.** Read `references/platforms/{platform}.md` and transform the locked core into that platform's delivery. LinkedIn: hook-first, short paragraphs, length and CTA rules. Instagram carousel: first run the worth-it gate in `references/carousel.md`. A single story or one belief is a caption, not a carousel, so do NOT build the carousel for it. Build the caption instead, tell the creator plainly why a single story lands harder as one thread than as slides, and build slides only if the creator explicitly insists after the recommendation. If the idea genuinely earns slides (a list, a framework, a process, a comparison, a multi-beat case study), decompose the core into beats per `references/carousel.md` (one idea per slide, 30 words and two short sentences max per slide, a cover that earns the swipe, the delete test on every slide), never sliced at the core's paragraph breaks, plus a text visual brief. Instagram caption: a warmer single-thread version. Each adaptation is a real transformation of the core, not a paste of another platform's version. **Re-engineer the opening line for each platform** per `references/hooks.md`. The same idea hooks differently on a LinkedIn feed, a carousel title slide, and a caption, so each version gets its own first line held to the hook test, never the core's opener reflowed. Run the anti-slop pass on each adaptation too, watch that no invented number leaks into a platform CTA, and vary the hook against what the batch has already used.
6. **Show the platform versions and get the call.** Present the adaptations. Offer the beat: "Good, or tweak a platform, drop one."
7. **Save the post note** from `assets/post-note-template.md`: provenance frontmatter, then the approved core and each platform adaptation as clean `## Publishable` blocks. Update the parent piece per the vault-integration "update both sides" rule. Settle this unit before the next. Never dump the whole batch at once.

### Phase 5: Batch pass and close

When the batch is done (or the creator stops):

1. **Hook-variety check across the batch.** Scan the openers. If more than two posts share an opening pattern, flag it and offer to re-roll the repeats with a different hook from the rotation library. Sameness across a batch is the loudest AI tell.
2. **Batch summary.** List what was produced, the platform and type of each, and where each saved. If voice context fell back to fingerprint-only (no reference-pieces for a platform), say so and suggest the creator add voice sources for that context.
3. **Surface any failures** per the vault-integration visibility rule: units dropped, partial saves, unresolved wikilinks. No silent swallowing.

## Conversational discipline

- **Conversation, not a document.** Short messages. Never paste the foundation or the references into chat. The loads are for your thinking.
- **One post at a time.** The creator judges each post and redirects before the next. A wall of posts dropped at once is impossible to give feedback on and reads as a machine dump.
- **The source is the voice.** Build from the creator's real words and real material. Never invent a story, a number, a client, or an example to make a post land. A thin unit gets flagged, not fabricated.
- **Specificity wins.** A post about "using AI well" is not a post. "Most AI content sounds generic because the input was generic, not because the model failed" is.
- **Translate, never recycle.** A LinkedIn post pasted into a carousel is recycling. Keep the idea, change the delivery.
- **The creator's call rules.** Switch type, change angle, drop a post on request without arguing.

## Hard friction (stop and flag)

- Foundation missing, or no source material: hard stop per Prerequisites.
- A unit you cannot ground in the creator's real material AND cannot get substance for: do not fabricate it. Flag it and drop it.
- An off-iceberg (NO/NO) unit: do not write it. If the creator insists the iceberg shifted, point them at `/foundation` to refresh positioning first.
- A publishable body that needs a wikilink to make sense: it does not. Wikilinks are provenance, they live in frontmatter and the provenance block, never in the copy that gets pasted.

## Soft friction (surface and let the creator decide)

- A post-type that is only a Medium fit for the chosen platform: write it if the creator wants, but say the fit is weaker and name the stronger platform for that type.
- A batch skewed to one post-type: flag the sameness and offer to mix in other shapes.
- A voice context with no reference-pieces file: write from fingerprint-only, flag the gap, suggest adding sources.
- An Instagram carousel whose idea is really a single story or one belief: default to the caption and do not build the carousel, since a single story hits harder as one thread than as slides. Build slides only if the creator insists after the recommendation.

## Reference index

| File | When to read it |
|------|-----------------|
| `references/format-rubric.md` | Phase 3. The decision tree (idea job to post-type) and the platform adaptation matrix. |
| `references/anti-slop.md` | Phase 4 and Phase 5. Slop tells, the hook rotation library, the editorial-pass checklist, the adaptation-not-recycling rule. |
| `references/hooks.md` | Phase 4. The hook standard: face the reader, open a gap. Run the hook test on the first line of the core and every platform version. |
| `knowledge/ai-hedging.md` | Phase 4. The precise definition of hedging and the 10-pattern checklist used in the anti-slop pass. |
| `references/post-types/{type}.md` | Phase 4. Structure plus a good example and a bad/slop example for the chosen type. Read only the one you are writing. |
| `references/platforms/linkedin.md` | Phase 4. LinkedIn hook style, length, rhythm, CTA, best-fit types, what to avoid. |
| `references/platforms/instagram.md` | Phase 4. Instagram carousel (slides plus visual brief) and caption, best-fit types, what to avoid. |
| `references/carousel.md` | Phase 4. The carousel standard: the worth-it gate (carousel vs caption), how to decompose the core into slides, per-slide limits, the cover, and the coherence checklist. Read when building any carousel. |
| `assets/post-brief-template.md` | Phase 4 step 1. The per-post brief you fill before writing. |
| `assets/post-note-template.md` | Phase 4 step 5. The saved-note shape: provenance frontmatter plus the core piece and each platform adaptation as clean publishable blocks. |
| `knowledge/iceberg-and-top-3-alignment.md` | Phase 2. The 2-layer fit gate and its 4 outcomes. Reuse, do not duplicate. |
| `knowledge/voice-profile-schema.md` | Phase 1. The voice load contract and graceful fallback. |
| `knowledge/voice-pressure-test.md` | Phase 4 step 4. The read-aloud voice test before save. |
| `knowledge/vault-integration.md` | Phase 1 and Phase 4. Frontmatter, wikilinks, and the update-both-sides rule. |

## Principles (the why)

- **Most repurposing is recycling.** People paste one platform's post into another and call it adaptation. The win is keeping the idea and rebuilding the delivery for where it lands. That is the difference between a post that fits and a post that obviously traveled.
- **One job per post.** A post that tries to teach seven things teaches none. Each unit gets one shape and one clear point. That is what makes a batch feel like a person wrote it, not a generator.
- **Voice lives in the source, not in a rule.** The creator's real words carry the grain. The skill organizes and shapes them, it never polishes them into smoother generic prose, and it never invents what the creator did not say.
- **The first line is the whole bet.** On social the opener decides whether the rest is read at all. A hook faces the reader and opens a gap; a flat, subject-facing opener ("Marcus ran an agency") is the most common reason a good post gets scrolled past. Engineer the first line, never let it be a warm-up.
- **Sameness is the tell.** Twenty posts that all open the same way read as a machine, even when each one is fine alone. Hook variety across the batch is a first-class quality bar, not an afterthought.
- **Clean copy ships, the graph stays in the vault.** The publishable body is an artifact that leaves the vault, so it carries no wikilinks. Provenance stays in frontmatter where it powers the graph without leaking into what the creator pastes.

## Related skills

- The `/foundation` chain produces `creator-foundation.md` (iceberg, pillars, avatar, Top 3) this skill reads.
- `vid-voice-capture` produces `voice-profile.md` and `reference-pieces/{voice_context}.md`, the voice this skill writes in.
- `vid-ideas` picks topics from a blank slate. This skill repurposes material the creator already has; it does not ideate.
- The iceberg + Top 3 alignment gate this skill reuses is the shared `knowledge/iceberg-and-top-3-alignment.md`, authored for `vid-intake` and used across the system.
- The script pipeline (`vid-structure` and the segment skills) writes video scripts. Their finished scripts are a valid source for this skill to repurpose into posts.
- `vid-pipeline` (future) may invoke this after a script locks, to spin platform derivatives.
- Future `post-` siblings (carousel rendering, scheduling) will consume the post notes this skill saves.
