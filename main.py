"""One-Line Roast: The Gadget You Use Every Day.

Writes a single-line roast of the everyday gadget (the phone) to
/output/entry.txt. The roast must stay one line and under 200 chars.
"""

import os
import sys

ROAST = (
    "My phone's battery dies by noon, yet I still check it first thing "
    "every morning — the most loyal toxic relationship I own."
)

GADGET_WORDS = ("phone", "battery", "screen", "charger", "gadget")


def summarize(line):
    """Return a small profile of the roast for the log line."""
    lowered = line.lower()
    found = [word for word in GADGET_WORDS if word in lowered]
    return {
        "chars": len(line),
        "words": len(line.split()),
        "gadget": found[0] if found else "unknown",
    }


def validate(line):
    """Check the roast is a single short line about the gadget."""
    if not line or "\n" in line.strip():
        return False, "roast must be exactly one line"
    if len(line) > 200:
        return False, "roast is over 200 characters"
    lowered = line.lower()
    if not any(word in lowered for word in GADGET_WORDS):
        return False, "roast must mention the gadget"
    return True, "ok"


def main():
    ok, reason = validate(ROAST)
    if not ok:
        print("invalid roast:", reason, file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")
    print(ROAST)
    profile = summarize(ROAST)
    print("profile:", profile)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
