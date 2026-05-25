---
name: playwright
description: Auto-invoke when the user asks to take a screenshot of a website or UI, visually verify a page on desktop or mobile, test browser interactions, check how a design looks in a real browser, capture a before/after comparison, automate a browser workflow, fill out a form, click through a user journey, test navigation, or perform any task that requires controlling a real browser. Also triggers on requests to "check how this looks", "screenshot the page", "test this in a browser", "verify the mobile layout", or "automate the browser".
status: approved
---

# Playwright

## Purpose

Use Playwright to control a real browser for screenshots, visual QA, interaction testing, browser automation, and user journey verification. It is the authoritative tool for confirming that visual artifacts, web apps, and UI changes actually work as expected in a real browser environment.

## When To Use

Use Playwright when:
- A screenshot of a page or UI component is needed (desktop or mobile).
- Visual QA on a web artifact before delivery or after a change.
- A browser interaction needs to be tested: clicking, filling forms, navigating, scrolling.
- Mobile layout or responsive behavior needs verification.
- A before/after visual comparison is needed.
- A user journey or workflow needs browser automation.
- A web page needs to be scraped with full JavaScript execution (complement to Scrapling).

## Setup

Install Playwright and browser binaries:

```bash
pip install playwright
playwright install chromium
# or install all browsers
playwright install
```

For Node.js projects:

```bash
npm install -D @playwright/test
npx playwright install chromium
```

## Common Patterns

### Take a screenshot (Python)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="output/screenshot-desktop.png")
    browser.close()
```

### Mobile viewport screenshot

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 390, "height": 844})
    page.goto("https://example.com")
    page.screenshot(path="output/screenshot-mobile.png")
    browser.close()
```

### Click and interact

```python
page.click("button#submit")
page.fill("input[name='email']", "user@example.com")
page.wait_for_selector(".confirmation-message")
```

### Full-page screenshot

```python
page.screenshot(path="output/full-page.png", full_page=True)
```

### Playwright CLI (quick screenshot)

```bash
playwright screenshot --browser chromium https://example.com output/screenshot.png
```

## QA Workflow

When verifying a visual artifact or UI change:

1. Take a desktop screenshot at standard width (1280px or 1440px).
2. Take a mobile screenshot at a common mobile size (390×844 for iPhone-size, 375×667 for smaller devices).
3. Check for: clipped text, broken layout, empty sections, misaligned elements, color contrast issues.
4. Test interactive elements: hover states, click behavior, modal/popover open/close.
5. Confirm data labels and chart values are readable.
6. Save screenshots to `output/` or `logs/qa/` with descriptive names.

## Evidence Rules

- Always report what was actually observed — not what was expected.
- Attach screenshots as evidence when claiming a design is correct, fixed, or ready.
- If behavior is unexpected, capture the error state and describe it before claiming done.
- Never claim a UI is verified without at least one screenshot from a real browser run.

## Risk Guardrails

- Do not use Playwright to interact with production systems, submit real forms, or take live actions without explicit approval.
- Do not store screenshots containing sensitive user data.
- Use `--headed` mode locally when you need to observe behavior in real time; use headless for automated runs.
