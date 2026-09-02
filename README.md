<div align="center">

# 🤖 Grok Bot Skills

**A curated library of ready-to-run [Grok Bot](https://x.ai) skills** — each one a
repeatable task recipe your Bot can run on demand or on a schedule.

`74 skills` · `12 categories` · `one consistent format`

</div>

---

## What is this?

A **skill** is a recipe. When a Bot needs to do a task, it shouldn't reinvent the
method each time — it should find the skill, read the inputs and steps, produce the
deliverable, and verify it meets the definition of done.

Every skill in this library captures the same six things:

> **Inputs** · **Steps** · **Decision rules** · **Definition of done** · **Safety & approvals** · **Suggested routine**

Attach any skill to a **routine** to run it on a schedule (a 7 a.m. brief) or a trigger
(a new Slack message). Reference a saved skill with `/` in the composer.

## How it's organized

```
skills/
├── <category>/
│   └── <skill-name>/
│       └── SKILL.md      ← the recipe (YAML front-matter + body)
├── _TEMPLATE.md          ← copy this to add a new skill
└── README.md             ← the in-directory index
```

Each `SKILL.md` opens with front-matter — `name`, `category`, `description`,
`connectors`, `approval_required`, `suggested_routine` — followed by the six-section body.

## Principles baked into every skill

| Principle | What it means |
|-----------|---------------|
| ✋ **Approval-first** | Anything that sends, posts, pays, or writes externally **drafts and waits** for your OK. |
| 🔗 **Cite sources** | Research and summaries name where each claim came from. |
| 🤫 **Quiet when clean** | Monitors report only when there's something to act on. |
| 🚫 **No invented data** | Gaps get flagged (`[NEEDS INPUT]`, `[TBD]`) — never guessed. |

---

## 📚 The Library

### From xAI's *Ways to use Grok Bot* catalog (56)

<details open>
<summary><b>🗂️ General</b> (6)</summary>

| Skill | What it does |
|-------|--------------|
| [Chief of Staff](skills/general/chief-of-staff/SKILL.md) | Scans Slack, email, calendar, and notes into one prioritized read-out tied to your goals. |
| [Daily Briefing Writer](skills/general/daily-briefing-writer/SKILL.md) | A tight daily brief of only the stories that matter to you. |
| [Executive Assistant](skills/general/executive-assistant/SKILL.md) | Morning briefing plus an instant catch-up whenever you join a new room. |
| [Inbox Manager](skills/general/inbox-manager/SKILL.md) | Triages email, surfaces urgent/blocked threads, drafts replies — every send behind approval. |
| [Presentation Designer](skills/general/presentation-designer/SKILL.md) | On-brand decks from your template, delivered as an editable link. |
| [Status Report Writer](skills/general/status-report-writer/SKILL.md) | Pulls open action items into one living list and a morning digest. |

</details>

<details>
<summary><b>💼 Sales</b> (10)</summary>

| Skill | What it does |
|-------|--------------|
| [Account Research Specialist](skills/sales/account-research-specialist/SKILL.md) | Scores fit and warmth and builds a shareable research pack per account. |
| [CRM Operations Manager](skills/sales/crm-operations-manager/SKILL.md) | Keeps CRM and org-chart hygiene clean before and after meetings. |
| [Deal Desk Coordinator](skills/sales/deal-desk-coordinator/SKILL.md) | Drafts sourced internal deal notes and submits in Salesforce on approval. |
| [Deck Updater](skills/sales/deck-updater/SKILL.md) | Updates the deal deck from discovery notes with next steps baked in. |
| [Meeting Prep Buddy](skills/sales/meeting-prep-buddy/SKILL.md) | Prep packs from calendar, CRM, Gong, and Slack for every meeting. |
| [Pipeline Analyst](skills/sales/pipeline-analyst/SKILL.md) | Scrubs the pipeline, flags stalls and commit risk, drops a Monday scoreboard. |
| [Prospecting Plan Builder](skills/sales/prospecting-plan-builder/SKILL.md) | Builds the week's enriched, ready-to-work outbound list. |
| [Renewal Desk Operator](skills/sales/renewal-desk-operator/SKILL.md) | 90-day renewal packs, drafted commercial notes, legal nudges only when stuck. |
| [Sales Call Coach](skills/sales/sales-call-coach/SKILL.md) | Timestamped coaching and a score on every recorded call. |
| [Sales Outbound](skills/sales/sales-outbound/SKILL.md) | Overnight research + personalized drafts in your voice, queued for approval. |

</details>

<details>
<summary><b>📣 Marketing</b> (13)</summary>

| Skill | What it does |
|-------|--------------|
| [Community Operations Manager](skills/marketing/community-operations-manager/SKILL.md) | Screens apps, triages DMs, drafts nurture on cadence. |
| [Compelling Events Monitor](skills/marketing/compelling-events-monitor/SKILL.md) | Watches for real reasons to engage and drafts on-voice responses. |
| [Competitive Intelligence Analyst](skills/marketing/competitive-intelligence-analyst/SKILL.md) | Surfaces only material competitor shifts, with a suggested response. |
| [Event Guest Screener](skills/marketing/event-guest-screener/SKILL.md) | Scores applicants against your ICP and batch-approves strong fits. |
| [Internal Communications Manager](skills/marketing/internal-communications-manager/SKILL.md) | On-voice internal copy tuned per audience — review-only. |
| [LinkedIn Campaign Manager](skills/marketing/linkedin-campaign-manager/SKILL.md) | Keeps lead-gen consistent across ads, forms, follow-up, and UTMs. |
| [Marketing Calendar Owner](skills/marketing/marketing-calendar-owner/SKILL.md) | Keeps content, launch, and event calendars in sync. |
| [Merch Fulfillment Operator](skills/marketing/merch-fulfillment-operator/SKILL.md) | Runs swag outreach, per-submission approval, and daily vendor orders. |
| [Newsletter Writer](skills/marketing/newsletter-writer/SKILL.md) | Drafts the recurring newsletter from what actually shipped. |
| [Paid Media](skills/marketing/paid-media/SKILL.md) | Recommends budget reallocations against plan — holds for approval. |
| [Paid Media Creative Strategist](skills/marketing/paid-media-creative-strategist/SKILL.md) | Spots early creative winners and proposes the next test. |
| [SEO / AEO Auditor](skills/marketing/seo-aeo-auditor/SKILL.md) | Tracks search + answer-engine movement and returns a fix plan. |
| [Social Media Manager](skills/marketing/social-media-manager/SKILL.md) | Drafts in your voice when something ships and keeps the queue moving. |

</details>

<details>
<summary><b>🤝 Customer Success & Support</b> (4)</summary>

| Skill | What it does |
|-------|--------------|
| [Account Health](skills/customer-success-support/account-health/SKILL.md) | Turns portfolio usage and signals into a ranked risk/expansion watch list. |
| [Account Manager](skills/customer-success-support/account-manager/SKILL.md) | Preps every account call and drafts follow-ups without rebuilding context. |
| [Enablement Fulfillment Specialist](skills/customer-success-support/enablement-fulfillment-specialist/SKILL.md) | Finds recordings/assets, builds one-pagers, drafts the reply with links. |
| [Ticket Triage Specialist](skills/customer-success-support/ticket-triage-specialist/SKILL.md) | Triages the queue and drafts replies — quiet when it's clean. |

</details>

<details>
<summary><b>🧑‍💼 Recruiting & People</b> (4)</summary>

| Skill | What it does |
|-------|--------------|
| [Calendar Coordinator](skills/recruiting-people/calendar-coordinator/SKILL.md) | Schedules across calendars and chases the holds nobody else will. |
| [Hiring Screener](skills/recruiting-people/hiring-screener/SKILL.md) | Scores applications against a defined bar and hands off an ATS-ready review. |
| [Onboarding Manager](skills/recruiting-people/onboarding-manager/SKILL.md) | Builds the checklist, pulls docs, answers day-one questions, routes blockers. |
| [Talent Scout](skills/recruiting-people/talent-scout/SKILL.md) | Sources, dedupes against the ATS, and drafts outreach in your voice. |

</details>

<details>
<summary><b>💰 Operations & Finance</b> (5)</summary>

| Skill | What it does |
|-------|--------------|
| [Contract Desk](skills/operations-finance/contract-desk/SKILL.md) | Summarizes contracts by stage and owner, pulls terms, flags blocked reviews. |
| [Expense Manager](skills/operations-finance/expense-manager/SKILL.md) | Logs receipts, chases missing categories, builds the weekly spend summary. |
| [Invoice Coordinator](skills/operations-finance/invoice-coordinator/SKILL.md) | Routes and matches invoices, nudges owners on exceptions. |
| [Security Questionnaire Filler](skills/operations-finance/security-questionnaire-filler/SKILL.md) | Drafts every field from your trust center and past RFPs, parks the submit. |
| [Vendor Portal Operator](skills/operations-finance/vendor-portal-operator/SKILL.md) | Runs weekly portal work with no API and returns exceptions only. |

</details>

<details>
<summary><b>🧩 Product</b> (5)</summary>

| Skill | What it does |
|-------|--------------|
| [Beta Adoption Watcher](skills/product/beta-adoption-watcher/SKILL.md) | Surfaces which customers are actually trying a new feature. |
| [Call FAQ Miner](skills/product/call-faq-miner/SKILL.md) | Mines recurring questions from calls with sourced, timestamped answers. |
| [Docs Auditor](skills/product/docs-auditor/SKILL.md) | Flags docs out of date with what shipped and drafts the rewrite. |
| [Feature Request Tracker](skills/product/feature-request-tracker/SKILL.md) | A living list of requests tied to the customers who asked. |
| [Product Feedback Analyst](skills/product/product-feedback-analyst/SKILL.md) | Clusters feedback into a prioritized view with drafted routing. |

</details>

<details>
<summary><b>🛠️ Engineering</b> (5)</summary>

| Skill | What it does |
|-------|--------------|
| [Bug Reproduction](skills/engineering/bug-reproduction/SKILL.md) | Reproduces the bug in staging and drops a trustworthy repro pack. |
| [Cloud Agent Orchestrator](skills/engineering/cloud-agent-orchestrator/SKILL.md) | Kicks off, monitors, and unsticks many cloud agent runs. |
| [Playtest Operator](skills/engineering/playtest-operator/SKILL.md) | Drives the UI to brute-force test flows and returns a findings pack. |
| [Product Performance](skills/engineering/product-performance/SKILL.md) | Walks flamegraphs and returns ranked hotspots with evidence. |
| [Prototype Builder](skills/engineering/prototype-builder/SKILL.md) | Builds a clickable prototype and returns a screenshot + live URL. |

</details>

<details>
<summary><b>🌱 Life & Leverage</b> (4)</summary>

| Skill | What it does |
|-------|--------------|
| [Apartment Scout](skills/life-leverage/apartment-scout/SKILL.md) | Shortlists eligible apartments and books tours as they hit the market. |
| [Personal Site Builder](skills/life-leverage/personal-site-builder/SKILL.md) | Scaffolds a personal site, untangles DNS, leaves you a live starting point. |
| [Subscription Cleaner](skills/life-leverage/subscription-cleaner/SKILL.md) | Finds forgotten subscriptions and unsubscribes/cancels what you approve. |
| [Travel Coordinator](skills/life-leverage/travel-coordinator/SKILL.md) | Compares flights and hotels to your rules and books after you confirm. |

</details>

### ✨ Original extensions — built for this library (18)

<details open>
<summary><b>🎨 Creative & Content</b> (8)</summary>

| Skill | What it does |
|-------|--------------|
| [Thread Writer](skills/creative-content/thread-writer/SKILL.md) | Turns a topic or doc into a structured, on-voice X thread. |
| [Image Concept Generator](skills/creative-content/image-concept-generator/SKILL.md) | Brief → distinct on-brand image concepts with generation-ready prompts. |
| [Meme Maker](skills/creative-content/meme-maker/SKILL.md) | Topical, brand-safe memes drafted for approval. |
| [Short Video Script Writer](skills/creative-content/short-video-script-writer/SKILL.md) | Shoot-ready Reels/Shorts scripts with hook, beats, and CTA. |
| [Brand Voice Keeper](skills/creative-content/brand-voice-keeper/SKILL.md) | Learns your voice once, then rewrites or audits any copy against it. |
| [Naming & Tagline Brainstormer](skills/creative-content/naming-tagline-brainstormer/SKILL.md) | Names and taglines with domain/handle and trademark sanity checks. |
| [Content Repurposer](skills/creative-content/content-repurposer/SKILL.md) | One asset → a pack of channel-native derivatives. |
| [Hook & Headline Tester](skills/creative-content/hook-and-headline-tester/SKILL.md) | Generates and ranks hooks/headlines/subject lines against your goal. |

</details>

<details open>
<summary><b>🔎 Research & Intelligence</b> (4)</summary>

| Skill | What it does |
|-------|--------------|
| [Deep Research Brief](skills/research-intelligence/deep-research-brief/SKILL.md) | A sourced, decision-ready brief — bottom line up front, citations throughout. |
| [Trend Radar](skills/research-intelligence/trend-radar/SKILL.md) | A real-time digest of emerging trends on X and the web, with sources. |
| [Fact Checker](skills/research-intelligence/fact-checker/SKILL.md) | Verifies claims against primary sources and returns a verdict with evidence. |
| [Call & Video Summarizer](skills/research-intelligence/call-and-video-summarizer/SKILL.md) | Recording → TL;DR, decisions, owner-tagged actions, timestamped highlights. |

</details>

<details open>
<summary><b>📊 Data & Analytics</b> (6)</summary>

| Skill | What it does |
|-------|--------------|
| [Metrics Report Builder](skills/data-analytics/metrics-report-builder/SKILL.md) | A recurring KPI digest that explains movement — drivers, anomalies, takeaways. |
| [Dashboard Builder](skills/data-analytics/dashboard-builder/SKILL.md) | Designs and builds a dashboard from your data, right chart per metric. |
| [Spreadsheet Cleaner](skills/data-analytics/spreadsheet-cleaner/SKILL.md) | Turns a messy sheet into analysis-ready data with a full change log. |
| [SQL Query Assistant](skills/data-analytics/sql-query-assistant/SKILL.md) | Plain-English question → a correct, explained, read-only SQL query. |
| [Anomaly Watcher](skills/data-analytics/anomaly-watcher/SKILL.md) | Monitors key metrics and alerts — with likely cause — only when truly off. |
| [Cohort & Funnel Analyzer](skills/data-analytics/cohort-funnel-analyzer/SKILL.md) | Retention curves and funnel drop-offs with a plain-language read. |

</details>

---

## 🧱 Add your own

1. Copy [`skills/_TEMPLATE.md`](skills/_TEMPLATE.md) to
   `skills/<category>/<skill-name>/SKILL.md`.
2. Fill in the front-matter and the six sections.
3. Keep the principles above — approval-first, cite sources, quiet when clean, no
   invented data.

The best skills start as a task you did once by hand: do it, make it reliable, write it
down as a recipe, *then* automate it with a routine.

## Category map

| # | Category | Count |
|---|----------|-------|
| 1 | General | 6 |
| 2 | Sales | 10 |
| 3 | Marketing | 13 |
| 4 | Customer Success & Support | 4 |
| 5 | Recruiting & People | 4 |
| 6 | Operations & Finance | 5 |
| 7 | Product | 5 |
| 8 | Engineering | 5 |
| 9 | Life & Leverage | 4 |
| 10 | Creative & Content | 8 |
| 11 | Research & Intelligence | 4 |
| 12 | Data & Analytics | 6 |
| | **Total** | **74** |
