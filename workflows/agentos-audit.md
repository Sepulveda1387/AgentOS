# AgentOS Audit

Status: active reference

## Purpose

Use this workflow when the user asks to review, audit, score, improve, or harden AgentOS itself. It evaluates whether the operating system is useful, safe, current, and easy to extend.

## Audit Dimensions

| Dimension | Check for |
| --- | --- |
| Context | User profile, system purpose, priorities, voice, decisions, source-of-truth map |
| Routing | Clear capability map, conservative triggers, workflow/skill coverage, no noisy over-routing |
| Capabilities | Approved skills, draft skills, workflows, templates, connection docs, missing high-leverage agents |
| Cadence | Daily loop, weekly review, checkpoints, follow-up capture, priority refresh |
| Memory | Markdown index freshness, FTS search, asset registry, usage events, recommendations, learnings |
| Safety | Approval gates, secrets handling, archive/delete discipline, external-system boundaries |
| Verification | Tests, smoke checks, index counts, register checks, documented remaining risk |
| Portability | No private source context, no machine-specific paths, clean setup docs, reusable patterns |

## Workflow

1. Confirm the request type and approval gates.
2. Search memory before broad file reading:
   ```bash
   python3 memory/scripts/search_memory.py "AgentOS audit"
   python3 memory/scripts/search_memory.py "improvement recommendation"
   ```
3. Inspect the operating surface:
   ```bash
   find . -maxdepth 3 -type f \( -name '*.md' -o -name 'SKILL.md' \) -not -path './.git/*' | sort
   python3 memory/scripts/register_assets.py
   python3 memory/scripts/index_markdown.py
   python3 memory/scripts/pattern_report.py
   python3 memory/scripts/recommendations.py list
   ```
4. Score each audit dimension as `Strong`, `Needs attention`, or `Missing`.
5. Recommend only small, reversible improvements unless the user asks for a rebuild.
6. Keep new skills in `.codex/skills-drafts/` until the user approves enabling them.
7. Refresh memory after durable Markdown, workflow, skill, or operating-system edits.

## Output Format

```markdown
# AgentOS Audit

## Score

## Strengths

## Gaps

## Top Improvements

## Suggested Agents Or Workflows

## Verification

## Approval Requests
```

## Best-Practice Defaults

- Prefer workflows for rules-based repeatable process.
- Prefer checklists for human-led tasks that are easy to forget.
- Prefer draft skills for recurring tasks that need specialized context, commands, or tool-specific judgment.
- Prefer specialized analyst agents only when the request is diagnostic, evidence-heavy, recurring, and has a clear output format.
- Keep the main AgentOS thread responsible for synthesis and final recommendations.

