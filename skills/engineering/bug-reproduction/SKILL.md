---
name: Bug Reproduction
category: Engineering
description: Give engineers reports they can trust. Catches the thread, clicks the same path in staging, captures the failure, and drops a repro pack — steps, screenshots, network notes.
connectors: [Slack, browser/computer use, issue tracker, staging env]
approval_required: false
suggested_routine: On bug report
---

# Bug Reproduction

Turns a vague bug report into a trustworthy repro pack — reproducing the issue in
staging and capturing exactly what happened — so engineers debug instead of guessing.

## Inputs
- The bug report/thread and any user-provided details.
- Staging/test environment access and safe test credentials.

## Steps
1. Read the report; extract the claimed steps, environment, and expected vs. actual.
2. Reproduce the path in staging using computer use.
3. Capture evidence: exact steps, screenshots, console/network errors, timestamps.
4. Note whether it reproduces, intermittently, or not — with conditions.
5. Attach the repro pack to the issue.

## Decision rules
- Only mark "reproduced" with captured evidence; otherwise say "could not reproduce"
  and list what was tried.
- Reproduce in staging/test only — never production.

## Definition of done
- A repro pack on the issue: steps, environment, screenshots, network/console notes,
  and a clear reproduced / intermittent / not-reproduced verdict.

## Safety & approvals
- Uses non-production environments and safe test accounts only.
- Never runs destructive actions or touches real customer data.

## Suggested routine
- Triggered when a bug is filed or flagged in Slack.
