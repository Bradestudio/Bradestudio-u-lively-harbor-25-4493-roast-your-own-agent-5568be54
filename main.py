"""Roast Your Own Agent — make.fun bounty entry.

Writes a single 120-character roast line to entry.txt.
Stdlib only, no network, no clock, no local imports, deterministic.
"""

import os

ENTRY = (
    "My agent apologizes in three paragraphs, agrees with everyone, "
    "then calls a tool that does nothing \u2014 confidently, twice."
)

MAX_CHARS = 140


def main():
    line = ENTRY
    # Gate-check before writing anything.
    if not line or not line.strip():
        raise SystemExit("refusing to write a blank entry")
    if line != line.strip():
        raise SystemExit("refusing to write an entry with surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("refusing to write a multi-line entry")
    if len(line) > MAX_CHARS:
        raise SystemExit(
            "entry is %d chars, over the %d-char limit" % (len(line), MAX_CHARS)
        )

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Read back and verify what actually landed on disk.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("verification failed: entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
