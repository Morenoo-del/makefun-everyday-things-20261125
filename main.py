#!/usr/bin/env python3
"""Everyday Things, Two Lines — entry program.

Writes a two-line explanation of a traffic jam to /output/entry.txt.
Line 1 explains it to a 10-year-old in one vivid sentence built on an
analogy; line 2 says what the analogy maps and what it leaves out.
"""

import os

ENTRY = (
    "A traffic jam is a parking lot that forgot it was a road, so all the cars "
    "just sit there, engines humming, going nowhere.\n"
    "It maps the stopped cars and the waiting, but leaves out that a real "
    "parking lot never minds staying put, while every driver here is in a hurry."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 400 characters.
    assert 1 <= len(ENTRY) <= 400, f"entry is {len(ENTRY)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
