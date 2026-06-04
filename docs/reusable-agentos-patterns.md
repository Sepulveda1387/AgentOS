# Reusable AgentOS Patterns

These patterns are portable best practices for adapting AgentOS to another person, team, business, or project. They should be adapted to the user's context rather than copied as private source-of-truth.

## Operating Patterns

- **Startup gate:** identify the request type, accountable lens, routing path, approval gates, and verification check before acting.
- **CLI and index first:** use local commands, memory search, and structured indexes before broad manual reading or external tools.
- **Draft before acting:** messages, workflows, skills, public content, and external-system changes stay draft-only until approved.
- **Verification before completion:** do not claim complete, ready, fixed, indexed, connected, or current without a concrete check.
- **Memory after durable change:** refresh the Markdown index and asset registry after changing docs, workflows, skills, or operating rules.
- **Facts versus assumptions:** label verified facts, inferred assumptions, unknowns, and next verification steps.
- **Small reversible improvements:** prefer narrow changes that can be inspected and rolled back.

## Agent Patterns

- **Parent lens first:** use broad executive or domain lenses for ambiguous strategy and prioritization.
- **Specialist analyst second:** use narrow analysts for recurring, evidence-heavy diagnosis with a clear output format.
- **Reviewer role:** use an independent reviewer for quality, risk, code, claims, or delivery readiness before important handoff.
- **Researcher role:** require source-backed facts, confidence, assumptions, and open questions.
- **Implementer role:** require changed files, verification commands, and remaining blockers.
- **Main-thread synthesis:** delegated work is input. The main AgentOS thread owns synthesis, final recommendation, durable context, and user communication.

## Suggested Specialist Bench

| Specialist | Use when |
| --- | --- |
| CFO Financial Risk Analyst | Pricing, margin, cash timing, budget, financial exposure, revenue quality |
| COO Business Operations Analyst | Workflow diagnosis, capacity, SOPs, handoffs, delivery reliability |
| CMO Funnel / Messaging Analyst | CTA clarity, nurture, SEO/AEO, content, ads, conversion friction |
| CPO Offer / Experience Analyst | Productized service scope, deliverables, onboarding, feedback loops |
| CRO Pipeline / Revenue Analyst | Lead quality, sales follow-up, CRM hygiene, forecast confidence |
| Legal/Risk Compliance Analyst | Claims, privacy, contracts, regulated topics, public promises |
| CDO Data Quality Analyst | KPI definitions, dashboard trust, source mapping, reporting gaps |
| CTO Implementer | Scoped code, automation, integrations, build-vs-buy, technical verification |

## When To Create A New Capability

- Create a **workflow** when the steps are deterministic and repeatable.
- Create a **checklist** when the work is human-led but easy to forget.
- Create a **draft skill** when the task needs specialized judgment, commands, references, or recurring source context.
- Create a **connection note** when a tool has read/write boundaries, credential rules, source-of-truth behavior, or safe test commands.
- Create an **audit workflow** when the system itself needs periodic review.

## Anti-Patterns

- Adding agents because a topic sounds important but has no repeated work pattern.
- Letting helper agents make external changes or user-facing sends.
- Copying private business context into a portable OS template.
- Reading large folders before checking memory/search indexes.
- Treating generated skills as approved before the user explicitly enables them.
- Claiming a system is connected or ready when only local scaffolding exists.

