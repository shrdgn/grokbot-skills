---
name: Docs Auditor
category: Product
description: Catch docs that are out of date with the product. Diffs help center and internal notes against what shipped last week, flags stale pages, and drafts the rewrite.
connectors: [Help center/CMS, changelog/release notes, Notion, Google Drive]
approval_required: true
suggested_routine: Weekly after release
---

# Docs Auditor

Keeps documentation in sync with the product — comparing docs against what actually
shipped, flagging stale pages, and drafting the fixes — so users aren't misled.

## Inputs
- Help-center + internal docs.
- Recent releases/changelog and PRs.

## Steps
1. Read what shipped since the last audit (changelog, release notes, PRs).
2. Find docs pages touching those areas.
3. Flag pages now inaccurate, incomplete, or referencing removed behavior.
4. Draft the rewrite for each flagged page.
5. Rank by user impact.

## Decision rules
- Flag only real mismatches with shipped behavior; cite the change.
- Draft edits preserve the doc's structure and voice.

## Definition of done
- A ranked list of stale pages, each with a drafted correction and the shipping change
  that made it stale — ready for review.

## Safety & approvals
- **Publishes nothing** — drafts for review/merge.
- Flags anything uncertain for a human SME rather than rewriting blindly.

## Suggested routine
- Weekly, after each release.
