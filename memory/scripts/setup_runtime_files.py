from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ENV_EXAMPLE = ROOT / ".env.example"
ENV_FILE = ROOT / ".env"
GITIGNORE = ROOT / ".gitignore"


LOCAL_GITIGNORE = """# Environment and local secrets
.env
.env.local
.env.*.local
credentials/
*.json.key
*.pem
*.key
service-account*.json
token.json
token*.pickle

# Generated SQLite sidecars
memory/*.db-*

# Python/runtime caches
__pycache__/
*.pyc
*.pyo
.venv/
venv/
*.egg-info/
dist/
build/

# Tool/cache output
cache/
.cache/
.claude/scratch/
.claude/tmp/

# OS/editor files
.DS_Store
.DS_Store?
Thumbs.db
ehthumbs.db
.vscode/settings.json
.idea/
*.swp
*.swo
"""


def main() -> None:
    if not ENV_FILE.exists():
        if ENV_EXAMPLE.exists():
            shutil.copyfile(ENV_EXAMPLE, ENV_FILE)
            print("Created .env from .env.example.")
        else:
            ENV_FILE.write_text("# AgentOS local environment\n", encoding="utf-8")
            print("Created minimal .env.")
    else:
        print(".env already exists; left unchanged.")

    GITIGNORE.write_text(LOCAL_GITIGNORE, encoding="utf-8")
    print("Wrote local .gitignore safety rules.")


if __name__ == "__main__":
    main()
