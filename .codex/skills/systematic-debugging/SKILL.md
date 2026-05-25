---
name: systematic-debugging
description: Use when something is broken, failing, unexpected, flaky, not authenticated, not syncing, not indexing, or not working across Windows/macOS. Find root cause before fixes for code, CLIs, workflows, skills, APIs, migrations, browser tests, memory, or integrations.
status: approved
---

# Systematic Debugging

## Goal

Fix the real problem, not the symptom. Use evidence, reproduction, isolation, and verification before declaring success.

## Workflow

1. State the observed failure and expected behavior.
2. Reproduce or inspect the smallest failing command, file, workflow, or API call.
3. Collect evidence:
   - exact command or action
   - error output
   - environment and path assumptions
   - changed files or recent decisions
4. Form 1-3 hypotheses and test the cheapest one first.
5. Isolate the failing layer:
   - credentials/auth
   - PATH/tool install
   - platform difference
   - source file/config
   - API/scope/permission
   - runtime/cache/index
6. Apply the smallest reversible fix.
7. Verify with a command or read-only live probe.
8. Preserve durable learning when the cause is repeatable: update docs, workflow, skill, or memory index when appropriate.

## Output Format

```markdown
# Systematic Debugging

## Failure

## Evidence

## Root Cause

## Fix

## Verification

## Durable Follow-Up
```

## Guardrails

- Do not guess when a command can prove the point.
- Do not run destructive commands unless explicitly approved.
- Do not copy credentials outside `.env`; Google Workspace encrypted local credentials are the approved exception.
