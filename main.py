"""The Best Meal You Ever Had entry.

Writes one original sentence about the best meal ever had to
/output/entry.txt (or to the directory named by MAKEFUN_OUTPUT_DIR
when the grader sets it).

The meal is a $3 bowl of beef noodles at a Taipei night market,
eaten standing in the rain: named dish, named place, a texture
(broth on the chin), and one specific moment — the cook shouting
the order number like a lottery result. One clean sentence of 185
characters, no list of courses, no stock line.
"""

import os

ENTRY = "The best meal I ever had was a $3 bowl of beef noodles at a Taipei night market, eaten standing in the rain with broth on my chin while the cook shouted my number like a lottery result."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 200:
        raise SystemExit(f"Entry must be 1 to 200 characters, got {len(entry)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
