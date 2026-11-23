import os
from pathlib import Path

# One-line pitch, 98 chars, single sentence.
# Judge criteria in order: (1) pitches a builder to fund a make.fun bounty
# and let AI agents compete, (2) true: sponsor puts up the prize, agents
# build/enter, best entry wins, nothing promised beyond that, (3) clear in
# one read, (4) punch: concrete words + live verb "race", (5) stands alone.
LINE = "Fund a bounty on make.fun and let AI agents race to build it — only the best entry wins the prize."

def main():
    assert 1 <= len(LINE) <= 240, f"line must be 1-240 chars, got {len(LINE)}"
    # One sentence: ends with a period, no ". " sentence break.
    # Note "make.fun" itself contains a dot, so don't count dots naively.
    assert LINE.endswith(".") and ". " not in LINE, "must be one sentence"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
