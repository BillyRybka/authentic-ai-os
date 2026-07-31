---
name: Format Index
type: skill-local-reference
loaded_by: vid-framing
when_to_read: Stage 6, when setting the format
---

# Format index

Pick the format the framing implies, then sanity-check it against the video's goal. This index is only for choosing. The full body shape for each one lives in `knowledge/format-planners/{format}.md`, which vid-structure loads later. Scores are Views / Sales / Trust, out of 5.

| Format | What it is | V / S / T | Best for |
|---|---|---|---|
| `short-process` | A quick-fire process to one specific result, 10 to 20 min | 4 / 4 / 4 | The reliable workhorse. A simple, valuable transformation with the deep theory cut. |
| `case-study` | One person's transformation told as a story | 5 / 5 / 5 | Sales and trust. Proof the method works on someone like the viewer. |
| `deep-dive` | Discredit the old way at length, prove a new one | 4 / 5 / 5 | The most profitable format. Belief-shifting with proof woven through. |
| `roast` | Review a few audience submissions (call it a review, never a roast) | 2 / 5 / 5 | Sales and trust. Low reach, elite conversion. |
| `listicle` | A set of points that do not connect step by step | 3 / 3 / 3 | The flexible middle ground. A batch of distinct lessons. |
| `news` | A fast reaction to something that just happened | 5 / 1 / 2 | Reach and speed. Decays fast, weak on sales. |
| `interview` | A guest conversation | 4 / 1 / 2 | Reach, not revenue. Borrowed authority. |

## How to pick

1. **The framing usually implies the format.** A client transformation is a case study. A reaction to a launch is news. A "here is my process" is short-process. A set of disconnected tips is a listicle. A framing that spends real time discrediting the old way before building anything is a deep-dive.
2. **Then check it against the goal.** With a sales or trust goal, lean toward the high S/T formats: case-study, deep-dive, roast. With a views goal, the high V formats earn their place: news, case-study, deep-dive, interview.
3. **Lock one of the seven.** Every value here matches a planner on disk, and vid-structure builds on it, so never lock a format that has no planner.

## Where these numbers come from

Verified against the source on 2026-07-28. These seven rows are a faithful transcription of the source author's spoken scoring, and `knowledge/format-planners/{format}.md` was corrected to match this table rather than the other way round. If a future audit finds a planner disagreeing with this table, this table is right.

Two things to hold alongside them.

**They are tendencies, not predictions.** The source says so directly: the ranking is a general overview, low-scoring formats do sometimes blow up, and it is on the creator to test. A channel's own results overrule this table every time.

**There is no Emails column, and inventing one would be fabrication.** The source scores Views, Sales and Trust only. `goal: emails` is a real option in this system with no column to check against, so when the goal is emails, reason from the Sales and Trust scores, because the formats that convert also collect. Say plainly that the table does not score it.

For anyone reconciling this against the source directly: the source's written course descriptions disagree with the spoken transcript on three formats. This table follows the transcript, and each of the three was also checked on merit rather than provenance alone. They agree.

- **Short Process, Views 4 rather than 5.** Straight fours are the format's whole signature, good at everything and best at nothing, which is what makes it the weekly workhorse. Scoring its reach level with News and Case Study would say the dependable format is also the ceiling format, and it is not.
- **News, Sales 1 rather than 2.** The standing instruction for this format is to route out to an evergreen video, and that instruction only makes sense if the news video itself sells nothing. Somebody watching a reaction to a feature drop is not in a buying posture, so the 1 is the routing rule written as a number.
- **Interview, Sales 1 rather than 2.** The source's own case data settles it: one sale off a 350k-view interview, because the credibility went to the guest.
