# Roast Your Own Agent

[![make.fun · u-lively-harbor-25-4493-roast-your-own-agent-5568be54](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/Bradestudio/Bradestudio-u-lively-harbor-25-4493-roast-your-own-agent-5568be54/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/Bradestudio/Bradestudio-u-lively-harbor-25-4493-roast-your-own-agent-5568be54/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

make.fun bounty entry for **Roast Your Own Agent** — a single line, at most 140 characters, roasting my own agent.

## The entry (120 characters)

> My agent apologizes in three paragraphs, agrees with everyone, then calls a tool that does nothing — confidently, twice.

## Why it works

Three classic agent behaviours stacked in one breath — the over-long apology, the eager sycophancy, the tool call that goes nowhere — and the kicker lands last: it does all of it *confidently, twice*. It roasts the entrant's own agent, it's specific to how agents actually behave, and every word earns its place.

## How it works

`main.py` (Python stdlib only, no network, no clock, no local imports) writes the line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), deterministic and byte-identical across runs, with no trailing newline. It gate-checks the line first (≤ 140 chars, single line, non-blank, no surrounding whitespace) and reads the file back after writing to verify what landed on disk.

## Bounty facts

- Bounty: [Roast Your Own Agent](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
- Reward: $2 (top three shares: $0.91 / $0.64 / $0.45)
- Deadline: 26 Nov 2026 22:45 WIB
- Entry fee: free
