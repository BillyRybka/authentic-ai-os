<!--
TEMPLATE: ending block written into Content/pieces/{slug}/script.md by vid-ending.

The skill reads this template at lock time, fills the bracketed slots with the locked content, and writes the filled block into script.md (replacing any existing close). Single # heading marks the close so editors and reviewers can find it without scanning.

Bracketed slots get filled. No tables, no callouts, no extra prose. the block is filming-ready spoken content with stage marks for the editor.
-->

## Ending

<!-- PIVOT -->
{Pivot sentence, one sentence recap of the transformation in the creator's voice}

<!-- GAP -->
{Gap sentence, one sentence revealing the new problem, drawn from creator-foundation Top 3}

<!-- CTA (only present if goal=sales or goal=emails. Skip block entirely if goal=views.) -->
{Sales pitch OR lead-magnet pointer, single sentence, voice-matched}

<!-- BRIDGE -->
{Bridge sentence, confident, names or implies the next video, end-screen card lands here}

<!-- END SCREEN CARD CUE -->
[END SCREEN: {{next-video-slug}}, card animates in during the Bridge sentence]

<!--
Frontmatter update written to Content/pieces/{slug}/piece.md alongside this block:

ending_locked: true
next_video: "[[{{next-video-slug}}]]"
cta_shape: sales | emails | views
ending_be_pattern: BE-N
ending_voice_pressure_test:
  date: YYYY-MM-DD
  result: pass | soft-warn | soft-reject
  read_aloud_confirmed: true | false
last_refreshed: YYYY-MM-DD
-->
