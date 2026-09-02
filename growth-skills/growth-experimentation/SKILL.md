---
name: growth-experimentation
description: Run trustworthy growth experiments end to end. Use when writing a hypothesis, prioritizing an experiment backlog (ICE/RICE), designing an A/B test, calculating sample size, judging statistical significance, or avoiding peeking and other analysis traps. Covers the experiment loop, prioritization, and statistics.
---

# Growth Experimentation

The growth engine runs on a fast loop of trustworthy experiments. What separates real
experimentation from guesswork: a testable hypothesis, isolated variables, adequate
sample size, and honest reading of significance.

## 1. The experiment loop

`Analyze → Ideate → Prioritize → Test → Analyze results → Systematize`

Run it on a regular cadence (e.g. weekly). Volume of *good* experiments, not any single
test, is what compounds. Aim to increase throughput while keeping rigor.

## 2. Write a real hypothesis

Not "let's try a green button." Use:

> **Because** [evidence/insight], **we believe** [change] **will cause** [metric] to
> [move by ~X%] **for** [segment]. **We'll know** when [result threshold].

A good hypothesis is specific, falsifiable, tied to a metric, and grounded in evidence
(data, user research, a funnel leak) — not a random idea.

## 3. Prioritize the backlog: ICE / RICE

**ICE** — score each idea 1–10 on:
- **Impact** — how much it moves the target metric if it works.
- **Confidence** — how sure you are it will (evidence-backed, not hope).
- **Ease** — how cheap/fast to build and run.

Score = `Impact × Confidence × Ease`. Start with the highest. ICE is fast but
subjective — keep the scoring honest, ideally with more than one scorer.

**RICE** adds **Reach** (how many users affected per period) and divides by **Effort**:
`(Reach × Impact × Confidence) / Effort`. Use RICE when reach varies widely across ideas.

## 4. Design the test

- **One variable at a time** (or a properly designed multivariate test) so you can
  attribute the result.
- **Define the primary metric before launch** — plus guardrail metrics you must not
  harm (revenue, latency, unsubscribes). No switching the metric after seeing data.
- **Randomize** properly and check the split is balanced.
- **Decide direction and MDE up front** — the minimum detectable effect you care about.

## 5. Sample size & significance (the part people get wrong)

- **Compute sample size *before* launch** from baseline conversion rate, your MDE, and
  desired power/significance. Use a calculator (Optimizely, VWO, Evan Miller). An
  underpowered test can't detect a real effect and wastes the traffic.
- **Significance threshold** — standard is **95%** confidence (**p < 0.05**): under 5%
  probability the difference is chance. Significance ≠ importance — a tiny, significant
  lift may not be worth shipping.
- **No peeking** — do **not** stop the moment it looks significant. Repeatedly checking
  and stopping early massively inflates false positives. Fix the sample size / duration
  in advance and wait, or use a method built for sequential testing.
- **Run full business cycles** — at least one, ideally two full weeks, to average out
  day-of-week and other cyclical behavior. Never end mid-cycle.
- **Watch power** — aim for ~80% power so you don't miss real effects (false negatives).

## 6. Analyze honestly

- Report effect size **with a confidence interval**, not just "significant/not".
- **Segment** results (new vs. returning, device, channel) — but treat surprise segment
  wins as *new hypotheses*, not conclusions (multiple-comparisons risk).
- A **flat or losing** result is a valid, valuable outcome — it saves you from shipping
  a dud. Record it.
- **Systematize wins** — bank the learning, roll winners out, and feed insights back
  into the next round of ideas.

## Checklist

- [ ] Hypothesis is specific, falsifiable, evidence-backed, tied to a metric + segment.
- [ ] Backlog prioritized with ICE/RICE; working top-down.
- [ ] One variable isolated; primary + guardrail metrics fixed before launch.
- [ ] Sample size and duration computed up front from baseline, MDE, 95%/80% power.
- [ ] No-peeking rule enforced; runs ≥ 1–2 full weeks / business cycles.
- [ ] Results reported with effect size + CI; wins and losses both banked.

## Common traps

- Calling a test at 95% after 2 days (peeking → false positive).
- Underpowered tests that can never detect the effect you care about.
- Changing the success metric after seeing the data.
- Ending mid-week and missing weekly cyclicality.
- Treating a post-hoc segment win as a validated result.
- Running many low-confidence tweaks instead of fewer high-ICE bets.

## Sources
- Aakash Gupta — [A/B Testing Best Practices](https://www.aakashg.com/a-b-testing-best-practices/)
- CXL — [Growth experiments vs. optimization vs. A/B testing](https://cxl.com/blog/growth-experiments-vs-optimization/)
- Quantum Metric — [A/B Testing Methodology](https://www.quantummetric.com/blog/ab-testing-methodology)
