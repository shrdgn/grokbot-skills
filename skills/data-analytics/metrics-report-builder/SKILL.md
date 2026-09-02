---
name: Metrics Report Builder
category: Data & Analytics
description: Turn raw data into a recurring metrics report that explains movement, not just numbers. Use for a weekly/monthly KPI digest with drivers, anomalies, and plain-language takeaways.
connectors: [Google Sheets, BigQuery/warehouse, analytics tool, Slack]
approval_required: false
suggested_routine: Weekly Monday 7:00 AM
---

# Metrics Report Builder

Turns your data sources into a recurring KPI report that says what moved, by how much,
and *why* — so readers get insight, not a spreadsheet dump.

## Inputs
- The metrics/KPIs to report and their data sources.
- The period and comparison basis (WoW, MoM, vs. target).
- Segments/dimensions that usually explain movement.

## Steps
1. Pull each KPI for the period and its comparison window.
2. Compute deltas vs. prior period and vs. target.
3. Attribute notable moves to segments/drivers where the data supports it.
4. Flag anomalies (unusual spikes/drops) and possible data-quality issues.
5. Write the report: headline takeaways, KPI table, drivers, anomalies, watch-items.

## Decision rules
- Lead with takeaways; put the table below.
- Only claim a driver when the data supports it; otherwise say "unexplained".
- Distinguish a real move from normal variance; flag suspected data issues, don't bury them.

## Definition of done
- A dated report: plain-language takeaways, KPI table with deltas vs. prior/target,
  attributed drivers, anomalies, and watch-items — delivered to your channel.

## Safety & approvals
- Reports only; changes no data or dashboards.
- Never fabricates a number or a cause; marks gaps and low confidence.

## Suggested routine
- Weekly or monthly on cadence; on demand before reviews.
