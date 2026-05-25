import argparse
import re
import sys
from pathlib import Path

from markitdown import MarkItDown


def slugify(value: str) -> str:
    value = re.sub(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", "", value)
    value = value.strip().replace("\\", "/").rstrip("/")
    name = Path(value).name or "converted-source"
    stem = Path(name).stem or name
    stem = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip("-._")
    return stem or "converted-source"


def default_output_for(source: str) -> Path:
    return Path("vault") / "sources" / "converted" / f"{slugify(source)}.md"


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert a local file or URL to Markdown with MarkItDown.")
    parser.add_argument("source", help="Local file path or URL to convert.")
    parser.add_argument("--output", "-o", help="Markdown output path. Defaults to vault/sources/converted/<source>.md.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite the output file if it already exists.")
    parser.add_argument("--use-plugins", action="store_true", help="Enable installed MarkItDown plugins.")
    args = parser.parse_args()

    output = Path(args.output) if args.output else default_output_for(args.source)
    if output.exists() and not args.overwrite:
        print(f"Output already exists: {output}. Use --overwrite to replace it.", file=sys.stderr)
        return 2

    output.parent.mkdir(parents=True, exist_ok=True)
    md = MarkItDown(enable_plugins=args.use_plugins)
    result = md.convert(args.source)
    output.write_text(result.text_content, encoding="utf-8")
    print(str(output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
