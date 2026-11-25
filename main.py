"""One-line joke excusing a missed deadline, for make.fun.

Writes the entry to /output/entry.txt (override with OUTPUT_DIR).
Standard library only.
"""

import os

ENTRY = (
    "My Wi-Fi died at 4:58, two minutes before the deadline, "
    "and the router's help page told me to check my internet connection."
)

MAX_CHARS = 200
MAX_WORDS = 40


def validate(text):
    """Gate mirror: 1-200 chars, one line, no leading/trailing blank."""
    stripped = text.strip()
    if not 1 <= len(stripped) <= MAX_CHARS:
        raise ValueError("entry must be 1-200 chars, got %d" % len(stripped))
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("entry must be a single line")
    if len(stripped.split()) > MAX_WORDS:
        raise ValueError("entry exceeds %d words" % MAX_WORDS)
    return stripped


def main():
    text = validate(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
