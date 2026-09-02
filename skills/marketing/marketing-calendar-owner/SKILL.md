---
name: Marketing Calendar Owner
category: Marketing
description: Keep regional and global content, launch, and events calendars in sync. Pulls from Notion and keeps webinars and campaigns current without a weekly chase.
connectors: [Notion, Google Calendar, Google Sheets, Slack]
approval_required: false
suggested_routine: Daily sync + weekly digest
---

# Marketing Calendar Owner

Keeps every marketing calendar — content, launches, events, webinars, regional and
global — in one synced, current view, without the weekly manual chase.

## Inputs
- Source calendars/boards (Notion, sheets, event tools).
- Regions/teams to reconcile and any dependencies.

## Steps
1. Pull items from all sources; normalize dates, owners, and status.
2. Reconcile regional vs. global; detect conflicts, gaps, and stale entries.
3. Update the master calendar; flag collisions (two launches same day, empty weeks).
4. Post a weekly digest: what's shipping, what's at risk, what needs an owner/date.

## Decision rules
- Never silently overwrite an owner's entry — flag conflicts for resolution.
- Missing owner or date → flagged, not guessed.

## Definition of done
- A synced master calendar and a weekly digest of upcoming items, conflicts, and gaps.

## Safety & approvals
- Syncs and flags; doesn't cancel or reschedule others' items without confirmation.

## Suggested routine
- Daily sync; weekly digest ahead of planning.
