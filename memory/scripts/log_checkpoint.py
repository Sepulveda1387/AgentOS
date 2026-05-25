from __future__ import annotations

import argparse

from common import connect, init_db, utc_now


def main() -> None:
    parser = argparse.ArgumentParser(description="Log a work checkpoint.")
    parser.add_argument("--label", required=True, help="Short label for the checkpoint")
    parser.add_argument("--notes", default="", help="What was completed, what's next")
    parser.add_argument("--files-touched", default="", help="Comma-separated file paths")
    args = parser.parse_args()

    init_db()
    with connect() as conn:
        conn.execute(
            """
            INSERT INTO checkpoints (logged_at, label, notes, files_touched)
            VALUES (?, ?, ?, ?)
            """,
            (utc_now(), args.label, args.notes, args.files_touched),
        )
    print(f"Checkpoint logged: {args.label}")


if __name__ == "__main__":
    main()
