---
type: skill-reference
skill: vid-structure
format: interview
purpose: the body plan for an interview
---

# Interview

The questions are the body. Each one is planned to pull a story first, then the insight. The host writes the prompts; the guest's answers are not planned, they are elicited.

## The body

```
## Q1: {question}
## Q2: {question}
...
## QN: {question}
```

- Package first. The title and thumbnail are locked before recording, and every question serves one of the viewer's top three questions raised by that package. A question that serves none is a cut.
- Every question forces a story. "What was the moment you realised..." not "tell me about your business." The planner's strong and weak shapes are the test.
- Plan for the edit. A forty-five minute recording becomes ten. Fewer, sharper questions beat coverage.

## What each section locks

Every field is a label line with its beats under it. Question and Serves are one line. Target story and Target insight carry what the host already knows, beat by beat.

Every question, before recording:

- **Question:** the host's exact wording, shaped to open on a moment.
- **Target story:** the real episode this question is meant to elicit, from the pre-call or the guest's public material, with the beats the host already knows and the ones to dig for. `to elicit in recording` on the label when the host knows the territory but not the episode. That is valid material for this format, not a hole.
- **Target insight:** what the audience needs the answer to make clear. The principle the edit will keep.
- **Serves:** which of the viewer's three questions this one answers.

After recording, when a transcript exists: replace targets with exact transcript spans or clips, and cut any question whose answer did not land. Never script words for the guest.

`vid-segment` writes only the host's framing line, the question, and follow-up prompts for a pre-recording plan. It never drafts the guest's answer.

## Where the payoff lands

The question whose answer delivers the title's promise, usually two thirds of the way through. The thread is the through-line the host weaves from question to question. A guest who keeps returning to their own story has handed you a second thread; let it play.

## Do not

- plan a question with no story target
- plan a yes or no question
- assert what the guest will say
- plan a product pitch; this format does not convert to sales
- lead the package with a non-famous guest's name

## Example

Title: "The man making YouTubers rich for free"

```markdown
## Q1: The month two anchor clients left at once
**Question:** "Walk me through the month you lost both anchor clients. What did the next Monday look like?"
**Target story:** pre-call, 09:15
- two clients churned in the same month, about 40 percent of revenue
- she did not replace them; she raised the price on the next three pitches instead
- dig for: the Monday morning itself, what she told the team
**Target insight:**
- the loss was the signal they were underpriced
- replacing revenue at the old price would have locked the problem in
**Serves:** viewer question 2, "what did they actually do?"

## Q2: The pitch after that
**Question:** "What did you charge on the very next pitch, and what were you charging before?"
**Target story:** to elicit in recording
- the host knows the raise was around sixty percent, not the pitch itself
- dig for: the number, the client's reaction, whether it closed
**Target insight:**
- the exact mechanics of raising price after a loss, so the viewer can copy the move
**Serves:** viewer question 3, "could I do this?"
```
