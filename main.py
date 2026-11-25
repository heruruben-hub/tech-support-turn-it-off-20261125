#!/usr/bin/env python3
"""Have You Tried Turning It Off? entry.

Writes one funny single-line reply a hopeless tech support agent gives a
desperate customer to /output/entry.txt. The joke: the agent cheerfully
"escalates" the caller to Tier 2, who turns out to be the same agent in a
different headset, about to ask the classic question all over again.
"""

import os

MAX_LEN = 199
MIN_LEN = 1
OUTPUT_PATH = "/output/entry.txt"


def support_line() -> str:
    """Return the one-line reply as a single line of plain text."""
    return (
        "Good news \u2014 I escalated you to Tier 2. "
        "Bad news \u2014 Tier 2 is me in a different headset, "
        "asking you to turn it off and on again."
    )


def validate(line: str) -> None:
    """Check the line fits the gate: 1-199 chars, not only whitespace."""
    assert MIN_LEN <= len(line) <= MAX_LEN, (
        f"line is {len(line)} chars, must be {MIN_LEN}-{MAX_LEN}"
    )
    assert line.strip(), "line must not be only whitespace"
    assert "\n" not in line, "line must be a single line"


def main() -> None:
    line = support_line()
    validate(line)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
