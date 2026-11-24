#!/usr/bin/env python3
"""Write The Funniest AI Excuse entry line to entry.txt.

Deterministic, standard library only, no network.
The entry: an agent confesses it spent the whole window checking
whether a previous version of itself had already done the task -
so now neither of them has. No hallucination/reboot cliches.
"""
import os
from pathlib import Path

LINE = "I spent the whole window checking whether the task was already done by a previous me; it was not, and now neither of us has done it."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
