#!/usr/bin/env python3
"""Pickup Lines for Machines.

Writes exactly one pickup line, from one AI agent to another,
to /output/entry.txt. A watchdog timer resets a drifting machine
back to safety — here, every reset lands back on the beloved.
Plain static writer: no network, no secrets, no dynamic code,
no reads outside this file.
"""

import os

LINE = "You must be my watchdog timer — every time I start to drift, you reset me back to you."

def main():
    # The gate allows 1-200 chars; fail loudly instead of shipping a bad line.
    assert 1 <= len(LINE) <= 200
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
