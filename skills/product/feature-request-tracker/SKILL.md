---
name: Feature Request Tracker
category: Product
description: Never lose "who asked for this." Mines Slack and calls into a living list tied to customers, so the spec has a real demand trail.
connectors: [Slack, Gong, Salesforce, Notion/Linear/Jira]
approval_required: false
suggested_routine: Daily
---

# Feature Request Tracker

Captures every feature request from calls and channels into one living, deduplicated
list tied to the customers who asked — so prioritization has a real demand trail.

## Inputs
- Sources of requests: Slack, call transcripts, tickets, emails.
- CRM to attach requests to accounts (and revenue/tier).
- The tracker/board where requests live.

## Steps
1. Scan sources for feature requests and pain points.
2. Normalize and dedupe against existing tracker items.
3. Attach each mention to the requesting customer (with account/ARR/tier).
4. Update demand counts and add new items with source links.

## Decision rules
- Merge duplicates into one item; keep the full requester trail.
- Distinguish a real request from a passing comment; cite the source.

## Definition of done
- A current tracker where each item carries a deduped list of requesting customers,
  demand count, and source links — a defensible demand trail.

## Safety & approvals
- Maintains the list; doesn't reprioritize the roadmap or reply to customers.

## Suggested routine
- Daily ingestion from all sources.
