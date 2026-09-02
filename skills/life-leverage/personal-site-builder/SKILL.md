---
name: Personal Site Builder
category: Life & Leverage
description: Scaffold a personal site from a description, untangle domain issues, and leave you with a live starting point.
connectors: [Computer use, code sandbox, hosting, domain/DNS, GitHub]
approval_required: true
suggested_routine: On demand
---

# Personal Site Builder

Takes you from "I want a personal site" to a live starting point — scaffolding the site,
sorting the domain/DNS, and deploying — so you have something real to build on.

## Inputs
- What the site is for, content/sections, and any style preference.
- Domain (owned or to register) and hosting preference.

## Steps
1. Turn the description into a simple site structure and design.
2. Build the site and deploy to a preview URL.
3. Diagnose domain/DNS issues; propose the exact records to set.
4. On approval, connect the domain and publish.
5. Hand off the live URL and how to edit it.

## Decision rules
- Keep it simple and maintainable; pick sensible defaults.
- Never register a domain or change DNS without explicit approval.

## Definition of done
- A live (or preview-ready) site with the domain connected on approval, plus a short
  guide to editing and next steps.

## Safety & approvals
- **Domain registration, DNS changes, and going live require your approval.**
- Handles registrar/hosting credentials securely.

## Suggested routine
- On demand; a one-time build with optional follow-ups.
