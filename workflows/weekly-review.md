# Weekly Review

A structured rhythm for reflecting on the past week and setting up the next one. Keeps priorities current, surfaces recurring patterns, and prevents context drift.

---

## Trigger

"Weekly review", "What happened this week", "Weekly planning", "Set up next week"

Recommended cadence: Friday end-of-day or Monday morning.

---

## Review Steps

### 1. Last Week — What Happened

- What were the original priorities at the start of last week?
- What actually got done vs. planned?
- What got deferred, and why?
- Any decisions made? Log them in `context/decisions.md` if not already there.
- Any risks or issues that surfaced?

### 2. Patterns

- Run `python3 memory/scripts/pattern_report.py` to surface recurring work.
- Are there tasks that keep coming up without a workflow? Propose one.
- Are there recurring blockers? Name and address them.

### 3. Priorities — Next Week

Update `context/priorities.md` with:
- Top 1–3 priorities for next week.
- Anything to explicitly deprioritize.
- Any new constraints or deadlines.

### 4. 90-Day Goal Check

- Read the 90-day goal in `context/priorities.md`.
- Is the work from last week moving toward it?
- If not, name the gap and recommend an adjustment.

### 5. System Health

- Are memory indexes current? Run `python3 memory/scripts/index_markdown.py` if needed.
- Are any skills in `.codex/skills-drafts/` worth approving or pruning?
- Is `context/about-system.md` still accurate (tools, integrations)?

### 6. Recommendation Sweep

Run `python3 memory/scripts/recommendations.py` and review any open recommendations.

---

## Output Format

```
## Weekly Review — [Date Range]

### Last Week
- Completed: [list]
- Deferred: [list]
- Decisions logged: [yes / no]
- Issues surfaced: [list]

### Patterns
- [any recurring items]

### Next Week Priorities
1. [P1]
2. [P2]
3. [P3]

### 90-Day Goal Progress
- On track / off track: [assessment]
- Recommended adjustment: [if any]

### System Health
- Memory index: [current / needs refresh]
- Skills queue: [any pending approvals]
```

---

## After the Review

Log the session:
```bash
python3 memory/scripts/log_event.py --event-type weekly-review --request "Weekly review [date]" --outcome "Priorities updated. [key findings]"
```
