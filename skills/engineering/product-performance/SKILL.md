---
name: Product Performance
category: Engineering
description: Get a clear view of the metrics that matter. Logs into observability tools, walks the flamegraphs, and comes back with hotspots plus a short writeup with screenshots.
connectors: [Observability (Datadog/Grafana/etc.), APM, Slack]
approval_required: false
suggested_routine: Weekly + on regression alert
---

# Product Performance

Reads your observability data, walks the traces and flamegraphs, and reports the real
performance hotspots — with evidence — so optimization targets the right code.

## Inputs
- Observability/APM access and the services/endpoints in scope.
- Baselines/SLOs and the time window.

## Steps
1. Pull latency, error, and throughput metrics for the window.
2. Compare to baseline/SLOs; find regressions and outliers.
3. Walk traces/flamegraphs to locate hotspots and their likely cause.
4. Write up findings with screenshots and a suggested next step per hotspot.

## Decision rules
- Prioritize by user impact (latency × traffic) and SLO breach.
- Distinguish a real regression from normal variance; cite the data.

## Definition of done
- A short performance report: ranked hotspots with flamegraph/trace screenshots,
  likely cause, and a suggested action for each.

## Safety & approvals
- Read-only analysis; changes no code or config.

## Suggested routine
- Weekly review; immediate look on a regression alert.
