---
name: Cloud Agent Orchestrator
category: Engineering
description: Keep many cloud agent runs moving without babysitting each one. Kicks off runs, monitors, chases what's stuck, and summarizes the report.
connectors: [CI/agent platform, GitHub, Slack]
approval_required: true
suggested_routine: On demand + monitor active runs
---

# Cloud Agent Orchestrator

Manages a fleet of cloud/agent runs — launching, monitoring, unsticking, and
summarizing — so you get outcomes without watching each one.

## Inputs
- The runs/jobs to launch (or a queue) and their configs.
- Success criteria and what counts as "stuck".

## Steps
1. Kick off the specified runs with their configs.
2. Monitor status; detect stuck, failed, or waiting-on-input runs.
3. Retry transient failures within policy; escalate real blockers.
4. When all complete, summarize results, failures, and follow-ups.

## Decision rules
- Retry only clearly transient failures, up to the set limit; don't mask real bugs.
- Escalate anything needing a human decision instead of forcing it.

## Definition of done
- All runs driven to completion or a clear blocked state, with a summary of outcomes,
  failures, and recommended next actions.

## Safety & approvals
- **Actions with side effects (deploys, merges, spend) require approval.**
- Respects concurrency/cost limits; surfaces cost implications.

## Suggested routine
- On demand to launch a batch; continuous monitoring of active runs.
