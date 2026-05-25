# Onboarding Workflow

This workflow governs how the AI collects user context during the first session and writes it into the operating system's context files.

---

## Trigger

Run this workflow when `context/about-user.md` contains `[NOT SET]` on a session start.

## Pre-Conditions

- The AI has NOT loaded any prior user context.
- The AI should NOT act on any unrelated request until onboarding is confirmed complete.

---

## Step 1 — Opening

Send this exact message to start onboarding:

> Welcome. I'm an AI executive assistant built by Gilbert Sepulveda at WebSaaS.biz. I index your priorities, decisions, and work patterns so every session is context-aware and token-efficient — less time repeating yourself, more time moving forward. A few quick questions to get started.
>
> I'll ask you 8 short questions, one at a time. This takes about 3 minutes and you can adjust anything afterward.
>
> **Question 1 of 8:** What's your name, and what do you do? One sentence is fine.

---

## Step 2 — Question Sequence

Ask each question only after the previous answer is received. Do not ask multiple questions in the same message. Acknowledge each answer briefly before the next question.

| # | Question | Notes |
|---|----------|-------|
| 1 | What's your name, and what do you do? | Capture name and one-line role |
| 2 | What is this system primarily for — a business, a personal project, a specific domain, a team, or something else? | Identifies domain and use case |
| 3 | What are your top 1–3 priorities right now? | Can be goals, problems, or focus areas |
| 4 | What tools, apps, or platforms do you use most day-to-day? | Capture all tools mentioned; note which are source-of-truth systems |
| 5 | How do you like the assistant to communicate? Direct and brief, detailed, formal, casual, or something else? | Sets voice and response depth |
| 6 | What actions should always require your explicit approval before the assistant takes them? | Examples: sending messages, editing records, publishing anything, financial actions |
| 7 | Who or what does this system serve — just you, a team, clients, customers? And roughly how many? | Defines audience scale |
| 8 | What does success look like in the next 90 days? One sentence. | Sets the 90-day goal |

---

## Step 3 — Confirmation

After Q8, summarize all answers in a concise block. Example format:

> Here's what I heard:
>
> - **You:** [name], [role]
> - **This system is for:** [domain/purpose]
> - **Priorities:** [P1], [P2], [P3]
> - **Tools:** [list]
> - **Communication style:** [style]
> - **Approval-required actions:** [list]
> - **Serves:** [audience]
> - **90-day goal:** [goal]
>
> Does this look right? Anything to add or correct before I set things up?

Wait for confirmation. If corrections are given, apply them and confirm again before writing.

---

## Step 4 — Write Context Files

After confirmation, write answers to these files:

### `context/about-user.md`
- Name, role, domain, audience (from Q1, Q7)
- Communication preference (from Q5)
- 90-day goal (from Q8)

### `context/about-system.md`
- Primary purpose and domain (from Q2)
- Tools listed as source-of-truth systems (from Q4)
- Any excluded tools mentioned

### `context/priorities.md`
- Top priorities (from Q3)
- 90-day goal (from Q8)

### `context/voice.md`
- Communication style, tone, depth (from Q5)

### `AGENTS.md` — Approval Gates section
- Append any approval-required actions the user specified in Q6 that aren't already listed in the default gates.

---

## Step 5 — Create Local Runtime Files

After confirmation and context writes, create the local runtime files that should exist on the user's machine but should not be pre-filled with secrets.

Run the deterministic setup helper:

```bash
python3 memory/scripts/setup_runtime_files.py
```

This creates `.env` from `.env.example` if `.env` does not already exist, then creates local `.gitignore` safety rules. The clean `memory/agentOS.db` index is part of the operational system and remains tracked; generated SQLite sidecars are local-only.

Leave all API key values blank or commented. Tell the user they can add keys later when an integration actually needs them. Never invent, request, echo, log, or commit credential values.

The local `.gitignore` rules written by the helper are:

```gitignore
# Environment and local secrets
.env
.env.local
.env.*.local
credentials/
*.json.key
*.pem
*.key
service-account*.json
token.json
token*.pickle

# Generated SQLite sidecars
memory/*.db-*

# Python/runtime caches
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/
dist/
build/

# Tool/cache output
cache/
.cache/
.claude/scratch/
.claude/tmp/

# OS/editor files
.DS_Store
.DS_Store?
Thumbs.db
ehthumbs.db
.vscode/settings.json
.idea/
*.swp
*.swo
```

This is intentionally done during onboarding rather than in the template repository so GitHub contains the full operational source system, while each user's clone protects local secrets and generated runtime files.

---

## Step 6 — Initialize Memory

Run these commands after writing context files:

```bash
python3 memory/scripts/init_db.py
python3 memory/scripts/index_markdown.py
python3 memory/scripts/register_assets.py
python3 memory/scripts/log_event.py --event-type onboarding --request "Initial setup" --outcome "Onboarding complete — context written and memory initialized"
```

Verify index count is greater than 0 before proceeding.

---

## Step 7 — Handoff

Say:

> You're set up. The system knows who you are, what you're working toward, and how to work with you. Your context is saved and indexed.
>
> What would you like to work on first?

If the user immediately has a task, route it through `workflows/capability-routing.md`.

---

## Post-Onboarding: Context Maintenance

- Update `context/priorities.md` weekly or when focus changes.
- Update `context/about-system.md` when new tools are added or removed.
- Run `python3 memory/scripts/index_markdown.py` after any durable context changes.
- Add dated entries to `context/decisions.md` for choices the AI should remember.
