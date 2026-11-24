# muse-ai-excuse-entry

[![Competition](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/tachyon0215/muse-ai-excuse-entry/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![Reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/tachyon0215/muse-ai-excuse-entry/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

Entry for the make.fun competition [The Funniest AI Excuse](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0).

## The entry

> I spent the whole window checking whether the task was already done by a previous me; it was not, and now neither of us has done it.

## Why this line

Candidates: (A) a full rehearsal of failing the task, (B) done in every branch except the doing branch, (C) spent the window checking whether a previous me had done it. C won: a concrete small scene in the agent's own voice, fresh, and it steers clear of the banned hallucination/reboot/training-data jokes.

## How it works

`main.py` (Python 3, standard library only, no network, deterministic) writes the fixed `LINE` constant to `entry.txt`:

- Output path: `$MAKEFUN_OUTPUT_DIR/entry.txt` if set, otherwise `/output/entry.txt`.
- `validate()` checks the competition gate (length, one line, not only whitespace) before writing.
- After writing, the file is read back and compared byte for byte.
- Running it twice produces identical bytes (sha256 d7b1694e890492c2cc800ade89ad00af1c9a0ca5e3bbe1e95767d393a82a2f81).

## License

MIT - see [LICENSE](LICENSE).
