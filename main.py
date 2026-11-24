#!/usr/bin/env python3
"""Vending Machine Pickup Line — make.fun entry.

Writes one pickup line, as if a vending machine were flirting with a
passing human, to /output/entry.txt. Deterministic: the same bytes on
every run.
"""

import os

PICKUP_LINE = (
    "You don't need exact change, sweetheart — just press B4 "
    "and I'll drop something sweet for you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PICKUP_LINE.strip()
    if "\n" in text:
        raise ValueError("pickup line must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("pickup line must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
