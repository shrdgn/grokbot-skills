# Grok Bot Skills

A directory of reusable **Grok Bot skills** — each a repeatable task recipe a Bot can
run on demand or on a routine. Skills mirror xAI's official *Ways to use Grok Bot*
catalog (all 56 use cases) and are written in one consistent format.

A skill is a recipe: it captures the **inputs**, **steps**, **decision rules**, the
**definition of done** (expected output), and the **safety boundaries** for a task, so a
Bot finds the skill, runs it, and verifies the result instead of improvising each time.
Reference a saved skill with `/` in the composer; attach it to a **routine** to run on a
schedule or trigger.

## Format

Every skill lives at `skills/<category>/<skill-name>/SKILL.md` with this shape:

```
---
name: <Skill name>
category: <Category>
description: <One line — what it does / when to use it>
connectors: [<tools the Bot needs>]
approval_required: <true|false>
suggested_routine: <schedule or trigger>
---
# <Skill name>
## Inputs · Steps · Decision rules · Definition of done · Safety & approvals · Suggested routine
```

See [`_TEMPLATE.md`](_TEMPLATE.md) to add a new one.

## Catalog — 56 skills across 9 categories

| Category | # | Skills |
|----------|---|--------|
| [General](general/) | 6 | Chief of Staff · Daily Briefing Writer · Executive Assistant · Inbox Manager · Presentation Designer · Status Report Writer |
| [Sales](sales/) | 10 | Account Research Specialist · CRM Operations Manager · Deal Desk Coordinator · Deck Updater · Meeting Prep Buddy · Pipeline Analyst · Prospecting Plan Builder · Renewal Desk Operator · Sales Call Coach · Sales Outbound |
| [Marketing](marketing/) | 13 | Community Operations Manager · Compelling Events Monitor · Competitive Intelligence Analyst · Event Guest Screener · Internal Communications Manager · LinkedIn Campaign Manager · Marketing Calendar Owner · Merch Fulfillment Operator · Newsletter Writer · Paid Media · Paid Media Creative Strategist · SEO / AEO Auditor · Social Media Manager |
| [Customer Success & Support](customer-success-support/) | 4 | Account Health · Account Manager · Enablement Fulfillment Specialist · Ticket Triage Specialist |
| [Recruiting & People](recruiting-people/) | 4 | Calendar Coordinator · Hiring Screener · Onboarding Manager · Talent Scout |
| [Operations & Finance](operations-finance/) | 5 | Contract Desk · Expense Manager · Invoice Coordinator · Security Questionnaire Filler · Vendor Portal Operator |
| [Product](product/) | 5 | Beta Adoption Watcher · Call FAQ Miner · Docs Auditor · Feature Request Tracker · Product Feedback Analyst |
| [Engineering](engineering/) | 5 | Bug Reproduction · Cloud Agent Orchestrator · Playtest Operator · Product Performance · Prototype Builder |
| [Life & Leverage](life-leverage/) | 4 | Apartment Scout · Personal Site Builder · Subscription Cleaner · Travel Coordinator |

## Conventions

- **Approval-first.** Any skill that sends, posts, pays, or writes to an external system
  drafts and holds for human approval unless you explicitly widen its scope.
- **Cite sources.** Outputs that summarize or research name where each item came from.
- **Stay quiet when clean.** Monitoring skills report only when there's something to act on.
- **No invented data.** Skills mark gaps (`[NEEDS INPUT]`, `[TBD]`) instead of guessing.
