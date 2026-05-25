# Onboarding Guide

This document explains what happens during onboarding and how to re-run or update it.

## What Onboarding Does

When you first open this workspace in Claude Code (or another Claude-powered tool), the AI detects that `context/about-user.md` is in template state and enters onboarding mode. It asks 8 questions, one at a time, then:

1. Summarizes what it heard and asks for confirmation.
2. Writes your answers into the context files.
3. Initializes the memory database.
4. Is ready to work.

## The 8 Questions

| # | Question | Written to |
|---|----------|-----------|
| 1 | Name and what you do | `context/about-user.md` |
| 2 | What this system is for | `context/about-system.md` |
| 3 | Top 1–3 priorities | `context/priorities.md` |
| 4 | Tools and platforms you use | `context/about-system.md` |
| 5 | Communication style | `context/voice.md` |
| 6 | Actions requiring approval | `AGENTS.md` |
| 7 | Who this system serves | `context/about-user.md` |
| 8 | 90-day goal | `context/priorities.md` |

## Re-Running Onboarding

To re-run onboarding, reset `context/about-user.md` so it contains `[NOT SET]`:

```bash
# Reset just the identity line to trigger onboarding again
# Or edit the file manually and set Name: [NOT SET]
```

On the next session start, the AI will enter onboarding mode.

## Updating Context Without Full Re-Run

You don't have to re-run onboarding to update your context. You can:

- Edit `context/priorities.md` directly when priorities change.
- Edit `context/voice.md` to adjust communication style.
- Edit `context/about-system.md` to add or remove tools.
- Add entries to `context/decisions.md` for important choices.

After editing context files, refresh the index:
```bash
python3 memory/scripts/index_markdown.py
```

## Onboarding for a New User on an Existing System

If a new person is taking over or joining, reset `context/about-user.md` to template state and let them run onboarding fresh. The system context (`context/about-system.md`) can remain in place if the domain hasn't changed.
