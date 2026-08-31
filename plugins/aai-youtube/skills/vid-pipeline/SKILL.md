---
name: vid-pipeline
description: Thin orchestrator for one video, idea to filming-ready script. Reads where a piece is in the writing pipeline and auto-invokes the next skill (vid-ideas when the creator is blank on ideas, then vid-braindump, vid-framing, vid-title, vid-thumbnail, vid-structure, vid-intro, vid-segment, vid-ending, vid-pressure-test). Use this when the creator says "work on my video", "continue this piece", "what's next on {piece}", "move this video forward", "run the pipeline", "let's make a video", or "/vid-pipeline". It routes and delegates; it never writes content itself.
---

# Video Pipeline

Thin orchestrator. It reads one piece's `piece.md` to find where it is, then invokes the next skill in the writing chain. It does not write angles, titles, hooks, prose, or any content. Every creative decision lives in a sub-skill. This is the per-video sibling of `/foundation`.

The chain it routes through:

`vid-braindump` → `vid-framing` → `vid-title` → `vid-thumbnail` → `vid-structure` → `vid-intro` → `vid-segment` (once per body segment) → `vid-ending` → `vid-pressure-test`.

Optional front door: when the creator is blank on ideas, `vid-ideas` runs first and its picked seed packet enters the chain at `vid-braindump`.

## Response format

Keep responses scannable. Lead with where the piece is and what's next, in one or two lines. Break by idea. Plain language. The creator should know the state and the next step in three seconds.



## How this runs

### Step 1: Prerequisites (silent)

Two checks, both silent. Surface output only if action is needed.

**Foundation (hard).** If `foundation/iceberg.md` or `foundation/avatar.md` doesn't exist, halt and point at `/foundation`:

> "No foundation yet. The pipeline writes from your avatar, Iceberg, and pillars. Run `/foundation` first, then come back."

Do not route further until both exist. Checking existence is not reading; the orchestrator loads neither file. Each sub-skill reads the foundation files it needs, never the whole set.

**Voice (soft).** If `foundation/voice-profile.md` doesn't exist, warn once and continue:

> "No `voice-profile.md` yet. The pipeline will draft from your foundation fingerprint, which is thinner. Run `/vid-voice-capture` anytime to upgrade the voice."

Voice is never a blocker.

### Step 2: Pick the piece

First, two fast paths that skip the menu, because the intent is already clear:

- **The creator named a slug** (`/vid-pipeline {slug}`, or "work on the retention piece"): load `content/pieces/{slug}/piece.md` and go to Step 3.
- **The creator led with material** (a brain dump, "I want to make a video about X", a pasted transcript): treat it as a new piece, invoke `vid-braindump` via the Skill tool, and stop here. Do not also run the scan below.

**Otherwise the intent is ambiguous** (a bare `/vid-pipeline`, "work on my video", "what's next" with no piece named and no material). Surface the entry menu with `AskUserQuestion`. Four options, plus the always-available Other escape:

- **"New video, I have an idea or material"** → invoke `vid-braindump`. This is the single authoritative path that starts a new piece; when it is chosen, do NOT also fire the zero-in-progress branch below, or capture double-fires.
- **"New video, I'm blank on ideas"** → invoke `vid-ideas`. It generates a signal-backed batch, the creator picks one, and `vid-ideas` hands the picked seed packet to `vid-braindump` itself. When `vid-braindump` has created the piece folder, re-read `piece.md` and resume routing at Step 3.
- **"Pick up where I left off"** → run the in-progress scan below.
- **"I have a script, just pressure-test it"** → run the in-progress scan below to resolve which piece, then follow the pressure-test shortcut note below.

If the creator picks Other and just tells you what they want, follow it. The menu is a convenience, never a cage. A stop signal (Step 5) at the menu halts cleanly. If the runtime does not render a selectable menu, present the same four options as a short numbered list and wait for a typed reply.

**The in-progress scan** (used by the two resume options, or whenever a slug was not named): scan `content/pieces/*/piece.md`, and consider ONLY files whose frontmatter has `type: content-piece`. A vault can hold `piece.md` files created by other systems; skip any without that type so they are never mistaken for in-progress videos. Among the real pieces, an in-progress one has `status` that is NOT `filming-ready`, `filmed`, `editing`, or `published`.

- **Zero in-progress pieces:** nothing to resume or test. Say so, and offer to start a new piece with `vid-braindump` via the Skill tool.
- **One in-progress piece:** name it and continue. "Picking up `{slug}` ({current phase}, last touched {last_updated})." Go to Step 3.
- **More than one:** list them and ask. One line each: slug, derived phase, `last_updated`. End with "Which one, or start a new piece?" Wait for the answer. Never silently pick.

**Pressure-test shortcut.** If the creator chose "just pressure-test it," resolve the piece first (the scan above), then route it through Step 3. Do not jump straight to `vid-pressure-test`. If Step 3 lands on the `vid-pressure-test` row (the script is complete), invoke it. If Step 3 lands on any earlier row (the piece is not script-complete yet), tell the creator where it actually is and route to the correct next skill instead. The pipeline never drops a half-written piece into an audit that will reject it.

