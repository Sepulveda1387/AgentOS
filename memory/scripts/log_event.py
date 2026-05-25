from __future__ import annotations

import argparse

from common import connect, init_db, utc_now


def main() -> None:
    parser = argparse.ArgumentParser(description="Log a AgentOS usage event.")
    parser.add_argument("--event-type", required=True)
    parser.add_argument("--request", default="")
    parser.add_argument("--outcome", default="")
    parser.add_argument("--skill-name", default="")
    parser.add_argument("--workflow-name", default="")
    parser.add_argument("--files-touched", default="")
    parser.add_argument("--notes", default="")
    args = parser.parse_args()

    init_db()
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO usage_events
              (occurred_at, event_type, request, outcome, skill_name, workflow_name, files_touched, notes)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                utc_now(),
                args.event_type,
                args.request,
                args.outcome,
                args.skill_name,
                args.workflow_name,
                args.files_touched,
                args.notes,
            ),
        )
    print("Logged usage event.")


if __name__ == "__main__":
    main()
