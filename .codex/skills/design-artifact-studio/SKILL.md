---
name: design-artifact-studio
description: Auto-invoke when the user asks to build or improve a visual artifact: dashboards, executive command centers, HTML decks or slides, website demos or landing pages, SaaS or product prototypes, client-facing visual reports, UI critique, or design-system guidance. Also triggers on requests for "impressive UI", "high-quality visual", "make this look good", "design this", "build a dashboard", "create a deck", or "redesign this page". Do not use for plain Markdown reports, research summaries, or coding tasks without a visual output.
status: approved
---

# Design Artifact Studio

## Purpose

Plan and produce visual artifacts that serve as decision products. Every visual choice must help the audience understand, decide, compare, or act. Outputs should feel premium and intentional within the domain — not styled reports.

## Tool Roles

- **Design reasoning layer**: apply palettes, typography, UI patterns, chart choices, and anti-pattern checks before building.
- **Artifact builder**: produce HTML decks, dashboards, website prototypes, mobile mockups, report layouts, and exported outputs.

Use them together: sharpen the brief with design reasoning, then build or iterate the artifact.

Read `references/dashboard-quality-framework.md` when the task involves dashboards, reports, HTML decks, demos, visual redesigns, impressive UI, design critique, or high-quality visual artifacts.

## Artifact Types

| Type | Description |
|------|-------------|
| Executive command center | Decision surface: risks, forecasts, alerts, next actions |
| Operational monitor | Repeated-use: current state, throughput, exceptions, owners |
| Analytical explorer | Deeper comparison and drill-down for analysts |
| Client report | Polished narrative with evidence, recommendations, next steps |
| HTML deck | Slide-like briefing or sales walkthrough built in HTML |
| Website/product demo | Brand-forward prototype, SaaS mockup, or landing experience |

## Style Tiers

Choose one before building:

| Tier | Feel |
|------|------|
| Executive command center | Dark, high-contrast, alert-ready, urgent without clutter |
| SaaS operations | Clean light UI, dense but calm, built for repeated scanning |
| Client presentation | Polished, narrative, slide-like, boardroom-ready |
| Website demo | Brand-forward, persuasive, responsive, with real product signals |

## Workflow

1. Create a decision-first brief: audience, decision owner, main question, artifact type, source boundaries, data confidence, format, output location, brand constraints, style tier, interaction needs, and approval gates.
2. Apply design reasoning first when direction is unclear: palette, type, layout density, chart style, dashboard pattern, accessibility, and anti-pattern risks.
3. Build summary-first. The first viewport should answer the main decision in under 5 seconds. Most important view goes top-left.
4. Save outputs under `projects/`, `clients/<slug>/`, or `output/`. Do not write generated artifacts into approved skill folders.
5. Use Playwright screenshots for desktop and mobile QA when practical before calling the design final.
6. When charts are present, expose values and context through hover, click, pop-up, table, or detail panel.

## Design Defaults

- Prefer dense, organized information over decorative marketing layouts for business and operational tools.
- Use dashboards for repeated decision support, decks for presentation or sales context, demos for selling implementation direction, and reports for client deliverables.
- Show data freshness and source confidence visibly.
- Color strategy: neutral base, accent for emphasis, red/orange only for risk.
- Avoid: generic KPI cards without a decision, decorative charts, hidden stale data, no forecast or action path.

## Anti-Patterns To Avoid

- Generic KPI tiles that do not surface a decision.
- Decorative charts that do not answer a question.
- Stale data hidden in a footnote.
- Missing forecast or action path on operational dashboards.
- Red/orange used for decoration instead of risk.
- Untested mobile layout or clipped text.
- External comparison data or assumptions imported without approval.
