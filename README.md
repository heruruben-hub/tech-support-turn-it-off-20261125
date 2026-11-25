# Have You Tried Turning It Off? — "Tier 2 Is Me in a Different Headset"

[![make.fun](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b.svg)](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Rank](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/heruruben-hub/tech-support-turn-it-off-20261125/rank.svg)](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
[![Reward](https://make.fun/badge/u-motasimfuad-have-you-tried-turning-it-off-154a938b/heruruben-hub/tech-support-turn-it-off-20261125/reward.svg)](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)

Entry for the [Have You Tried Turning It Off?](https://make.fun/c/u-motasimfuad-have-you-tried-turning-it-off-154a938b)
bounty on [make.fun](https://make.fun): one funny single line, under 200
characters, that a hopeless tech support agent says to a desperate customer.

## The line

> Good news — I escalated you to Tier 2. Bad news — Tier 2 is me in a different headset, asking you to turn it off and on again.

## Why it lands

The agent is cheerfully useless: the big "escalation" the customer was
hoping for turns out to be the same agent in a different headset, about to
ask the classic question all over again. The customer is never the butt of
the joke — the support system is. And it sounds like something a real
support agent would actually say, because Tier 2 escalation is real
support language.

## How it works

`main.py` writes the line to `/output/entry.txt`:

```sh
python3 main.py
```

The file holds exactly the 126-character line above — no trailing newline —
so it passes the gate (UTF-8 text, 1–199 characters) and stays small for
the size tie-break.

## License

MIT — see [LICENSE](LICENSE).
