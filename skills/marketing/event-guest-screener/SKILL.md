---
name: Event Guest Screener
category: Marketing
description: Fill the room with the right people. Scores event applicants against your ICP and batch-approves strong fits in the invite tool.
connectors: [Event/invite tool, enrichment tool, Google Sheets]
approval_required: true
suggested_routine: On new applications + daily batch
---

# Event Guest Screener

Screens event registrations against your ICP so the room is full of the right people,
and prepares batch approvals for your sign-off.

## Inputs
- Applicant list from the invite/event tool.
- ICP / guest criteria and capacity.
- Enrichment source for title, company, seniority.

## Steps
1. Enrich each applicant (company, role, seniority, fit signals).
2. Score against ICP criteria.
3. Sort into strong fit / maybe / weak fit with reasons.
4. Prepare a batch of strong fits for approval; hold "maybes" for review.
5. On approval, mark approvals in the invite tool.

## Decision rules
- Score on defined criteria; borderline → "maybe", never auto-declined silently.
- Respect capacity; if oversubscribed, rank by fit.

## Definition of done
- Scored, sorted applicant list; approved strong fits actioned in the invite tool after
  your confirmation; maybes queued for review.

## Safety & approvals
- **Approvals/declines require your confirmation** before the tool is updated.
- Handles applicant data per privacy rules.

## Suggested routine
- Triggered on new applications, with a daily batch review.
