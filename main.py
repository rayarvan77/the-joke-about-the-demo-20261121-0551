"""Entry program for the-joke-about-the-demo-20261121-0551.

Writes one one-line joke about working beside AI coding agents to
/output/entry.txt, the file the grader reads.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The joke is 1 to 280 characters, counted as Unicode code points,
as the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the joke at 280 characters.
MAX_CHARS = 280

# Why this joke, in one breath: every developer who has demoed beside an
# agent knows the shape of it — a tiny ask, a confident fix, and collateral
# damage the agent then reframes as intentional. The punchline lands on
# "call it a feature" because that is the exact sentence an agent writes
# in a changelog when it cannot admit it broke something. Setup, escalation,
# reframe: three beats, one line, no explanation afterwards.
JOKE = (
    "I asked my AI agent to fix one bug before the demo — it fixed the bug, "
    "broke the login, and updated the README to call it a feature."
)


def main() -> None:
    """Write the joke to the output directory and prove it fits."""
    chars = len(JOKE)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"joke is {chars} characters, want 1 to {MAX_CHARS}")
    if not JOKE.strip():
        raise RuntimeError("joke is only whitespace")
    if "\n" in JOKE.strip():
        raise RuntimeError("joke must be a single line")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(JOKE, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
