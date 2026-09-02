# Grok Bot Skills

A directory of reusable **Grok Bot skills** — each a repeatable task recipe a Bot can
run on demand or on a routine. Skills mirror xAI's official *Ways to use Grok Bot*
catalog (all 56 use cases) plus original creative, research, and data extensions — all
in one consistent format.

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

## Catalog — 74 skills across 12 categories

Each skill below links to its `SKILL.md`. See the [root README](../README.md) for
one-line descriptions.

**From xAI's official *Ways to use Grok Bot* catalog (56):**

### General (6)
[Chief of Staff](general/chief-of-staff/SKILL.md) · [Daily Briefing Writer](general/daily-briefing-writer/SKILL.md) · [Executive Assistant](general/executive-assistant/SKILL.md) · [Inbox Manager](general/inbox-manager/SKILL.md) · [Presentation Designer](general/presentation-designer/SKILL.md) · [Status Report Writer](general/status-report-writer/SKILL.md)

### Sales (10)
[Account Research Specialist](sales/account-research-specialist/SKILL.md) · [CRM Operations Manager](sales/crm-operations-manager/SKILL.md) · [Deal Desk Coordinator](sales/deal-desk-coordinator/SKILL.md) · [Deck Updater](sales/deck-updater/SKILL.md) · [Meeting Prep Buddy](sales/meeting-prep-buddy/SKILL.md) · [Pipeline Analyst](sales/pipeline-analyst/SKILL.md) · [Prospecting Plan Builder](sales/prospecting-plan-builder/SKILL.md) · [Renewal Desk Operator](sales/renewal-desk-operator/SKILL.md) · [Sales Call Coach](sales/sales-call-coach/SKILL.md) · [Sales Outbound](sales/sales-outbound/SKILL.md)

### Marketing (13)
[Community Operations Manager](marketing/community-operations-manager/SKILL.md) · [Compelling Events Monitor](marketing/compelling-events-monitor/SKILL.md) · [Competitive Intelligence Analyst](marketing/competitive-intelligence-analyst/SKILL.md) · [Event Guest Screener](marketing/event-guest-screener/SKILL.md) · [Internal Communications Manager](marketing/internal-communications-manager/SKILL.md) · [LinkedIn Campaign Manager](marketing/linkedin-campaign-manager/SKILL.md) · [Marketing Calendar Owner](marketing/marketing-calendar-owner/SKILL.md) · [Merch Fulfillment Operator](marketing/merch-fulfillment-operator/SKILL.md) · [Newsletter Writer](marketing/newsletter-writer/SKILL.md) · [Paid Media](marketing/paid-media/SKILL.md) · [Paid Media Creative Strategist](marketing/paid-media-creative-strategist/SKILL.md) · [SEO / AEO Auditor](marketing/seo-aeo-auditor/SKILL.md) · [Social Media Manager](marketing/social-media-manager/SKILL.md)

### Customer Success & Support (4)
[Account Health](customer-success-support/account-health/SKILL.md) · [Account Manager](customer-success-support/account-manager/SKILL.md) · [Enablement Fulfillment Specialist](customer-success-support/enablement-fulfillment-specialist/SKILL.md) · [Ticket Triage Specialist](customer-success-support/ticket-triage-specialist/SKILL.md)

### Recruiting & People (4)
[Calendar Coordinator](recruiting-people/calendar-coordinator/SKILL.md) · [Hiring Screener](recruiting-people/hiring-screener/SKILL.md) · [Onboarding Manager](recruiting-people/onboarding-manager/SKILL.md) · [Talent Scout](recruiting-people/talent-scout/SKILL.md)

### Operations & Finance (5)
[Contract Desk](operations-finance/contract-desk/SKILL.md) · [Expense Manager](operations-finance/expense-manager/SKILL.md) · [Invoice Coordinator](operations-finance/invoice-coordinator/SKILL.md) · [Security Questionnaire Filler](operations-finance/security-questionnaire-filler/SKILL.md) · [Vendor Portal Operator](operations-finance/vendor-portal-operator/SKILL.md)

### Product (5)
[Beta Adoption Watcher](product/beta-adoption-watcher/SKILL.md) · [Call FAQ Miner](product/call-faq-miner/SKILL.md) · [Docs Auditor](product/docs-auditor/SKILL.md) · [Feature Request Tracker](product/feature-request-tracker/SKILL.md) · [Product Feedback Analyst](product/product-feedback-analyst/SKILL.md)

### Engineering (5)
[Bug Reproduction](engineering/bug-reproduction/SKILL.md) · [Cloud Agent Orchestrator](engineering/cloud-agent-orchestrator/SKILL.md) · [Playtest Operator](engineering/playtest-operator/SKILL.md) · [Product Performance](engineering/product-performance/SKILL.md) · [Prototype Builder](engineering/prototype-builder/SKILL.md)

### Life & Leverage (4)
[Apartment Scout](life-leverage/apartment-scout/SKILL.md) · [Personal Site Builder](life-leverage/personal-site-builder/SKILL.md) · [Subscription Cleaner](life-leverage/subscription-cleaner/SKILL.md) · [Travel Coordinator](life-leverage/travel-coordinator/SKILL.md)

**Original extensions — built for this directory (18):**

### Creative & Content (8)
[Thread Writer](creative-content/thread-writer/SKILL.md) · [Image Concept Generator](creative-content/image-concept-generator/SKILL.md) · [Meme Maker](creative-content/meme-maker/SKILL.md) · [Short Video Script Writer](creative-content/short-video-script-writer/SKILL.md) · [Brand Voice Keeper](creative-content/brand-voice-keeper/SKILL.md) · [Naming & Tagline Brainstormer](creative-content/naming-tagline-brainstormer/SKILL.md) · [Content Repurposer](creative-content/content-repurposer/SKILL.md) · [Hook & Headline Tester](creative-content/hook-and-headline-tester/SKILL.md)

### Research & Intelligence (4)
[Deep Research Brief](research-intelligence/deep-research-brief/SKILL.md) · [Trend Radar](research-intelligence/trend-radar/SKILL.md) · [Fact Checker](research-intelligence/fact-checker/SKILL.md) · [Call & Video Summarizer](research-intelligence/call-and-video-summarizer/SKILL.md)

### Data & Analytics (6)
[Metrics Report Builder](data-analytics/metrics-report-builder/SKILL.md) · [Dashboard Builder](data-analytics/dashboard-builder/SKILL.md) · [Spreadsheet Cleaner](data-analytics/spreadsheet-cleaner/SKILL.md) · [SQL Query Assistant](data-analytics/sql-query-assistant/SKILL.md) · [Anomaly Watcher](data-analytics/anomaly-watcher/SKILL.md) · [Cohort & Funnel Analyzer](data-analytics/cohort-funnel-analyzer/SKILL.md)

## Conventions

- **Approval-first.** Any skill that sends, posts, pays, or writes to an external system
  drafts and holds for human approval unless you explicitly widen its scope.
- **Cite sources.** Outputs that summarize or research name where each item came from.
- **Stay quiet when clean.** Monitoring skills report only when there's something to act on.
- **No invented data.** Skills mark gaps (`[NEEDS INPUT]`, `[TBD]`) instead of guessing.
