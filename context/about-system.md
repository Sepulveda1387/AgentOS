# About This System

> Filled in during onboarding. Describes what this AI OS manages and which tools it connects to.

## What This OS Is For

- **Primary purpose:** [NOT SET]
- **Domain / context:** [NOT SET]

## Source-of-Truth Systems

List the tools that own the authoritative version of each data type. Add or remove rows as needed.

| Data type | System | Access level |
|-----------|--------|--------------|
| Email | [NOT SET] | read / write |
| Calendar | [NOT SET] | read / write |
| Tasks / projects | [NOT SET] | read / write |
| Documents / notes | [NOT SET] | read / write |
| CRM / contacts | [NOT SET] | read-only |
| Financial data | [NOT SET] | read-only |
| Code / repos | [NOT SET] | read / write |
| Other | [NOT SET] | |

## Tools and Platforms in Use

<!-- Filled from onboarding Q4. List the apps, CLIs, and APIs the user works with. -->

- [NOT SET]

## Excluded Tools

<!-- List tools that should NOT be connected or used, even if they seem relevant. -->

- None specified yet.

## Connection Notes

Each connected tool should have a dedicated file in `connections/<tool>.md` describing:
- What it does
- Read vs. write scope
- Approval gates
- CLI commands or API patterns if available

## Environment Variables

Credentials and API keys live in `.env` (gitignored). See `.env.example` for the list of supported variables.
