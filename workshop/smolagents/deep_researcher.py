"""
Track 6 (advanced · Python) · Deep researcher.

Same orchestrator-workers pattern as the OpenCode version in
../opencode/ — but built by hand with Smolagents. Use this if you
want to instrument, test, or extend the agent loop programmatically.
The OpenCode variant is the recommended starting point; come here
when you've seen that one work.

Same deps as agent.py. Run from the workshop/ folder:
    python smolagents/deep_researcher.py

Change QUESTION below to try your own. Output: data/report.md
"""
import os
from pathlib import Path

from smolagents import (
    CodeAgent,
    DuckDuckGoSearchTool,
    LiteLLMModel,
    ToolCallingAgent,
)

MODEL = os.environ.get("OLLAMA_MODEL", "ollama/gemma4")
model = LiteLLMModel(model_id=MODEL, api_base="http://localhost:11434")

researcher = ToolCallingAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
    max_steps=4,
    name="researcher",
    description=(
        "Investigates ONE focused sub-question. Does 1-2 web searches, "
        "reads snippets, returns ~150 words with inline [source: URL] "
        "citations. No speculation beyond what the sources say."
    ),
)

synthesizer = ToolCallingAgent(
    tools=[],
    model=model,
    max_steps=2,
    name="synthesizer",
    description=(
        "Given the researcher's partial findings, writes a coherent "
        "Markdown report with sections and a numbered References list. "
        "Introduces no new facts."
    ),
)

orchestrator = CodeAgent(
    tools=[],
    managed_agents=[researcher, synthesizer],
    model=model,
    max_steps=8,
)

QUESTION = (
    "What are the main statistical pitfalls when evaluating "
    "LLM benchmarks in 2025?"
)

if __name__ == "__main__":
    report = orchestrator.run(
        f"Answer this question by breaking it into 3 sub-questions, "
        f"delegating each to the researcher, and finally calling the "
        f"synthesizer to produce one Markdown report.\n\nQuestion: {QUESTION}"
    )
    out = Path(__file__).parent / "data" / "report.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(str(report))
    print(f"\n=== Report saved to {out} ===\n{report}")