Derive the phase label for the list from the same signals Step 3 routes on (e.g. "framed, no title yet", "drafting, 3/5 segments", "body done, needs pressure-test"). The stored `status` is the coarse lifecycle; the derived label is the fine detail. Do not invent a status field to store the detail.

### Step 3: Route to the next skill

Read `piece.md` frontmatter plus the presence of sibling files. Match top-to-bottom; the first matching row wins. Then invoke that skill via the Skill tool, passing the slug.

| State of the piece | Next skill |
|---|---|
| No `piece.md` for the slug | `vid-braindump` |
| `brain-dump.md` still carries `## Still capturing` | `vid-braindump` (resume the dump) |
| No `frame` | `vid-framing` |
| `frame` set, no `title` | `vid-title` |
| `title` set, no `thumbnail_text` | `vid-thumbnail` |
| `thumbnail_text` set, no `segment_purposes` | `vid-structure` |
| `segment_purposes` set, no `intro_locked` | `vid-intro` |
| `intro_locked`, `segments_completed` count < `segment_purposes` count | `vid-segment` (next unwritten segment) |
| `segments_completed` count == `segment_purposes` count, no `ending_locked` | `vid-ending` |
| `ending_locked`, `status` not `filming-ready` | `vid-pressure-test` |
| `status: filming-ready` | DONE. See Step 5. |

Title always comes before thumbnail (vid-thumbnail needs the locked title to avoid repeating its words). That order is fixed; do not offer to reverse it.

### Step 4: Tell the creator, then auto-invoke

Short message. Mirror the state, name the next skill, then invoke it immediately via the Skill tool. No "type the next command" friction.

Shape:

> "`{slug}` is {one-line state}. Next: `{skill}` to {one sentence on what it produces}."

Then invoke `{skill}`. When that sub-skill finishes and the creator wants to keep going, re-read `piece.md` and route again. The whole video can run end-to-end unless the creator stops.

**Pre-flight and prerequisites run once, here, and never again this session.** You ran pre-flight at the top of this skill and verified foundation + voice in Step 1. A sub-skill must not repeat either. Pass a short context line with every invocation so it goes straight to the work: `[pipeline session: pre-flight done, foundation verified, voice {present|absent}, slug={slug}. Skip pre-flight and prerequisite re-checks; do not re-announce them.]` And keep your own between-step messages to the one-line state plus next-skill shape above. Never recap "foundation and voice both exist" or "pre-flight already ran." That recap is exactly the noise the creator does not want.

For the segment loop: after each `vid-segment` lock, `segments_completed` grows by one. Re-route. While the count is below `segment_purposes`, the next route is `vid-segment` again (the next unwritten segment). When they're equal, the route advances to `vid-ending`.

### Step 5: Handle stop signals

If the creator says "stop here", "stop", "halt", "pause", "let me come back", or "hold on", do not invoke the next skill. The piece's state is saved in `piece.md`; re-running `/vid-pipeline {slug}` later resumes exactly here.

### Step 6: Filming-ready

When `status: filming-ready`, congratulate and stop:

> "`{slug}` is filming-ready. Script passed pressure-test. Go film. After it's published, `vid-measurement` (coming) will read performance back into your banks."

Do not invoke anything further. Post-production states (`filmed`, `editing`, `published`) are set by the creator, not the pipeline.

## What this is NOT

- A content writer. It never drafts an angle, a title, a hook, prose, or a thumbnail. Every word the creator sees comes from a sub-skill.
- A re-writer. To re-frame or re-title a locked piece, the creator runs that skill directly (`/vid-framing`, `/vid-title`). The pipeline only moves a piece forward.
- A batch runner. One piece per invocation. Multiple in-progress pieces means the creator picks one each run.
- The voice manager. `vid-voice-capture`, `vid-voice-audit`, and `vid-voice-update` are not steps in this chain. They fire on their own triggers (a creator reword that reads like a rule, a pre-publish voice check). The pipeline only warns when `voice-profile.md` is missing; it never invokes them.

## Anti-patterns

- Inlining a sub-skill's logic to "save a step." Always delegate. If you catch yourself drafting a hook or picking an angle here, stop and invoke the responsible skill.
- Writing `piece.md` yourself. The sub-skills own their fields and write them in both standalone and pipeline mode. The orchestrator only reads. If a route keeps firing for the same skill, the sub-skill isn't persisting its field; fix the sub-skill, don't patch it here.
- Reading a sub-skill's reference docs (format planners, tension architecture, the banks). Those belong to the skill that needs them.
- Asking the creator to type the next command. Always auto-invoke via the Skill tool.
- Re-running or re-narrating pre-flight or prerequisite checks between steps. You verified them once (pre-flight at the top, foundation + voice in Step 1). Sub-skills skip them silently because you pass them the pipeline-session context line. Every step starts on the work, never on a status recap.
- Continuing after a clear stop signal.
- Silently picking a piece when several are in progress. Always surface the choice.
- Inventing a second status field. `status` is the one lifecycle field. The next step is decided by which artifact exists, not by a parallel micro-status.
