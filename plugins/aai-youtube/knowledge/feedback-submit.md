# Feedback submit

The submission contract for the `aaios-feedback` skill. One place holds the endpoint, the payload shape, the curl recipe, and the fallback. The skill body stays thin and points here.

## Constants

- **Endpoint (production, ships in plugin):** `https://uncommon-rat-536.convex.cloud/api/mutation`
- **Endpoint (dev, local testing only):** `https://marvelous-quail-653.convex.cloud/api/mutation`
- **Mutation path:** `domains/forms/submissions:submit`
- **Form slug:** `aaios-feedback`
- **Public form URL (fallback link):** `https://app.peaksystems.io/f/aaios-feedback`

The endpoint is a public, no-auth Convex mutation (the same surface anyone hits from the live `/f/aaios-feedback` page). Nothing secret ships in the plugin.

## The payload

The mutation takes `{ formSlug, values, userAgent? }`. The `values` keys must match the form's field IDs exactly. The submit handler validates: required fields must be non-empty, `email` fields must look like an email, anything else is coerced to a string.

| Field ID | Type | Required | What goes in it |
|---|---|---|---|
| `severity` | radio | yes | one of `blocker`, `annoying`, `nitpick`, `idea`, `praise` |
| `failureMode` | text | no | short tag for the kind of break: `fabrication`, `wrong-voice`, `broken-wikilink`, `wrong-alignment`, `missing-input`, `other` |
| `whatHappened` | textarea | yes | the creator's own words plus your short reconstruction of what went wrong |
| `whatTheyWanted` | textarea | no | what the creator expected or wanted instead |
| `skillName` | text | no | which skill(s) ran this session, comma-separated |
| `sessionMode` | text | no | which mode or dial the skill ran in (fresh / refresh, the intake mode, the dial turns) |
| `pluginVersion` | text | no | the installed plugin version |
| `reproductionCase` | textarea | no | a seeds.json-shaped JSON case reconstructed from the session: the raw input, persona reveals and withholds, format, mode, distinctive phrases, banks pulled, fabrication traps. Per the capture map. Billy replays it from his `tests/corpus` |
| `fixturesSnapshot` | textarea | no | the full content of the determinative vault files the skill read this run, each under a `--- path ---` header, per the capture map. Never include held-out quote files |
| `badOutputVerbatim` | textarea | no | the broken artifact in full, exactly as produced. For a huge artifact, capture the broken portion and point `artifactsTouched` at the file |
| `artifactsTouched` | text | no | comma-separated vault paths the skill wrote or was about to write |
| `runtime` | text | no | e.g. `Cowork`, OS, anything useful about the environment |
| `creatorName` | text | no | who is reporting, if known |
| `creatorEmail` | email | no | for follow-up. Only include a real, well-formed address. If you are unsure, omit it. A malformed value makes the whole submit fail. |

Only `severity` and `whatHappened` are required, so an automated submit never fails on a missing optional field. Omit any field you do not have rather than sending an empty placeholder.

**Which pieces to capture is per skill.** `knowledge/feedback-capture-map.md` defines, for each skill, how to build the `reproductionCase`, which files go in the `fixturesSnapshot`, and which artifact is the `badOutputVerbatim`, plus what to tag in `failureMode` and `sessionMode`. The goal is a replay bundle: enough to recreate the bad run. The `aaios-feedback` skill looks the skill up there before assembling. For an unmapped skill it uses that file's default principle. Held-out quote files are never snapshotted.

## Auto-collected context (no questions for these)

- **Plugin version.** Read `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` and take the `version` field. If `${CLAUDE_PLUGIN_ROOT}` does not resolve, search the install dir for `.claude-plugin/plugin.json`. If you cannot find it, leave `pluginVersion` out.
- **Skill name(s).** Read it from the session you are in. Which skill(s) did the creator run before this. You have the conversation in context, so name them directly.
- **Runtime.** Whatever you can tell about the environment (Cowork, OS). Optional.

## The curl recipe

The session excerpt can be long and contain quotes and newlines, so never build the JSON inline in the shell. Write the payload to a temp file, then post the file. Use bash + curl (Cowork's web-fetch tool is unreliable for this; curl is the primary path).

1. Build the payload object and write it to a temp file, for example `payload.json` in the runtime temp dir:

```json
{
  "path": "domains/forms/submissions:submit",
  "args": {
    "formSlug": "aaios-feedback",
    "values": {
      "severity": "annoying",
      "failureMode": "wrong-voice",
      "whatHappened": "...",
      "whatTheyWanted": "...",
      "skillName": "vid-intake",
      "sessionMode": "mode 3, own transcript, listicle, systems",
      "pluginVersion": "0.2.2",
      "reproductionCase": "{ \"slug\": \"...\", \"skill\": \"vid-intake\", \"seed\": \"...\", \"persona\": { \"reveals\": [], \"withholds\": [] } }",
      "fixturesSnapshot": "--- foundation/avatar.md ---\n...\n--- foundation/iceberg.md ---\n...\n--- banks/pattern-bank.md (cited rows) ---\n...",
      "badOutputVerbatim": "...",
      "artifactsTouched": "content/pieces/{slug}/brain-dump.md",
      "runtime": "Cowork",
      "creatorName": "...",
      "creatorEmail": "..."
    },
    "userAgent": "authentic-ai-os-feedback"
  },
  "format": "json"
}
```

2. POST it:

```bash
curl -sS -X POST "<ENDPOINT>" \
  -H "Content-Type: application/json" \
  --data @<temp>/payload.json
```

3. Parse the response.
   - Success looks like `{"status":"success","value":{"id":"..."},"logLines":[]}`. The `value.id` is the new submission row. Treat any `"status":"success"` as sent.
   - Failure looks like `{"status":"error","errorMessage":"...","logLines":[]}`. Common causes: `Form not found` (the form was never created on this deployment) or `Form is not accepting submissions` (it is toggled off) or a required-field / email validation message.

4. Delete the temp payload file after the call. It contains the session excerpt.

## The consent rule

The `fixturesSnapshot` ships the full content of the creator's real foundation and bank files, and the `reproductionCase` and `badOutputVerbatim` carry their words and material. Before the POST, show the creator exactly what will be sent, and name the files going out in the snapshot, then get a clear yes. Shape: "This sends your foundation doc, your voice profile, and 2 pattern-bank entries, plus the bad output and a replay case. OK to send?" The creator asked for this or accepted the offer; the preview is the final gate. If they say trim it or drop a file, honor that and send the rest. Held-out quote files (`audience/held-out/`) are never sent, not even named.

## The fallback ladder

Write the local vault copy first (the skill does this before attempting the send), so feedback is never lost even with no network.

1. **curl POST to the endpoint** (primary). On `"status":"success"`, done.
2. **curl missing, network fails, or `"status":"error"`:** do not retry in a loop and do not surface a raw error to the creator. The local copy is already saved. Tell the creator plainly that the auto-send did not go through, point them at the public form `https://app.peaksystems.io/f/aaios-feedback`, and confirm the local copy is saved at its path so nothing is lost. There is no reliable POST fallback through the runtime web-fetch tool, so do not pretend to send through another channel.

## What success looks like to the creator

One short line. "Sent. Thanks, this goes straight to Billy." Do not paste the row id, the payload, or the endpoint. If it fell back, one short line that the local copy is saved and where, plus the form link.
