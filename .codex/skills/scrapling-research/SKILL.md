---
name: scrapling-research
description: Auto-invoke when the user asks to scrape a website, extract content from a known URL, run a repeatable extraction, use CSS or XPath selectors to pull specific page elements, capture a web source as Markdown or JSON, crawl a small set of URLs, or conserve Firecrawl API credits by running local extraction instead. Also triggers when the user wants to save a public web source into a research or client folder.
status: approved
---

# Scrapling Research

## Purpose

Use Scrapling as a local, dependency-light extraction layer for repeatable public-source scraping. It complements search tools, Firecrawl, and Playwright by providing selector-based, adaptive, and browser-style fetching without burning hosted API credits.

## When To Use

Use Scrapling when:
- A known public URL needs repeatable extraction.
- CSS selectors, XPath, or text matching is needed to target specific elements.
- Hosted API credits (e.g. Firecrawl) should be conserved.
- Browser-style fetching or session handling is needed locally.
- Outputs should be saved directly into `clients/<slug>/sources/` or a research folder.

Do not use Scrapling for:
- Authenticated systems, login-gated content, or private sources without explicit approval.
- Form submissions or actions that change remote state.
- Sites where scraping violates terms of service.

## Default Research Stack

| Tool | Use for |
|------|---------|
| Search API (Brave, Serper, etc.) | Discovery — find relevant URLs |
| Official websites and public sources | Verification |
| Firecrawl | Hosted crawl/map/deep-research when API features save time |
| Playwright | Screenshots, visual QA, form behavior, browser state |
| Scrapling | Local repeatable extraction from known public URLs |

## Setup

Install Scrapling from the tools directory if present:

```bash
# macOS / Linux
python3 tools/scrapling/scripts/setup.sh

# Windows (PowerShell)
powershell.exe -ExecutionPolicy Bypass -File .\tools\scrapling\scripts\setup.ps1
```

Add browser fetchers only when session or JS rendering is needed:

```bash
# Windows
powershell.exe -ExecutionPolicy Bypass -File .\tools\scrapling\scripts\setup.ps1 -WithFetchers
```

Or install directly:

```bash
pip install scrapling
playwright install chromium  # only if browser fetching is needed
```

## Commands

Extract a full URL to a file:

```bash
# macOS / Linux
python3 tools/scrapling/scripts/extract-url.py --url "https://example.com" --output "vault/sources/example-home.md"

# Windows
python .\tools\scrapling\scripts\extract-url.py --url "https://example.com" --output "vault\sources\example-home.md"
```

Extract selector matches:

```bash
python3 tools/scrapling/scripts/extract-selector.py --url "https://example.com" --selector "main" --output "vault/sources/example-main.md"
```

Crawl a small known URL set:

```bash
python3 tools/scrapling/scripts/crawl-site.py --urls "https://example.com" "https://example.com/about" --output-dir "vault/sources/example/"
```

## Evidence Rules

- Treat scraped content as source material, not verified truth.
- Cite the original URL in every report or note that uses scraped content.
- Keep source files under `clients/<slug>/sources/` or `vault/sources/`.
- Mark unavailable or conflicting facts as `Unknown` or `Requires clarification`.
- Do not embed full page dumps into context — extract and distill only what is needed.
