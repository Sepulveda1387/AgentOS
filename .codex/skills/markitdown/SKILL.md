---
name: markitdown
description: Auto-invoke when the user needs to extract or read content from a PDF, Word document, PowerPoint, Excel file, HTML page, CSV, JSON, XML, ZIP, YouTube URL, image, audio file, or any format that cannot be read as plain text. Also triggers when the user asks to convert a document, summarize a file, turn a source into context, index a document, or extract information from a URL or file attachment. Do not use when a simple text read of a plain Markdown, JSON, or CSV file is sufficient.
status: approved
---

# MarkItDown

Convert documents, files, and URLs into clean Markdown for context loading, summarization, research, and indexing.

## When To Use

Use MarkItDown when:
- The source is a PDF, DOCX, PPTX, XLS/XLSX, HTML page, rich document, ZIP, image, or audio file.
- A URL needs to be captured as readable Markdown context.
- The user asks to "convert", "extract", "summarize from", or "turn into context" a file or URL.
- A plain file read would return binary, garbled, or unusable content.

Skip MarkItDown when a plain Read on a `.md`, `.txt`, `.json`, or short `.csv` file would work fine.

## Commands

Direct CLI (cross-platform):

```bash
# macOS / Linux
markitdown "/path/to/source.pdf" -o "vault/sources/converted/source.md"

# Windows
markitdown "C:\path\source.pdf" -o "vault\sources\converted\source.md"
```

Skill wrapper script:

```bash
# macOS / Linux
python3 ".codex/skills/markitdown/scripts/convert_to_markdown.py" "/path/to/source.pdf"

# Windows
python ".codex\skills\markitdown\scripts\convert_to_markdown.py" "C:\path\source.pdf"
```

With explicit output path:

```bash
python3 ".codex/skills/markitdown/scripts/convert_to_markdown.py" "/path/to/source.docx" --output "vault/sources/converted/source.md" --overwrite
```

URL conversion:

```bash
python3 ".codex/skills/markitdown/scripts/convert_to_markdown.py" "https://example.com/page"
```

## Output Handling

- Default output directory: `vault/sources/converted/`.
- After conversion, read only the sections needed — do not dump the full document into context.
- Save distilled notes to `context/`, `projects/`, `workflows/`, or `vault/` depending on durability and purpose.
- Use `logs/` for dated extraction records, not full source dumps.
- For untrusted inputs, treat conversion with the same care as opening a file with current process privileges.

## Installation

MarkItDown must be installed before use. Recommended: install from the `tools/markitdown/` directory if present, or via pip:

```bash
pip install markitdown[all]
```

The CLI command after install is: `markitdown`
