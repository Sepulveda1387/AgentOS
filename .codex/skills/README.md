# Approved Skills

Skills in this folder are active and may be invoked when a request clearly matches their trigger.

Skills start in `.codex/skills-drafts/` and are promoted here only after explicit user approval.

## How to Use Skills

The AI routes to skills automatically based on request intent. You do not need to name them. If you want to explicitly invoke a skill, you can say "use the [skill-name] skill" or "run [skill-name]."

## How to Disable a Skill

1. Move the skill folder back to `.codex/skills-drafts/`.
2. Change `status: approved` to `status: draft` in `SKILL.md`.
3. Run `python3 memory/scripts/register_assets.py`.
4. Update `workflows/capability-routing.md` to remove or adjust the routing trigger.

## Active Skills

| Skill | Purpose |
|-------|---------|
| `c-level` | Executive board review and strategic recommendations |
| `chief-ai-engineering` | AI model selection, prompt strategy, paid API guardrails, and model-specific validation |
| `video-research-ingestion` | Convert videos, tutorials, webinars, and training recordings into verified operating knowledge |
| `markitdown` | Convert non-plain-text documents and URLs into Markdown |
| `scrapling-research` | Local-first web extraction and scraping |
| `playwright` | Browser automation, screenshots, and visual QA |
| `frontend-motion` | Anime.js motion for non-React artifacts |
| `motion-dynamic-views` | Motion/Framer Motion patterns for React views |
| `design-artifact-studio` | High-quality dashboards, decks, demos, and visual artifacts |
| `skill-creator` | Draft and structure reusable skills |
| `self-learning-review` | Pattern analysis and system improvement recommendations |
| `business-risk-review` | Operational, security, privacy, credential, compliance, financial, and client-trust risk review |
| `service-delivery-qa` | Quality check for client-facing or operationally important deliverables before use |
| `systematic-debugging` | Root-cause debugging for failing tools, workflows, CLIs, APIs, memory, and integrations |
| `verification-before-completion` | Evidence gate before claiming work is complete, fixed, ready, migrated, or indexed |
| `cfo-financial-risk-analyst` | Financial analysis, revenue quality, cash timing, pricing, margin, and financial risk |
| `coo-business-operations-analyst` | Workflow diagnosis, capacity, handoffs, SOPs, delivery reliability, and operational risk |
| `cmo-funnel-messaging-analyst` | Funnel analysis, positioning, CTA consistency, SEO/AEO, nurture, and conversion risk |
| `cpo-offer-client-experience-analyst` | Productized-service design, offer scope, client journey, delivery artifacts, and feedback loops |
| `cro-pipeline-revenue-analyst` | Pipeline analysis, lead quality, sales follow-up, revenue conversion, and forecast confidence |
| `legal-risk-compliance-claims-analyst` | Claims review, compliance risk, contract language, privacy, and public promise risk |
| `cdo-data-quality-analyst` | Data quality, dashboard reliability, metric definitions, source mapping, and reporting risk |
