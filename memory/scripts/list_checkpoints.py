from __future__ import annotations

import argparse
import sys

from common import connect, init_db


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main() -> None:
    parser = argparse.ArgumentParser(description="List work checkpoints.")
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--status", default="open", choices=["open", "closed", "all"])
    args = parser.parse_args()

    init_db()
    with connect() as conn:
        if args.status == "all":
            rows = conn.execute(
                "SELECT * FROM checkpoints ORDER BY logged_at DESC LIMIT ?",
                (args.limit,),
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT * FROM checkpoints WHERE status = ? ORDER BY logged_at DESC LIMIT ?",
                (args.status, args.limit),
            ).fetchall()

    if not rows:
        print("No checkpoints found.")
        return

    for row in rows:
        print(f"\n[{row['id']}] [{row['logged_at'][:10]}] {row['label']} — {row['status']}")
        if row["notes"]:
            print(f"  {row['notes']}")
        if row["files_touched"]:
            print(f"  Files: {row['files_touched']}")


if __name__ == "__main__":
    main()
