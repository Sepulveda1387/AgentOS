# Setup Guide

How to get AgentOS running from scratch.

## Prerequisites

- Python 3.8+ (for memory scripts)
- Claude Code CLI, Claude desktop app, or any Claude-powered interface
- Git (recommended — keeps your context versioned)

## Step 1 — Clone or Copy the Workspace

```bash
# If you received this as a git repo
git clone <repo-url> AgentOS
cd AgentOS

# If you received it as a folder, just open it
```

## Step 2 — Open in Claude Code

```bash
cd AgentOS
claude  # or open this folder in the Claude desktop app
```

The AI will detect that onboarding hasn't been completed and guide you through 8 questions.

During onboarding, AgentOS runs:

```bash
python3 memory/scripts/setup_runtime_files.py
```

That creates:

- `.env` from `.env.example`, with API key values left blank.
- A local `.gitignore` that protects `.env`, credentials, runtime memory databases, caches, and machine-specific files.
- `memory/agentOS.db`, rebuilt from the committed Markdown, skills, and workflows.

## Step 3 — Initialize Memory Manually (Optional)

After onboarding, the AI initializes memory automatically. If you ever need to do it manually:

```bash
python3 memory/scripts/init_db.py
python3 memory/scripts/index_markdown.py
python3 memory/scripts/register_assets.py
```

Verify it worked:
```bash
python3 memory/scripts/search_memory.py "priorities"
```

## Step 4 — Back Up to Your Own Private Repo (Recommended)

Your `context/`, `logs/`, `vault/`, and `projects/` folders will fill up with real decisions, priorities, and personal context. Back them up in a private repo so nothing is ever lost.

```bash
# Create a new private repo on GitHub (requires GitHub CLI)
gh repo create my-agentos --private --source . --remote origin --push

# Or set a remote manually if you created the repo on github.com
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git push -u origin main
```

After that, commit and push whenever you add meaningful context:

```bash
git add context/ logs/ vault/ projects/ .codex/skills/
git commit -m "Update context and logs"
git push
```

**What stays out of git after onboarding:** `.env`, `memory/agentOS.db`, credentials, and cache — all covered by the local `.gitignore` created during onboarding.

> This repo is yours. Keep it private. Do not push to the public AgentOS template repo.

## Step 5 — Add Tool Connections (Optional)

For each tool you use, create a file in `connections/<tool>.md` with:
- What the tool does
- Read vs. write scope
- Approval gates specific to that tool
- CLI commands or API patterns

See `connections/` for examples (add your own as you go).

## Maintenance

| Task | Command |
|------|---------|
| Refresh memory index | `python3 memory/scripts/index_markdown.py` |
| Search memory | `python3 memory/scripts/search_memory.py "query"` |
| View patterns | `python3 memory/scripts/pattern_report.py` |
| View recommendations | `python3 memory/scripts/recommendations.py` |
| Draft a new skill | `python3 memory/scripts/skill_draft.py --name "skill-name" --description "what it does"` |

## Local Gitignore

The starter repository intentionally ships with no active ignore rules so the full operational system can be committed to GitHub. During onboarding, AgentOS writes local ignore rules for:

```
memory/agentOS.db
memory/scripts/__pycache__/
.env
credentials/
cache/
*.pyc
```

Add equivalent rules manually only if you skip onboarding.
