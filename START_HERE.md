# Start Here

Welcome to your AI operating system.

This system is designed to adapt to you — not the other way around. It will ask you a short series of questions when you first use it, then build a working understanding of your context, tools, and goals. From then on, it acts as a proactive partner: surfacing what matters, routing requests to the right capability, and getting better the more you use it.

---

## How the First Session Works

When you open this workspace for the first time in Claude Code or another Claude-powered interface, the AI will detect that setup hasn't been completed yet. It will:

1. Introduce itself briefly.
2. Ask you **8 short questions, one at a time** — no forms, no clipboard paste required.
3. Summarize what it heard and ask you to confirm.
4. Write your answers into the right context files.
5. Initialize the memory database.
6. Be ready to work.

The whole thing takes about 3 minutes.

---

## The 8 Onboarding Questions

You don't need to prepare answers — just respond naturally. Here's what's coming:

1. **Who are you?** Your name and what you do.
2. **What is this for?** The domain or context — business, project, research, personal, team.
3. **Top priorities?** 1–3 things you're focused on right now.
4. **Tools you use?** Apps, platforms, integrations you rely on.
5. **Communication style?** How direct, how detailed, how formal.
6. **Approval gates?** What actions always need your OK first.
7. **Who does this serve?** Just you, a team, clients, customers.
8. **90-day goal?** What success looks like in one sentence.

---

## What Happens After Setup

The system configures itself based on your answers. It will:

- Use your name and adapt its tone to your communication preference.
- Know which tools to reference as the source of truth.
- Apply the right decision-making lens (business, technical, operational, creative) based on the work.
- Always ask before taking actions you flagged as approval-required.
- Log repeated patterns and propose workflows or shortcuts when something comes up more than twice.

---

## How to Use It Day-to-Day

Just describe what you need. You don't have to use any special commands or call skills by name. Examples:

- "Plan my day" → routes to the daily command center
- "Review my pipeline" → routes to the pipeline or advisory review
- "Help me prep for a call with [company]" → routes to company research
- "Something broke" → routes to systematic debugging
- "Which AI model should I use for this?" → routes to chief AI engineering
- "Summarize this training video and extract the steps" → routes to video research ingestion
- "What should I be doing this week?" → routes to weekly review
- "Help me draft a message to [person]" → drafts, asks for approval before sending

---

## Approval Culture

The system will always ask before:
- Sending any message
- Editing any external record
- Publishing anything
- Deleting or archiving files
- Taking any financial action
- Handling credentials

It will never take those actions silently. If it tries, that's a bug — tell it so.

---

## Back Up to Your Own Private Repo

Your context, decisions, logs, and skills are yours. Keep them in a private GitHub repo so they're never lost.

```bash
gh repo create my-agentos --private --source . --remote origin --push
```

Commit and push any time you add meaningful context. See `docs/setup.md` for the full walkthrough.

> Keep your repo private — it will contain your personal profile, priorities, and decisions.

---

## Maintenance

Keep the system useful with a few habits:

- Run `python3 memory/scripts/index_markdown.py` after adding or editing context files.
- Add dated notes to `logs/` after significant decisions or changes.
- When a repeated task deserves a shortcut, say "let's make this a workflow."
- Review `context/priorities.md` every week or two to keep it current.

---

## Files Worth Knowing

| File | What it is |
|------|-----------|
| `AGENTS.md` | The operating charter — how the AI behaves, what it checks, what it gates |
| `context/about-user.md` | Your profile |
| `context/about-system.md` | What this OS manages and which tools it touches |
| `context/priorities.md` | Current goals and focus |
| `context/voice.md` | How the AI communicates with you |
| `workflows/capability-routing.md` | How requests get routed to the right skill or workflow |
| `memory/scripts/` | Python scripts for memory management |

---

You're ready. Open a Claude session in this workspace and say hello.
