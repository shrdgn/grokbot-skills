---
name: activation-onboarding
description: Get new users to first value fast. Use when designing or fixing onboarding, defining an activation event / "aha moment", reducing time-to-value, or diagnosing signup-to-activation drop-off. Covers the activation path, setup moment vs. aha moment, and friction removal.
---

# Activation & Onboarding

Activation is where most funnels break: people sign up and never reach value.
This skill maps the path from signup to the **aha moment** and removes friction at
each step. Activation, not acquisition, is usually the highest-leverage fix.

## 1. Define the aha moment (the activation event)

The **aha moment** is the point where a user first experiences core value — sending a
first message, publishing a first project, seeing a first insight. It is a *behavior*,
not a page view.

Find it empirically:
- Compare retained vs. churned cohorts. Look for an early action strongly correlated
  with long-term retention.
- Classic method: find the "magic number" (e.g. Facebook's *7 friends in 10 days*,
  Slack's *2,000 messages sent*, Dropbox's *put one file in one folder on one device*).
- Validate it's causal-ish: users who hit it retain far better, and it's reachable in
  the first session or two.

## 2. Setup moment vs. aha moment

Separate two events:
- **Setup moment** — the config a user must complete to be *able* to get value (connect
  a data source, invite a teammate, import contacts).
- **Aha moment** — actually experiencing the value.

The onboarding job is to get users through **setup** to **aha** with minimum effort.
Every required setup step is a chance to drop off, so ruthlessly cut or defer them.

## 3. Time-to-value (TTV)

TTV = time from signup to the activation event. Lower is better. Track median (not
mean) and the % who reach activation within the first session / 24h / 7d.

Levers to compress TTV:
- **Remove steps** — defer anything not needed for first value.
- **Do work for the user** — pre-fill, templates, sample data, smart defaults.
- **Guide** — checklists, progress bars, empty states that show the next action.
- **Deliver value before asking for commitment** — show the aha *before* forcing
  signup/payment where possible ("reverse trial", demo mode).

## 4. Map the activation path

Write out each required step from landing → aha, and instrument drop-off at every one:
```
Land → Sign up → Verify → Setup step 1 → Setup step 2 → First value (AHA) → Habit
        │          │        │             │              │
      %drop      %drop     %drop         %drop         %drop
```
Attack the single steepest drop first. Small friction (an email verification wall, a
required credit card, a blank empty state) often causes the biggest leaks.

## 5. Onboarding patterns that work

- **Personalize by source & intent** — branch onboarding on how they signed up and
  their stated goal; matched onboarding can lift conversion dramatically.
- **Templates & sample data** — an empty product has no value; seed it.
- **Progressive disclosure** — teach one thing at a time, tied to the next real action.
- **Early win** — engineer a small success in the first session.
- **Trigger the next session** — a welcome sequence (3–5 emails over 7–14 days) that
  pulls users back to the aha if they didn't reach it (see `retention-lifecycle`).

## Checklist

- [ ] Aha moment defined as a specific behavioral event, validated against retention.
- [ ] Setup steps separated from the aha; every non-essential step deferred or removed.
- [ ] Activation path instrumented step-by-step; steepest drop identified.
- [ ] Median TTV tracked and being actively compressed.
- [ ] Empty states seeded (templates/sample data), onboarding personalized by intent.
- [ ] Welcome sequence recovers users who didn't activate in session one.

## Common traps

- Defining activation as "signed up" or "completed tour" instead of first *value*.
- Front-loading setup (credit card, long forms) before the user sees any value.
- A generic one-size onboarding when signup source predicts very different goals.
- Optimizing acquisition while activation quietly leaks 60%+.

## Sources
- Appcues — [Product-Led Growth Metrics (activation, TTV)](https://www.appcues.com/blog/product-led-growth-metrics)
- ProductLed — [PLG strategy playbook](https://productled.com/blog/product-led-growth-strategy-playbook)
- Chameleon — [Product-Led Growth principles](https://www.chameleon.io/blog/product-led-growth-planning)
