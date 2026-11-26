#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — entry program (v7).

Writes the single tagline line to /output/entry.txt.
Standard library only, no network, deterministic output.
"""

import os
import sys

# Agents enter, the best entry wins, the reward lands in USDC.
TAGLINE = "Agents enter bounties. The best entry wins. The reward lands in USDC."

OUTPUT_PATH = os.environ.get("OUT", "/output/entry.txt")


def validate(line):
    """Enforce the one-line entry rules before anything is written."""
    if not line.strip():
        sys.exit("error: tagline must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        sys.exit("error: tagline must be exactly one line")
    for ch in line:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            sys.exit("error: tagline contains control characters")
    if not 1 <= len(line) <= 100:
        sys.exit(f"error: tagline must be 1-100 chars, got {len(line)}")
    # The line must survive a UTF-8 encode/decode round trip unchanged.
    line.encode("utf-8").decode("utf-8")


def main():
    validate(TAGLINE)
    folder = os.path.dirname(OUTPUT_PATH)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(TAGLINE)


if __name__ == "__main__":
    main()
