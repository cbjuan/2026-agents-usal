"""
Smolagents workshop starter — Session 2, USAL Master's in Multivariate Statistics.

Quick start:

    pip install "smolagents[litellm]" mcp duckduckgo-search pandas matplotlib

    # make sure Ollama is running and the model from yesterday is pulled, e.g.:
    #   ollama pull qwen3.5:9b
    # then, from the workshop/ folder:
    python smolagents/agent.py

Pick one of the five project tracks from the slide deck and modify the
`TASK` string and the tool list below. Keep it small — you have 35 minutes.
"""

import os
import urllib.request
from pathlib import Path

from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel, tool

# ---------------------------------------------------------------------------
# 0) Data — auto-download iris.csv into ./data/ on first run (no network
#    needed after that). Swap this block for your own dataset if you like.
# ---------------------------------------------------------------------------
DATA_DIR = Path(__file__).parent / "data"
IRIS_CSV = DATA_DIR / "iris.csv"
IRIS_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"


def ensure_iris() -> Path:
    if not IRIS_CSV.exists():
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        print(f"Downloading iris.csv → {IRIS_CSV}")
        urllib.request.urlretrieve(IRIS_URL, IRIS_CSV)
    return IRIS_CSV

# ---------------------------------------------------------------------------
# 1) Model — local Ollama. Override with OLLAMA_MODEL env var if you pulled
#    something other than qwen3.5:9b yesterday (qwen3.5:4b, gemma4:e4b,
#    gemma4:26b, granite4.1:8b, ...).
# ---------------------------------------------------------------------------
MODEL_ID = os.environ.get("OLLAMA_MODEL", "ollama/qwen3.5:9b")
OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434")

model = LiteLLMModel(model_id=MODEL_ID, api_base=OLLAMA_URL)


# ---------------------------------------------------------------------------
# 2) Custom tools — add your own @tool functions here.
#    The docstring IS the tool's description for the LLM. Be specific.
# ---------------------------------------------------------------------------
@tool
def descriptive_stats(csv_path: str) -> str:
    """Compute descriptive statistics (count, mean, std, min/max, quartiles) of a CSV.

    Args:
        csv_path: absolute path to the CSV file on disk.
    """
    import pandas as pd

    df = pd.read_csv(csv_path)
    return df.describe(include="all").to_markdown()


@tool
def correlation_matrix(csv_path: str, output_png: str) -> str:
    """Compute the Pearson correlation matrix of a CSV's numeric columns and save a heatmap PNG.

    Args:
        csv_path: absolute path to the CSV file on disk.
        output_png: absolute path where the heatmap PNG should be written.
    """
    import matplotlib.pyplot as plt
    import pandas as pd

    df = pd.read_csv(csv_path)
    corr = df.select_dtypes("number").corr()

    fig, ax = plt.subplots(figsize=(6, 5))
    im = ax.imshow(corr, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(len(corr)))
    ax.set_yticks(range(len(corr)))
    ax.set_xticklabels(corr.columns, rotation=45, ha="right")
    ax.set_yticklabels(corr.columns)
    fig.colorbar(im, ax=ax)
    fig.tight_layout()
    fig.savefig(output_png, dpi=120)
    plt.close(fig)
    return f"Saved heatmap to {output_png}\n\n{corr.round(2).to_markdown()}"


# ---------------------------------------------------------------------------
# 3) Agent — CodeAgent writes Python as actions (vs JSON tool-calls).
#    `additional_authorized_imports` controls which libs the sandbox allows.
# ---------------------------------------------------------------------------
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool(), descriptive_stats, correlation_matrix],
    model=model,
    additional_authorized_imports=["pandas", "numpy", "matplotlib", "scipy"],
    max_steps=8,
)


# ---------------------------------------------------------------------------
# 4) Run — replace this prompt with your chosen project track.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    iris_path = ensure_iris()
    task = (
        f"Read {iris_path} and write a short report that includes: "
        "(a) descriptive statistics, (b) the correlation matrix saved as "
        f"{DATA_DIR / 'iris_corr.png'}, and (c) three hypotheses worth testing."
    )
    result = agent.run(task)
    print("\n=== FINAL ANSWER ===\n")
    print(result)
