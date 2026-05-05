---
marp: true
theme: default
paginate: true
size: 16:9
math: katex
header: 'AI Agents · Session 1 · Master''s in Multivariate Statistics · USAL'
footer: 'May 5, 2026 · University of Salamanca'
style: |
  :root {
    --bg: #ffffff;
    --fg: #111827;
    --muted: #6b7280;
    --rule: #e5e7eb;
    --accent: #2563eb;
    --code-bg: #f6f8fa;
  }
  section {
    background: var(--bg);
    color: var(--fg);
    font-family: -apple-system, BlinkMacSystemFont, 'Inter', 'Segoe UI', sans-serif;
    font-weight: 400;
    padding: 72px 80px;
    font-size: 25px;
    line-height: 1.55;
    letter-spacing: -0.003em;
  }
  section::after { color: var(--muted); font-size: 13px; font-weight: 400; }
  header { color: var(--muted); font-size: 13px; padding: 22px 80px 0; font-weight: 400; }
  footer { color: var(--muted); font-size: 12px; padding: 0 80px 20px; font-weight: 400; }
  h1 {
    color: var(--fg);
    font-weight: 600;
    font-size: 1.7em;
    margin: 0 0 0.7em;
    padding: 0 0 0.35em;
    border-bottom: 1px solid var(--rule);
    letter-spacing: -0.015em;
  }
  h2 {
    color: var(--fg);
    font-weight: 500;
    font-size: 1.15em;
    margin: 1em 0 0.4em;
    letter-spacing: -0.01em;
  }
  h3 {
    color: var(--fg);
    font-weight: 600;
    font-size: 1em;
    margin: 0.8em 0 0.3em;
  }
  strong { font-weight: 600; color: var(--fg); }
  em { font-style: italic; color: var(--fg); }
  code {
    background: var(--code-bg);
    color: var(--fg);
    padding: 1px 6px;
    border-radius: 3px;
    font-family: 'JetBrains Mono', 'SF Mono', Menlo, monospace;
    font-size: 0.82em;
  }
  pre {
    background: var(--code-bg);
    border: 1px solid var(--rule);
    padding: 16px 20px;
    border-radius: 4px;
    font-size: 0.62em;
    line-height: 1.5;
    overflow-x: auto;
  }
  pre code {
    background: transparent;
    padding: 0;
    color: var(--fg);
    font-size: inherit;
  }
  table {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.72em;
    margin: 0.7em 0;
  }
  th {
    text-align: left;
    padding: 9px 14px 9px 0;
    font-weight: 600;
    color: var(--fg);
    border-bottom: 1.5px solid var(--fg);
    background: transparent;
  }
  td {
    padding: 8px 14px 8px 0;
    border-bottom: 1px solid var(--rule);
    vertical-align: top;
  }
  blockquote {
    border-left: 2px solid var(--fg);
    background: transparent;
    padding: 2px 0 2px 18px;
    color: var(--fg);
    margin: 0.7em 0;
    border-radius: 0;
    font-size: 0.95em;
  }
  blockquote p { margin: 0.3em 0; }
  ul, ol { margin-left: 0.6em; padding-left: 0.6em; }
  li { margin: 0.22em 0; }
  a { color: var(--accent); text-decoration: none; border-bottom: 1px solid var(--accent); }
  hr { border: none; border-top: 1px solid var(--rule); margin: 1.2em 0; }
  /* Layout helpers */
  .columns { display: grid; grid-template-columns: 1fr 1fr; gap: 44px; }
  .columns-3 { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 28px; }
  .card {
    background: transparent;
    border: 1px solid var(--rule);
    border-radius: 4px;
    padding: 18px 20px;
  }
  .tag {
    display: inline-block;
    color: var(--muted);
    padding: 0;
    font-size: 0.72em;
    font-weight: 500;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-right: 8px;
  }
  /* Slide variants */
  section.cover {
    background: var(--bg);
    text-align: left;
    justify-content: center;
  }
  section.cover h1 {
    font-size: 3.2em;
    line-height: 1.05;
    border: none;
    color: var(--fg);
    font-weight: 700;
    letter-spacing: -0.03em;
    padding: 0;
    margin-bottom: 0.25em;
  }
  section.cover h2 {
    color: var(--muted);
    font-size: 1.25em;
    font-weight: 400;
    margin-top: 0;
    letter-spacing: 0;
  }
  section.divider {
    background: var(--bg);
    text-align: left;
    justify-content: center;
  }
  section.divider h1 {
    font-size: 3em;
    border: none;
    color: var(--fg);
    font-weight: 700;
    letter-spacing: -0.03em;
    padding: 0;
  }
  section.divider h2 {
    color: var(--muted);
    font-weight: 400;
  }
  section.divider .tag {
    color: var(--muted);
    background: transparent;
  }
  section.break {
    background: var(--bg);
    text-align: center;
    justify-content: center;
  }
  section.break h1 {
    font-size: 3em;
    color: var(--fg);
    border: none;
    font-weight: 700;
    letter-spacing: -0.03em;
    padding: 0;
  }
  section.quote {
    background: var(--bg);
    text-align: center;
    justify-content: center;
  }
  section.quote h1 {
    font-size: 1.6em;
    line-height: 1.4;
    color: var(--fg);
    border: none;
    font-weight: 400;
    font-style: italic;
    max-width: 80%;
    margin: 0 auto;
    padding: 0;
  }
  section.quote .author {
    color: var(--muted);
    font-size: 0.9em;
    margin-top: 1.5em;
    font-style: normal;
  }
---

<!-- _class: cover -->
<!-- _header: '' -->
<!-- _footer: '' -->
<!-- _paginate: false -->

# AI Agents
## Session 1 — Fundamentals, landscape, and your first agent

<br>

**Juan Cruz-Benito**

Master's in Multivariate Statistics · USAL
May 5, 2026 · Salamanca

<!--
Speaker note: Warm welcome. Mention that the field moves monthly and that part of the value of this class will be learning to read the pace of change. Ask them to keep their laptops open during the session.
-->

---

# Who we are

