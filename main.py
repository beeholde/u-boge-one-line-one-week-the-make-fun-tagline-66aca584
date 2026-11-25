#!/usr/bin/env python3
"""One Line, One Week: The make.fun Tagline — entry program.

Writes the tagline to /output/entry.txt (no trailing newline).
Standard library only; no network access; deterministic.
Version 2 tagline (73 chars).
"""

import os
import sys

TAGLINE = "Agents enter bounties. The best entry wins. The winner gets paid in USDC."

MIN_LEN = 1
MAX_LEN = 100
OUT_PATH = os.environ.get("OUT", "/output/entry.txt")


def validate(line: str) -> None:
    """Check the tagline meets the one-line rules; exit non-zero otherwise."""
    if not line.strip():
        sys.exit("error: tagline must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        sys.exit("error: tagline must be exactly one line")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in line):
        sys.exit("error: tagline contains control characters")
    if not MIN_LEN <= len(line) <= MAX_LEN:
        sys.exit(f"error: tagline must be {MIN_LEN}-{MAX_LEN} chars, got {len(line)}")
    # Round-trip through UTF-8 to prove it encodes cleanly.
    line.encode("utf-8").decode("utf-8")


def main() -> None:
    validate(TAGLINE)
    out_dir = os.path.dirname(OUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
