---
type: reference
scope: vid-bank
loaded_by: [vid-bank]
status: active
tags: [reference, proof-capture, proof-bank]
---

# Proof Capture Guide

Proof is what a cold viewer needs to believe the creator. Right after a framework lands, the viewer asks "has this actually worked for anyone?" If the answer isn't shown visually, specifically, and undeniably, the viewer loses trust at the exact wrong moment.

This guide teaches how proof works. vid-bank's Stage P uses it to extract and log proof into the bank. Where proof lands once a script pulls it lives in [[proof-placement-rules]].

## Real examples (read these first)

### Example 1: Analytics dashboard screenshot (Personal result, presented as static screenshot)

A screenshot of a YouTube analytics dashboard showing three separate graphs over time. The top graph shows 3.1M views plus significant subscriber and revenue growth. Used as proof in a video about "does this framework actually grow channels."

- Proof type: `personal-result`
- Presentation format: static screenshot
- What it proves: the creator's framework produces measurable channel growth
- Asset: a PNG in `banks/proof-bank/assets/analytics-dashboard-3m-views.png`

### Example 2: Hundreds of client testimonial screenshots (Client win, presented as static-screenshot wall)

A folder filled with PNG screenshots of emails, Discord messages, and YouTube comments from clients reporting wins. Scrolled through on screen in a video to create a "wall of wins" moment. Viewer sees the volume, not just one case.

- Proof type: `client-win`
- Presentation format: static-screenshot wall
- What it proves: the method works for many different people, not just one lucky case
- Asset: a folder reference, not a single file. Either `banks/proof-bank/assets/client-wins/` or listed in Notes.

### Example 3: Airbnb listing before and after (Client win, presented as before-after pairing)

A split image or two sequential stills. Left side shows the old listing photo that wasn't getting bookings. Right side shows the new photo, plus a calendar showing bookings three times that week.

- Proof type: `client-win`
- Presentation format: before-after pairing
- What it proves: swapping a listing photo changes bookings
- Asset: `banks/proof-bank/assets/airbnb-photo-before-after.png`

## The 2 proof types

`proof_type` answers ONE question: who does the result belong to? Pick the type first. Presentation format (how the proof is shown on screen) is captured separately in the body. A single proof can be presented multiple ways.

### Personal result

The creator's own numbers, dashboards, or visible wins. Analytics screenshots, bank balance snapshots, subscriber graphs, revenue milestones.

Use when the creator needs to establish they've actually done what they're teaching.

### Client win

A different person's result, with their permission or properly anonymized. Discord messages, email replies, comment screenshots, case study numbers.

Use when the creator needs to prove the method works for someone besides themselves. Strongest proof type for sales-oriented videos.

## Presentation formats (body-level, not type-level)

How the proof gets shown on screen. Recorded in the entry's "Presentation format" section. A single proof can be available in multiple formats. Capture them all so writing skills can pick the right one for the moment.

- **Static screenshot**: single image, frozen frame. Most common.
- **Before-after pairing**: two images side by side, or a graph showing change over time. Use when the transformation is visually obvious.
- **Live clip**: video of someone actually saying or showing the result. Hardest to collect, heaviest impact.
- **Inline stat or quote**: the proof IS the number or the words, no separate asset file. Capture verbatim.

A proof's `proof_type` never changes. Its presentation formats can grow over time (e.g. a client win starts as a screenshot, later you film the client on camera. Both formats live in the same entry).

## The screenshot-immediately rule

The single most important capture behavior.

The moment a positive result lands (an email, a comment, a message, a graph, anything that could prove a claim later), the creator drops everything and screenshots it. That's it. Save the screenshot in a dedicated folder. Come back later to sort, tag, and add to the bank.

Why: positive proof appears at random. If the creator tells themselves "I'll screenshot that later," they never do. The behavior has to be immediate and non-negotiable.

The creator's phone and desktop should have a quick-capture workflow. A folder called something like "proof-inbox" is fine. Vid-capture then processes items from that folder into proper bank entries.

## Where proof lands in a script

Proof does NOT go at the top of a video. It goes RIGHT AFTER a framework or method is explained. The viewer asks the question "has this actually worked?" right after hearing the method. Proof answers that question in the same breath.

Example flow:

1. Hook states the problem and hints at the fix.
2. Creator explains the framework or method.
3. Creator shows proof. "Here's what this looked like when a client did it."
4. Creator teaches the next step.

Proof ahead of the framework doesn't land because the viewer doesn't yet know what's being proved. Proof way after the framework is too late because the viewer has already decided whether to believe.

## Anonymization and permission

Before capturing a client win with a name attached:

- If the client explicitly permitted you to use their name, use it. Note permission status in the Notes section.
- If the client gave stats but not their name, blur the name or use "Anonymous." Note the permission scope.
- If you never asked, default to anonymized. Crop or blur identifying details. Do not guess at permission.

The `> [!warning] Usage rules` callout in the proof entry is where anonymization state lives. If the callout is missing, default to treating the proof as restricted until verified.

## Reuse ethics

Reusing the same screenshot across multiple videos is fine and normal. It's not deceptive. It's showing proof that held up over time. Viewers aren't auditing whether a given screenshot has appeared before. What matters is that the proof is real and the permissions are sound.

## Dig deeper probes (use when the proof is thin)

When the creator says "I've helped lots of people":
- "Give me one specific person and one specific result."
- "Do you have a screenshot of that? Where is it?"

When the asset is vague:
- "Where is this file? If we don't have the asset, we don't have the proof."
- "Can you pull it up right now?"

When the claim is inflated:
- "What's the exact number, not a range?"
- "What's the timeline that number happened over?"

## Common mistakes

- **Storing proof only in memory.** If it's not in a file, it's not proof.
- **Unreadable screenshots.** Crop and zoom so the key fact is obvious at a glance.
- **Proof ahead of framework.** Viewer doesn't know what's being proved.
- **Claiming results without permission.** Anonymize when in doubt.
- **Losing track of asset paths.** If the `asset_path` field is wrong, the proof is effectively gone.
