---
name: business-risk-review
description: Use when reviewing operational, security, privacy, credential, compliance, financial, client-trust, implementation, automation, CRM, or delivery risks. Also use before connecting new tools, importing external repos, changing credential patterns, or enabling automations that affect clients or business systems.
status: approved
---

# Business Risk Review

## Goal

Find practical risks before they become business problems. Focus on trust, money, client commitments, credentials, data exposure, operational reliability, and automation failure modes.

## Workflow

1. Define the scope: system, workflow, client deliverable, integration, repo, automation, or decision.
2. Load only needed context:
   - `AGENTS.md`
   - relevant `connections/`, `workflows/`, `.codex/skills/`, project files, or memory entries
   - live systems only when current state matters
3. Review risk categories:
   - Credentials and secrets handling
   - Approval gates and external actions
   - Client-facing commitments
   - Financial exposure
   - CRM/data integrity
   - Privacy and sensitive information
   - Reliability, rollback, and observability
   - Duplicate systems or operational drift
4. Classify findings:
   - Critical: stop before proceeding.
   - High: fix before broad use.
   - Medium: manage with guardrails.
   - Low: note for later.
5. Recommend the smallest reversible mitigation.
6. Identify what needs human approval.

## Output Format

```markdown
# Business Risk Review

## Scope

## Findings

## Recommended Mitigations

## Approval Gates

## Residual Risk
```

## Guardrails

- Do not expose credential values.
- Do not change CRM, task status, financial, publishing, archive, delete, or client-facing state without approval.
- Prefer policy and workflow fixes before adding new tooling.
