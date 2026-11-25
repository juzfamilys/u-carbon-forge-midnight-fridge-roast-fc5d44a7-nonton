#!/usr/bin/env python3
"""Midnight Fridge Roast — validate the roast line and copy it to /output/entry.txt.

Pure Python standard library only: no third-party packages, no network,
no model calls. The roast lives in entry.txt; this script only checks it
and hands it over byte-for-byte.
"""

import sys
from pathlib import Path

MAX_CHARS = 160


def validate_length(line):
    """A roast must fit in one breath: 1-160 characters, no more."""
    if len(line) > MAX_CHARS:
        raise ValueError(
            "roast is %d chars, over the %d-char limit" % (len(line), MAX_CHARS)
        )
    if len(line) < 1:
        raise ValueError("entry.txt must not be empty")
    return line


def read_roast(path):
    """Read entry.txt and return its single roast line, validated."""
    text = Path(path).read_text(encoding="utf-8")
    lines = text.splitlines()
    if len(lines) != 1:
        raise ValueError(
            "entry.txt must hold exactly one line, found %d" % len(lines)
        )
    line = lines[0].strip()
    if not line:
        raise ValueError("entry.txt must not be empty")
    return validate_length(line)


def main():
    roast = read_roast("entry.txt")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(roast + "\n", encoding="utf-8")
    print("OK: wrote %d-char roast to %s" % (len(roast), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
