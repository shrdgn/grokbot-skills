---
name: Prospecting Plan Builder
category: Sales
description: Build the week's book of work. Seeds contacts, enriches email/mobile, and writes a ready-to-work tracker so outbound starts from a list.
connectors: [Salesforce, LinkedIn, enrichment tool, Google Sheets]
approval_required: false
suggested_routine: Weekly, Sunday evening or Monday 6:00 AM
---

# Prospecting Plan Builder

Builds a ready-to-work prospecting list each week — the right contacts at the right
accounts, enriched with contact info — so outbound starts immediately.

## Inputs
- Target accounts/segment and ICP persona(s).
- Weekly volume target and any exclusion rules (already-in-sequence, do-not-contact).

## Steps
1. From target accounts, identify contacts matching the ICP persona(s).
2. Enrich with verified email/mobile; drop unverifiable or opted-out records.
3. Deduplicate against existing sequences, open opps, and DNC lists.
4. Prioritize by fit and any intent signals.
5. Write the tracker: contact, account, why-now, suggested first touch.

## Decision rules
- Only include contacts matching persona + not excluded.
- Verified contact data only; mark low-confidence emails.
- Respect DNC and regional consent rules.

## Definition of done
- A tracker of the week's prospects, enriched and prioritized, ready to work, with
  duplicates and excluded contacts removed.

## Safety & approvals
- Builds the list; does not send outbound (see Sales Outbound for drafting).
- Honors consent/DNC and privacy rules.

## Suggested routine
- Weekly before the sprint starts.
