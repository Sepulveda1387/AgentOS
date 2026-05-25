---
name: frontend-motion
description: Auto-invoke when the user asks to add animation or motion to a website, dashboard, HTML deck, landing page, visual report, or UI prototype using Anime.js. Triggers on requests for smooth transitions, entrance animations, loading animations, chart animations, attention effects, sequential reveals, scroll-triggered motion, or any task where motion improves clarity, feedback, or perceived quality of a non-React visual artifact. Use motion-dynamic-views instead when the artifact is React-based.
status: approved
---

# Frontend Motion (Anime.js)

## Purpose

Use Anime.js motion when it improves a visual artifact's clarity, feedback, perceived quality, or narrative flow. Motion should have a job — it should not be decorative by default.

## Runtime

Default to the repo-local runtime when present:

```text
tools/animejs-runtime/
```

Install globally if the local runtime is not available:

```bash
npm install animejs
# or via CDN in HTML
<script type="module">
  import { animate } from 'https://cdn.jsdelivr.net/npm/animejs/+esm';
</script>
```

## When To Use

Use this skill when the task involves:
- Website or landing-page entrance/scroll animations.
- Dashboard state change, alert flash, chart reveal, or data-refresh feedback.
- HTML deck or presentation slide transitions.
- SaaS or product prototype interaction polish.
- Client-facing visual report motion and reveal sequences.
- Evaluating whether motion belongs in a visual artifact.

Do not use it for React-based UIs (use `motion-dynamic-views` instead), backend work, CRM/API operations, static Markdown reports, or anything where motion does not affect the user experience.

## Motion Jobs

Choose one before adding animation:

| Job | Description |
|-----|-------------|
| Attention | Draw the eye to what matters most |
| State change | Communicate a shift in system or data state |
| Loading or refresh | Provide feedback while data loads |
| Feedback | Confirm user actions (click, hover, submit) |
| Reveal sequence | Guide attention through a narrative |
| Continuity | Smooth transitions between states or sections |
| Restrained delight | Add polish without distraction |

## Workflow

1. Define the motion job from the table above.
2. Use `design-artifact-studio` when the artifact is client-facing or needs design judgment.
3. Import from the local runtime or the npm package:
   ```js
   import { animate } from '../../tools/animejs-runtime/vendor/animejs/modules/index.js';
   // or
   import { animate } from 'animejs';
   ```
4. Respect reduced-motion preferences for all user-facing interfaces.
5. Keep durations short for operational dashboards; avoid text/content overlap.
6. Verify with a browser console check and a desktop/mobile layout review for client-facing work.

## Import Example

```js
import { animate } from 'animejs';

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!reduceMotion) {
  animate('.js-reveal', {
    opacity: [0, 1],
    translateY: [8, 0],
    duration: 420,
    easing: 'out(3)',
  });
}
```

## Risk Guardrails

- Do not add CDN dependencies to production client-facing work without approval.
- Do not use motion to hide stale data, missing source confidence, or unclear decisions.
- Do not let animation block dashboard refreshes, financial views, or client-critical controls.
- Always include a reduced-motion path for accessibility.
