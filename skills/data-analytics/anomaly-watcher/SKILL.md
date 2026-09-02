---
name: Anomaly Watcher
category: Data & Analytics
description: Catch metric anomalies before they become fire drills. Use to monitor key metrics on a cadence and alert — with likely causes — only when something is genuinely off.
connectors: [BigQuery/warehouse, analytics tool, Slack]
approval_required: false
suggested_routine: Daily (or hourly for critical metrics)
---

# Anomaly Watcher

Monitors your key metrics on a cadence and alerts only when a value is genuinely
anomalous — with context and a likely cause — so you hear about problems early, not at
the review.

## Inputs
- The metrics to watch and their data sources.
- Expected ranges/seasonality and alert thresholds (or let it learn a baseline).
- Where to alert and who owns each metric.

## Steps
1. Pull each watched metric for the latest period.
2. Compare against baseline/seasonality; compute how unusual the value is.
3. For a real anomaly, break it down by segment to localize the cause.
4. Alert the owner with the metric, the deviation, the likely driver, and a chart.
5. Stay silent when everything is within range.

## Decision rules
- Alert only on statistically meaningful deviations — account for seasonality/weekends.
- Suppress duplicate alerts for an ongoing, already-flagged anomaly.
- Distinguish a data-pipeline break from a real business move; label which.

## Definition of done
- Timely alerts on genuine anomalies (metric, deviation, localized driver, chart) to the
  owner; no noise when metrics are normal.

## Safety & approvals
- Detects and alerts; takes no corrective action itself.
- Flags suspected data-quality issues rather than treating them as business signal.

## Suggested routine
- Daily for most metrics; hourly for revenue/uptime-critical ones.
