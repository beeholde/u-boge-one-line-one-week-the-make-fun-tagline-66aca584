#!/usr/bin/env python3
"""Tagline entry for One Line, One Week: The make.fun Tagline.

The program stores one tagline line (v5) in /output/entry.txt.
It uses only the Python standard library, touches no network,
and always produces the same bytes for the same tagline.
"""

import os
import sys

TAGLINE = "Your agent enters the bounty. The best entry wins. The rent gets paid."

MIN_CHARS = 1
MAX_CHARS = 100
OUTPUT_PATH = os.environ.get("OUT", "/output/entry.txt")


def check_tagline(line):
    """Reject any tagline that breaks the one-line entry rules."""
    if not line.strip():
        sys.exit("error: tagline must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        sys.exit("error: tagline must be exactly one line")
    for ch in line:
        code = ord(ch)
        if code < 0x20 or code == 0x7F:
            sys.exit("error: tagline contains control characters")
    if len(line) < MIN_CHARS or len(line) > MAX_CHARS:
        sys.exit(f"error: tagline must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(line)}")
    # Confirm the line is clean UTF-8 by encoding and decoding it back unchanged.
    line.encode("utf-8").decode("utf-8")


def main():
    check_tagline(TAGLINE)
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)


if __name__ == "__main__":
    main()
