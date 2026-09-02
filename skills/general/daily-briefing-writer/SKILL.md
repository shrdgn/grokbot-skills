---
name: Daily Briefing Writer
category: General
description: Start the day with high-quality inputs instead of noise. Delivers a tight daily brief of only the stories that matter to you.
connectors: [Web/News, X, RSS, Slack or Gmail (delivery)]
approval_required: false
suggested_routine: Daily 6:30 AM
---

# Daily Briefing Writer

Delivers a short, curated brief of the news and updates relevant to your interests and
work — signal only, no filler.

## Inputs
- Your topics, companies, and people to track (watchlist).
- Preferred sources and any sources to exclude.
- Length target (default: 5–8 items).

## Steps
1. Gather items published since the last brief across your sources and watchlist.
2. Cluster duplicates covering the same event into one entry.
3. Score each cluster on relevance to your watchlist and materiality.
4. Keep the top N; write a one-line "why it matters" for each.
5. Order by importance and deliver.

## Decision rules
- Prefer primary sources; note when something is rumor or unconfirmed.
- Skip pure repetition of yesterday's brief unless there's a real development.
- No editorializing beyond a short, factual "why it matters".

## Definition of done
- A dated brief with N items, each: headline, one-line why-it-matters, source link.
  Delivered to your chosen channel.

## Safety & approvals
- Summarize and link; never fabricate quotes, numbers, or sources.
- If confidence is low on a claim, label it clearly.

## Suggested routine
- Every morning before work; optional midday update for fast-moving topics.
