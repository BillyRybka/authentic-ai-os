---
type: reference
scope: vid-bank
loaded_by: [vid-bank]
status: active
tags: [reference, testimonial-capture, proof-bank]
---

# Testimonial Capture Guide

A testimonial is captured client voice. Not the creator narrating what a client achieved (that's a story). Not a number on a dashboard (that's proof). A testimonial is the client's own words, preserved verbatim, with a source and a date.

This guide teaches how testimonials work. vid-bank's Stage T uses it to log testimonials that already exist. Where testimonials land once a script pulls them lives in [[proof-placement-rules]].

Soliciting new testimonials from clients is outside this skill's scope.

## Real examples (read these first)

### Example 1: DM testimonial

A client messages the creator on Instagram after watching a video: "Hey, I tried the photo-swap thing you mentioned last week. My listing got booked three times since Monday. First time I've had that in months, thank you."

- Source: `dm`
- Client: "[[Client Name]]" (with their permission) or "Anonymous"
- Verbatim: preserve the message exactly as sent, including the casual phrasing
- Placement in script: after the creator teaches the photo-swap fix, drop this message on screen

### Example 2: YouTube comment testimonial

A public YouTube comment on a video: "Ok I didn't think this would work but I made the change you said and literally booked a call 2 hours later. wtf thank you."

- Source: `comment`
- Client: "Anonymous" (it's a public comment, not everyone wants their handle blown up)
- Verbatim: preserve lowercase, swearing, typos, all of it. The authenticity is the point.
- Placement in script: multiple of these scrolled through as a "wall of wins" moment

### Example 3: Email testimonial with permission

A client emails the creator three months into working together: "Billy, hit $50K this month. Last year I was at $8K. Everything we built in the first session is still running. Still can't believe it."

- Source: `email`
- Client: "[[Client Name]]" (with explicit written permission to use full name)
- Verbatim: exact wording
- Placement in script: as a single anchor testimonial after a big claim about the method

## The 4 sources

Pick the source first. This drives the `source:` field and the way the testimonial is rendered in the script.

### `comment`

Public YouTube comment, Instagram comment, blog comment. Public by default. The creator can screenshot without asking (it's already public). If the commenter wants their handle hidden, anonymize.

### `dm`

Direct message on any platform. Private by default. Do NOT share without the client's permission. If permission is granted, use the full name. If not, anonymize heavily.

### `email`

Email reply from a client. Private by default. Same permission rules as DM.

### `video`

A video clip or voice note from a client saying the testimonial out loud. Strongest format because viewers can hear the client's voice. Requires explicit permission before use.

## Verbatim is non-negotiable

Do NOT paraphrase the client's words. Do NOT clean up grammar. Do NOT remove profanity unless the creator specifically needs a family-friendly version. The authenticity is what makes a testimonial land.

If a testimonial has a typo, keep the typo. If a sentence is weird, keep it weird. The client's actual voice is the point.

The only edit allowed is trimming for length. If a testimonial is three paragraphs and the relevant part is one sentence, pull out the one sentence and note the trim in the Context section.

## Anonymization rules

Before capturing:

- Has the client given explicit permission to use their full name? Use the name.
- Has the client given permission to use just their first name or initials? Use what they allowed.
- Is this from a public comment? Use the handle if the handle is already public, consider "Anonymous" if blowing it up feels off.
- Private message with no explicit permission? Anonymize. Use "Anonymous" in `client:` and set `anonymized: true`.

When in doubt, anonymize. Ask later.

Note the permission status in the Anonymization section of the body. Future Claude needs to know what's allowed.

## Where testimonials land in a script

Testimonials fit in the same slot as proof (right after a framework), with two differences:

1. **Rendering on screen.** Testimonials are usually shown as a chat screenshot, email capture, or comment screenshot. The viewer sees the original source.
2. **One strong testimonial or many weak testimonials.** Either use one anchor quote that packs a punch, or stack 10 short ones for a "wall of wins" effect. The middle zone (2-3 testimonials) doesn't hit as hard as one or ten.

## Dig deeper probes (use when the testimonial context is thin)

When the creator doesn't remember when the testimonial came in:
- "Roughly when? A month? Six months? We need `captured` to be accurate."

When the creator isn't sure about permission:
- "Did the client ever say it was okay to use publicly? If not, we default to anonymize."

When the testimonial is too long:
- "What's the single sentence that matters most? We can trim."

## Common mistakes

- **Paraphrasing.** Kills the authenticity.
- **Editing grammar.** Also kills authenticity.
- **Losing the source.** A testimonial without a `source` field is a claim, not proof.
- **Assuming permission.** Default to anonymous when you can't verify.
- **Forgetting the date.** `captured` field lives in frontmatter. Fill it.

## Scope note

vid-bank captures testimonials that already exist in the creator's comments, DMs, emails, or video clips. Writing request emails to ask clients for testimonials is a separate workflow outside vid-bank's scope.
