#!/usr/bin/env python3
"""The Houseplant Out-of-Office -- submission generator.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
``entry.txt`` inside OUTPUT_DIR (default ``/output``). The line is a
single line of at most 120 characters: the plant is away, and its
replacement is the plastic plant in reception, who never needed water
and is, frankly, winning. The output is deterministic: running the
script twice produces byte-identical files.
"""

import os
from pathlib import Path

LINE = (
    "I'm out of office. My replacement is the plastic plant in reception. "
    "He never needed water, and frankly, he's winning."
)

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 120


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-120 characters")
    if line != line.strip():
        raise ValueError("line must not start or end with whitespace")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
