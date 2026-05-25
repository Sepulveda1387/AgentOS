from __future__ import annotations

from common import DB_PATH, init_db, sqlite3_available


def main() -> None:
    init_db()
    mode = "sqlite3 CLI" if sqlite3_available() else "Python sqlite3 fallback"
    print(f"Initialized {DB_PATH} using {mode}.")


if __name__ == "__main__":
    main()
