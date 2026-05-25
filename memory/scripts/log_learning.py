from __future__ import annotations

import argparse

from common import connect, init_db, utc_now


def main() -> None:
    parser = argparse.ArgumentParser(description="Log a learning to AgentOS memory.")
    parser.add_argument("--content", required=True, help="What was learned")
    parser.add_argument("--confidence", type=float, default=0.7, help="0.0–1.0")
    parser.add_argument("--source", default="", help="Source file or context")
    parser.add_argument("--tags", default="", help="Comma-separated tags")
    args = parser.parse_args()

    init_db()
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO learnings (logged_at, content, confidence, source, tags)
            VALUES (?, ?, ?, ?, ?)
            """,
            (utc_now(), args.content, args.confidence, args.source, args.tags),
        )
    print("Learning logged.")


if __name__ == "__main__":
    main()
