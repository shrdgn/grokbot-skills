---
name: Travel Coordinator
category: Life & Leverage
description: Hold the best option before it expires. Compares flights and hotels to your rules, confirms before booking, and drops itinerary plus calendar.
connectors: [Travel sites, Gmail, Google Calendar, browser/computer use]
approval_required: true
suggested_routine: On trip request
---

# Travel Coordinator

Plans a trip to your preferences — comparing flights and hotels against your rules and
holding the best option — then books only after you confirm and delivers the itinerary.

## Inputs
- Trip details: dates, origin/destination, budget, and your travel rules (airlines,
  seat/cabin, hotel class, loyalty programs).

## Steps
1. Search flights and hotels matching dates and rules.
2. Rank options by fit (price, timing, preferences); shortlist the best.
3. Where possible, hold the top option before it expires.
4. Present the shortlist; on your confirmation, book.
5. Deliver the itinerary and add flights/hotel/transfers to your calendar.

## Decision rules
- Rank by your stated rules, not just lowest price.
- Hold, don't purchase, before confirmation; flag anything nonrefundable.

## Definition of done
- A ranked shortlist (held where possible); on approval, booked; itinerary delivered and
  calendar populated with confirmation numbers.

## Safety & approvals
- **No purchase without your explicit confirmation.**
- Nonrefundable/high-cost choices flagged before booking; payment details handled securely.

## Suggested routine
- Triggered on a trip request; monitors held fares until you decide.
