# Dashboard Quality Framework

Use this reference only for dashboards, reports, HTML decks, demos, visual redesigns, impressive UI, design critique, or high-quality visual artifacts.

---

## Standard

Visual outputs from this system are decision products. They must help a specific audience understand the current state, decide what matters, and act with confidence. They should feel impressive within the domain without adding decoration that does not support the decision.

---

## Decision-First Brief

Before building, define:

- Audience and decision owner.
- Main question the artifact must answer.
- Artifact type: executive command center, operational monitor, analytical explorer, client report, HTML deck, or website/product demo.
- Data sources, source boundaries, data freshness, and confidence level.
- Style tier: executive command center, SaaS operations, client presentation, or website demo.
- Required interactions: hover, click, pop-up, filter, drill-down, tabs, or table detail.
- Output files and QA requirements.

---

## Quality Rubric

Score each item from 1 to 5 before delivery:

- **Audience**: designed for the real decision maker, not generic viewers.
- **Decision**: first viewport answers the main question in under 5 seconds.
- **Data model**: numbers match source payloads, stale data is visible, assumptions are explicit.
- **Layout**: summary flows to detail, top-left carries the primary view, sections scan cleanly.
- **Visual hierarchy**: strong contrast between primary, secondary, and supporting information.
- **Chart choice**: each chart has a job — trend, comparison, composition, control, forecast, funnel, concentration, or cash timing.
- **Interaction**: charts expose values and context through hover, click, pop-up, table, or detail panel.
- **Story**: includes what happened, why it matters, what is next, and what data is missing when relevant.
- **Polish**: visually intentional, premium, and domain-appropriate without empty decoration.
- **Accessibility**: readable text, meaningful color, adequate contrast, keyboard-safe modal behavior where practical.
- **QA**: desktop/mobile screenshots reviewed, clipped text checked, chart labels readable, interactions tested.

---

## Chart Selection Matrix

| Job | Chart type |
|-----|-----------|
| Trend over time | Line, area, or small multiples |
| Category comparison | Bar or ranked bar |
| Part-to-whole | Stacked bar, treemap, or donut (few categories only) |
| Concentration | Ranked horizontal bars with percentage of total |
| Funnel | Staged conversion with counts, value, and loss points |
| Forecast | Line with projection band, scenario table, or waterfall |
| Cash timing | Calendar, waterfall, runway strip, or dated obligation table |
| Control/threshold | Bullet chart, gauge sparingly, status band, or target line |

---

## Required Dashboard Qualities

- First viewport answers the main decision.
- Data freshness and source confidence are visible.
- Current state, forecast, risk/alerts, priority actions, and data gaps appear when relevant.
- Charts expose values, assumptions, and drill-down context on hover or click.
- Color has meaning: neutral base, accent for emphasis, red/orange only for risk.
- Visual energy comes from hierarchy, spacing, type, charts, and motion/interactions — not decoration.

---

## Anti-Patterns

- Generic KPI cards without a decision.
- Decorative charts that do not answer a question.
- Flat text-only dashboards when graphs would clarify comparison or trend.
- Stale data hidden in a footnote.
- No forecast or action path for operational dashboards.
- Red/orange used as decoration instead of risk.
- One-note palette with weak hierarchy.
- Untested mobile layout, clipped text, unreadable labels, or broken modals.

---

## QA Checklist

- Capture desktop screenshot.
- Capture mobile screenshot.
- Test hover/click behavior for interactive charts.
- Check chart labels, clipped text, contrast, empty whitespace, and first-viewport clarity.
- Confirm key numbers match source payloads.
- Add a short evaluator note comparing the output against this framework.
