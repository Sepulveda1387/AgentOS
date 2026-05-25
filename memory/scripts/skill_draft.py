from __future__ import annotations

import argparse
import sys
from pathlib import Path

from common import ROOT, connect, init_db, utc_now


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SKILL_TEMPLATE = """\
---
name: {name}
description: {description}
status: draft
---

# {title}

## Goal

{description}

## Trigger

Use this skill when: {description}

## Steps

1. [Define steps for this skill]

## Output

[Describe what this skill produces]

## Approval Gates

- [List any actions that require user approval]
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Draft a new AgentOS skill.")
    parser.add_argument("--name", required=True, help="Skill name (kebab-case)")
    parser.add_argument("--description", required=True, help="One-line description")
    args = parser.parse_args()

    slug = args.name.lower().replace(" ", "-")
    title = slug.replace("-", " ").title()
    skill_dir = ROOT / ".codex" / "skills-drafts" / slug
    skill_dir.mkdir(parents=True, exist_ok=True)
    skill_path = skill_dir / "SKILL.md"

    if skill_path.exists():
        print(f"Skill already exists: {skill_path}")
        sys.exit(1)

    skill_path.write_text(
        SKILL_TEMPLATE.format(name=slug, title=title, description=args.description),
        encoding="utf-8",
    )
    print(f"Draft skill created: {skill_path}")
    print("Review and refine before enabling. Run register_assets.py to index.")

    init_db()
    now = utc_now()
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO skill_registry (name, status, path, trigger_summary, created_at, updated_at)
            VALUES (?, 'draft', ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
              status='draft', path=excluded.path, trigger_summary=excluded.trigger_summary, updated_at=excluded.updated_at
            """,
            (slug, str(skill_path.relative_to(ROOT)).replace("\\", "/"), args.description, now, now),
        )


if __name__ == "__main__":
    main()
