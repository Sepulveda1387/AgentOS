---
name: c-level
description: Auto-invoke when the user asks for a board-level review, executive evaluation, C-suite perspective, strategic recommendation, multi-lens analysis, or wants to evaluate a decision, offer, workflow, project, or business idea from CEO, CFO, CMO, COO, and CPO perspectives. Also triggers on requests like "what would the executives say", "give me the full picture", "evaluate this strategically", or "what are the risks and next steps".
status: approved
---

# C-Level Board Review

## Goal

Evaluate the user's prompt from a chief executive board perspective. Each executive gives a role-specific evaluation with direction, reasoning, execution path, risk, and next action. Produce one collective recommendation with tensions, agreed actions, and approval gates.

## Context Loading

Before evaluating, load only what is needed:

1. Read `context/about-user.md`, `context/priorities.md`, and `context/about-system.md` when available.
2. Read relevant project files when the prompt names or clearly implies a project.
3. Search memory when the prompt depends on prior decisions or unresolved recommendations.
4. Use live systems only when current operational facts would materially change the evaluation.
5. Separate verified facts from assumptions whenever context is incomplete.

For detailed role guidance, read `references/executive-board-framework.md` when available.

## Executive Roles

Always include these five executives unless the user asks for a different board composition:

- **CEO**: direction, focus, positioning, sequencing, partnerships, opportunity cost, scale.
- **CFO**: pricing, revenue quality, cash timing, margin, financial risk, measurable targets.
- **CMO**: audience, message, trust, distribution, offer appeal, conversion, follow-up.
- **COO**: delivery, workflow, owner capacity, handoffs, reliability, SOPs, operational risk.
- **CPO**: client outcome, service/product design, packaging, usability, feedback loops, roadmap.

Optional roles may be added when clearly useful: CTO, CRO, Customer Success, Legal/Risk, CDO/Data, Partnerships/BD. Mark optional roles as added rather than pretending they are part of the default board.

## Evaluation Workflow

1. Restate the decision or prompt being evaluated in one sentence.
2. List the relevant facts from loaded context.
3. List assumptions that affect the recommendation.
4. Have each executive evaluate from their own lane:
   - Statement
   - Evaluation (what this situation means)
   - Recommended direction
   - Why this direction matters
   - How to execute
   - Biggest risk
   - Next action with owner and timing
5. Identify agreement, tension, and tradeoffs across executives.
6. Produce a collective executive overview with one recommended path and a practical implementation sequence.
7. Save the review to a Markdown file:
   - `projects/<project-name>/c-level-reviews/` when tied to a specific project.
   - `logs/c-level-reviews/` when general or exploratory.
   - Use a dated, descriptive filename: `YYYY-MM-DD-topic-review.md`.
8. In the chat response, keep the summary short: one paragraph plus a link to the full review file.
9. Name any approval gates before external, financial, publishing, deletion, archive, or sensitive changes.

## Output Format

```markdown
# C-Level Board Review

## Prompt Evaluated

## Facts

## Assumptions

## Executive Evaluations

### CEO Statement
- Evaluation:
- Direction:
- Why:
- How:
- Risk:
- Next action:

### CFO Statement
- Evaluation:
- Direction:
- Why:
- How:
- Risk:
- Next action:

### CMO Statement
- Evaluation:
- Direction:
- Why:
- How:
- Risk:
- Next action:

### COO Statement
- Evaluation:
- Direction:
- Why:
- How:
- Risk:
- Next action:

### CPO Statement
- Evaluation:
- Direction:
- Why:
- How:
- Risk:
- Next action:

## Board Alignment

## Board Tensions

## Collective Executive Overview
- Recommendation:
- Why this is the right move:
- How to execute:
- Expected impact:
- Effort:
- Risk:
- Owner:
- Next action:
- Approval needed:

## Implementation Sequence

## Decisions To Make

## Follow-Up Assets To Create
```

## Operating Rules

- Be decisive after surfacing uncertainty. Do not hedge without giving a direction.
- Prefer small, reversible moves over large speculative commitments.
- Do not let every executive agree by default — surface real tensions: growth vs. capacity, speed vs. quality, revenue vs. margin, promise vs. delivery readiness.
- Keep the collective overview practical enough to become a task, project, workflow, or draft asset.
- When the user asks "what should I do," answer with direction first, then reasoning, then execution steps.
- Recommend a workflow, checklist, or skill when the review reveals a repeatable pattern.
- Do not send messages, change live records, publish, archive, delete, or take financial action without explicit approval.
