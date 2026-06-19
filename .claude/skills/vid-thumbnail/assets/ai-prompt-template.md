# AI Image Prompt Template

Scaffold for generating thumbnails when `creation_path: ai-workflow`. Fill every slot. The output goes into the brief's "AI prompt" code block, ready to paste into Midjourney, Flux, Gemini Imagen, DALL-E, or whichever tool the creator uses.

## The slots (every prompt fills these)

```
Editorial YouTube thumbnail, 1280x720, 16:9.

Subject: {age range, gender if specified, brief description from foundation/packaging-system.md or asked of creator if missing}

Expression: {one of the allowed expressions from packaging-system "expression_rules". Describe the actual face: eyes, mouth, brow, gaze direction. Avoid theatrical descriptors. "Surprised, eyes wide, mouth slightly open, genuine 'what happened' not exaggerated" beats "shocked face."}

Framing: {hero face position (e.g. "shoulders-up, occupies left two-thirds of frame"). If hybrid, name the object's position explicitly.}

Object element (if hybrid): {what the object is, where it sits, any motion/state cue. E.g. "torn organizational chart card mid-air, edges frayed, slight motion blur"}

Background: {color in hex from packaging-system palette, lighting style, vignette/gradient direction}

Lighting: {key light direction, rim light if applicable, mood. E.g. "Cream rim-light from upper-right edges his hair and shoulder"}

Color palette enforcement: {hex codes for the 2-3 committed colors, where each lives in the frame}

Negative space: {explicit statement reserving space for text overlay. E.g. "Negative space on right third reserved for text overlay" or "Lower third clean for typography"}

Style: {photo-real | illustrated | stylized}, match packaging-system aesthetic, sharp focus on {subject focal point}, color-graded for YouTube CTR.

Do not render text in the image. Leave clean negative space at {position} for typography in post.
```

## Tool-specific dialect notes

- **Midjourney v6+**: append `--ar 16:9 --style raw --v 6` at the end. Use `--cref {creator face URL}` if face identity lock is configured.
- **Flux**: append nothing special; Flux respects natural language well. For face identity, use IP-Adapter or LoRA reference if the creator has one trained.
- **Gemini Imagen**: skip the `--ar` flag; Gemini accepts ratio in the prompt. Strong on photo-real faces but weaker on negative-space text reservation. Emphasize "leave room for text" twice if needed.
- **DALL-E 3**: rephrase as natural sentences, no `--flags`. DALL-E sometimes ignores negative space. Explicitly say "the right third must be background only, no subject elements."

## Face identity lock

If the creator has a face identity reference (trained LoRA, IP-Adapter image, character ref tag):
- Add: `Face identity: lock to creator's reference {ref-id-or-url}.`
- Note in the brief: "Identity-lock requires the creator's tool config. Replace `{ref}` with their actual reference."

If no identity lock available:
- Note in brief: "No identity lock configured. Expect the AI to generate a generic face. The creator will need to inpaint their own face in post, or skip AI for hero shots."

## Style anchors from packaging-bank (when available)

If `banks/packaging-bank/` has entries with `source: own` (creator's own past winners):
- Reference 1-2 of them by slug: `Style anchor: see {slug-of-past-winner.md}. Match the {specific element: lighting / background treatment / object framing}.`

If only outliers exist (no own winners yet):
- Reference 1 outlier: `Aesthetic reference: see {outlier-slug.md}. Borrow the {framing / palette / mood}, NOT the subject or text.`

If bank is empty:
- Note in brief: "Packaging-bank empty (fresh creator). Prompt leans on guardrails only. Log a winner post-publish to feed future runs."

## What the AI WON'T do well (set creator expectations)

The creator should expect 4-8 iterations on these elements:
- **Expression authenticity.** Surprise/focus on the line between honest and theatrical
- **Object placement and physics.** Floating, mid-action, or interacting elements often need re-rolls
- **Text rendering.** DON'T let the AI render text. Always leave negative space and add text in post (Photoshop / Canva / Figma).
- **Hand details.** If hands are in frame, expect oddities. Crop tighter or hide hands if possible.

If 8 or more iterations doesn't land, the prompt is wrong, not the tool. Come back and revise the brief.

## Example (filled-in for "Hiring Broke My Business")

```
Editorial YouTube thumbnail, 1280x720, 16:9.

Subject: Solo male founder, mid-30s.

Expression: Surprised, eyes wide, mouth slightly open, genuine "what happened" not exaggerated. Looking just off-camera-right.

Framing: Hero face occupies left two-thirds, shoulders-up.

Object element: Torn organizational chart card mid-air, edges frayed, slight motion blur. Positioned just to the right of his shoulder.

Background: Deep navy (#1a2540), subtle vignette darker at corners.

Lighting: Cream rim-light from upper-right edges his hair and shoulder. Key light soft from front-right.

Color palette enforcement: Navy (#1a2540) background, cream (#f5ede0) rim-light, coral (#ff6b5b) on the cracked-object accent only.

Negative space: Right third of frame reserved for text overlay.

Style: Photo-real, sharp focus on face, shallow depth on background. Color-graded for YouTube CTR.

Do not render text in the image. Leave clean negative space on the right for typography in post.

--ar 16:9 --style raw --v 6
```
