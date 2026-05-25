# Connections

Per-tool integration rules and approval gates. Create one file per connected tool.

## File Structure

Each file should cover:
- What this tool does and what data it owns
- Read vs. write scope
- Actions that require explicit approval
- CLI commands or API patterns if available
- Credentials location (reference `.env` key name only — never paste values)

## Example File Names

- `connections/google-workspace.md`
- `connections/github.md`
- `connections/slack.md`
- `connections/notion.md`
- `connections/hubspot.md`

Create files here as you connect tools during or after onboarding.
