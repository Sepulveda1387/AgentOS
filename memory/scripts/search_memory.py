from __future__ import annotations

import argparse
import re
import sys

from common import connect, init_db


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def to_fts_query(query: str) -> str:
    terms = re.findall(r"[A-Za-z0-9_]+", query)
    if not terms:
        return '""'
    return " OR ".join(f'"{term}"' for term in terms[:12])


def main() -> None:
    parser = argparse.ArgumentParser(description="Search AgentOS memory.")
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=8)
    args = parser.parse_args()

    init_db()
    fts_query = to_fts_query(args.query)
    with connect() as conn:
        rows = conn.execute(
            """
            SELECT path, title, summary, bm25(knowledge_fts) AS rank
            FROM knowledge_fts
            WHERE knowledge_fts MATCH ?
            ORDER BY rank
            LIMIT ?
            """,
            (fts_query, args.limit),
        ).fetchall()

    if not rows:
        print("No memory results.")
        return

    for row in rows:
        print(f"{row['path']} | {row['title']}")
        if row["summary"]:
            print(f"  {row['summary']}")


if __name__ == "__main__":
    main()
