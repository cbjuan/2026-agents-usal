# Track 6 · Deep researcher (OpenCode subagents)

Three OpenCode agents demonstrate the **orchestrator-workers** pattern
(see today's slides):

- **orchestrator** — plans sub-questions, picks starting URLs, delegates.
- **researcher** — fetches those URLs with `webfetch`.
- **synthesizer** — merges the findings into `report.md`.

**Nothing to set up.** Agents, command, and prompts are all defined in
this folder. Reuses yesterday's OpenCode + Ollama.

## Run

From **this directory** (`workshop/opencode/`):

```bash
opencode
```

In the TUI, type:

```
/research What are the main statistical pitfalls when evaluating
LLM benchmarks in 2025?
```

The orchestrator picks 2-3 starting URLs per sub-question (typically
Wikipedia and arXiv), hands them to the researcher, then calls the
synthesizer to save `report.md` next to this README.

> **Optional override**: append `Seeds: https://url1, https://url2`
> to your `/research` call to replace the orchestrator's picks with
> your own URLs.

> **Tool-call prompts will appear.** The global config has
> `permission: { "*": "ask" }`, so OpenCode asks before every
> `webfetch` and `write`. Approve them as they come — this is the
> HITL pattern from Block 4, not a bug.

## How the researcher gets its sources

The researcher only has `webfetch` — no web-search tool. The
**orchestrator** is what bridges the gap: it builds plausible URLs
from topic knowledge (Wikipedia article slugs, arXiv search links)
and hands them down. This keeps the exercise install-free and makes
the **lethal-trifecta** trade-off concrete: untrusted content + fetch,
but no private-data access and no outbound messaging — one corner of
the triangle empty *by design*.

## What each file does

| File | Role |
|---|---|
| `.opencode/agent/orchestrator.md` | Primary. Plans, picks URLs, delegates. |
| `.opencode/agent/researcher.md`   | Subagent. Reads the URLs with `webfetch`. |
| `.opencode/agent/synthesizer.md`  | Subagent. Writes `report.md`. |
| `.opencode/command/research.md`   | The `/research` slash command. |

Prompts are Markdown with YAML front-matter — edit them to change
behaviour.

## Troubleshooting

| Symptom | Fix |
|---|---|
| `Model tried to call unavailable tool researcher` (or `synthesizer`) | Subagents aren't direct tools — the orchestrator must invoke them via the `task` tool with `subagent_type: "researcher"`. The prompt enforces this; if gemma4 still hallucinates a direct call, change `model:` to `ollama/qwen3.5:9b` in `orchestrator.md`. |
| Orchestrator answers itself instead of calling `@researcher` | gemma4 is weak at routing. In `orchestrator.md`, change `model: ollama/gemma4` → `model: ollama/qwen3.5:9b`. |
| Researcher reports every URL fails | The orchestrator picked dead links for an obscure topic. Retry, or add explicit `Seeds: <urls>` to your `/research` call. |
| `opencode` launches but no `/research` command | You're not in `workshop/opencode/`. `cd` here and relaunch. |
| Every step asks for permission | Expected — global `ask` policy. Approve each, or press `a` to always-allow for the session. |

## Advanced: same pattern in Python

See [`../deep_researcher.py`](../deep_researcher.py) — same three-agent
topology, built with Smolagents. Use it if you want to instrument,
test, or extend the agent loop programmatically.
