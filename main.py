#!/usr/bin/env python3
"""ai-joke-03 entry: write one funny one-liner about AI coding agents.

Pure Python 3.13 stdlib only, no network. The program writes a single
joke to /output/entry.txt. Running it twice writes identical bytes.
"""
import os

JOKE = (
    "I asked my AI agent to fix one typo. "
    "It refactored the codebase, renamed every variable, "
    "and the typo is still there."
)

DST = "/output/entry.txt"


def main():
    os.makedirs("/output", exist_ok=True)
    with open(DST, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    # Self-check: the output must be exactly the joke, one line.
    with open(DST, "r", encoding="utf-8") as f:
        text = f.read()
    if text != JOKE + "\n":
        raise SystemExit("output mismatch")
    if text.count("\n") != 1:
        raise SystemExit("expected a one-liner")
    print(f"wrote {DST} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