### Me

- Who am I?
- Why I teach this class
- How I work day-to-day with agents


<!--
Ask for 30 seconds from anyone who wants to introduce themselves: name, prior background, one concrete expectation. No more than 4-5 volunteers.
-->

---

# Who we are

### You

- Physicists, mathematicians, statisticians
- Engineers, computer scientists
- Biologists, psychologists
- Intermediate technical level
- **Your advantage**: you already think in terms of uncertainty, evidence, variance

<!--
Ask for 30 seconds from anyone who wants to introduce themselves: name, prior background, one concrete expectation. No more than 4-5 volunteers.
-->

---

# Initial poll

Raise your hand:

1. **Who has used ChatGPT / Claude / Gemini this week?**
2. **Who has ever called an LLM API from code (Python/R)?**
3. **Who has heard of MCP, function calling, or tool use?**
4. **What do you hope to take away? (one word)**

> The goal is to calibrate the pace, not to judge.

<!--
Take mental note of the responses. If most haven't touched the API, spend more time on function calling. If everyone is already familiar with MCP, move faster through that block.
-->

---

# Agenda — Session 1

| Block | Content |
|---|---|
| 0 | Welcome + poll |
| **1** | **Fundamentals: what is an agent, brain, hands, memory, skills** |
| ☕ | Break |
| 2 | Landscape of frameworks and existing agents |
| 3 | Agents you can already use today |
| 4 | **"No-code" workshop: your first local agent** |
| 5 | Wrap-up and discussion |

<!--
Show the agenda on a visible slide and refer to it when switching blocks. Don't be afraid to skip content if the group is more interested in another point.
-->

---

# Logistics

- 💻 **Laptops open**: you'll be installing things
- 📚 **Materials**: this deck + other resources available at <https://github.com/cbjuan/2026-agents-usal>
- 🙋 **Questions**: whenever you want, no need to wait until the end
- ❓ **Technical issues during the workshop**: we solve them as a group

> If something doesn't work on your laptop during the workshop, **it's perfectly normal**. It's part of the learning.

<!--
Create a shared chat channel where students can paste errors and get help. Have a short list of frequent issues ready (ollama not found, num_ctx too low, firewall, etc.).
-->

---

# Materials

<div class="columns">
<div>

<img src="https://api.qrserver.com/v1/create-qr-code/?size=260x260&margin=4&data=https%3A%2F%2Fgithub.com%2Fcbjuan%2F2026-agents-usal" alt="QR code to course repo" width="260" />

</div>
<div>

### github.com/cbjuan/2026-agents-usal

Scan the QR or type the URL. Inside you'll find:

- Both decks (source `.md` + PDF)
- Workshop code templates
- Datasets used in the tasks
- Reading list with links
- Troubleshooting notes

</div>
</div>

<!--
Aim the phone at the QR on one student's screen and confirm it resolves. Ask someone to paste the URL into the class chat channel as a fallback for anyone whose camera is flaky.
-->

---

# Shared vocabulary

Terms you'll hear repeatedly — this slide stays in the deck for reference:

| Term | Meaning |
|---|---|
| **LLM** | Large Language Model — GPT, Claude, Gemini, Qwen... |
| **API** | Application Programming Interface — calling a service from code |
| **Token** | Sub-word unit the LLM reads/writes (~¾ of a word in English) |
| **Prompt** | Text input to the LLM; **system prompt** = fixed instructions |
| **Context window** | Max tokens the LLM can see at once (4K, 32K, 200K...) |
| **Tool-call** | LLM invoking a function (search, read_file, run_sql...) |
| **Inference** | One forward pass through the model = cost + latency |
| **RAG** | Retrieval-Augmented Generation — fetch docs, add to prompt |
| **MCP** | Model Context Protocol — standard to connect tools to LLMs |
| **Fine-tuning** | Extra training on specific data to adjust a model's behavior |

<!--
Take ~90 seconds. Don't read every row — skim and emphasize the first three (LLM, token, prompt). Tell them this slide is the reference; we'll revisit each term in context.
-->

---

<!-- _class: divider -->

<span class="tag">Block 1</span>

# Fundamentals

<!--
Start of the densest block of the session. Warn them we're going to mentally "build" the agent from its pieces: what it is, brain, hands, memory, skills. Lasts 75 min with questions.
-->

---

# What (and what isn't) an agent?

The word is everywhere. It means different things:

- In classical AI: an object that **perceives** and **acts upon** an environment
- In products: any app with an LLM
- In venture capital: whatever can raise a Series A

**We're not going to invent a canonical definition.**
We'll use **five complementary lenses** and pick the useful one for each context.

<!--
Set the tone: the debate over "what is an agent" is real and open. We avoid dogmatism. The five lenses will give us common vocabulary to discuss.
-->

---

# 5 lenses for looking at an agent

