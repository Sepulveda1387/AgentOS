from __future__ import annotations

import sys
from collections import Counter

from common import connect, init_db, utc_now


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


THRESHOLD = 2


def main() -> None:
    init_db()
    with connect() as conn:
        rows = conn.execute(
            "SELECT event_type, request, skill_name, workflow_name FROM usage_events"
        ).fetchall()

    if not rows:
        print("No usage events recorded yet.")
        return

    event_types = Counter(row["event_type"] for row in rows)
    skill_uses = Counter(row["skill_name"] for row in rows if row["skill_name"])
    workflow_uses = Counter(row["workflow_name"] for row in rows if row["workflow_name"])

    print("=== Pattern Report ===\n")

    print("Event types:")
    for event_type, count in event_types.most_common():
        print(f"  {event_type}: {count}")

    if skill_uses:
        print("\nTop skills:")
        for name, count in skill_uses.most_common(10):
            print(f"  {name}: {count}")

    if workflow_uses:
        print("\nTop workflows:")
        for name, count in workflow_uses.most_common(10):
            print(f"  {name}: {count}")

    recurring = [
        (request, count)
        for request, count in Counter(
            row["request"] for row in rows if row["request"]
        ).most_common()
        if count >= THRESHOLD
    ]

    if recurring:
        print(f"\nRecurring requests (>= {THRESHOLD} times):")
        for request, count in recurring[:10]:
            short = request[:80] + "..." if len(request) > 80 else request
            print(f"  [{count}x] {short}")
        print("\nConsider converting recurring requests into draft skills or workflows.")

    with connect() as conn:
        conn.execute(
            """
            INSERT INTO usage_events (occurred_at, event_type, request, outcome)
            VALUES (?, 'pattern-report', 'pattern_report.py', 'report generated')
            """,
            (utc_now(),),
        )


if __name__ == "__main__":
    main()
