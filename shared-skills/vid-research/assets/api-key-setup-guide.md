# YouTube Data API Key Setup

vid-research needs a YouTube Data API key to pull channel data. Setup takes 5 minutes via Google Cloud Console. Free tier (10,000 units/day) is plenty for one creator's research sessions.

This guide walks the creator through the one-time setup. After this, the key goes in a `.env` file at the vault root and gets reused on every vid-research run.

## Step 1: Create or open a Google Cloud project

1. Go to [console.cloud.google.com](https://console.cloud.google.com).
2. Sign in with the Google account you want to use (any Google account works, doesn't need to match your YouTube channel account).
3. Click the project dropdown at the top of the page (next to "Google Cloud").
4. Click "NEW PROJECT".
5. Give it a name like "vid-research" or "youtube-pattern-bank". The project ID auto-generates.
6. Click "CREATE". Wait 10-15 seconds for the project to provision.
7. Confirm the project is selected (project name shows in the top dropdown).

## Step 2: Enable the YouTube Data API v3

1. In the left sidebar (or via the search bar at the top), navigate to "APIs & Services" → "Library".
2. In the API Library search, type "YouTube Data API v3".
3. Click the result, it'll show a description page for "YouTube Data API v3".
4. Click the blue "ENABLE" button.
5. Wait for the API to enable (10-15 seconds).

## Step 3: Create an API key

1. After enabling, you'll be redirected to the API's overview page. If not, navigate to "APIs & Services" → "Credentials".
2. Click the "+ CREATE CREDENTIALS" button at the top.
3. Choose "API key" from the dropdown.
4. A modal will pop up showing your new API key, a long string starting with "AIza...".
5. **Copy the key immediately.** Save it somewhere safe (a password manager is ideal).

## Step 4: (Optional but recommended) Restrict the key to YouTube Data API only

This prevents accidental misuse if the key leaks.

1. In the modal that showed your key, click "EDIT API KEY".
2. Under "API restrictions", select "Restrict key".
3. In the dropdown, check ONLY "YouTube Data API v3".
4. Click "OK", then "SAVE".

**Do NOT** add "Application restrictions" (HTTP referrers, IP addresses, etc.). vid-research runs locally on your machine, not through a website. HTTP referrer restrictions will cause API calls to fail.

## Step 5: Save the key to your workspace

vid-research reads the key from a `.env` file at the vault root. You can either:

**Option A: Skill walks you through it.**
The next time you run vid-research, it'll detect the missing key and walk you through adding it to `.env`.

**Option B: Save it manually.**
Copy `.env.example` to `.env` at the vault root (creator-setup scaffolds `.env.example` for you) and paste your key after `YT_API_KEY=`:

```
YT_API_KEY={paste your key here}
```

Either way, the key stays in `.env`, which is gitignored. It never gets written into any skill file, committed, or saved to the foundation docs.

## Step 6: Verify the key works

When you run vid-research, the first call validates the key. If you see this error:

```
ERROR: YouTube API HTTP 400 on /channels: API_KEY_INVALID
```

The key is malformed. Re-copy from Google Cloud Console.

If you see:

```
ERROR: YouTube API HTTP 403 on /channels: API_NOT_ENABLED
```

The YouTube Data API v3 isn't enabled on the project. Go back to Step 2.

If you see:

```
ERROR: YouTube API HTTP 403 on /channels: quotaExceeded
```

You've hit the 10,000 unit daily limit. Quota resets at midnight Pacific Time. Wait and resume.

## Quota usage reference

- channels.list: 1 unit per call (resolves channel handles, gets uploads playlist ID)
- playlistItems.list: 1 unit per page of 50 (lists video IDs from a channel's uploads)
- videos.list: 1 unit per batch of 50 video IDs (gets view counts, thumbnails, durations)

A typical full research session (1 own + 5 niche + 5 adjacent = 11 channels):

- channels.list calls: 11 (1 per channel) = 11 units
- playlistItems.list calls: ~3-5 per channel (depending on how many videos) × 11 = ~40 units
- videos.list calls: ~3-5 per channel × 11 = ~40 units

**Total per session: ~90 units.** Daily quota is 10,000. You can run ~100 full sessions per day before hitting limits, way more than any creator needs.

## Common gotchas

**Gotcha 1: API key tied to wrong Google account.**
If you're running vid-research from a workspace tied to one Google account but generated the key in a different Google Cloud project, the key still works, keys aren't account-locked, they're project-locked. You can use one key across multiple workspaces.

**Gotcha 2: Project deleted.**
If the Google Cloud project is deleted, the API key dies with it. Re-run this guide to generate a new key in a new project. Update the `YT_API_KEY=` line in `.env`.

**Gotcha 3: Billing not required.**
You do NOT need to enable billing on the Google Cloud project. The free tier (10k units/day) is enough for vid-research. Don't add a credit card unless you're sure you need to (and you don't).

**Gotcha 4: Application restrictions break local scripts.**
If you accidentally added HTTP referrer or IP restrictions in Step 4, the script will fail. Edit the key in Cloud Console, remove the application restriction, save. API restrictions (Step 4 main path) are fine and recommended.

## Cost summary

YouTube Data API v3 free tier: **$0/month** for any creator using vid-research. Free tier handles way more than vid-research needs.

If for some reason you hit the daily quota limit (you ran 50 research sessions in one day), Google offers paid quota expansion. Almost no creator should ever need this.

## Privacy note

The API key only lets vid-research READ public YouTube data, channel metadata, public video stats, public thumbnail URLs. It does NOT access:

- Your YouTube Studio analytics
- Your audience-also-watches data
- Any private videos
- Subscriber counts beyond what's publicly visible
- Comments or any private engagement data

For audience-also-watches access, vid-research v2 will use OAuth (creator grants explicit permission). Out of scope for v1.
