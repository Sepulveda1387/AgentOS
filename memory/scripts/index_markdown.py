from __future__ import annotations

import re
from pathlib import Path

from common import ROOT, connect, init_db, rel, sha256_text, should_skip_path, utc_now


TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
TAG_RE = re.compile(r"(?<!\w)#([A-Za-z0-9_-]+)")


def summarize(text: str, max_chars: int = 360) -> str:
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]
    summary = " ".join(lines)
    if len(summary) > max_chars:
        return summary[: max_chars - 3].rstrip() + "..."
    return summary


def title_for(path: Path, text: str) -> str:
    match = TITLE_RE.search(text)
    return match.group(1).strip() if match else path.stem.replace("-", " ").title()


def main() -> None:
    init_db()
    now = utc_now()
    count = 0
    live_paths: set[str] = set()
    with connect() as conn:
        for path in ROOT.rglob("*.md"):
            if should_skip_path(path):
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            item_path = rel(path)
            live_paths.add(item_path)
            title = title_for(path, text)
            summary = summarize(text)
            tags = ",".join(sorted(set(TAG_RE.findall(text))))
            content_hash = sha256_text(text)
            modified_at = utc_now()
            conn.execute(
                """
                INSERT INTO knowledge_items
                  (path, title, summary, tags, kind, content_hash, modified_at, indexed_at)
                VALUES (?, ?, ?, ?, 'markdown', ?, ?, ?)
                ON CONFLICT(path) DO UPDATE SET
                  title=excluded.title,
                  summary=excluded.summary,
                  tags=excluded.tags,
                  content_hash=excluded.content_hash,
                  modified_at=excluded.modified_at,
                  indexed_at=excluded.indexed_at
                """,
                (item_path, title, summary, tags, content_hash, modified_at, now),
            )
            conn.execute("DELETE FROM knowledge_fts WHERE path = ?", (item_path,))
            conn.execute(
                "INSERT INTO knowledge_fts(path, title, summary, content) VALUES (?, ?, ?, ?)",
                (item_path, title, summary, text),
            )
            count += 1
        indexed_paths = [row["path"] for row in conn.execute("SELECT path FROM knowledge_items")]
        stale_paths = [p for p in indexed_paths if p not in live_paths]
        for stale_path in stale_paths:
            conn.execute("DELETE FROM knowledge_fts WHERE path = ?", (stale_path,))
            conn.execute("DELETE FROM knowledge_items WHERE path = ?", (stale_path,))
    print(f"Indexed {count} Markdown files.")
    if stale_paths:
        print(f"Removed {len(stale_paths)} stale indexed paths.")


if __name__ == "__main__":
    main()
