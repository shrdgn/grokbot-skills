---
name: plg-metrics
description: Instrument growth with the right metrics tree. Use when defining or auditing growth metrics, building a dashboard, diagnosing where growth is breaking, or setting up AARRR / PLG flywheel / North Star + input-lever tracking. Distinguishes value metrics from vanity metrics.
---

# PLG & Growth Metrics

Diagnose *where* growth breaks, then instrument the *engine* that fixes it. Use two
complementary frameworks: **AARRR** to find the leak, the **PLG flywheel** to design
the loop, and a **North Star + input levers** tree to steer day to day.

## 1. AARRR — Pirate Metrics (diagnosis)

Five stages; measure conversion between each to find the biggest leak.

| Stage | Question | Example metric |
|-------|----------|----------------|
| **Acquisition** | Do people arrive? | new signups, traffic → signup % |
| **Activation** | Do they reach first value? | % reaching the aha event, time-to-value |
| **Retention** | Do they come back? | Dn/Wn retention, cohort curves |
| **Revenue** | Do they pay / expand? | conversion to paid, NRR, ARPU |
| **Referral** | Do they bring others? | k-factor, % who invite |

**Use it to prioritize:** the stage with the steepest drop-off relative to benchmark
is usually the highest-leverage place to work. Retention leaks are worth fixing
*before* pouring more into acquisition — a leaky bucket wastes acquisition spend.

## 2. The PLG flywheel (design)

Once AARRR shows the leak, design a self-reinforcing loop:

`Evaluate (try) → Activate (first value) → Adopt (habit) → Expand (more seats/usage)
→ Advocate (invite/refer) → feeds new Evaluate`

Each stage should push energy into the next with as little manual GTM friction as
possible. The flywheel is the loop; AARRR is the measurement grid laid over it.

## 3. North Star + input metrics tree (steering)

- **North Star Metric (output of value):** one behavioral metric that captures
  delivered value and predicts revenue (see `growth-strategy`).
- **Input metrics (levers):** 3–5 metrics teams directly own that *sum/multiply* into
  the NSM. Each maps to a team and a roadmap.
- **Guardrail metrics:** things you must not break while pushing inputs (e.g. latency,
  refund rate, unsubscribe rate).

Example tree for "weekly active projects":
```
North Star: Weekly Active Projects
├─ new projects created / week      (activation team)
├─ project reactivation rate        (lifecycle team)
├─ collaborators added per project  (virality team)
└─ project retention D30            (retention team)
Guardrails: p95 load time, support tickets/project
```

## 4. Value vs. vanity

A metric is **vanity** if it can go up while the business gets no healthier.

| Prefer (value) | Over (vanity) |
|----------------|---------------|
| activation rate, time-to-value | total signups |
| cohort retention, NRR | cumulative registered users |
| revenue per active user | total pageviews |
| paid conversion, payback period | app downloads |

## 5. Metric ownership

A metric with no owner is a report, not a lever. Assign each input metric to a team so
a drop *triggers action*, not just a note in a dashboard. When product, sales, and
finance each track different siloed numbers, the metrics stop driving decisions.

## Checklist

- [ ] AARRR mapped with conversion % between each stage; biggest leak identified.
- [ ] One North Star Metric, behavioral and value-capturing.
- [ ] 3–5 input levers, each with a named owning team.
- [ ] Guardrail metrics defined so you don't win one number by breaking another.
- [ ] Every metric on the dashboard is value, not vanity — or explicitly labeled.

## Common traps

- Optimizing acquisition while retention leaks (filling a leaky bucket).
- A North Star that's actually revenue (a lagging output, not a steerable value signal).
- Too many "north stars" — teams pull in different directions.
- Dashboards full of totals (cumulative signups) that only ever go up.

## Sources
- Appcues — [Product-Led Growth Metrics](https://www.appcues.com/blog/product-led-growth-metrics)
- Insight Partners — [Measuring your PLG strategy](https://www.insightpartners.com/ideas/measuring-your-product-led-growth-strategy/)
- [North Star Metric Framework (PLG)](https://umbrex.com/resources/frameworks/marketing-frameworks/north-star-metric-framework-product-led-growth/)
