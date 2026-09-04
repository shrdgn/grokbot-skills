#!/usr/bin/env python3
"""Generate catalog.json from every skills/**/SKILL.md front-matter.

Run from the repo root:  python3 scripts/build_catalog.py
Writes catalog.json (machine-readable index of all skills).
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"

# Display order + labels for categories (folder slug -> pretty name).
CATEGORY_ORDER = [
    ("general", "General"),
    ("sales", "Sales"),
    ("marketing", "Marketing"),
    ("customer-success-support", "Customer Success & Support"),
    ("recruiting-people", "Recruiting & People"),
    ("operations-finance", "Operations & Finance"),
    ("product", "Product"),
    ("engineering", "Engineering"),
    ("life-leverage", "Life & Leverage"),
    ("creative-content", "Creative & Content"),
    ("research-intelligence", "Research & Intelligence"),
    ("data-analytics", "Data & Analytics"),
]
ORDER_INDEX = {slug: i for i, (slug, _) in enumerate(CATEGORY_ORDER)}


def parse_front_matter(text):
    """Return the YAML-ish front-matter block as a dict of scalars/lists."""
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    data = {}
    for line in m.group(1).splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, _, value = line.partition(":")
        key, value = key.strip(), value.strip()
        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            data[key] = [v.strip() for v in inner.split(",")] if inner else []
        elif value in ("true", "false"):
            data[key] = value == "true"
        else:
            data[key] = value
    return data


def main():
    skills = []
    for skill_md in SKILLS_DIR.glob("*/*/SKILL.md"):
        fm = parse_front_matter(skill_md.read_text(encoding="utf-8"))
        category_slug = skill_md.parent.parent.name
        skills.append(
            {
                "name": fm.get("name", skill_md.parent.name),
                "slug": skill_md.parent.name,
                "category": fm.get("category", category_slug),
                "category_slug": category_slug,
                "description": fm.get("description", ""),
                "connectors": fm.get("connectors", []),
                "approval_required": fm.get("approval_required", False),
                "suggested_routine": fm.get("suggested_routine", ""),
                "path": str(skill_md.relative_to(ROOT)),
            }
        )

    skills.sort(key=lambda s: (ORDER_INDEX.get(s["category_slug"], 99), s["name"]))

    categories = []
    for slug, name in CATEGORY_ORDER:
        count = sum(1 for s in skills if s["category_slug"] == slug)
        if count:
            categories.append({"slug": slug, "name": name, "count": count})

    catalog = {
        "name": "Grok Bot Skills",
        "description": "A curated library of reusable Grok Bot skill recipes.",
        "skill_format": [
            "Inputs",
            "Steps",
            "Decision rules",
            "Definition of done",
            "Safety & approvals",
            "Suggested routine",
        ],
        "total": len(skills),
        "categories": categories,
        "skills": skills,
    }

    out = ROOT / "catalog.json"
    out.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} — {len(skills)} skills, {len(categories)} categories.")


if __name__ == "__main__":
    main()
