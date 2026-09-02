---
name: Executive Assistant
category: General
description: Stay oriented without living in channels. Delivers a morning briefing plus an automatic catch-up summary whenever you join a new room, so you're never lost in a thread you just entered.
connectors: [Slack, Microsoft Teams, Google Calendar, Gmail]
approval_required: false
suggested_routine: Daily 8:00 AM + on "joined new channel/thread"
---

# Executive Assistant

Keeps you oriented: a morning briefing of the day ahead, and an instant catch-up
whenever you're added to a new room so you can contribute without scrolling.

## Inputs
- Connected messaging + calendar.
- Your role/context (to judge what matters when you join a room).

## Steps
1. **Morning:** summarize today's calendar, prep needs, and any overnight threads
   awaiting you.
2. **On join:** when you're added to a channel/thread, read its recent history.
3. Produce a catch-up: purpose of the room, key decisions so far, open questions,
   who's asking what of whom, and where (if anywhere) you're expected to weigh in.
4. Deliver privately to you.

## Decision rules
- Catch-up length scales with thread size; keep it to what you need to participate.
- Surface any direct asks of you at the top.
- Don't summarize rooms you've marked private/excluded.

## Definition of done
- Morning briefing delivered; and for each new room joined, a private catch-up with
  purpose, decisions, open items, and your expected role.

## Safety & approvals
- Read-only. Never posts in the room or replies on your behalf.
- Catch-ups go only to you, never back into the channel.

## Suggested routine
- Morning briefing daily; catch-up triggered automatically on room join.
