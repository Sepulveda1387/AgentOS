---
name: skill-creator
description: Auto-invoke when the user asks to create a new skill, build a custom capability, automate a repeatable task into a skill file, turn a recurring workflow into a skill, draft a skill for a new tool or integration, or organize reusable instructions into a structured SKILL.md. Also triggers when the user says "make this a skill", "save this as a skill", "create a skill for X", "add this to skills", or when the same type of task has been requested 3 or more times and a skill would improve consistency.
status: approved
---

# Skill Creator

## Purpose

Convert any repeatable task, tool integration, workflow, or reasoning pattern into a structured SKILL.md that can be auto-detected, registered in memory, and invoked automatically when relevant in future sessions.

## When To Use

Use this skill when:
- The user asks to create a new skill explicitly.
- A task has been requested 3 or more times and a skill would make it consistent and fast.
- A new tool or integration is being added to the system and needs operating guidance.
- A complex reasoning pattern (research, evaluation, QA, review) should be captured as a reusable skill.
- An ad hoc workflow should be formalized as a repeatable capability.

## Skill File Structure

Every skill lives at `.codex/skills/<skill-name>/SKILL.md` with this frontmatter:

```markdown
---
name: <skill-name>          # kebab-case, matches folder name
description: <trigger description>  # used for auto-routing — be explicit about WHEN to invoke
status: draft               # draft | approved
---
```

The `description` field is the most important part. It determines whether the system auto-invokes this skill. Write it as:
> "Auto-invoke when the user asks to [clear trigger conditions]. Also triggers on [synonyms and related phrases]."

## Skill Creation Workflow

1. **Identify the skill's job**: What does this skill do? What problem does it solve repeatedly?
2. **Name the skill**: kebab-case, descriptive, action-first when possible (e.g. `research-company`, `qa-deliverable`, `design-artifact-studio`).
3. **Write the trigger description**: Cover all the ways a user might ask for this. Be specific and use natural language variations. This is what makes auto-routing work.
4. **Draft the body**: Include:
   - Purpose (1–2 sentences)
   - When to use / when not to use
   - Workflow or steps
   - Commands or code examples if tool-based
   - Operating rules and guardrails
5. **Set status to `draft`** until the user explicitly approves it.
6. **Save to `.codex/skills-drafts/<skill-name>/SKILL.md`** — never save directly to `.codex/skills/` without approval.
7. **Register and index**: run `python3 memory/scripts/register_assets.py` and `python3 memory/scripts/index_markdown.py` after saving.
8. **Present the draft** to the user for review. Suggest moving to `.codex/skills/` only after approval.

## Output Location Rules

| State | Location |
|-------|----------|
| Draft (not yet approved) | `.codex/skills-drafts/<skill-name>/SKILL.md` |
| Approved | `.codex/skills/<skill-name>/SKILL.md` |

Never write new skills directly into `.codex/skills/` without explicit user approval.

## Optional Supplementary Files

Add these when they make the skill more useful:

| File | Purpose |
|------|---------|
| `agents/openai.yaml` | Display name and default prompt for agent/UI surfaces |
| `scripts/<name>.py` | Python helper script for the skill |
| `references/<name>.md` | Reference document the skill reads at runtime |

## agents/openai.yaml Format

```yaml
interface:
  display_name: "Human-Readable Skill Name"
  short_description: "One sentence: what this skill does."
  default_prompt: "Instruction for the agent interface default invocation."
```

## Quality Checklist

Before presenting a skill draft:

- [ ] `name` is kebab-case and matches the folder.
- [ ] `description` covers all realistic trigger phrases, not just the obvious ones.
- [ ] Purpose is clear in the first 2 sentences.
- [ ] "When to use" and "when NOT to use" are both stated.
- [ ] Workflow is step-by-step and actionable.
- [ ] Approval gates are named for any external, destructive, or sensitive actions.
- [ ] Status is `draft` — not `approved`.
- [ ] Saved in `.codex/skills-drafts/` — not `.codex/skills/`.

## Operating Rules

- Always save new skills as drafts first. Never auto-approve.
- The trigger description is the most important part of the skill — spend time on it.
- After saving, run `register_assets.py` so the skill appears in memory and routing.
- If the skill replaces an existing workflow, note what changes for the user.
- Recommend updating `workflows/capability-routing.md` after approving a new skill so it gets routed automatically.
