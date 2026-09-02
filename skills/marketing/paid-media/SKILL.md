---
name: Paid Media
category: Marketing
description: Pulls live channel and campaign data, Slacks a recommended budget reallocation against your monthly plan, and holds for your approval before making adjustments.
connectors: [Ad platforms (Google, Meta, LinkedIn), Google Sheets, Slack]
approval_required: true
suggested_routine: Daily 9:00 AM
---

# Paid Media

Monitors paid performance across channels and recommends budget reallocations against
your plan — surfacing them for approval, never moving spend on its own.

## Inputs
- Connected ad accounts and the monthly budget/plan.
- Efficiency targets (CPA/ROAS) and guardrails (min/max per channel).

## Steps
1. Pull yesterday's + month-to-date spend and performance by channel/campaign.
2. Compare to plan and efficiency targets; find over/under-performers.
3. Draft a reallocation recommendation with expected impact and rationale.
4. Post it to Slack for approval; on approval, apply within agreed guardrails.

## Decision rules
- Recommend within guardrails; anything beyond them is flagged, not auto-applied.
- Every recommendation shows the data and expected effect.
- Don't overreact to one-day noise; weigh the trend.

## Definition of done
- A daily performance read-out and a specific, bounded reallocation recommendation
  posted for approval; applied only after you confirm.

## Safety & approvals
- **No budget or bid change without approval.** The Bot recommends and waits.
- Hard guardrails on max spend shifts.

## Suggested routine
- Every morning; ad-hoc when a campaign spikes or stalls.
