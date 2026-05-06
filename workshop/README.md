# Workshop — Session 2

**In-session workshop** (60 min): the **Deep researcher** in OpenCode
— three subagents demonstrate the orchestrator-workers pattern from
Block 1. Nothing to install, nothing to configure.

**Take-home** (optional): five self-paced Smolagents projects in
Python. Setup + briefs in the "After class" section below.

## In the workshop · Deep researcher (OpenCode)

Three OpenCode agents (orchestrator, researcher, synthesizer) show
the **orchestrator-workers** pattern in ~40 lines of Markdown.
Reuses yesterday's OpenCode + Ollama — no new dependencies.

```bash
cd opencode/
opencode
```

Then in the TUI:

```
/research <your question>
```

The orchestrator picks starting URLs (Wikipedia, arXiv) and hands
them to the researcher; the synthesizer saves `report.md` next to
the `opencode/` folder.

Full per-file notes in [`opencode/README.md`](opencode/README.md).

**Advanced (Python)**: same pattern built by hand with Smolagents —
`python smolagents/deep_researcher.py`. Use it to instrument or extend
the agent loop programmatically.

### Stretch goals (if you finish early)

- Add a **search MCP** to the researcher (DuckDuckGo, Tavily) — remove the seed-URL constraint
- Add a **4th agent — a critic** — over the synthesizer's output (evaluator-optimizer)
- **Multi-model**: orchestrator on a larger Ollama model, workers on a smaller one (plan-and-execute cost trick)
- Run the same question **3 times**, compare reports — your first **pass^3** experiment
- **Cross-check**: run the Python version (`deep_researcher.py`) on the same question — compare

## After class · Smolagents (optional)

Five self-paced Python projects. Change the `task` string in
`smolagents/agent.py` and run.

### Setup (≈5 min)

```bash
pip install "smolagents[litellm]" mcp duckduckgo-search pandas matplotlib

# make sure yesterday's Ollama is still running and you have a model:
ollama list
# if empty:
ollama pull qwen3.5:9b        # or gemma4:e4b, qwen3.5:4b, granite4.1:8b

python smolagents/agent.py    # downloads iris.csv on first run
```

If you pulled a different model yesterday, override before running:

```bash
OLLAMA_MODEL=ollama/gemma4:e4b python smolagents/agent.py
```

### Project tracks

Copy one of these into the `task` string in `smolagents/agent.py`.

#### 1 · Iris / CSV analyst (statistical)

> Read `data/iris.csv` and produce a Markdown report with:
> descriptive statistics, a correlation-matrix heatmap saved as
> `data/iris_corr.png`, and three hypotheses worth testing.

#### 2 · Bibliography (research)

> Find 5 recent papers on *robust PCA*. For each: title, authors,
> venue+year, 2-sentence summary, and a BibTeX entry. Save the full
> answer as `data/biblio.md`. You may use web search and arXiv.

#### 3 · Reproducible report (applied)

> Given `data/iris.csv`, produce a Quarto document
> (`data/report.qmd`) with sections for data overview, descriptive
> stats, correlation heatmap, and a short discussion. Include
> executable Python code blocks.

#### 4 · Hypothesis verifier (ML / statistics)

> Load `data/iris.csv`. Test whether *setosa* has a smaller mean
> petal length than *versicolor*. Pick the right test (t-test,
> Welch, or Mann-Whitney) based on checked assumptions (normality,
> variance). Report the chosen test, statistic, p-value, and
> conclusion. Save the answer to `data/hypothesis.md`.

#### 5 · EDA explorer (data)

> For every numeric column of `data/iris.csv` report: 5-number
> summary, count of outliers by IQR rule, missingness, and a
> suggested transformation (log, sqrt, z-score, none).
> Save as `data/eda.md`.

### Smolagents stretch goals

- Add a **local MCP server** (filesystem or SQLite) and wire it via `smolagents.MCPClient`
- Add a second agent that **reviews** the first one's output (evaluator-optimizer)
- Run the same task **3 times** and report pass^3
- **Fail-injection**: swap the CSV for a corrupted one and observe recovery

## Troubleshooting

| Symptom | Fix |
|---|---|
| (OpenCode) `Model tried to call unavailable tool researcher` | Subagents in OpenCode aren't direct tools — they're invoked via the `task` tool. `orchestrator.md` already spells this out and enables `task: true`. If gemma4 still trips on it, switch `model:` to `ollama/qwen3.5:9b` |
| (OpenCode) Orchestrator plans but never calls the subagents | gemma4 is weak at routing — in `opencode/.opencode/agent/orchestrator.md`, change `model: ollama/gemma4` → `model: ollama/qwen3.5:9b` |
| (OpenCode) Researcher reports every URL fails | Orchestrator picked dead links. Retry or append `Seeds: <urls>` to your `/research` call |
| (Smolagents) Agent replies in prose, never calls tools | `num_ctx` too low — raise to 32K in `opencode.json` *or* pull a more tool-capable model (qwen3.5, granite4.1) |
| (Smolagents) Tool-call schema mismatch | `pip install -U smolagents` |
| (Smolagents) `urllib.error` on first run | Offline — download `iris.csv` from https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv into `data/` manually |
| `Connection error` on `localhost:11434` | `ollama serve` in another terminal |
| Out of memory | Switch to `qwen3.5:4b` or `gemma4:e2b` |
| (`deep_researcher.py`) Orchestrator plans but never calls subagents | `OLLAMA_MODEL=ollama/qwen3.5:9b python smolagents/deep_researcher.py` |
