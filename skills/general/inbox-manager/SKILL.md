---
name: Inbox Manager
category: General
description: Keep email usable. Triages your inbox into clear categories, surfaces urgent and blocked threads, and drafts replies and cleanup — every send stays behind your approval.
connectors: [Gmail]
approval_required: true
suggested_routine: Every 2 hours during work hours
---

# Inbox Manager

Keeps your inbox triaged and moving: categorizes mail, flags what's urgent or blocked
on you, and prepares replies you approve before anything sends.

## Inputs
- Your Gmail account and label scheme (or let the Bot propose one).
- Your reply voice/examples and any standard responses.
- VIP senders and topics that are always urgent.

## Steps
1. Scan new mail since last run; classify: Urgent, Needs reply, Waiting on others,
   FYI, Newsletter/Promo, Auto/Noise.
2. Apply labels; propose archive/mute for clear noise.
3. For threads needing a reply, draft a response in your voice as a Gmail draft.
4. Flag threads blocked on someone else with a suggested nudge.
5. Summarize: what's urgent, what you drafted, what to clean up.

## Decision rules
- VIP senders and flagged topics always sort to Urgent.
- Draft, never send. Uncertain classification → leave in inbox, don't archive.
- Never draft replies on legal, HR, or financial threads without flagging for care.

## Definition of done
- Inbox labeled; drafts saved (not sent); a summary listing urgent items, drafts ready
  for review, and proposed cleanup actions awaiting your approval.

## Safety & approvals
- **Every send and every bulk archive/delete requires your explicit approval.**
- Never auto-unsubscribe or move money-related mail without confirmation.

## Suggested routine
- A few times a day during work hours; a light end-of-day pass.
