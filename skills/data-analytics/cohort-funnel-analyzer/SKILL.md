---
name: Cohort & Funnel Analyzer
category: Data & Analytics
description: Find where users drop off and which cohorts retain. Use to build retention curves and funnel breakdowns from event data and get a plain-language read on where to focus.
connectors: [Product analytics, BigQuery/warehouse, Google Sheets]
approval_required: false
suggested_routine: On demand + monthly
---

# Cohort & Funnel Analyzer

Builds retention curves and funnel breakdowns from your event data and returns a
plain-language read of where users drop and which cohorts stick — so effort goes to the
biggest leak.

## Inputs
- The funnel steps and/or the activation + retention events.
- Cohort dimension (signup week, plan, channel) and the window.
- Event source/tables.

## Steps
1. **Funnel:** compute step-to-step conversion; find the steepest drop.
2. **Cohorts:** build retention curves by cohort; check whether they flatten (retention
   PMF) or decay to zero.
3. Segment to see which cohorts/paths retain or convert better.
4. Summarize: biggest drop, best/worst cohorts, and where to focus, in plain language.

## Decision rules
- Define "active" as a real value event, not just app-open; state it.
- Match the retention window to natural usage frequency.
- Separate a genuine trend from small-sample noise; note cohort sizes.

## Definition of done
- Funnel conversion by step (with the steepest drop called out), cohort retention curves
  with a flatten/decay read, segment comparisons, and a focus recommendation.

## Safety & approvals
- Analysis only; changes nothing.
- Notes definitions and sample sizes; no overclaiming on thin data.

## Suggested routine
- On demand for a specific funnel; monthly retention review.
