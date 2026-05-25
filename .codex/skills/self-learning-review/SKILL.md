---
name: self-learning-review
description: Auto-invoke when the user asks about patterns in their work, what to automate, what keeps coming up, whether the system is learning, what the AI has noticed, what should become a workflow or skill, or how to improve the operating system. Also triggers on "what are we doing repeatedly", "what should we systematize", "run a pattern report", "what have you learned", "review what we've been doing", or any request to analyze recurring tasks and surface improvement opportunities.
status: approved
---

# Self-Learning Review

## Purpose

Analyze usage patterns, surface recurring tasks, and recommend concrete improvements — new skills, workflows, or checklists — that will make the system faster and more consistent over time. This is the mechanism by which the operating system improves itself based on real usage.

## When To Use

Use this skill when:
- The user asks what keeps coming up or what should be automated.
- The user asks for a pattern report, self-learning summary, or system review.
- The weekly review surfaces recurring patterns that need action.
- The user wants to know what the AI has observed or learned.
- 3 or more similar requests have occurred and no skill exists yet.

## Review Workflow

### Step 1 — Run Pattern Analysis

```bash
python3 memory/scripts/pattern_report.py
```

Read the output. Note:
- Which event types are most frequent.
- Which skills and workflows are used most.
- Which requests recur 2+ times without a dedicated skill or workflow.

### Step 2 — Review Learnings

```bash
python3 memory/scripts/search_learnings.py
```

Surface any logged learnings that may inform recommendations.

### Step 3 — Review Open Recommendations

```bash
python3 memory/scripts/recommendations.py list
```

Check what has already been recommended and not yet acted on. Do not re-recommend the same thing — close stale ones or escalate them.

### Step 4 — Classify Each Recurring Pattern

For each recurring request identified in Step 1, classify it:

| Pattern type | Recommended action |
|---|---|
| Repeatable, rules-based process | Propose a new workflow in `workflows/` |
| Human-led task that is easy to forget | Propose a checklist or template in `templates/` |
| Task needing specialized context, commands, or tool judgment | Propose a draft skill via `skill-creator` |
| Already handled by a skill/workflow but slow or inconsistent | Propose an improvement to the existing skill |
| One-off — not worth systematizing | Note and move on |

### Step 5 — Present Recommendations

For each recommendation, use this format:

```
Recommendation: [what to create or change]
Why: [pattern evidence — how many times, what type of request]
Expected impact: [faster / more consistent / less context needed / fewer errors]
Effort: [low / medium / high]
Type: [skill / workflow / checklist / template / skill improvement]
Next action: [exact step — e.g. "run skill-creator for X" or "create workflows/Y.md"]
Approval needed: [yes — new skill must be reviewed before enabling]
```

Present all recommendations together, prioritized by frequency × impact.

### Step 6 — Log the Review

```bash
python3 memory/scripts/log_event.py --event-type self-learning-review --request "Self-learning review" --outcome "Found [N] patterns. Recommended [N] improvements."
```

## After Recommendations Are Accepted

- For new skills: use `skill-creator` skill to draft them into `.codex/skills-drafts/`.
- For new workflows: create the file in `workflows/` and add a route in `capability-routing.md`.
- For templates: create in `templates/` and reference from the relevant skill or workflow.
- After any new file is created: run `register_assets.py` and `index_markdown.py`.

## Operating Rules

- Never recommend the same thing twice without noting it is still open from a prior review.
- Do not create skills or workflows during this review — surface the recommendations and let the user decide.
- Separate confirmed patterns (based on usage events) from inferred patterns (based on conversation context).
- Keep recommendations short and actionable. One paragraph per recommendation maximum.
- If the database has no usage events yet, say so clearly and explain how to start logging: `log_event.py`.
