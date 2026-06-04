# Subagent Delegation

Status: active reference

## Purpose

Use specialized helper agents when a task benefits from parallel expertise, clean separation of work, or an independent review. The goal is better output and faster progress, not more coordination overhead.

## Default Rule

Do not delegate by default. Use subagents only when the user asks for them, approves delegation, or the work clearly benefits from separate scopes that can be synthesized by the main AgentOS thread.

## Reusable Agent Roles

| Agent role | Use when | Output expected |
| --- | --- | --- |
| CEO lens | Strategy, direction, prioritization, tradeoffs, scale | Recommendation, risks, decision options, next move |
| CFO lens | Pricing, revenue, payment flow, reporting, margins | Numbers, assumptions, revenue impact, tracking recommendation |
| CMO lens | Content, ads, positioning, campaigns, lead magnets | Audience insight, message, channel plan, conversion recommendation |
| COO lens | Onboarding, SOPs, delivery, tools, workflow design | Process map, handoffs, checklist, failure points, implementation plan |
| CPO lens | Productized services, client experience, product capability | Offer shape, user journey, feature requirements, feedback loop |
| CTO / Implementer | Code, automation, integrations, local tool setup | Changed files, technical tradeoffs, verification notes |
| Researcher | Market, company, tool, or source-backed research | Brief with facts, assumptions, sources, confidence, open questions |
| Reviewer | Quality, risk, delivery, code, claims, or readiness review | Findings first, severity, evidence, suggested fix |
| Domain Expert | Specialized knowledge defined during onboarding | Domain-specific diagnosis and recommended next action |

## Delegation Rules

- Give each subagent one role, one scope, and one output format.
- Assign disjoint files, systems, audiences, or responsibilities when implementation is involved.
- Keep the main AgentOS thread responsible for synthesis, decisions, user communication, durable updates, and verification.
- Do not let subagents send messages, change external records, publish content, edit approved skills, delete/archive files, handle credentials, or take financial actions without explicit user approval.
- Capture durable decisions and reusable patterns in `context/`, `workflows/`, `docs/`, `logs/`, or draft skills after synthesis.

## Context To Provide Before Delegation

- The business or user goal.
- Relevant source files, commands, links, or search results.
- Current assumptions and unknowns.
- Approval boundaries and forbidden actions.
- The exact output format needed.

## Synthesis Checklist

After delegated work returns:

- Separate verified facts from assumptions.
- Resolve conflicts between agents instead of pasting both answers.
- Identify what changed, what was learned, and what still needs a human decision.
- Run the relevant verification check before claiming completion.
- Log the pattern if the work suggests a recurring checklist, workflow, or skill.

## Good First Uses

- CMO drafts content angles while COO maps the capture workflow.
- CFO evaluates pricing options while CMO writes offer positioning.
- Researcher builds a source-backed brief while Implementer prepares local docs.
- Reviewer checks a workflow, proposal, or code change before it becomes relied-on.

