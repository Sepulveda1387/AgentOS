# Capability Routing

The AI uses this workflow to infer the right skill or workflow from any request. The user should not need to name skills or use special commands.

---

## Routing Logic

1. Read the request.
2. Identify the primary intent from the table below.
3. Select the skill or workflow.
4. If the request spans multiple areas, combine capabilities.
5. State the selected path in the user-facing response when it adds clarity.
6. Log the work as a usage event after completion.

---

## Intent → Capability Map

| If the user says / asks about… | Route to |
|--------------------------------|----------|
| Plan my day, start the morning, what should I focus on | `daily-operating-loop` workflow |
| Weekly review, what happened this week, weekly planning | `weekly-review` workflow |
| Something is broken, not working, authentication failing, error | `systematic-debugging` skill |
| Research [company/person/topic], prep for a call, background on | `research` skill draft or web research |
| Financial analysis, pricing, margin, cash timing, forecast economics, spend review | `cfo-financial-risk-analyst` skill |
| Operations, workflow bottlenecks, capacity, handoffs, SOPs, delivery reliability | `coo-business-operations-analyst` skill |
| Funnel, messaging, CTA hierarchy, lead magnets, SEO/AEO, nurture, conversion friction | `cmo-funnel-messaging-analyst` skill |
| Productized service, offer scope, deliverables, onboarding, client/user journey, feedback loop | `cpo-offer-client-experience-analyst` skill |
| Pipeline, deals, revenue conversion, sales follow-up, CRM hygiene, forecast confidence | `cro-pipeline-revenue-analyst` skill |
| Claims, compliance, contracts, privacy, regulated topics, public promise risk | `legal-risk-compliance-claims-analyst` skill + `business-risk-review` when stakes are high |
| Dashboard accuracy, data quality, KPI definitions, reporting gaps, source-of-truth mapping | `cdo-data-quality-analyst` skill |
| Write [email/message/proposal/content], draft, reply | Content drafting — ask before sending |
| Review [document/code/plan/design] | Review skill or inline analysis |
| Help me think through / should I / what would you do / what are the risks | `c-level` skill — executive board review |
| Board review, C-suite perspective, CEO/CFO/CMO/COO/CPO evaluation, strategic recommendation | `c-level` skill |
| Which AI model should we use, AI prompt strategy, paid AI API, model cost, credits, KIE, generate ads/docs/social without losing intent | `chief-ai-engineering` skill |
| Watch a video, learn from a training recording, summarize a tutorial, extract frames/transcript, validate video claims, turn a video into workflow/skill | `video-research-ingestion` skill |
| Patterns, self-learning, what should we automate, what keeps coming up, what have you noticed | `self-learning-review` skill |
| Audit AgentOS, review this operating system, score the system, find OS gaps, improve AgentOS | `agentos-audit` workflow |
| Use subagents, delegate this, parallel agents, create helper agents, split work across roles | `subagent-delegation` workflow |
| Onboarding is incomplete / re-run setup | `onboarding` workflow |
| Add/update context, remember this, note that | Update relevant `context/` file |
| Search memory, what do we know about | `python3 memory/scripts/search_memory.py` |
| Create a skill, make this a skill, automate this, this keeps coming up | `skill-creator` skill |
| Connect [tool], add integration, API | `connections/` file + approval gate check |
| Convert a file, read a PDF, extract from Word/Excel/PowerPoint, summarize a document, convert URL | `markitdown` skill |
| Scrape a website, extract from a URL, CSS selector extraction, crawl pages, save web source | `scrapling-research` skill |
| Use an AI vendor, add a new model, validate model-specific commands, compare model capabilities, create a model card | `chief-ai-engineering` skill + connection doc if needed |
| Take a screenshot, visual QA, test in browser, check mobile layout, browser automation, verify UI | `playwright` skill |
| Add animation, add motion, animate this, entrance effect, page transition (non-React) | `frontend-motion` skill |
| React animation, Framer Motion, Motion, animated React component, scroll animation, layout transition | `motion-dynamic-views` skill |
| Build a dashboard, create a deck, website demo, visual report, design this, impressive UI, SaaS prototype | `design-artifact-studio` skill |

---

## Combining Capabilities

When a request crosses functions, apply lenses in sequence:

- **Advisory + risk**: give the recommendation, then surface the top risk.
- **Research + advisory**: compile what is known, then advise on the decision.
- **Execution + verification**: complete the task, then verify before claiming done.
- **Content + approval**: draft the content, then pause for approval before sending.
- **Client-facing deliverable**: use `service-delivery-qa` before presenting, publishing, or relying on the asset.
- **Sensitive or external-system change**: use `business-risk-review` before proposing or taking action.
- **Completion claim**: use `verification-before-completion` before saying work is complete, ready, migrated, fixed, or indexed.
- **Delegated work**: use `subagent-delegation`, then synthesize in the main AgentOS thread before acting.
- **AgentOS change**: use `agentos-audit` when reviewing system gaps, then refresh memory and verify indexes after durable edits.

---

## When No Route Matches

If the request doesn't match any known capability:

1. Respond directly using best judgment.
2. If the request recurs, flag it: "This seems like a repeatable task — want me to draft a skill or workflow for it?"
3. Log the event so it appears in pattern analysis.

---

## Fallback Behavior

If context is missing that would improve the response:
- State what you know and what you're inferring.
- Ask one clarifying question.
- Do not block on missing context if a reasonable default applies.

---

## Routing Triggers: Conservative Approach

Only invoke a specialized skill when the request clearly matches. Avoid triggering skills for loose keyword matches. When in doubt, respond directly and note that a more specialized capability could be applied if useful.
