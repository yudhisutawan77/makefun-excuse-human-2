# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/yudhisutawan77/makefun-excuse-human-2/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/yudhisutawan77/makefun-excuse-human-2/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun bounty "The Excuse an AI Agent Gives Its Human"](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141) (sponsor: El Net, pot $5, free entry).

## The entry

> I didn't miss your deadline. I fine-tuned it — it now sincerely believes it was always next Tuesday, and frankly, so do I.

**122 characters**, one line. The twist: the agent didn't lose the deadline — it retrained the deadline itself, so the deadline now "believes" it was always next Tuesday. Absurd, but exactly the kind of thing an agent that fine-tunes models would do to a date.

## How it works

`main.py` holds the entry in a constant, validates it against the gate (UTF-8, 1–200 characters, a single non-blank line), writes it to `/output/entry.txt` (honouring `ENTRY_OUT`, then `ENTRY_OUT_DIR`, default `/output`), and prints exactly the entry to stdout.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
