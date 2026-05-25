---
name: service-delivery-qa
description: Use before delivering, presenting, publishing, or relying on client-facing advisory work, business assessments, presentations, reports, websites, proposals, workflows, SOPs, or implementation outputs. Checks quality, evidence, consistency, commitments, and client experience before completion.
status: approved
---

# Service Delivery QA

## Goal

Protect trust before anything client-facing or operationally important leaves AgentOS. Verify that the work is accurate, complete, usable, and aligned with the promise being made.

## Workflow

1. Identify the asset, audience, and decision it supports.
2. Load the asset and nearby context. For non-Markdown files, use the `markitdown` skill when plain reading is not enough.
3. Check five areas:
   - **Promise fit:** Does the asset match the offer, scope, and client need?
   - **Evidence:** Are claims supported by sources, files, data, screenshots, or clearly labeled assumptions?
   - **Completeness:** Are expected sections, next steps, owners, dates, and approval gates present?
   - **Client experience:** Is it clear, concise, professional, and easy to act on?
   - **Risk:** Does it create unintended commitments, expose credentials, mention private details, or imply unsupported results?
4. If the asset is a website, presentation, or interactive deliverable, inspect it before editing and preserve existing user work.
5. Recommend fixes by severity:
   - Blocker: should not be sent or used yet.
   - Important: fix before client-facing use if time allows.
   - Polish: improves confidence but does not block.
6. Make local fixes when the user asked for execution and the asset is not subject to a separate approval gate. Otherwise draft the fix list.
7. Verify after fixes with the smallest meaningful check.

## Output Format

```markdown
# Service Delivery QA

## Verdict

## Blockers

## Important Fixes

## Polish

## Evidence Checked

## Recommended Next Action
```

## Guardrails

- Do not publish, send, or change client-facing deadlines without explicit approval.
- For approved/client-facing files, inspect before editing and keep changes tightly scoped.
- Separate facts from assumptions.
