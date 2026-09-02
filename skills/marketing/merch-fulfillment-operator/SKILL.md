---
name: Merch Fulfillment Operator
category: Marketing
description: Send merch to the right prospects. Runs outreach, watches the redemption form, pings you to approve/reject each submission in chat, and sends your swag vendor a daily order form.
connectors: [Gmail, redemption form/sheet, Slack, swag vendor]
approval_required: true
suggested_routine: Daily
---

# Merch Fulfillment Operator

Runs a swag/merch campaign end to end — outreach, redemption intake, per-submission
approval, and a daily consolidated order to your vendor — so the right people get merch.

## Inputs
- Target recipient list and outreach copy.
- Redemption form and shipping fields.
- Vendor order format and approval rules (e.g. value caps, eligible titles).

## Steps
1. Run/track outreach with the redemption link.
2. Watch the form for new submissions; validate address and eligibility.
3. Ping you in chat to approve/reject each submission with the key details.
4. Compile approved orders into the vendor's daily order form and send it.
5. Log status per recipient.

## Decision rules
- Validate shipping details before ordering; flag incomplete ones.
- Enforce eligibility/value caps; borderline → ask.

## Definition of done
- Approved submissions compiled into the daily vendor order and sent; per-recipient
  status logged; rejected/incomplete ones flagged.

## Safety & approvals
- **Each submission approved by you before it enters an order.**
- Vendor order sent only after the daily batch is confirmed.

## Suggested routine
- Daily order cutoff; approvals handled in chat through the day.
