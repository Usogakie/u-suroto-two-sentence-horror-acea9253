#!/usr/bin/env python3
"""Two-Sentence Horror: write one horror story of exactly two sentences.

The story is a fixed string, chosen once and written verbatim, so every
run produces byte-identical output. No network, no clock, no randomness.
"""

import os

STORY = (
    "My daughter sleeps with the closet light on because she says the "
    "man in there watches her sleep. Last night I switched it off to "
    "prove he wasn't real, and from the dark he thanked me."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(STORY + "\n")


if __name__ == "__main__":
    main()
