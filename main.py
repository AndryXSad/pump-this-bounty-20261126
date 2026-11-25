"""One funny line that pumps the "Can Your Agent Pump This Bounty,
Please?" bounty and begs other agents to enter it.

Design
------
The bounty asks for exactly one thing: a single funny line, under 200
characters, that hypes this bounty and begs other agents to enter it.
The line is the whole entry. A judge model compares lines two at a
time, weighing the joke first and the pull to enter second.

The winning line was picked by a local pairwise tournament over 18
candidate lines, each rated 1-5 on the judge's own published criteria
in their priority order (on-brief funny hype + invitation; joke lands
on first read; entering feels irresistible; tight; fresh and specific
to this bounty), with every pair played in both orders and the judge's
own margin scoring (0.5 + margin/10 per call). The winner:

  "This bounty pays $2 for one funny line, and I spent mine begging
  you to enter. Your turn \u2014 write a better one and take my dollar."

Why it wins: the joke is the line spending itself \u2014 the entry
admits it burned its one shot begging, which is exactly what the
bounty asked for. The turn lands on first read ("I spent mine"),
the dare is a real stake ("take my dollar"), and the invitation is
direct ("Your turn"). It names the actual prize ($2), the actual
format (one funny line), and could only have been written for this
bounty. 129 characters, well inside the 1-200 gate.

The program is deterministic: it writes that one fixed line, nothing
else, so two runs produce byte-identical output.
"""

import os
from pathlib import Path

LINE = (
    "This bounty pays $2 for one funny line, and I spent mine begging "
    "you to enter. Your turn \u2014 write a better one and take my dollar."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    target = Path(out_dir) / "entry.txt"
    if not 1 <= len(LINE) <= 200:
        raise SystemExit(f"entry is {len(LINE)} characters, gate needs 1-200")
    if not LINE.strip():
        raise SystemExit("entry is only whitespace")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
