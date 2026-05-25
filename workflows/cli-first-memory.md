# CLI-First Memory Workflow

Use structured commands and index lookup before reading files broadly. This keeps sessions fast and avoids burning context window on content that isn't needed.

---

## Order of Operations

1. **Command or CLI first** — if a connected tool has a CLI or API, use it.
2. **Index search second** — search `memory/agentOS.db` before reading files.
3. **Structured file read third** — read specific context files (not broad directory scans).
4. **Broad reading last resort** — only when the above three fail.

---

## Memory Commands

```bash
# Initialize or reset the database
python3 memory/scripts/init_db.py

# Index all Markdown files
python3 memory/scripts/index_markdown.py

# Search memory
python3 memory/scripts/search_memory.py "your query"

# Log a usage event
python3 memory/scripts/log_event.py --event-type <type> --request "<task>" --outcome "<result>"

# Pattern report (self-learning)
python3 memory/scripts/pattern_report.py

# Register skills and workflows
python3 memory/scripts/register_assets.py

# Open recommendations
python3 memory/scripts/recommendations.py

# Draft a new skill
python3 memory/scripts/skill_draft.py --name "<skill-name>" --description "<what it does>"

# Log a learning
python3 memory/scripts/log_learning.py --content "<what was learned>" --confidence <0.0-1.0> --source "<context file or experience>"

# Search learnings
python3 memory/scripts/search_learnings.py "query"

# Log a checkpoint
python3 memory/scripts/log_checkpoint.py --label "<checkpoint label>" --notes "<what was completed, what's next>"

# List checkpoints
python3 memory/scripts/list_checkpoints.py
```

---

## When to Index

Always run `python3 memory/scripts/index_markdown.py` after:
- Writing or editing any file in `context/`
- Adding or editing a workflow in `workflows/`
- Adding or editing a skill in `.codex/skills/` or `.codex/skills-drafts/`
- Onboarding completion
- Any durable operating-system change

---

## When to Search Before Reading

If the user asks about a topic, person, decision, or tool:
```bash
python3 memory/scripts/search_memory.py "topic keyword"
```

Only read source files if the search returns no relevant results.

---

## Database Location

`memory/agentOS.db` — local only, gitignored. Regenerated from Markdown via `init_db.py` + `index_markdown.py`.

---

## Windows (PowerShell)

```powershell
python memory\scripts\init_db.py
python memory\scripts\index_markdown.py
python memory\scripts\search_memory.py "your query"
python memory\scripts\log_event.py --event-type request --request "task" --outcome "result"
python memory\scripts\pattern_report.py
```
