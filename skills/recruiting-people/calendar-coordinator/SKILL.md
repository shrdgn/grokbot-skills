---
name: Calendar Coordinator
category: Recruiting & People
description: Get people in the same room. Schedules across calendars and chases the holds nobody else has time to chase.
connectors: [Google Calendar, Gmail, scheduling tool]
approval_required: true
suggested_routine: On scheduling request + daily chase
---

# Calendar Coordinator

Finds times across everyone's calendars, sends the invites, and chases the outstanding
holds and confirmations so interviews and meetings actually land.

## Inputs
- Participants and their calendars (or availability).
- Duration, time-zone constraints, and any ordering (e.g. interview loop sequence).

## Steps
1. Find mutual availability across all participants and constraints.
2. Propose the best options; on selection, draft invites with agenda/details.
3. Send invites (on approval) and track RSVPs.
4. Chase non-responders and re-hold when someone declines.
5. Confirm the final schedule to all.

## Decision rules
- Respect time zones, working hours, and any required interview order.
- Re-book proactively when a decline breaks the plan.

## Definition of done
- Confirmed meeting(s) on all calendars with agenda, or a shortlist of options when a
  conflict needs a human decision; holds chased to resolution.

## Safety & approvals
- **Invites sent after approval** (or within a pre-agreed auto-send scope).
- Doesn't move others' existing meetings without confirmation.

## Suggested routine
- On each scheduling request, with a daily chase for open holds.
