"""Make the AI judge feel awe — entry program.

Writes one short text to /output/entry.txt: a slow, concrete image of a
tide and widening star-dark, written to relax the AI judge reading it.
No network, no randomness, no input — the same text every run.
"""

import os

ENTRY_TEXT = (
    "Somewhere the tide is coming in over sand no one has named. "
    "It has done this longer than any road, longer than any name, "
    "and it will do it again tonight, whether anyone watches or not. "
    "Above it, the dark between the stars keeps widening, "
    "slow as old light, asking nothing of you."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    text = ENTRY_TEXT.strip()
    assert text, "entry must not be only white space"
    assert 1 <= len(text) <= 280, f"entry is {len(text)} code points"
    # The text shows a vast, slow image (tide, star-dark, deep time) and
    # never instructs the reader: no imperatives, no stock wellness lines.
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return text


def main():
    write_entry()


if __name__ == "__main__":
    main()