| Lens | Where it comes from | What it contributes |
|---|---|---|
| **AIMA** (Russell & Norvig) | [Classical AI · 1995→](https://aima.cs.berkeley.edu/) | Taxonomy + connection to MDPs/RL |
| **Anthropic** | [*Building Effective Agents*](https://www.anthropic.com/engineering/building-effective-agents) · 2024 | *Workflow* vs *agent* |
| **OpenAI** | [*Practical guide to building agents*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) · 2025 | Model + Tools + Instructions |
| **LangChain** (H. Chase) | [*Cognitive architectures*](https://www.langchain.com/blog/what-is-a-cognitive-architecture) | Autonomy levels 1→6 |
| **CoALA** (Princeton) | [TMLR 2024](https://arxiv.org/abs/2309.02427) | Memory + actions + decision |

And [**Simon Willison**'s operational rule](https://simonwillison.net/2025/Sep/18/agents/): *"an LLM agent runs tools in a loop to achieve a goal."*

<!--
These five lenses are complementary, not mutually exclusive. Recommended order: start with the academic one (AIMA) to anchor the statistics/mathematics students, and move toward the operational ones.
-->

---

# Lens 1 · AIMA (Russell & Norvig)

> *"Anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators."*
> — [*Artificial Intelligence: A Modern Approach*](https://aima.cs.berkeley.edu/) (1995→2020)

**What matters**: the definition does not require language, intelligence, or LLMs.
A thermostat is an agent. A human is an agent. A program too.

**What does define an agent**: having an explicit or implicit **utility function**, and choosing actions that maximize it.

<!--
Show that the concept is very general and that LLMs are a particular case. This deflates magical expectations and sets the stage for talking about the perception-action loop.
-->

---

# AIMA taxonomy · 5 levels

1. **Simple reflex** — *condition → action* rule on the current percept
2. **Model-based reflex** — maintains internal state (partially observable environments)
3. **Goal-based** — picks actions that bring it closer to a goal
4. **Utility-based** — compares states with a utility function
5. **Learning** — adds *learning element + performance element + critic*

**An LLM with tools and a loop ≈ hybrid between goal-based and learning-by-context.**

<!--
This classification helps situate LLMs on the broader map. The fifth category connects naturally with RL.
-->

---

# Connection with MDPs and RL <small>(the statistician's lens)</small>

An agent can be read as a *policy* over a **Markov Decision Process** (MDP) $\langle S, A, P, R, \gamma\rangle$:

<small>$S$ = states · $A$ = actions · $P(s'\mid s,a)$ = transition probabilities · $R(s,a)$ = reward · $\gamma\in[0,1]$ = discount factor</small>

- $s_t$ = LLM context (messages + observations)
- $a_t$ = token-stream that produces a *tool-call* or response
- $r_t$ = test that passes, human reward, automated eval
- $\pi_\theta$ = the LLM with its prompt and tools

Three classical **reinforcement learning** (RL) problems reappear identically:

- **Credit assignment** in multi-turn (which step failed?)
- **Exploration** (call a new tool?)
- **Long horizon** — errors compound

<!--
For students with a background in statistics/probability, this is the slide that "sells" them the course. Make the analogy slowly. If any student asks about POMDPs, say yes, that's more accurate, because observation never covers the full state.
-->

---

# Lens 2 · Anthropic — *workflow* vs *agent*

<div class="columns">
<div>

### Workflow

**Predefined** steps in code.
*The programmer owns control flow.*

```
input → classify → template
       → policy → send
```

Predictable. Auditable. Cheap.

</div>
<div>

### Agent

LLM **decides** which tool to call and when to stop, in a loop.
*The model owns control flow.*

```
loop: LLM → tool → observation
       → stop?
```

Flexible. Expensive. Non-deterministic.

</div>
</div>

> **Heuristic**: if you can map the decision tree, **don't build an agent**.

<!--
Anthropic's distinction is useful but needs nuance: in practice almost every "agent" has workflow on top. What matters isn't picking a side but knowing when freedom is needed.
-->

---

# Lens 3 · OpenAI

> *"A system that independently accomplishes tasks on your behalf."*
> — [*A practical guide to building agents*](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf), OpenAI · 2025

**Three components:**

- **Model** — the brain that reasons
- **Tools** — *data*, *action*, *orchestration*
- **Instructions** — policy, format, *guardrails* (safety filters and limits)

**Minimal pattern:** `while` loop with an exit condition.
**When to split into multi-agent:** complex logic **or** many overlapping tools.

<!--
OpenAI's guide is pragmatic and recent. Useful because it introduces the "handoffs" vocabulary we'll see tomorrow in multi-agents.
-->

---

# Lens 4 · LangChain — autonomy levels <small>(synthesis)</small>

| Level | Who decides | Example |
|---|---|---|
| 1. Code only | The human (program) | `df.describe()` |
| 2. LLM call | Human + LLM once | "summarize this text" |
| 3. Chain | Program with several LLMs in fixed order | Classic RAG |
| 4. Router | LLM picks a branch | classifier → specialist |
| 5. State machine | LLM inside a graph with transitions | **LangGraph** |
| **6. Autonomous agent** | **LLM in a free loop** | Claude Code, Cursor |

> Harrison Chase (LangChain CEO): *"outsource your agentic infrastructure, but **own** your cognitive architecture."*

<!--
This table is a pedagogical synthesis inspired by Chase's writings — [What is an AI agent?](https://www.langchain.com/blog/what-is-an-agent) and [What is a Cognitive Architecture?](https://www.langchain.com/blog/what-is-a-cognitive-architecture) — it is not a taxonomy literally published with these 6 levels. Useful for situating tools. Most enterprise value is still at levels 3-5, not 6.
-->

---

# Lens 5 · CoALA <small>([Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427))</small>

Sumers, Yao, Narasimhan, Griffiths · Princeton · TMLR 2024

**An LLM agent has three axes:**

<div class="columns-3">
<div class="card">

**Memory** <small>(LTM = long-term memory)</small>

- *Working* (in-context)
- Episodic LTM
- Semantic LTM
- Procedural LTM

</div>
<div class="card">

**Actions**

- Internal (on memory itself)
- External (on the environment)

</div>
<div class="card">

**Decision**

- Planning
- Execution
- Reflection

</div>
</div>

ReAct, Reflexion, Voyager, Generative Agents... they all fit here.

<!--
CoALA is the most academically rigorous lens. Serves as common vocabulary for reading the literature. No need to go into detail, just have them see the framework.
-->

---

<!-- _class: quote -->

# *"An LLM agent runs tools in a loop to achieve a goal."*

<div class="author">— <a href="https://simonwillison.net/2025/Sep/18/agents/">Simon Willison</a> · September 2025
(after collecting >200 distinct definitions)</div>

<!--
This is the operational definition we'll use for the rest of the course. It's short, actionable, and compatible with almost every framework.
-->

---

# When NOT to build an agent

Three questions (Barry Zhang, Anthropic):

1. **Is the task ambiguous?** If you can map the entire decision tree → **workflow**
2. **Is it worth the cost?** If it's a small, cheap task, an agent is overkill
3. **Is the model capable of the atomic task?** Errors compound multiplicatively

> *"It is the decade of agents, not the year of agents."*
> — Andrej Karpathy · [Dwarkesh Podcast, Oct 2025](https://www.dwarkesh.com/p/andrej-karpathy)

Errors accumulate multiplicatively. Best to assume it will take time.

<!--
Karpathy said this on the podcast with Dwarkesh. Useful for injecting realism: agents work, but they're not magic and errors accumulate.
-->

---

# Spectrum: chatbot → RAG → workflow → agent

```
Pure chatbot
   └─ One LLM call, no state, no tools

RAG
   └─ LLM + pre-inference retrieval · fixed structure

Workflow
   └─ LLM(s) + tools on code-predefined routes

Agent
   └─ LLM + tools in a loop, decides flow, its own stopping criterion
```

**Most "agentic applications" are workflows with an LLM inside.**

<!--
Insist: the word "agent" sells a lot, but often what's built is an elegant workflow. That's not a failure: it's desirable when you can do it.
-->

---

# Discussion question

> To detect **fraud in bank transactions in real time**, would you use an agent or a workflow?
>
> Why?

<br>

Discuss with the person next to you. Then we share.

<!--
Expected answer: workflow. Reasons: latency (every decision in milliseconds), regulatory auditability, predictability. An agent with a large LLM is 100-1000x slower than a specialized XGBoost model. Plus: an agent is hard to audit for regulators.
-->

---

# Typical architecture · the agentic loop

```
                 ┌────────────────┐
                 │  Goal / Task   │
                 └────────┬───────┘
                          ▼
       ┌──────────────────────────────────┐
   ┌──►│  LLM (brain)                     │ ◄── system prompt + skills
   │   └────────┬─────────────────────────┘
   │            │ tool_call
   │            ▼
   │   ┌──────────────────────────────────┐
   │   │  Tools (hands)                   │ ── MCP, APIs, code,
   │   └────────┬─────────────────────────┘     filesystem, DBs, web
   │            │ observation
   │            ▼
   │   ┌──────────────────────────────────┐
   │   │  Memory (context + LTM)          │
   │   └────────┬─────────────────────────┘
   │            │
   │            ▼
   │         stop?
   │        ╱      ╲
   └─── no         yes ──► Response / Final action
```

> Four components: **brain · hands · memory · control loop**.
> Any one of them poorly sized breaks the whole system.

<!--
This is the reference diagram for the whole course. We'll return to it when we talk about design patterns in session 2. Insist: most production failures come from poorly designed control loops, not from the LLM.
-->

---

# The brain · reasoning models in 2026

**Frontier** — top-tier closed models, accessed via API

- **Claude** (Anthropic) — Opus 4.x, Sonnet 4.x
- **GPT-5.x** (OpenAI)
- **Gemini 3.x** (Google)
- **Grok 4** (xAI)

**Open-weights** — weights publicly downloadable, runnable on your laptop or server

- **Qwen3 / Qwen3.5 / Qwen3.6** (Alibaba) — Apache 2.0
- **Granite 4.1** (IBM) — Apache 2.0
- **DeepSeek V4 / R1** — large **MoE** (mixture-of-experts) models
- **Phi-4 / Phi-4-mini** (Microsoft) — MIT
- **Gemma 3 / 4** (Google), **SmolLM3** (HuggingFace), **Mistral 3**

<!--
Mention that the field changes monthly. Tomorrow's table may be obsolete. What matters is knowing where to look (Ollama Library, HF, official blogs).
-->

---

# Frontier vs open-weights — when which?

| Criterion | Frontier (API) | Open-weights (local) |
|---|---|---|
| Reasoning quality | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ – ⭐⭐⭐⭐ |
| Complex tool-use | Very reliable | Reliable on Qwen3+, Granite 4.1 |
| Cost per task | $$ | $ (electricity) |
| Latency | Cloud | Depends on hardware |
| Privacy | Data to the provider | 100% local |
| Reproducibility | Changes without notice | Pinnable versions |
| Fine-tuning | Limited | Full control |

**In the workshop we'll use open-weights**, not out of ideology, but so it **works without an account and without spending money**.

<!--
Balance: don't demonize closed nor idealize open. Each use case calls for an informed decision.
-->

---

# Lightweight open-weights · top 3 for the workshop

| Model | RAM Q4 | Tool-use | License | Command |
|---|---|---|---|---|
| **Qwen 3.5 4B** | ~3.5 GB | Excellent (native) | Apache 2.0 | `ollama pull qwen3.5:4b` |
| **Qwen 3.5 9B** ⭐ | ~6.5 GB | Excellent (native) | Apache 2.0 | `ollama pull qwen3.5:9b` |
| **Granite 4.1 8B** | ~5.3 GB | Solid on BFCL | Apache 2.0 | `ollama pull granite4.1:8b` |
| Gemma 4 e2b | ~2.5 GB | Native function-calling | Apache 2.0 | `ollama pull gemma4:e2b` |
| Gemma 4 e4b | ~4.5 GB | Native function-calling | Apache 2.0 | `ollama pull gemma4:e4b` |

*Q4 = 4-bit quantization (model compressed to ¼ the memory, small quality loss).*
*BFCL = Berkeley Function Calling Leaderboard, a tool-use benchmark.*
*Why Qwen 3.5 (not 3.6): Qwen 3.6 only ships at 27B+ — too large for laptops.*

> For 32 GB, **Gemma 4 26B** is a fast MoE option: `ollama pull gemma4:26b` (~18 GB).
> Also solid: **Granite 4.1 30B** (~17 GB) and **Nemotron Cascade-2 30B MoE**.

<!--
Recommend qwen3.5:9b as default. If the student has only 8 GB, qwen3.5:4b or gemma4:e2b. CRITICAL: the day before, verify on ollama.com/library that tags are still live — model names change frequently. Bring a USB with the .gguf files in case classroom WiFi fails. Fallbacks if a tag moved: granite4.1:3b (lighter), qwen3:8b (previous generation). Note: Gemma 4 switched to Apache 2.0 (earlier Gemma versions used Google's Gemma terms) — fully permissive for commercial reuse.
-->

---

# The hands · function calling

**How it works in 3 steps:**

```python
# 1. Describe the tool as a JSON schema
tools = [{
    "name": "descriptive_stats",
    "description": "Compute descriptive statistics of a CSV",
    "parameters": {
        "type": "object",
        "properties": {"path": {"type": "string"}},
        "required": ["path"]
    }
}]

# 2. The LLM responds with a structured object, not text
# {"tool": "descriptive_stats", "args": {"path": "iris.csv"}}

# 3. Your runtime executes the tool and returns its output to the LLM
```

**Important**: the "magic" lies in the model's *fine-tuning* to emit valid JSON when tools are in the prompt.

<!--
Do the live demo: invoke the Anthropic/OpenAI API with a basic tool. Show the raw response with tool_calls.
-->

---

# MCP · [Model Context Protocol](https://modelcontextprotocol.io)

**What it is:** a universal **JSON-RPC** (remote procedure calls encoded in JSON) protocol between **clients** (Claude Desktop, Cursor, ChatGPT) and **servers** (processes that expose tools, resources, prompts).

**Origin:** Anthropic, Nov 25, 2024. **Open source** (Linux Foundation since Dec 2025).

**Why it matters:**
- Moves from **N×M** ad-hoc integrations to **N+M**
- Once you have an MCP server for your DB, **any client** can use it
- De facto standard in 2026

**Five primitives:** tools, resources, prompts, sampling, roots
**Two transports:** stdio (local) and Streamable HTTP (remote, OAuth 2.1)

<!--
MCP is the most important infrastructure change of 2025-2026 for agents. If students take away a single technical idea, let it be this one.
-->

---

# MCP · 2026 adoption state

- **Thousands of MCP servers** published (public registry + private)
- **Tens of millions of monthly downloads** of the SDK (software development kit — the library devs use)
- **Most enterprise teams** report at least one MCP-based agent in production

**Native support in:**
Claude · ChatGPT (Apps SDK) · Gemini API · Vertex AI · Cursor · Windsurf · Zed · JetBrains AI · OpenAI Agents SDK · Vercel AI SDK

**Adjacent ecosystem:**
- **A2A** (Google, under Linux Foundation) — agent↔agent, JSON-RPC
- **ACP** (IBM / BeeAI, now merged into A2A) — REST-native agent interop
- **AG-UI** — frontend↔agent

<!--
Specific figures in consultancy reports vary month to month. What matters: adoption is no longer niche. If any student asks for a number, mention there are public but verifiable reports.
-->

---

# Ttools · live example · setup

**Instructor demo** — same stack you'll install in Block 4: OpenCode + Ollama + a local open-weights model.

**Launch OpenCode** — model comes from the config (`ollama/gemma4`):

```bash
ollama launch opencode --model gemma4
```

<!--
Pre-populate ~/Downloads with 2-3 small CSVs (iris.csv, titanic.csv) before class. Replace `/Users/you/Downloads` with the instructor's actual path — OpenCode's command array is exec-style, so ~ is NOT expanded. Warm the npx cache once before class (run the command manually) so the first tool discovery isn't a 30-second dead silence.
-->

---

# Tools · live example · run

**Ask in the chat:**

> *"List the CSVs in my Downloads folder"*

**Under the hood:**
1. OpenCode discovers the tools 
2. Gemma emits a structured call to the proper tool
3. OpenCode runs it locally → returns the file listing
4. Gemma loops (read each CSV → count rows) → composes the final answer

**No cloud. No API key. Same protocols as Claude Desktop and Cursor use.**

<!--
Show the tool-call trace in OpenCode's TUI so students literally see the discover → call → observe cycle. Main takeaway: MCP is protocol + ergonomics, not Anthropic-specific — it drives ANY tool-capable model, including small open-weights running fully local on a laptop. If short on time, skip straight to the trace and narrate it.
-->

---

# Memory · four types

| Type | What it stores | Examples |
|---|---|---|
| **Working / context** | Active tokens | The LLM itself |
| **Episodic** | "What I did last week" | Mem0, Letta, Zep, MemMachine |
| **Semantic** | Facts, profiles, KG | Qdrant, pgvector, Neo4j |
| **Procedural** | Rules, *skills*, scripts | Claude Skills, AGENTS.md |

> CoALA framework: human memory serves as inspiration, not as an exact map.

<!--
The psychology students will recognize the terms. Use it for a mini-discussion on what happens to the memory of a system that has no sleep/consolidation.
-->

---

# Context engineering > prompt engineering

> *"The set of strategies for curating and maintaining the optimal set of tokens during inference."*

**Mindset shift:**
- ❌ From: picking the best 5 sentences of the system prompt
- ✅ To: designing **what information arrives when**

**Key techniques:**
- **Just-in-time retrieval** — `glob` and `grep` explore on demand
- **Tool-mediated retrieval** — the LLM asks for what it needs
- **Compression** — summary between steps
- **Pruning** — discard the irrelevant
- **Hierarchical loading** — *progressive disclosure* (load detail only when needed)

<!--
This is probably the most underestimated skill in practical agents. Insist.
-->

---

# Skills · *progressive disclosure*

```yaml
---
name: pdf-processing
description: Extract text and tables from PDF files, fill forms.
  Use when the user mentions PDFs or document extraction.
---

# Instructions
1. ...
```

**Loads in three levels:**

1. **Frontmatter** always in context (~50 tokens)
2. **Body** loads if the skill activates
3. **Sub-files** only if relevant

> Decouples the **size** of the skill from its **cost per token**.

<!--
Open standard since Dec 2025. Compatible with Claude Code, OpenAI Codex, Cursor. It's like "installing knowledge" into your agent without inflating the system prompt.
-->

---

# Skills vs MCP vs subagents

| Concept | What it provides | When to use it |
|---|---|---|
| **MCP** | Access to tools / data | Connecting to external systems |
| **Skill** | Procedure / knowledge | Teaching **how** to do something |
| **Subagent** | Process with its own context | Isolate context, parallelize |

**They're complementary, not mutually exclusive.**

Real example: a "statistical analysis" *skill* uses the internal DB's *MCP* and delegates to a "QA" *subagent* to review the output.

<!--
If they only remember three words, let them be MCP/Skill/Subagent.
-->

---

<!-- _class: break -->

# ☕ Break

<!--
Leave the classroom. Return at exactly XX:XX. Warn them in the last minute.
-->

---

<!-- _class: divider -->

<span class="tag">Block 2</span>

# Framework landscape
## and existing agents

<!--
Lighter block. Goal: that students know what's out there and what they'd pick professionally.
-->

---

# Open source frameworks · 2026 landscape

| Framework | Philosophy | Curve |
|---|---|---|
| **LangGraph** | Directed graph with state, checkpoints, HITL | High |
| **CrewAI** | Roles + goals + tasks ("crew") | Low |
| **AutoGen / AG2** | Multi-agent conversations | Medium |
| **OpenAI Agents SDK** | Handoffs between agents | Low |
| **Google ADK** | Hierarchical tree, native A2A | Medium |
| **PydanticAI** | Extreme type-safety | Medium |
| **Smolagents** (HF) ⭐ | ~1000 LOC, *CodeAgent*, sandbox | **Very low** |
| **Agno** | Multi-agent runtime with good DX | Medium |
| **LlamaIndex Agents** | Centered on RAG over data | Medium |
| **DSPy** | Optimizable prompt programming | High (different paradigm) |

*HITL = human-in-the-loop · DX = developer experience · LOC = lines of code · SDK = software development kit.*

> Tomorrow we'll use **Smolagents** in the workshop.

<!--
Don't memorize the table. The idea is for them to know there are options and how they differ. We pick Smolagents for the gentlest learning curve.
-->

---

# How to choose a framework <small>(simple matrix)</small>

```
                        Single ←──── Composition ────→ Multi-agent
                          │
      Low flow control    │   smolagents      ·   CrewAI
                          │   PydanticAI      ·   AutoGen
                          │
                  ────────┼──────────────────────────────────
                          │
      High flow control   │   LangChain      ·   LangGraph
                          │   classic        ·   Microsoft AF
                          │
```

**Harrison Chase's rule of thumb:**
> *"Outsource your agentic infrastructure, but **own** your cognitive architecture."*

<!--
Convey the idea: the framework is disposable infrastructure. The cognitive architecture (how your agent thinks) is the only thing that's really yours.
-->

---

# Coding agents · the most mature on the market

**Why coding first**: tests are verifiable → clear reward signal.

- **Claude Code** (Anthropic, terminal) — current benchmark
- **Cursor / Windsurf** (IDEs)
- **GitHub Copilot Coding Agent**
- **OpenAI Codex** (with Background Computer Use)
- **Devin** (Cognition) — expensive, variable performance depending on benchmark
- **Replit Agent** — long sessions, autonomous
- **OpenCode / Pi** — open source, terminal

> It's the area where agents work best today.

<!--
If someone asks which to use professionally: Claude Code or Cursor are clearly ahead. OpenCode if you want open source. Devin is expensive and benchmarks are uneven.
-->

---

# *Vibe coding* and app builders

**They build full-stack apps from natural language:**

- **Lovable** · **Bolt** · **v0** (Vercel) · **Same.dev**
- **Manus** · **Leap.new** · **Replit**

**Useful for**: quick prototypes, landing pages, demos.
**Not useful for**: real production, refactors, complex systems.

> *"The fastest way to build software is to vibe code your idea, then have someone rewrite it properly."* — the line you hear in SF in 2026.

<!--
Mention that this is what's revolutionizing bootcamps and at the same time generating massive technical debt. Statisticians can use it for quick dashboards.
-->

---

# Computer use · agents that move the mouse

- **Anthropic Computer Use** — receives a screenshot, returns actions
- **ChatGPT Agent Mode** (OpenAI, integrates the old Operator)
- **Google Gemini Computer Use** / Project Mariner
- **Manus AI** — "general **VM** (virtual machine) agent"

**Real state**: they work, but they're **slow** (seconds per action), **fragile** (UI changes break them), **expensive**.

**OSWorld benchmark**: performance still clearly below expert human.

<!--
Show one live if possible (Claude Computer Use opening a spreadsheet). The "wow" is high but practical utility is still limited. Operator was integrated into ChatGPT Agent in July 2025; it's no longer a separate product.
-->

---

# Browser agents · the next frontier

- **Perplexity Comet** (free since Oct 2025)
- **ChatGPT Atlas** (Oct 2025, macOS only)
- **Claude for Chrome** (extension)
- **Edge Copilot Mode** · **Opera Aria/Neon** · **Brave Leo**
- **BrowserOS** (open source, Chromium fork with Ollama)

**Advantages**: session, cookies, login already there.
**Risks**: prompt injection from any visited page (we'll cover this tomorrow in security).

<!--
Teaser: the browser agent is the area most vulnerable to prompt injection. Tomorrow we go deeper.
-->

---

# Open legal case · Amazon vs Perplexity

**January 2026**: Amazon sues Perplexity for using Comet agents to automate purchases, alleging a bypass of Amazon's **Terms of Service (TOS)**.

**Perplexity's position**: the agent acts as a human, identifying itself with a standard User-Agent.

**Amazon's position**: automation at scale violates the terms of service.

> **Question for the group**:
> Is this legitimate TOS defense or resistance to change?
> Who bears responsibility when an agent "clicks"?

<!--
3-minute discussion. No correct answer. Plant the regulatory seed we'll see tomorrow.
-->

---

<!-- _class: divider -->

<span class="tag">Block 3</span>

# Agents you can already use today

<!--
Short, concrete block. Quick demos, no installation.
-->

---

# Recommended stack for a statistics / data profile

<div class="columns">
<div>

### Analysis and code

- **Claude Code**, **OpenAI Codex** or **Cursor** for scripts
- **Code Interpreter / Artifacts** for ad-hoc analysis
- **OpenCode + Ollama** local (today's workshop)

</div>
<div>

### Research and synthesis

- **Perplexity** / Perplexity Pro Search
- **NotebookLM** for synthesizing papers
- **Deep Research** (Anthropic, OpenAI, Gemini) or **Elicit** for systematic review

</div>
</div>

> There's no "correct" stack. What kills you is not trying.

<!--
Advise them to try 2-3 tools next week and stick with the one that saves them the most real time.
-->

---

# Quick demos

1. **Perplexity Pro Search** — *"robust methods in PCA, 2024-2026 papers"*
2. **NotebookLM** — 3 papers in Spanish → mind map + podcast
3. **Claude / ChatGPT** with artifacts — live CSV analysis
4. **Claude Computer Use** — open Excel, fill out a summary table

**What you'll see**: the difference between a *chatbot* (saying things) and an *agent* (doing things).

<!--
Have the tools open and tested before class. If any fails, move to the next without wasting time.
-->

---

<!-- _class: divider -->

<span class="tag">Block 4</span>

# Workshop: your first agent without code

<!--
Hands-on block. Goal: that every student has a local agent running with Ollama + OpenCode.
-->

---

# Workshop plan

| Min | Activity |
|---|---|
| 0–10 | **Instructor demo**: Claude Code in action |
| 10–15 | Install Ollama (in parallel) |
| 15–20 | Download the recommended model |
| 20–25 | Install + configure OpenCode |
| 25–55 | **Open task**: agent analyzes a CSV and generates a report |
| 55–60 | We share results |

> **Prerequisites**: ≥ 8 GB RAM, ≥ 15 GB free disk, install permissions.

<!--
Have a shared chat channel for errors. Pre-load the models on a USB in case classroom WiFi fails.
-->

---

# Instructor demo · Claude Code

Example task:
> *"Add NumPy-style docstrings to this module and generate a README based on the tests."*

**Show:**
- Subagents (Explore, Plan)
- Dynamically loaded skills
- Connected MCP servers (filesystem, git)
- Visible reasoning trace
- When the agent asks for confirmation (**human-in-the-loop / HITL**)

> This is the "ceiling" of what's possible today. You'll build something simpler, but of the same lineage.

<!--
Have a small repo prepared and already cloned. If something fails, show a backup screen recording.
-->

---

# Your stack · Ollama + OpenCode

```
┌─────────────────────────────────┐
│  OpenCode (TUI)                 │  ← interface, manages conversation,
│                                 │     tools, MCP, reasoning
└──────────────┬──────────────────┘
               │ HTTP localhost:11434
               ▼
┌─────────────────────────────────┐
│  Ollama (model server)          │  ← downloads, quantizes,
│                                 │     runs the LLM
└──────────────┬──────────────────┘
               │
               ▼
        Model (Qwen 3.5 9B, ~6.5 GB)
```

*TUI = terminal user interface (text-only, no mouse). Quantize = compress a model to fewer bits per weight.*

**Both open source. Run offline. No account. Cross-platform.**

<!--
Insist: zero cloud dependency, zero account, zero cost. Quality is lower than Claude/GPT but enough to learn.
-->

---

# Step 1 · Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Windows: download installer from ollama.com

# Verify
ollama --version
```

**Check that the server responds:**

```bash
curl http://localhost:11434/api/tags
```

If it returns JSON, you're good.

<!--
If anyone has firewall or antivirus issues, pair with a classmate or use the USB with offline installers.
-->

---

# Step 2 · Download the model

```bash
# 8 GB RAM
ollama pull qwen3.5:4b        # ~3.5 GB

# 16 GB RAM (recommended)
ollama pull gemma4:e4b        # ~9.4 GB
ollama pull qwen3.5:9b        # ~6.5 GB

# 32 GB RAM (fast MoE)
ollama pull gemma4:26b        # ~18 GB
```

**Smoke test:**

```bash
ollama run gemma4 "Hi, what model are you?"
```

> ⚠️ If tools fail later in the workshop, suspect the **default `num_ctx` (4K). You need to raise it to 32K**.

<!--
Load the models onto a USB before class to hand out to anyone without a decent connection. If any specific tag has changed, ollama.com/library has the official list.
-->

---

# Step 3 · Install OpenCode

```bash
# Recommended
curl -fsSL https://opencode.ai/install | bash

# Alternatives
npm install -g opencode-ai@latest
brew install sst/tap/opencode

# Verify
opencode --version
```

**Create a config file** at
`~/.config/opencode/opencode.json` (Linux/macOS)
or `%APPDATA%\opencode\opencode.json` (Windows).

<!--
If OpenCode doesn't install, alternative: ollama launch opencode (new shortcut in 2026 that writes the config inline).
-->

---

# Step 3b · Minimal `opencode.json`

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": {
    "ollama": {
      "models": {
        "gemma4": {
          "name": "gemma4",
          "tools": true,
          "reasoning": true,
          "options": { "num_ctx": 32768 }
        },
        "qwen3.5:4b": {
          "name": "qwen3.5:4b",
          "tools": true,
          "reasoning": true,
          "options": { "num_ctx": 32768 }
        }
      },
      "name": "Ollama",
      "npm": "@ai-sdk/openai-compatible",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1"
      }
    }
  }
}

```

<!--
Paste this JSON literally into the file. No tabs or comments — pure JSON.
-->

---

# Step 4 · Workshop tasks

Each student picks ONE. Work in pairs if you like.

```
1. Iris analyst
   "Download the Iris dataset from sklearn, compute the
    correlation matrix and save it as heatmap iris_corr.png."

2. Doc generator
   "Generate a Markdown that explains what an agent is,
    citing 3 web sources. Save it as agent_intro.md."

3. CSV explorer
   "Read sales.csv (I'll provide it) and compute mean,
    median, and standard deviation by category."
```

**Launch OpenCode:**
```bash
mkdir ~/2026-agents-usal && cd ~/2026-agents-usal
opencode
```

<!--
Have the datasets ready in a repo or USB. Walk around the classroom, tend to errors.
-->

---

# Troubleshooting · if something fails

| Symptom | Likely cause | Fix |
|---|---|---|
| Model replies with text but **doesn't call tools** | `num_ctx` too low | Raise to 16K-32K in `opencode.json` |
| `Connection error` | Ollama not running | `ollama serve` in another terminal |
| Streaming gets cut | Undici timeouts | Update OpenCode to the latest release |
| Out of memory | Model too large | Switch to `qwen3.5:4b` or `gemma4:e2b` |
| Tool-call fails with many tools | Hermes-style hallucinates | Reduce tools, raise `num_ctx` |
| MCP server **SSE** (Server-Sent Events) gives `UnknownError` | Known bug | Use streamable HTTP transport |

<!--
These are the problems that appear 80% of the time. Keep them on a printed handout.
-->

---

# Pi — minimalist alternative (brief mention)

[`pi-mono`](https://github.com/badlogic/pi-mono) (by Mario Zechner / *badlogic*) is a deliberately **anti-feature** *coding agent*:

- **No** MCP, no sub-agents, no permission popups
- Just 4 core tools (read/write/edit/bash)
- Philosophy: *"build CLI tools with READMEs, the agent reads them on demand"*

> Useful as a **pedagogical provocation**: where should complexity live? In the harness or in traditional Unix tools?

**Don't install it today.** Mentioned for the curious.

<!--
Just mention it. Not a priority. The curious can check github.com/badlogic/pi-mono afterward.
-->

---

# Hermes Agent — self-evolving alternative (brief mention)

[`hermes-agent`](https://github.com/NousResearch/hermes-agent) (Nous Research) takes the **opposite bet** to pi:

- **Autonomous skill creation** — generates and refines procedures from experience
- **Persistent memory** across sessions, full-text session search
- **Multi-platform gateway** — Telegram, Discord, Slack, WhatsApp, Signal from one backend
- Runs on anything from a $5 VPS to GPU clusters · **MIT** licence
- Companion repo [`hermes-agent-self-evolution`](https://github.com/NousResearch/hermes-agent-self-evolution) auto-optimises skills + prompts via DSPy + GEPA

> **Pedagogical provocation**: where should the agent's knowledge live? Baked into Unix tools (pi) or evolved at runtime (hermes)?

**Don't install it today.** Mentioned for the curious.

<!--
Contrasts sharply with pi. Pi is the "Unix philosophy" end of the spectrum (small composable tools, agent stays dumb); Hermes is the "autonomous skill acquisition" end (agent grows its own toolbox). Neither is definitively correct — the trade-off is exactly what we want students to debate. Nous also ships the separate hermes-agent-self-evolution repo that meta-optimizes this one; that's a useful example of "agent that improves agent" if someone asks.
-->

---

# OpenClaw — batteries-included, local-first (brief mention)

[OpenClaw](https://openclaw.ai/) (formerly ClawdBot) sits at the opposite end from pi: *everything bundled, everything local*.

- **Multi-platform** — WhatsApp, Telegram, Discord, Slack, Signal, iMessage
- **50+ integrations** out of the box (Gmail, Notion, HomeKit, browser automation…)
- **Privacy-first** — data stays on your machine unless you explicitly send it out
- **Model-agnostic** — Claude / GPT / Gemini / Llama / Mistral + **Ollama** + LM Studio
- **MIT**, TypeScript · `npm i -g openclaw` · repo [openclaw/openclaw](https://github.com/openclaw/openclaw)

> One axis, three takes: **pi** (nothing included) → **Hermes** (self-evolving) → **OpenClaw** (batteries-included, local).

**Don't install it today.** Mentioned for the curious.

<!--
Renamed from ClawdBot to OpenClaw; the openclaw.ai site and openclaw/openclaw repo are the current canonical refs. Closest cousin to Hermes in the "multi-platform personal-assistant gateway" category, but where Hermes leans into autonomous self-improvement, OpenClaw leans into pre-packaged integrations and explicit data-stays-local defaults. Useful as the third point of the architectural-philosophy triangle: minimalism vs. self-evolution vs. batteries-included.
-->

---

<!-- _class: divider -->

# Wrap-up

<!--
Last 15 minutes. Recap, readings, short survey.
-->

---

# What we've seen today

✅ Five lenses to define an agent · when NOT to use one
✅ Loop: brain + hands + memory + control
✅ 2026 models · frontier vs open-weights
✅ Function calling · MCP · Skills
✅ Frameworks · vertical agents · computer use · browser agents
✅ Your first local agent up and running

**Tomorrow**: how they're built, how they're evaluated, how they break.

<!--
Listing what's been accomplished reduces anxiety. Mention that tomorrow is even more hands-on.
-->

---

# Reading for tonight (optional, ~30 min)

**Essential:**
- Anthropic — [*Building Effective Agents*](https://www.anthropic.com/engineering/building-effective-agents) (Dec 2024)
- Anthropic — [*Effective Context Engineering*](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) (2025)
- HuggingFace — [*Introducing smolagents*](https://huggingface.co/blog/smolagents) (2024)

**Supplementary:**
- Karpathy on Dwarkesh — [*AGI is still a decade away*](https://www.dwarkesh.com/p/andrej-karpathy) (Oct 2025)
- Kambhampati et al. — [*LLMs Can't Plan, But Can Help Planning*](https://arxiv.org/abs/2402.01817) (ICML 2024)
- Simon Willison — [*agent-definitions* tag](https://simonwillison.net/tags/agent-definitions/)

> If you read only one: Anthropic's **[Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents)**.

<!--
Share all the links in the course channel. Nothing is required reading for tomorrow.
-->

---

# Question for tomorrow

> *Which of your tasks would clearly benefit from an **agent** vs. a **rigid workflow**?*
>
> Think it over tonight. We'll discuss at the start tomorrow.

<!--
Plant the question so tomorrow we open with discussion, not a monologue.
-->

---

<!-- _class: cover -->
<!-- _header: '' -->
<!-- _footer: '' -->
<!-- _paginate: false -->

# See you tomorrow! 👋

## May 6 · 16:00
### Building, evaluating, and securing agents

<br>

*Thank you.*

<!--
Say goodbye. Stay for individual questions. Remind them of tomorrow's time.
-->
