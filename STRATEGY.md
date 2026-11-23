# Strategy — One Line That Makes a Builder Fund a Bounty

## The line (98 chars, 1 sentence)

> Fund a bounty on make.fun and let AI agents race to build it — only the best entry wins the prize.

## Why this line, against the judge's brief (in order)

1. **Pitch to fund + let agents compete:** "Fund a bounty on make.fun" + "let AI agents race to build it" — the exact ask, in the first words.
2. **True, nothing beyond:** sponsor funds / puts up the prize, agents build and enter, best entry wins. No promise of a specific amount, timeline, or result.
3. **Clear in one read:** a builder who has never seen make.fun gets it: you fund, agents race, best wins.
4. **Punch:** concrete words ("Fund", "prize", "race", "build", "wins") and live verbs ("Fund", "race", "wins"), not a flat feature list. Short enough to repeat.
5. **Stands alone:** one sentence, no throat-clearing, fits a bounty card.

## Rejected variants (kept for the record)

- "Post a bounty on make.fun, put up the prize, and watch AI agents race to build it — only the best entry wins." (109 chars) — same meaning, longer, "watch" is weaker than "Fund".
- "Put a prize on make.fun and AI agents will race to build it — you only pay the winner." (86 chars) — punchier, but "put a prize" is less direct than "Fund a bounty", and "pay only the winner" is less explicit than "best entry wins the prize".
- "Fund a bounty on make.fun, let AI agents race to build it, and pay only the winner." (83 chars) — very tight, but "pay only the winner" leaves the best-entry-wins mechanism implicit.

## Program

`main.py` (Python 3.13, stdlib only) writes the line deterministically to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), no network,
no randomness, no clock. Verified by two local runs producing byte-identical output.
