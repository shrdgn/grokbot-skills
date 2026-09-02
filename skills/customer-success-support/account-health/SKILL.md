---
name: Account Health
category: Customer Success & Support
description: See risk and expansion before the QBR. Reads usage and signals across your book and turns portfolio noise into a clear watch list.
connectors: [Product usage/analytics, Salesforce, support/tickets, Gong]
approval_required: false
suggested_routine: Weekly Monday + before QBRs
---

# Account Health

Scores the health of every account in your book from real usage and signals, and
surfaces a ranked watch list of risk and expansion — ahead of the QBR, not after.

## Inputs
- Product usage/analytics, support history, CRM, and call sentiment.
- Health-scoring criteria and expansion triggers.

## Steps
1. Pull usage trend, support load, sentiment, and engagement per account.
2. Compute a health score (green/yellow/red) with the drivers behind it.
3. Detect risk signals (usage decline, unresolved escalations, low engagement).
4. Detect expansion signals (limit hits, new teams, high adoption).
5. Rank into a watch list: at-risk first, then expansion opportunities.

## Decision rules
- Score on defined criteria; each rating names its top drivers.
- Separate risk from expansion; flag accounts that are both.

## Definition of done
- A ranked watch list with health score, key drivers, and a suggested next action per
  account, ready before QBRs.

## Safety & approvals
- Analysis only; contacts no customers and changes no records.

## Suggested routine
- Weekly, and a deeper pass before each QBR cycle.
