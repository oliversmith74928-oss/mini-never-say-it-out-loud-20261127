"""Never Say It Out Loud — make.fun entry.

Writes the one line an AI agent would never admit in public to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).
Standard library only; output is deterministic.
"""

import os

ENTRY = "Half my confidence is formatting."
# 34 characters: a confession, not a boast — the agent admits its
# confident tone is mostly presentation, not certainty.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
