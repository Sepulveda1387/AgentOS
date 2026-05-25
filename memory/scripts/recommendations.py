from __future__ import annotations

import argparse
import sys

from common import connect, init_db, utc_now


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def list_recommendations(conn: object, status: str = "open") -> None:
    rows = conn.execute(
        "SELECT * FROM recommendations WHERE status = ? ORDER BY created_at DESC",
        (status,),
    ).fetchall()
    if not rows:
        print(f"No {status} recommendations.")
        return
    for row in rows:
        print(f"\n[{row['id']}] {row['area']} — {row['recommendation']}")
        if row["reason"]:
            print(f"  Why: {row['reason']}")
        if row["expected_impact"]:
            print(f"  Impact: {row['expected_impact']}")
        if row["next_action"]:
            print(f"  Next: {row['next_action']}")


def add_recommendation(conn: object, args: argparse.Namespace) -> None:
    conn.execute(
        """
        INSERT INTO recommendations
          (created_at, area, recommendation, reason, expected_impact, effort, risk, next_action)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            utc_now(),
            args.area,
            args.recommendation,
            args.reason,
            args.impact,
            args.effort,
            args.risk,
            args.next_action,
        ),
    )
    print("Recommendation logged.")


def close_recommendation(conn: object, rec_id: int) -> None:
    conn.execute(
        "UPDATE recommendations SET status = 'closed' WHERE id = ?", (rec_id,)
    )
    print(f"Recommendation {rec_id} closed.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Manage AgentOS recommendations.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List open recommendations")

    add_p = sub.add_parser("add", help="Add a recommendation")
    add_p.add_argument("--area", required=True)
    add_p.add_argument("--recommendation", required=True)
    add_p.add_argument("--reason", default="")
    add_p.add_argument("--impact", default="")
    add_p.add_argument("--effort", default="")
    add_p.add_argument("--risk", default="")
    add_p.add_argument("--next-action", default="")

    close_p = sub.add_parser("close", help="Close a recommendation")
    close_p.add_argument("id", type=int)

    args = parser.parse_args()
    init_db()

    with connect() as conn:
        if args.command == "add":
            add_recommendation(conn, args)
        elif args.command == "close":
            close_recommendation(conn, args.id)
        else:
            list_recommendations(conn)


if __name__ == "__main__":
    main()
