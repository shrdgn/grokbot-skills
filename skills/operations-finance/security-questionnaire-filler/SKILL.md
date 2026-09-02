---
name: Security Questionnaire Filler
category: Operations & Finance
description: Speed through vendor security portals. Logs into the questionnaire site, pulls answers from your trust center and past RFPs, drafts every field, and parks the submit for you.
connectors: [Trust center/knowledge base, past RFP library, Google Drive, browser]
approval_required: true
suggested_routine: On request
---

# Security Questionnaire Filler

Drafts vendor security questionnaires by pulling from your approved answer library and
past responses — filling every field — then parks the submission for human sign-off.

## Inputs
- The questionnaire (portal or file).
- Your trust center / approved security answer library and past RFPs.

## Steps
1. Read all questions in the questionnaire/portal.
2. Match each to an approved answer from the library/past RFPs.
3. Draft every field; mark any question with no approved answer as `[NEEDS SECURITY]`.
4. Assemble the completed draft and park the submit for review.

## Decision rules
- Use only approved, sourced answers; never invent a security claim.
- Any gap or changed control → flag for the security team, don't guess.

## Definition of done
- Every field drafted from approved sources, gaps clearly flagged, submission staged
  for human review — not submitted.

## Safety & approvals
- **Never submits** — a human reviews and submits.
- Only approved security statements are used; unknowns escalate.

## Suggested routine
- On each incoming questionnaire request.
