from __future__ import annotations

import hashlib
import os
import shutil
import sqlite3
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MEMORY_DIR = ROOT / "memory"
DB_PATH = MEMORY_DIR / "agentOS.db"
SCHEMA_PATH = MEMORY_DIR / "schema.sql"


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def connect() -> sqlite3.Connection:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def sqlite3_available() -> bool:
    return shutil.which("sqlite3") is not None


def init_db() -> None:
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    with connect() as conn:
        conn.executescript(SCHEMA_PATH.read_text(encoding="utf-8"))


def should_skip_path(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    parts = set(relative.parts)
    skipped = {
        ".git",
        ".cache",
        ".venv",
        "cache",
        "credentials",
        "node_modules",
        "__pycache__",
    }
    return bool(parts & skipped)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT)).replace(os.sep, "/")
