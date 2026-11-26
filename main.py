#!/usr/bin/env python3
# Entry for make.fun bounty u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c
"""The Dog Ate My Homework: Funniest Excuse.

Deterministic entry: writes exactly one line to /output/entry.txt
and prints that same line, nothing else.
"""

import os

LINE = "It wasn't homework, it was a dare: the worksheet stared at me, smelled of pencil and panic, and I am a dog, not a librarian \u2014 so I ate the evidence."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
