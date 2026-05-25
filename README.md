<div align="center">

# AgentOS

**An AI executive assistant OS you can adapt to any context.**

[![License: Source Available](https://img.shields.io/badge/License-Source%20Available-blue.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Compatible-8A2BE2?logo=anthropic&logoColor=white)](https://claude.ai/code)
[![Multi-Model](https://img.shields.io/badge/Works%20With-Claude%20%7C%20GPT%20%7C%20Gemini-green)](AGENTS.md)
[![Built by WebSaaS.biz](https://img.shields.io/badge/Built%20by-WebSaaS.biz-orange)](https://websaas.biz)

A business, a project, a team, or your personal workflow — AgentOS adapts to any context. It indexes your priorities, decisions, and work patterns so every session is context-aware and token-efficient. Less time repeating yourself, more time moving forward.

</div>

---

## Table of Contents

- [What Is AgentOS](#what-is-agentos)
- [Quick Start](#quick-start)
- [After Setup](#after-setup)
- [Pre-Installed Skills](#pre-installed-skills)
- [How It Works](#how-it-works)
- [Protocol](#protocol--applies-to-all-ai-models)
- [Memory Commands](#memory-commands)
- [Folder Map](#folder-map)
- [Key Files](#key-files)
- [Requirements](#requirements)
- [License](#license)

---

## What Is AgentOS

AgentOS is a local, Git-friendly AI operating system workspace. Open it in [Claude Code](https://claude.ai/code) (or any Claude-powered tool) and the AI becomes a context-aware partner — not a blank-slate chatbot.

**What makes it different:**

- **Automatic onboarding.** First run detects you haven't been configured and asks 8 short questions to learn how it should work for you.
- **Auto-routing by intent.** You don't name skills or workflows — the system infers what you need and routes automatically.
- **Persistent memory.** SQLite-backed index of your priorities, decisions, and patterns. Searchable. Updated after every durable change.
- **Self-improvement loop.** Recurring tasks get proposed as draft skills. You approve; the system gets faster.
- **Multi-model protocol.** Every AI model that opens this workspace — Claude, GPT, Gemini, or any other — is bound by the same operating rules.

---

## Quick Start

> **Requirements:** Python 3.9+, [Claude Code](https://claude.ai/code) (or another Claude-powered tool)

```bash
# 1. Clone the repo
git clone https://github.com/Sepulveda1387/AgentOS.git
cd AgentOS

# 2. Open in Claude Code
code .
# Then open the Claude Code panel and say anything — onboarding starts automatically.
```

That's it. The system detects that `context/about-user.md` is unconfigured and enters onboarding mode. During onboarding, the AI runs `python3 memory/scripts/setup_runtime_files.py` to create `.env`, writes the local `.gitignore`, and initializes memory.

---

## First Run

The first thing you'll hear:

> *Welcome. I'm an AI executive assistant built by Gilbert Sepulveda at WebSaaS.biz. I index your priorities, decisions, and work patterns so every session is context-aware and token-efficient — less time repeating yourself, more time moving forward. A few quick questions to get started.*

The system then asks **8 short questions, one at a time** — about who you are, what you're optimizing for, which tools you use, how you want the assistant to communicate, and what success looks like in 90 days. No data leaves your machine.

---

## After Setup

Once onboarding is complete, the system knows:

- Who you are and what you're optimizing for
- Which tools and systems are your source of truth
- How you want it to communicate
- What actions always require your explicit approval

From there, work naturally. You don't need to name workflows or skills — the system infers what you need and routes automatically.

---

## Pre-Installed Skills

These skills are active out of the box and **auto-invoked by intent** — you never need to name them:

| Skill | Auto-invokes when you ask about… |
|-------|----------------------------------|
| `c-level` | Board review, executive evaluation, strategic decision, CEO/CFO/CMO/COO/CPO perspective |
| `chief-ai-engineering` | AI model selection, paid AI APIs, prompt strategy, cost or credit guardrails, intent-preserving generation |
| `video-research-ingestion` | Training recordings, tutorials, webinars, social videos, transcripts, frames, video claims, best-practice extraction |
| `markitdown` | Converting PDFs, Word, Excel, PowerPoint, HTML, URLs, images, or audio to Markdown |
| `scrapling-research` | Scraping a site, extracting from a known URL, CSS/XPath selection, conserving API credits |
| `playwright` | Screenshots, browser QA, mobile layout, visual verification, browser automation |
| `frontend-motion` | Adding Anime.js animation to a website, dashboard, or HTML deck |
| `motion-dynamic-views` | React animation with Motion (Framer Motion): transitions, scroll effects, layout changes |
| `design-artifact-studio` | Dashboards, HTML decks, website demos, SaaS prototypes, visual reports |
| `skill-creator` | Creating a new skill, formalizing a repeatable task, 3+ recurring requests |
| `self-learning-review` | Pattern report, what to automate, what keeps coming up, how to improve the system |
| `business-risk-review` | Operational, security, privacy, credential, compliance, financial, client-trust risk |
| `service-delivery-qa` | QA before delivering, presenting, publishing, or relying on important work |
| `systematic-debugging` | Root-cause debugging for failing tools, workflows, APIs, memory, or integrations |
| `verification-before-completion` | Evidence check before claiming work is complete, fixed, ready, migrated, or indexed |
| `cfo-financial-risk-analyst` | Financial analysis, pricing, margin, cash timing, revenue quality, budget, financial risk |
| `coo-business-operations-analyst` | Operations analysis, workflow diagnosis, capacity, handoffs, SOPs, delivery reliability |
| `cmo-funnel-messaging-analyst` | Funnel analysis, messaging clarity, CTA consistency, SEO/AEO, nurture, conversion risk |
| `cpo-offer-client-experience-analyst` | Offer scope, productized services, client/user journey, onboarding, feedback loops |
| `cro-pipeline-revenue-analyst` | Pipeline analysis, lead quality, sales follow-up, revenue conversion, forecast confidence |
| `legal-risk-compliance-claims-analyst` | Claims review, compliance risk, contracts, privacy, regulated topics, public promise risk |
| `cdo-data-quality-analyst` | Data quality, dashboard reliability, metric definitions, source mapping, reporting gaps |

New skills go to `.codex/skills-drafts/` first and are **never auto-invoked** until you explicitly approve them.

---

## How It Works

### Auto-Routing
Every SKILL.md file has a `description` field with explicit intent triggers. The AI reads incoming requests, matches intent, and routes to the right skill — no manual naming required.

### Memory System
A local SQLite database (`memory/agentOS.db`) stores:
- Indexed Markdown files (full-text searchable)
- Registered skills and workflows
- Usage events and patterns
- Learnings, decisions, and recommendations
- Session checkpoints

The clean operational database is committed with the repo and rebuilds from Markdown using `index_markdown.py`. The starter repo ships with the full operational source; onboarding writes local ignore rules for runtime sidecars and secrets.

### Self-Improvement Loop
When the same task recurs 3 or more times, the system proposes a draft skill. You review, approve, and the capability becomes part of the OS — auto-invoked forever after.

---

## Protocol — Applies to All AI Models

Every model operating in this workspace — Claude, GPT, Gemini, or any other — is bound by the same rules. These are hard stops, not suggestions.

1. **Local tools first.** Memory index → installed skills → local CLIs → `markitdown` → `scrapling-research` → `playwright` → external APIs (only when no local option exists, you request it, or the AI recommends it and you approve).
2. **Draft before acting.** Nothing is sent, published, deleted, or changed externally without your approval.
3. **Approval gates are hard stops.** Not suggestions.
4. **No invented context.** Missing information gets labeled as unknown, not filled with assumptions.
5. **Verify before done.** No claiming complete without a concrete check.
6. **Refresh memory after every durable change.** Run `index_markdown.py` after any Markdown, skill, workflow, or config change.
7. **Keep credentials in `.env`.** Never write secrets, API keys, or tokens into docs, prompts, or logs.
8. **Respect the self-improvement loop.** Log recurring tasks. When the same work recurs 3+ times, propose a draft skill — never enable it without your approval.

See [AGENTS.md](AGENTS.md) for the full operating charter.

---

## Memory Commands

```bash
python3 memory/scripts/init_db.py                            # Initialize the database
python3 memory/scripts/index_markdown.py                     # Index all Markdown files
python3 memory/scripts/register_assets.py                    # Register skills and workflows
python3 memory/scripts/setup_runtime_files.py                # Create local .env and safety .gitignore during onboarding
python3 memory/scripts/search_memory.py "query"              # Search memory
python3 memory/scripts/log_event.py --event-type request --request "task" --outcome "result"
python3 memory/scripts/pattern_report.py                     # Self-learning pattern report
python3 memory/scripts/recommendations.py list               # Open recommendations
python3 memory/scripts/skill_draft.py --name "x" --description "what it does"  # Draft a skill
python3 memory/scripts/log_learning.py --content "what was learned" --confidence 0.8
python3 memory/scripts/search_learnings.py "query"           # Search logged learnings
python3 memory/scripts/log_checkpoint.py --label "label" --notes "where I left off"
python3 memory/scripts/list_checkpoints.py                   # List session checkpoints
```

Run `index_markdown.py` and `register_assets.py` after any durable content or skill change.

---

## Folder Map

| Folder | What lives here |
|--------|----------------|
| `context/` | Your profile, priorities, voice, decisions, executive board |
| `workflows/` | Routing, daily loop, onboarding, weekly review, memory patterns |
| `memory/` | SQLite database and all scripts |
| `.codex/skills/` | Approved enabled skills — auto-invoked by intent |
| `.codex/skills-drafts/` | Proposed capabilities — never auto-invoked |
| `docs/` | Setup guide and onboarding docs |
| `templates/` | Reusable input templates |
| `vault/` | Notes, research, converted documents |
| `connections/` | Per-tool integration rules and approval gates |
| `logs/` | Dated reviews, audits, and checkpoints |
| `projects/` | Active initiatives |
| `archive/` | Approved archived material only |

---

## Key Files

| File | Purpose |
|------|---------|
| [`AGENTS.md`](AGENTS.md) | Operating charter — behavior, routing, approval gates, self-improvement loop |
| [`START_HERE.md`](START_HERE.md) | Detailed first-run guide |
| [`.claude/CLAUDE.md`](.claude/CLAUDE.md) | Model-level instructions — mandatory for all AI models |
| [`context/about-user.md`](context/about-user.md) | Your profile — onboarding trigger file |
| [`workflows/capability-routing.md`](workflows/capability-routing.md) | How requests are routed to skills and workflows |
| [`workflows/onboarding.md`](workflows/onboarding.md) | Onboarding question flow and write procedure |

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| Python 3.9+ | For memory scripts |
| [Claude Code](https://claude.ai/code) | Primary AI interface (also works with other Claude-powered tools) |
| No cloud database | Memory is local SQLite — your data stays on your machine |

**Optional dependencies** (for specific skills):

```bash
pip install playwright markitdown scrapling        # Browser automation, doc conversion, scraping
brew install yt-dlp ffmpeg                         # Optional video ingestion helpers on macOS
playwright install chromium                        # For playwright screenshots
pip install anime-js                               # Only needed for frontend-motion skill
```

---

## Design Principles

- Local tools before external APIs — always.
- Ask before any external action, send, publish, delete, or financial move.
- Facts separate from assumptions — always labeled.
- Draft before acting.
- Index before reading broadly.
- Verify before claiming complete.
- Log repeated work. When the same task recurs 3+ times, propose a skill.

---

## License

[Source Available — MIT + Commons Clause](LICENSE)

Free to use, share, fork, and build on — attribution to WebSaaS.biz required. Commercial use, resale, and sublicensing as a paid product or service are reserved exclusively by Web Services And Automation Solutions LLC (WebSaaS.biz). Contact [websaas.biz](https://websaas.biz) for commercial licensing.

---

<div align="center">

Built by **Gilbert Sepulveda** · [WebSaaS.biz](https://websaas.biz)

*Web Services And Automation Solutions LLC*

</div>
