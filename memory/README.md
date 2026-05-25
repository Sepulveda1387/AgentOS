# Memory

AgentOS uses a two-layer memory system: Markdown for durable, human-readable context and SQLite for fast operational lookup.

## Database

`memory/agentOS.db` — local only, gitignored. Regenerated at any time from source Markdown.

## Scripts

| Script | Purpose |
|--------|---------|
| `init_db.py` | Initialize or reset the database schema |
| `index_markdown.py` | Index all Markdown files into SQLite + FTS |
| `search_memory.py "query"` | Full-text search across indexed content |
| `log_event.py` | Log a usage event |
| `pattern_report.py` | Self-learning pattern analysis |
| `register_assets.py` | Register skills and workflows in the registry |
| `recommendations.py` | List, add, or close recommendations |
| `skill_draft.py` | Scaffold a new draft skill |
| `log_learning.py` | Log a typed learning with confidence |
| `search_learnings.py` | Search logged learnings |
| `log_checkpoint.py` | Log a work checkpoint |
| `list_checkpoints.py` | List checkpoints |

## Quick Start

```bash
python3 memory/scripts/init_db.py
python3 memory/scripts/index_markdown.py
python3 memory/scripts/search_memory.py "priorities"
```

## When to Refresh the Index

Run `index_markdown.py` after:
- Onboarding completion
- Editing any file in `context/`
- Adding or editing workflows or skills
- Any durable operating-system change

## Tables

| Table | Stores |
|-------|--------|
| `knowledge_items` | Indexed Markdown files |
| `knowledge_fts` | Full-text search virtual table |
| `usage_events` | Session activity log |
| `patterns` | Recurring task patterns |
| `skill_registry` | Skill catalog and status |
| `workflow_registry` | Workflow catalog |
| `decisions` | Durable decisions |
| `recommendations` | Open and closed recommendations |
| `learnings` | Typed learnings with confidence |
| `checkpoints` | Work checkpoints |
| `archive_candidates` | Proposed archive items |

## .gitignore

The database file is excluded from version control:
```
memory/agentOS.db
memory/__pycache__/
.env
```
