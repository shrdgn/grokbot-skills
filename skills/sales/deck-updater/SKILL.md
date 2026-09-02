---
name: Deck Updater
category: Sales
description: Leave the room with the slide already moving. Updates your deck from discovery notes mid-call or right after, with next steps baked in.
connectors: [Google Slides or PowerPoint, meeting-notes source, Google Drive]
approval_required: false
suggested_routine: During/after discovery calls
---

# Deck Updater

Keeps a deal's deck current with what you just learned — updating discovery findings,
tailoring value slides, and baking in next steps — so follow-up is instant.

## Inputs
- The account's working deck.
- Live or post-call discovery notes/transcript.
- Your slide template and messaging library.

## Steps
1. Read the discovery notes for pains, goals, stakeholders, timeline, objections.
2. Update the deck: tailor problem/value slides to their words, refresh the tailored
   use case, and add a next-steps/mutual-plan slide.
3. Keep everything on-template and on-brand.
4. Return the updated deck link and a summary of what changed.

## Decision rules
- Use the customer's own language for pains and goals.
- Don't remove approved content; add/tailor. Mark assumptions `[CONFIRM]`.

## Definition of done
- Updated deck link reflecting discovery, with a next-steps slide and a change summary.

## Safety & approvals
- Produces a draft; does not send to the customer.
- Flags any claim it couldn't ground in the notes.

## Suggested routine
- Mid-call where supported, or immediately after each discovery/demo.
