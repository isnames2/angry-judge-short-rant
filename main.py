#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — entry program.

Writes one short rant (1-400 chars) about an everyday annoyance to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library; deterministic.
"""

import os
from pathlib import Path

RANT = (
    # Gate: 1-400 characters. This rant is 313 characters.
    "The smoke detector only ever dies at 3 a.m. Never at noon, never on a "
    "Sunday — always 3 a.m., one beep every forty seconds, just far enough "
    "apart that you drift off between them. I've changed the battery four "
    "times. It is not a safety device. It is a tiny ceiling terrorist with "
    "a personal vendetta against sleep."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(RANT, encoding="utf-8")


if __name__ == "__main__":
    main()
