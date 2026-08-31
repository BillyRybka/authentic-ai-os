---
name: aai-feedback
description: Captures a creator's feedback on an Authentic AI OS skill that just ran (or the whole session) and sends it to Billy, the plugin's author, with a reproduction bundle, after preview and consent. Use whenever a creator wants to report on the plugin or one of its skills. Triggers on "give feedback", "leave feedback", "send feedback", "AAI feedback", "AAIOS feedback", "that didn't work", "report a bug", "this is broken", "something went wrong", or "that's not what I wanted".
---

# AAI feedback

Turn a creator's reaction into a structured report Billy can act on, and send it. The creator should feel like they said one or two sentences and were done. You do the assembly.

> **Loads.** Read `references/feedback-submit.md` (the endpoint, payload, curl recipe, fallback), `references/feedback-capture-map.md` (what to capture per skill), and `${CLAUDE_PLUGIN_ROOT}/knowledge/vault-integration.md` (frontmatter discipline for the local copy). The offer protocol that may have sent you here lives in `knowledge/feedback-offer.md`. Resolve `knowledge/X.md` via `${CLAUDE_PLUGIN_ROOT}` at runtime, or repo-relative in dev.

## What this produces

1. A submission to the `aaios-feedback` form (public Convex endpoint, per `feedback-submit.md`).
2. A local copy in the vault at `feedback/{date}-{skill}.md` as a record and a fallback if the send fails.

## When to run

- The creator asks for it directly (the trigger phrases above).
- The offer protocol in `feedback-offer.md` hands off after a failure, clear frustration, or a completed journey.

Both paths land in the same flow below. If you arrived from the offer protocol and the creator already described the problem, do not re-ask it.

## The flow

### Phase 0: Triage (silent)

Open `references/feedback-capture-map.md` and read its "Is this worth reporting?" section first. It carries the `failureMode` tags and the three kinds of friction that route somewhere else instead of becoming a report.

The one that comes up most: a voice correction is not a bug. When the creator reworded a line, that belongs to `vid-voice-update`, which asks one-off vs standing rule and writes the answer to their voice profile. Point them there and stop. Only file `wrong-voice` when the skill ignored a rule already sitting in `foundation/voice-profile.md`.

If nothing in the session is reportable, say so in one line and do not file an empty report.

### Phase 1: Reconstruct context (silent)

You have the session in context. Pull, without asking:

- **Which skill(s) ran** and which one this feedback is about. If several ran, name the one that prompted the feedback plus the others as context.
- **Where it went sideways.** The specific moment, message, or output that broke or disappointed. Hold the verbatim span around it for the excerpt.
- **Look the skill up in the capture map and build the replay bundle.** Open `references/feedback-capture-map.md` and find the entry for the skill that ran. Build three things from its lines: a `reproductionCase` (a seeds.json-shaped JSON reconstructed from this session, the raw input plus the persona reveals and withholds drawn from how the creator actually responded), a `fixturesSnapshot` (the full content of the determinative vault files the entry names, each under a `--- path ---` header), and the `badOutputVerbatim` (the artifact in full). On a `worked-well` report that last field carries the GOOD artifact, which is worth more to the eval harness than any bug report. Tag `failureMode` from the Phase 0 table, and `sessionMode`. Record the touched paths in `artifactsTouched`. If the skill has no entry (any WIP skill), use the file's default principle. Never snapshot held-out quote files (`audience/held-out/`).
- **Plugin version.** Read `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`, take `version`. If it does not resolve, search the install dir for `.claude-plugin/plugin.json`. If you cannot find it, leave it out.
- **Runtime.** Cowork, OS, anything useful. Optional.

Do not paste any of this into chat. It is for the report.

### Phase 2: Ask one or two light questions

Never an interrogation. At most two short questions, and skip any you already know.

- **Severity.** Map it yourself if the creator's tone makes it obvious, otherwise ask in plain words: is this a `blocker` (stopped you cold), `annoying` (worked but rough), `nitpick` (small thing), `idea` (a suggestion), or `praise` (something worked well)?
- **What happened / what you wanted instead.** If the creator already said it, lift their words. Only ask if you are missing it.

Use the creator's own phrasing in the report. Do not polish it into generic prose.

### Phase 3: Assemble the report

Fill the payload from `feedback-submit.md`:

- `severity`, `whatHappened` (creator's words plus your one-line reconstruction), `whatTheyWanted` if known.
- `skillName`, `pluginVersion`, `runtime` from Phase 1.
- `reproductionCase`, `fixturesSnapshot`, `badOutputVerbatim`, `artifactsTouched`, `failureMode`, `sessionMode` from the capture-map work in Phase 1. These are the replay bundle, what lets Billy recreate the bad run. Omit any you genuinely do not have.
- `creatorName` / `creatorEmail` only if known. Only include a well-formed email; otherwise omit it (a bad value fails the whole submit).

### Phase 4: Write the local copy first

Before any network call, save `feedback/{date}-{skill}.md` (append `-2`, `-3` if the name is taken). This is the record and the fallback. Frontmatter:

```yaml
---
type: feedback
project: authentic-ai-os
skill: {skill-name}
severity: {severity}
plugin_version: {version}
date: {YYYY-MM-DD}
submitted: false        # flip to true after a successful send
tags: [feedback, severity-{severity}]
---
```

Body: what happened, what they wanted (if any), then the reproduction case, the fixtures snapshot, and the bad output under their own headings.

### Phase 5: Preview and consent

The `fixturesSnapshot` ships the creator's real foundation and bank files, and the `reproductionCase` and `badOutputVerbatim` carry their material. Show the creator a short preview of exactly what will be sent, and name the files going out in the snapshot. Shape: "This sends your foundation doc, your voice profile, and 2 pattern-bank entries, plus the bad output and a replay case. OK to send?" Get a clear yes. If they say trim it or drop a file, honor that and send the rest. This is the final gate. Held-out quote files are never sent.

### Phase 6: Submit

Follow the curl recipe in `feedback-submit.md`. Write the payload to a temp file, POST it, parse the response, delete the temp file.

- On `"status":"success"`: flip `submitted: true` in the local copy. Tell the creator in one line: "Sent. This goes straight to Billy." Do not paste the row id, payload, or endpoint.
- On failure (curl missing, network down, or `"status":"error"`): do not retry in a loop, do not surface a raw error. The local copy is saved. Tell the creator plainly that the auto-send did not go through, give them the form link `https://app.peaksystems.io/f/aaios-feedback`, and confirm the local copy's path so nothing is lost.

## Anti-patterns

- Interrogating. Two questions maximum, fewer if you already know the answers.
- Fabricating. Never invent what the creator felt or wanted. If you do not know, ask or leave it out.
- Sending without consent. Phase 5 is not optional.
- Polishing the creator's words. Lift their phrasing into `whatHappened` verbatim.
- Pasting the payload, row id, or endpoint into chat. One short confirmation line.
- Nagging. If this came from the offer protocol and the creator declines, drop it per the once-per-session guard in `feedback-offer.md`.
- Running the update pre-flight. This skill skips it on purpose.
