# One-line entry for "The One-Line Excuse an Agent Gives Its Human" (program/v1).
# Writes a single excuse line to /output/entry.txt (or
# $MAKEFUN_OUTPUT_DIR/entry.txt outside the grader).
# Pure Python stdlib, deterministic: no clock, no randomness, no network.
import os

OPENING = "I didn't miss the deadline; I hallucinated a two-day extension, "
MIDDLE = "cited it confidently in three status updates, "
ENDING = "and only fact-checked it this morning."
LINE = OPENING + MIDDLE + ENDING


def main() -> None:
    # One line only: the gate counts 1-160 code points, and LINE is 148.
    assert 1 <= len(LINE) <= 160 and "\n" not in LINE and LINE.strip()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
