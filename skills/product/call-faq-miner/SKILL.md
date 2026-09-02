---
name: Call FAQ Miner
category: Product
description: Keep enablement current from real calls. Tracks recurring questions, timestamps answers, and links back to the source recording.
connectors: [Gong, Zoom, knowledge base, Google Drive]
approval_required: true
suggested_routine: Weekly
---

# Call FAQ Miner

Mines customer and sales calls for the questions that keep coming up, capturing the
best answer and a link to the source, so enablement/FAQ content stays current and real.

## Inputs
- Recorded calls + transcripts.
- Existing FAQ/enablement library.

## Steps
1. Scan recent call transcripts for questions asked.
2. Cluster recurring questions across calls; count frequency.
3. Capture the best answer given, with a timestamp and recording link.
4. Diff against the existing FAQ; draft new/updated entries for the gaps.

## Decision rules
- Prioritize by frequency and by whether the current answer was strong.
- Every proposed FAQ answer cites a real call moment; no invented answers.

## Definition of done
- A ranked list of recurring questions with sourced answers and drafted FAQ additions/
  updates, ready for review.

## Safety & approvals
- **FAQ/library updates await approval** before publishing.
- Answers are grounded in real calls; uncertain ones flagged for an SME.

## Suggested routine
- Weekly mining pass over recent calls.
