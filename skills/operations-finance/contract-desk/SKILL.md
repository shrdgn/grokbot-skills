---
name: Contract Desk
category: Operations & Finance
description: See the week of paper at a glance. Summarizes contracts by stage and owner, pulls key terms, and flags blocked reviews.
connectors: [CLM/contract tool, Google Drive, DocuSign, Slack]
approval_required: false
suggested_routine: Daily 8:00 AM + weekly digest
---

# Contract Desk

Gives you a single view of every contract in flight — by stage and owner, with key
terms extracted and blockers flagged — so nothing stalls silently.

## Inputs
- Contract repository / CLM and signature tool.
- Stage definitions and SLA/turnaround targets.

## Steps
1. Pull all in-flight contracts; group by stage and owner.
2. Extract key terms (value, dates, renewal, nonstandard clauses).
3. Flag blocked/overdue reviews and missing signatures against SLA.
4. Produce the at-a-glance view and a weekly digest.

## Decision rules
- Flag anything past its review SLA or missing an owner.
- Surface nonstandard terms prominently; never interpret legal language as advice.

## Definition of done
- A stage/owner view of all contracts with key terms and a ranked list of blocked or
  overdue items; weekly digest delivered.

## Safety & approvals
- Reads and reports; signs and edits nothing.
- Extracted terms are for triage, not legal interpretation — flags for counsel.

## Suggested routine
- Daily status; weekly digest for the paper pipeline.
