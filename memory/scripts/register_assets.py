from __future__ import annotations

import re
import sys
from pathlib import Path

from common import ROOT, connect, init_db, utc_now


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NAME_RE = re.compile(r"^name:\s*(.+)$", re.MULTILINE)
STATUS_RE = re.compile(r"^status:\s*(.+)$", re.MULTILINE)
TRIGGER_RE = re.compile(r"^description:\s*(.+)$", re.MULTILINE)
CADENCE_RE = re.compile(r"^cadence:\s*(.+)$", re.MULTILINE)
TOOLS_RE = re.compile(r"^required_tools:\s*(.+)$", re.MULTILINE)


def register_skills(conn: object) -> int:
    count = 0
    for skill_dir in [ROOT / ".codex" / "skills", ROOT / ".codex" / "skills-drafts"]:
        if not skill_dir.exists():
            continue
        for skill_md in skill_dir.glob("*/SKILL.md"):
            text = skill_md.read_text(encoding="utf-8", errors="ignore")
            name_m = NAME_RE.search(text)
            status_m = STATUS_RE.search(text)
            trigger_m = TRIGGER_RE.search(text)
            if not name_m:
                continue
            name = name_m.group(1).strip()
            status = status_m.group(1).strip() if status_m else "draft"
            trigger = trigger_m.group(1).strip() if trigger_m else ""
            path = str(skill_md.relative_to(ROOT)).replace("\\", "/")
            now = utc_now()
            conn.execute(
                """
                INSERT INTO skill_registry (name, status, path, trigger_summary, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(name) DO UPDATE SET
                  status=excluded.status,
                  path=excluded.path,
                  trigger_summary=excluded.trigger_summary,
                  updated_at=excluded.updated_at
                """,
                (name, status, path, trigger, now, now),
            )
            count += 1
    return count


def register_workflows(conn: object) -> int:
    count = 0
    workflows_dir = ROOT / "workflows"
    if not workflows_dir.exists():
        return 0
    for wf_md in workflows_dir.glob("*.md"):
        text = wf_md.read_text(encoding="utf-8", errors="ignore")
        name = wf_md.stem.replace("-", " ").title()
        cadence_m = CADENCE_RE.search(text)
        tools_m = TOOLS_RE.search(text)
        cadence = cadence_m.group(1).strip() if cadence_m else ""
        tools = tools_m.group(1).strip() if tools_m else ""
        path = str(wf_md.relative_to(ROOT)).replace("\\", "/")
        now = utc_now()
        conn.execute(
            """
            INSERT INTO workflow_registry (name, status, path, cadence, required_tools, created_at, updated_at)
            VALUES (?, 'active', ?, ?, ?, ?, ?)
            ON CONFLICT(name) DO UPDATE SET
              path=excluded.path,
              cadence=excluded.cadence,
              required_tools=excluded.required_tools,
              updated_at=excluded.updated_at
            """,
            (name, path, cadence, tools, now, now),
        )
        count += 1
    return count


def main() -> None:
    init_db()
    with connect() as conn:
        skills = register_skills(conn)
        workflows = register_workflows(conn)
    print(f"Registered {skills} skills and {workflows} workflows.")


if __name__ == "__main__":
    main()
