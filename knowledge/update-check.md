# Update check

**MANDATORY. NON-NEGOTIABLE. RUN THIS BEFORE ANYTHING ELSE.**

This is the first thing every skill does on the first message of a session. Not after reading the rest of the SKILL.md. Not after responding to the creator. First. The creator's request waits until this completes.

## Once-per-session guard

Before running this check, scan the conversation so far:

- Has any earlier message in this session already mentioned checking for updates? Skip.
- Has the creator already been shown a "v{latest} is available" notice this session? Skip.
- Has any earlier turn confirmed "you're up to date"? Skip.

If any of the above is true: do NOT run the check again. Proceed directly to the skill's actual job. The check is per-session, not per-skill-invocation.

If none of the above: continue with the check below.

## The check

1. **Read the installed version.** Read `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`. The `version` field is the source of truth. If `${CLAUDE_PLUGIN_ROOT}` does not resolve in this runtime, locate `plugin.json` by searching the plugin install directory for a file at `.claude-plugin/plugin.json`.
2. **Fetch the latest release.** Try fetchers in order. Empty / 404 / timeout / parse-fail all count as "try the next one." Public distribution mirror is `BillyRybka/aaios-releases`; the source repo is private.
   - **a. Bash + curl on JSON API** (primary): `curl -sL https://api.github.com/repos/BillyRybka/aaios-releases/releases/latest`. Parse: `tag_name`, `assets[*].browser_download_url` matching `*.plugin`, `size`. This is the most reliable path; curl handles the JSON API correctly even when the runtime's web-fetch tool does not.
   - **b. Runtime web-fetch tool on JSON API** (fallback): same URL as (a). Cowork's `mcp__workspace__web_fetch` returns empty on `api.github.com`; treat empty as fail and continue.
   - **c. Runtime web-fetch tool on HTML releases page** (fallback): `https://github.com/BillyRybka/aaios-releases/releases/latest`. Auto-redirects to the latest release page. Version from the redirected URL or `<title>`. Asset URL from an anchor `href` ending `.plugin`.
   - **d. Expanded-assets HTML** (last resort, needs a version from elsewhere): `https://github.com/BillyRybka/aaios-releases/releases/expanded_assets/v{latest}`.
3. **Parse the response.** `tag_name` is the latest version (strip a leading `v` if present). Find the asset whose `name` ends with `.plugin`. Its `browser_download_url` is the download URL, `size` is the expected byte count.
4. **Compare versions.** Split each on `.`, compare integers left to right. If latest > installed, an update exists.

If versions match: proceed silently to the skill's actual job. Say nothing about updates. Do not announce that you checked.

If you cannot verify the latest version after exhausting step 2's ladder: proceed silently. "Silently" means:

- Say NOTHING about the update check.
- Do NOT claim "no update available." You did not verify that.
- Do NOT claim "you're up to date." You did not verify that.
- Do NOT mention the check ran, succeeded, or failed.
- Do NOT surface errors, empty responses, or any diagnostic to the creator.

Start the skill's job as if the pre-flight was never written. The only positive update-status claim you can ever make is one you actually verified by completing steps 1-4 successfully.

If an update exists: continue to the steps below. Do NOT proceed with the skill's job yet.

## Deliver the file

5. **Download the .plugin file to the runtime's user-visible outputs folder.** The exact path varies by runtime. Resolve it dynamically, never hardcode:
   - **Cowork sandbox:** the outputs folder mounts at `/sessions/<session-name>/mnt/outputs/` from inside bash, and surfaces on the user's machine at `${CLAUDE_DATA_DIR}\...\local_<id>\outputs\`. Treat both as runtime values you read from the environment, not strings you write into this doc.
   - **Other runtimes:** use whichever file-output mechanism the runtime exposes. If no user-visible outputs folder exists, skip this step and the next one, and use the URL-only fallback below.
   
   Use bash (or whatever shell tool the runtime gives) to download. Example shape, with `<outputs-path>` resolved at runtime:
   ```
   curl -sL -o <outputs-path>/authentic-ai-os-v{latest}.plugin "{browser_download_url}"
   ```
   After download, verify the file size matches the API's reported `size` field. If sizes differ, the download was incomplete; skip to the URL-only fallback below.

6. **Present the file inline.** Call `mcp__cowork__present_files` with the downloaded file path. The creator sees a clickable file card in chat. If `mcp__cowork__present_files` is not available in this runtime, skip step 6 and use the URL-only fallback below.

## Silent execution

Run all steps above (1-6) silently. Do NOT announce what you're doing. Do NOT say "I'll run the pre-flight check," "I need to halt," or any narration of the process. The first text the creator sees in the session is either:

- Nothing (if up to date or any step errors): proceed silently to the skill's actual job.
- The notice below (if an update exists): the entire output, formatted exactly as shown.

No preamble. No status updates. No "let me check first." Silent until the notice or silent forever.

## Tell the creator and STOP

Two notice variants depending on whether the file card was presented. Output exactly the shape shown, then halt. Markdown formatting (bold, emojis, horizontal rules if used) renders in Cowork.

### Variant A (file card succeeded)

```
🚨 **Update available**

Authentic AI OS v{latest} is ready to install.
You're currently on v{current}.

&nbsp;

**How to update**

Right-click "Save plugin" on the file card below and save it to your computer.

&nbsp;

⚠️ **Heads up**

After installing, you'll need to start a new session.
The update won't apply to this one.

---

Not ready? Just say "continue without updating" and we'll keep going on v{current}.
```

### Variant B (URL-only fallback)

Use this if the download failed, the size didn't match, or `mcp__cowork__present_files` isn't available.

```
🚨 **Update available**

Authentic AI OS v{latest} is ready to install.
You're currently on v{current}.

&nbsp;

**How to update**

Download here: {browser_download_url}

&nbsp;

⚠️ **Heads up**

After installing, you'll need to start a new session.
The update won't apply to this one.

---

Not ready? Just say "continue without updating" and we'll keep going on v{current}.
```

## After the notice: halt

Do not run any further tools. Do not start the skill's actual work. Wait for the creator's response.

- If the creator says "continue without updating" (or any clear equivalent): proceed with the skill's job normally.
- If the creator goes silent or talks about something else: stay halted. The update is the active topic.
- If the creator installs the new version and starts a new session: that new instance handles its own pre-flight.

## What this is NOT

- Optional. It runs every first message of a session, every time.
- Quiet when it should be loud. If an update exists, it stops the skill. Period.
- An auto-installer. Cowork's runtime owns plugin installs. We deliver the file and signal "new session needed." We do not prescribe a drag-drop or click action; the creator follows whatever install UX their runtime provides.
- A nag. Once per session, ever. The guard above is the rule.
