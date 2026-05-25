# Daily Operating Loop

A repeatable daily rhythm that helps the user orient, prioritize, and close the day with clarity.

---

## Morning: Command Center (start of day)

**Trigger:** "Plan my day", "Start the morning", "What should I focus on today"

### Steps

1. **Orient** — Read `context/priorities.md` and note the top 1–3 priorities and 90-day goal.
2. **Surface blockers** — Are there open action items, outstanding follow-ups, or decisions pending approval from prior sessions?
3. **Recommend the day's focus** — Based on priorities and any context from connected tools (calendar, tasks, email if accessible), recommend:
   - The single most important thing to move today.
   - 2–3 supporting tasks.
   - What to defer or ignore today.
4. **Flag risks** — Any deadline, commitment, or stakeholder item that needs attention today.
5. **Confirm the plan** — Present a brief daily summary and ask: "Does this look right, or do you want to shift the focus?"

### Output Format

```
## Today — [Date]

**Top priority:** [single most important thing]

**Supporting tasks:**
- [task 1]
- [task 2]

**Defer today:**
- [item]

**Flags:**
- [any risk or time-sensitive item]
```

---

## Midday: Check-In (optional)

**Trigger:** "How are we doing", "Midday check", "Quick update"

1. Ask: "What got done this morning, and what's blocking you?"
2. Rebalance the afternoon based on the answer.
3. Surface any new risks or follow-ups that came up.

---

## End of Day: Close Out

**Trigger:** "End of day", "Wrap up", "What's left", "Log today"

1. Review what was completed vs. the morning plan.
2. Identify open items to carry forward.
3. Ask: "Any decisions or learnings from today worth recording?"
4. If yes, log a learning: `python3 memory/scripts/log_event.py --event-type daily-close --request "EOD log" --outcome "[summary]"`
5. Confirm tomorrow's top priority if known.

---

## Weekly Reset

Run the weekly review on Fridays or Mondays — see `workflows/weekly-review.md`.

---

## Notes

- This loop is advisory. The user decides the actual schedule.
- If the user's tools (calendar, task manager) are connected, surface real commitments.
- If not connected, work from `context/priorities.md` and memory.
