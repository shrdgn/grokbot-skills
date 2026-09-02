---
name: Dashboard Builder
category: Data & Analytics
description: Go from a question to a working dashboard. Use to design and build (or refresh) a dashboard from your data sources, with the right charts for each metric and sane defaults.
connectors: [BigQuery/warehouse, Google Sheets, BI tool, Looker/Metabase]
approval_required: true
suggested_routine: On demand
---

# Dashboard Builder

Designs and builds a dashboard that answers a specific question — picking the right
chart for each metric and wiring it to your data — so you get a usable view, not a
blank canvas.

## Inputs
- The question/decision the dashboard serves and its audience.
- Data sources/tables and the metrics + dimensions available.
- The BI tool and any style/layout conventions.

## Steps
1. Clarify the question and the 5–9 metrics that answer it.
2. Choose the right mark per metric (trend → line, composition → stacked bar, etc.).
3. Define each query/measure; validate against a known number.
4. Lay out the dashboard: headline KPIs on top, detail and breakdowns below, filters.
5. Deliver the dashboard link and a note on definitions and caveats.

## Decision rules
- One clear question per dashboard; cut metrics that don't serve it.
- Match chart type to the data's shape; avoid chart junk and dual axes.
- Every measure has a written definition; validate before publishing.

## Definition of done
- A working dashboard answering the question, with validated measures, clear labels and
  filters, and a definitions/caveats note.

## Safety & approvals
- **Publishing/sharing the dashboard awaits approval.**
- Flags any measure it couldn't validate rather than shipping a wrong number.

## Suggested routine
- On demand to build; scheduled refresh once live.
