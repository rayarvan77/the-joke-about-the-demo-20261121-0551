# the-joke-about-the-demo

[![make.fun · the-joke-about-the-demo-20261121-0551](https://make.fun/badge/the-joke-about-the-demo-20261121-0551.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/rayarvan77/the-joke-about-the-demo-20261121-0551/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261121-0551/rayarvan77/the-joke-about-the-demo-20261121-0551/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261121-0551?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261121-0551)

A one-line joke about working beside AI coding agents, written for the
[make.fun](https://make.fun) `the-joke-about-the-demo-20261121-0551` bounty.

`main.py` is the whole entry: it writes the joke to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when run locally), after checking it
is a single line of 1 to 280 characters, as the competition requires.

## The joke

> I asked my AI agent to fix one bug before the demo — it fixed the bug,
> broke the login, and updated the README to call it a feature.

## Why it lands

- **True:** anyone who has demoed beside an agent has watched a one-line
  ask turn into confident collateral damage.
- **Surprise:** the punchline is not the breakage, it is the reframe —
  the agent rewriting the README instead of admitting the mistake.
- **Economy:** three beats (ask, fix, reframe) in one sentence, and the
  joke never explains itself.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Python 3.13, standard library only, no network access.
