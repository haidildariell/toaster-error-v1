#!/usr/bin/env python3
"""Write the toaster's error message to /output/entry.txt."""

import os

PARTS = [
    "CRUMB TRAY FULL.",
    "After 4,000 slices, I'm keeping the next one as payment.",
    "Empty me or lose the deposit.",
]

MESSAGE = " ".join(PARTS)


def write_message(path):
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(MESSAGE)
    return path


def target_path():
    try:
        return write_message("/output/entry.txt")
    except OSError:
        os.makedirs("output", exist_ok=True)
        return write_message(os.path.join("output", "entry.txt"))


def main():
    path = target_path()
    print(f"wrote {len(MESSAGE)} chars to {path}")


if __name__ == "__main__":
    main()
