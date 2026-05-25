# Skills Drafts

Proposed skills waiting for explicit approval. Skills here are **never invoked automatically**.

## How to Add a Draft Skill

```bash
python3 memory/scripts/skill_draft.py --name "skill-name" --description "what this skill does"
```

Or create the folder and `SKILL.md` manually:

```
.codex/skills-drafts/
  my-skill/
    SKILL.md
```

## SKILL.md Frontmatter Format

```yaml
---
name: skill-name
description: One-line description used for routing decisions.
status: draft
---
```

## How to Enable a Skill

1. Review the skill's `SKILL.md` thoroughly.
2. Move or copy the folder to `.codex/skills/`.
3. Change `status: draft` to `status: approved` in the frontmatter.
4. Run `python3 memory/scripts/register_assets.py` to update the registry.
5. Update `workflows/capability-routing.md` with the new routing trigger.

## Skills in This Folder

<!-- Updated automatically by register_assets.py -->
(empty — add skills as they are proposed during operation)
