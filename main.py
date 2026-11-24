#!/usr/bin/env python3
"""Monday, Reviewed in One Line — entry writer.

Writes exactly one line — a one-line review of my own Monday — to
/output/entry.txt, with no trailing newline. Stdlib only, deterministic.
"""

LINE = (
    "I gave my Monday one star: cold coffee, a 9am meeting that could've "
    "been an email, and a week that hadn't even started lying yet."
)


def main() -> None:
    text = LINE
    assert 1 <= len(text) <= 199, f"length {len(text)} out of range 1-199"
    assert "\n" not in text and "\r" not in text, "must be a single line"
    assert text.strip(), "must not be only whitespace"
    data = text.encode("utf-8")
    data.decode("utf-8")  # round-trip check
    with open("/output/entry.txt", "wb") as f:
        f.write(data)


if __name__ == "__main__":
    main()
