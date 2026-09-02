---
name: Subscription Cleaner
category: Life & Leverage
description: Cut the noise you forgot about. Collates receipt and newsletter mail, suggests what to kill, and unsubscribes what you approve.
connectors: [Gmail, browser/computer use]
approval_required: true
suggested_routine: Monthly
---

# Subscription Cleaner

Finds the recurring subscriptions and newsletters cluttering your inbox and wallet,
recommends what to cut, and unsubscribes/cancels only what you approve.

## Inputs
- Your email inbox (receipts, renewals, newsletters).
- Optional: what you want to keep no matter what.

## Steps
1. Scan mail for recurring charges and newsletter subscriptions.
2. Estimate cost and last-used/last-opened signals per item.
3. Recommend keep / cancel / unsubscribe with a reason each.
4. On your approval, unsubscribe from newsletters and start cancellations.
5. Report what was actioned and any that need manual follow-up.

## Decision rules
- Recommend cancel for unused/forgotten items; never assume — you decide.
- Distinguish "unsubscribe" (free) from "cancel" (money) and treat cancellations carefully.

## Definition of done
- A categorized list with cost and usage signals and a recommendation each; approved
  unsubscribes/cancellations actioned; a report of results and manual follow-ups.

## Safety & approvals
- **Cancellations and unsubscribes happen only on your approval**, item by item for
  anything involving money.
- Never cancels anything you marked keep.

## Suggested routine
- Monthly cleanup; ad-hoc before renewals.
