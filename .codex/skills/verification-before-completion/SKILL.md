---
name: verification-before-completion
description: Use before claiming work is complete, fixed, migrated, authenticated, indexed, installed, ready, current, or safe. Requires evidence from commands, file checks, live read-only probes, tests, screenshots, or memory counts before final success claims.
status: approved
---

# Verification Before Completion

## Goal

Never close the loop on vibes. Before saying work is done, prove the claim with the smallest meaningful verification.

## Workflow

1. List the claims that need proof.
2. Choose the lightest verification for each claim:
   - file exists / frontmatter parses
   - command exits successfully
   - tool version is present
   - read-only API probe succeeds
   - test or smoke test passes
   - memory counts match
   - screenshot or browser check confirms UI behavior
3. Run the verification when safe.
4. If verification fails, either fix and re-run or report the blocker clearly.
5. Final response must separate:
   - Verified facts
   - Remaining assumptions
   - Pending work

## Common AgentOS Checks

```bash
git status --short
python3 memory/scripts/init_db.py
python3 memory/scripts/index_markdown.py
python3 memory/scripts/search_memory.py "<query>"
```

For memory integrity, compare live Markdown count, `knowledge_items`, `knowledge_fts`, and missing indexed paths.

For integrations, prefer read-only probes. Do not send messages, change CRM, change task statuses, publish, archive, delete, or take financial action as a verification shortcut.

## Output Format

```markdown
# Verification

## Claims Checked

## Evidence

## Result

## Remaining Risk
```
