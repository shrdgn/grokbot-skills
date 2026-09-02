---
name: referral-viral-loops
description: Design referral programs and viral loops and model their math. Use when building a referral/invite feature, estimating virality, computing k-factor and viral cycle time, or diagnosing why a referral program isn't compounding. Covers loop types, k-factor, cycle time, and incentive design.
---

# Referral & Viral Loops

Virality is a growth *loop*, not a growth *hack*: existing users produce new users who
produce more users. The loop compounds only when the math and the moment are right.

## 1. Viral vs. word-of-mouth vs. referral

- **Inherent virality** — using the product exposes non-users to it (a shared doc, an
  email signature, a "sent via" badge). No incentive needed.
- **Word of mouth** — users tell others because the product is good. Not engineered,
  but you can create shareable moments.
- **Referral program** — an explicit, often incentivized invite mechanic. Engineered
  and measurable.

The strongest loops are inherent (built into core usage). Incentivized referral is a
lever on top, not a substitute for a product worth sharing.

## 2. The viral loop, step by step

```
User reaches a value/sharing moment
  → is prompted to invite (low friction)
  → sends N invitations
  → invitations convert at rate C
  → new users activate and reach their own sharing moment → loop repeats
```

Every step is a multiplier and a leak. The loop is only as strong as its weakest step.

## 3. The math: k-factor and cycle time

**k-factor** = `invites sent per user (i) × conversion rate per invite (c)`.

- **k > 1** → self-sustaining exponential growth (each user brings more than one, who
  each bring more than one). Rare and powerful.
- **k < 1** → not self-sustaining, but still a *multiplier* on other channels: an
  amplification factor of `1 / (1 − k)`. E.g. k = 0.5 means every 100 acquired become
  ~200 total. That's hugely valuable even below 1.

**Viral cycle time (CT)** = time for one full loop (invite → new user invites). Shorter
CT compounds far faster than a higher k. Halving cycle time can beat doubling k over
the same period — so optimize *speed to the sharing moment*, not just invite counts.

Levers:
- Raise **i** — invite at the right moment, make it one-tap, allow bulk/contacts import.
- Raise **c** — social proof, clear value to the invitee, low-friction landing/signup,
  a reason to accept *now*.
- Shorten **CT** — move the invite prompt earlier (near the aha), speed invitee activation.

## 4. Incentive design

- **Double-sided incentives** (reward both referrer and invitee — the Dropbox/PayPal
  model) usually beat one-sided: they give the referrer a *generous* reason to share
  and the invitee a reason to accept.
- **Match the reward to the product's value** (more storage, credit, a free month) so it
  reinforces usage rather than attracting reward-hunters.
- **Trigger the ask at a success moment** — right after the user got value, not at
  signup. Asks land far better post-aha.
- **Guard against fraud/abuse** — self-referrals, fake accounts; incentives invite gaming.

## 5. Instrument it

Track, per cohort: invites sent per user, invite→signup conversion, invited-user
*activation and retention* (referred users are often higher quality — or lower, if
you're bribing), k-factor, and cycle time. A referral program that drives signups but
not *activated, retained* users is a cost center, not a loop.

## Checklist

- [ ] Is there an inherent-virality path built into core usage, not just an incentive?
- [ ] Invite prompt fires at/after the aha moment, one-tap, low friction.
- [ ] k-factor and viral cycle time measured per cohort.
- [ ] Optimizing cycle time (speed), not only invite volume.
- [ ] Incentives double-sided and tied to product value.
- [ ] Referred users tracked for activation/retention, not just signup.
- [ ] Fraud/abuse guardrails in place.

## Common traps

- Bolting on a referral incentive to a product nobody wants to share.
- Asking for the invite at signup, before the user has experienced value.
- Chasing k-factor while ignoring cycle time (the faster compounding lever).
- Counting invited *signups* while referred users never activate.
- One-sided incentives that give the invitee no reason to accept.

## Sources
- Reforge — [Growth loops (viral loops)](https://www.reforge.com/blog/growth-loops)
- Elena Verna — [Favorite growth frameworks (referral loops)](https://www.elenaverna.com/p/my-9-favorite-growth-frameworks)
- ReferralCandy — [Lifecycle & referral integration](https://www.referralcandy.com/blog/lifecycle-email-marketing-ecommerce-the-2026-complete-guide-to-maximizing-customer-value)
