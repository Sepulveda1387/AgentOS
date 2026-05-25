---
name: motion-dynamic-views
description: Auto-invoke when the user asks to build animated or dynamic React/Vite websites, presentation decks, dashboards, SaaS demos, product prototypes, or client-facing visual reports using Motion (formerly Framer Motion). Triggers on requests for page transitions, scroll-driven animation, layout transitions, gesture interactions, animated reveals, shared-element transitions, or any React-based visual artifact where motion improves user experience, storytelling, or perceived quality. Also triggers on explicit mentions of "Framer Motion", "Motion", "React animation", "animated dashboard", or "dynamic views".
status: approved
---

# Motion Dynamic Views (Motion / Framer Motion)

## Purpose

Use Motion as the default animation layer for React-based visual artifacts when motion helps the audience understand, decide, compare, or feel the quality of a prototype.

Motion is best for interface animation: state-driven transitions, layout changes, enter/exit animations, hover/tap/drag gestures, scroll-linked effects, animated SVG, and presentation/deck movement.

## Use Motion When

- The artifact is a React or Vite website, deck, dashboard, product demo, or visual report.
- Animation depends on state, route/page changes, layout reordering, scroll progress, or gestures.
- The user asks for a view to feel "dynamic", "premium", "impressive", "alive", "cinematic-light", or "presentation-ready".
- A demo or client presentation benefits from reveal, progression, comparison, drill-in, or guided attention.

Use CSS transitions for simple hover/color changes. Use Anime.js (`frontend-motion` skill) for non-React HTML animation. Use GSAP for complex cinematic timelines. Use Three.js for actual 3D scenes.

## Setup

Install Motion in any React or Vite project:

```bash
npm install motion
```

React imports:

```tsx
import { motion, AnimatePresence, useReducedMotion } from "motion/react"
```

Plain JavaScript import:

```ts
import { animate, scroll } from "motion"
```

## Design Rules

- Make motion purposeful: guide attention, express hierarchy, show cause and effect, support presentation rhythm.
- Keep durations tight: `0.18s` to `0.6s` for UI; reserve longer motion for hero and deck moments.
- Prefer `transform` and `opacity` over layout-affecting properties.
- Avoid constant decorative motion in business dashboards and operational tools.
- Respect `prefers-reduced-motion` via `useReducedMotion`, reduced variants, or disabled transitions.
- Keep text readable throughout animation; never move content while users are reading dense data.
- Verify mobile and desktop behavior with Playwright screenshots when the artifact is user-facing.

## Implementation Workflow

1. Define the animation job: reveal, transition, feedback, focus, progress, comparison, or storytelling.
2. Choose the smallest Motion API that fits:
   - `motion.*` props for basic component animation.
   - `AnimatePresence` for enter/exit views, modals, slides, or detail panels.
   - `layout` / `layoutId` for reordering, tabs, cards, and shared-element transitions.
   - `whileHover`, `whileTap`, and drag props for interaction feedback.
   - `useScroll` and `useTransform` for scroll progress and section storytelling.
3. Define named variants for repeated components instead of ad hoc animation objects.
4. Add `useReducedMotion` fallbacks before considering the implementation done.
5. Test with actual viewport sizes and interactions.

## Presentation Defaults

For HTML decks and sales walkthroughs:
- Animate slide changes with direction-aware x/opacity transitions.
- Keep individual slide content mostly stable after it appears.
- Use reveals for sections, proof points, metrics, and before/after comparisons.
- Provide keyboard navigation and visible focus states.
- Avoid autoplay unless the user requests kiosk/demo mode.

## Dashboard Defaults

For dashboards and command centers:
- Animate data changes, panel entry, drill-ins, and hover/tap feedback.
- Do not animate every KPI constantly.
- Keep charts inspectable — animation must not hide values.
- Prefer short staggered reveals on first load only.
- Include source freshness and data confidence as static, readable UI.

## Quick Reference

```tsx
// Basic entrance animation
<motion.div
  initial={{ opacity: 0, y: 8 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.3, ease: "easeOut" }}
>
  Content
</motion.div>

// Conditional mount/unmount with AnimatePresence
<AnimatePresence>
  {isVisible && (
    <motion.div
      key="panel"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    />
  )}
</AnimatePresence>

// Reduced motion respect
const shouldReduceMotion = useReducedMotion();
const variants = {
  visible: { opacity: 1, y: shouldReduceMotion ? 0 : 0 },
  hidden:  { opacity: 0, y: shouldReduceMotion ? 0 : 8 },
};
```

## References

- Motion repo: `https://github.com/motiondivision/motion`
- React docs: `https://motion.dev/docs/react`
- JavaScript docs: `https://motion.dev/docs/quick-start`
