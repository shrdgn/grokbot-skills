---
name: Sales Outbound
category: Sales
description: Hand off research and outbound. Researches accounts overnight, scores contacts with intent, drafts email and LinkedIn in your voice, and leaves a review list for you to approve.
connectors: [Salesforce, LinkedIn, enrichment tool, Gmail, sequencer]
approval_required: true
suggested_routine: Nightly; review each morning
---

# Sales Outbound

Does the overnight legwork of outbound — research, scoring, and drafting personalized
first touches in your voice — and leaves a review queue you approve before anything sends.

## Inputs
- Target contacts/accounts (e.g. from Prospecting Plan Builder).
- Your voice/examples, messaging pillars, and sequence structure.
- Intent signals to weigh.

## Steps
1. Overnight, research each account/contact and gather personalization hooks.
2. Score contacts by fit + intent; prioritize the list.
3. Draft a personalized email and LinkedIn message per contact in your voice.
4. Skip contacts already in sequence or opted out.
5. Assemble a morning review queue with the drafts and the hook behind each.

## Decision rules
- Personalization must be specific and true — cite the hook; never fabricate.
- Honor DNC/consent and per-contact frequency caps.
- Low-confidence personalization → flag rather than send generic filler.

## Definition of done
- A review queue of prioritized contacts, each with an email + LinkedIn draft and its
  personalization rationale, ready for your approval.

## Safety & approvals
- **Nothing sends without your approval.** The Bot drafts and queues only.
- Respects consent, DNC, and privacy rules; no gated-data scraping.

## Suggested routine
- Runs nightly; you approve/edit the queue each morning.
