---
name: Spreadsheet Cleaner
category: Data & Analytics
description: Turn a messy spreadsheet into clean, analysis-ready data. Use to fix malformed rows, inconsistent formats, duplicates, and stray headers — with a log of every change.
connectors: [Google Sheets, Excel, Google Drive]
approval_required: true
suggested_routine: On demand
---

# Spreadsheet Cleaner

Turns a messy tabular file into clean, analysis-ready data — normalizing formats,
removing junk, and deduping — with a full change log so nothing happens silently.

## Inputs
- The source file/sheet and what it's for.
- Any known rules (key columns, valid ranges, canonical formats, dedup keys).

## Steps
1. Profile the data: columns, types, missing values, obvious errors.
2. Propose a cleaning plan (header fix, type coercion, date/number formats, trims,
   dedup keys, split/merge columns).
3. On approval, apply the plan to a copy (never the original).
4. Log every transformation and flag rows it couldn't confidently fix.
5. Deliver the cleaned file plus a change log and a list of remaining issues.

## Decision rules
- Work on a copy; never overwrite the source.
- Don't drop rows/values without logging them; flag ambiguous fixes for review.
- Preserve meaning — no silent value changes.

## Definition of done
- A cleaned copy that's analysis-ready, a change log of every transformation, and a
  list of rows/values needing human judgment.

## Safety & approvals
- **The cleaning plan and any row removals are approved before applying.**
- Original file left untouched.

## Suggested routine
- On demand whenever a messy file needs prepping.
