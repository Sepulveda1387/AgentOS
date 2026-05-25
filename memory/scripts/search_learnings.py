from __future__ import annotations

import argparse
import sys

from common import connect, init_db


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser(description="Search logged learnings.")
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()

    init_db()
    with connect() as conn:
        if args.query:
            pattern = f"%{args.query}%"
            rows = conn.execute(
                """
                SELECT * FROM learnings
                WHERE content LIKE ? OR tags LIKE ? OR source LIKE ?
                ORDER BY logged_at DESC LIMIT ?
                """,
                (pattern, pattern, pattern, args.limit),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM learnings ORDER BY logged_at DESC LIMIT ?",
                (args.limit,),
            ).fetchall()

    if not rows:
        print("No learnings found.")
        return

    for row in rows:
        conf = f"{row['confidence']:.0%}" if row["confidence"] else ""
        print(f"\n[{row['logged_at'][:10]}] {row['content']}")
        if conf:
            print(f"  Confidence: {conf}")
        if row["source"]:
            print(f"  Source: {row['source']}")
        if row["tags"]:
            print(f"  Tags: {row['tags']}")


if __name__ == "__main__":
    main()
