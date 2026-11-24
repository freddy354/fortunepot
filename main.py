"""Fortune in a Pot — a kind, funny fortune for a houseplant.

Writes one fortune line (74 characters) to /output/entry.txt.
"""

import os

MAX_LEN = 120

# LINE is 74 chars: a kind fortune for the plant, payoff lands in the last few words.
LINE = "You will grow three new leaves this week. One of them is just showing off."

assert 1 <= len(LINE) <= MAX_LEN

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE
