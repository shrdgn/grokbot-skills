---
name: Beta Adoption Watcher
category: Product
description: See who's actually trying the new feature. Monitors usage and surfaces which customers are in, so the team can follow up.
connectors: [Product analytics, Salesforce, Slack]
approval_required: false
suggested_routine: Daily during a beta
---

# Beta Adoption Watcher

Tracks who is actually using a new/beta feature and surfaces the accounts and users
adopting (or not) so the team can follow up while interest is fresh.

## Inputs
- The feature's usage events in analytics.
- The beta cohort and any target accounts.
- CRM to attach usage to accounts/owners.

## Steps
1. Pull usage of the feature since last run.
2. Map users → accounts → owners via CRM.
3. Identify who's in (active), who tried once, and who hasn't touched it.
4. Surface notable adopters and stalled accounts to the owning team.

## Decision rules
- Distinguish real usage from a single incidental event.
- Highlight target accounts prominently; flag drop-off after first use.

## Definition of done
- A daily adoption read-out: active adopters, one-and-done users, and non-starters —
  each tied to an account and owner for follow-up.

## Safety & approvals
- Reports only; contacts no customers and changes no records.

## Suggested routine
- Daily through the beta window.
