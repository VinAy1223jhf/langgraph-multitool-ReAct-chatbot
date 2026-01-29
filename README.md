# LangGraph Multi-Tool ReAct Chatbot 🤖

A learning-focused chatbot that demonstrates **how LangGraph can be used to explicitly control reasoning and tool usage**, while leveraging **LangChain for LLMs and tools**.

This project explores *why* and *when* LangGraph is useful compared to traditional LangChain agents.

---

## 🧠 Core Idea

- **LangChain** → builds the components (LLMs, tools, wrappers)
- **LangGraph** → controls the reasoning flow between those components

Instead of relying on implicit agent loops, the chatbot follows an **explicit ReAct-style workflow**:
Think → Act (tool call) → Observe → Decide → Respond.

---

## 🔁 Workflow

START → Assistant → Tools → Assistant → END


The assistant can loop between tools (Wikipedia, Arxiv, Web Search) based on reasoning logic defined in the graph.

---

## 🛠️ Tools Used

- Wikipedia
- Arxiv
- Internet / Web Search
- LLM via LangChain

---

## 📁 Project Files

- `chatbotmultipletools.ipynb` — main implementation
- `requirements.txt` — dependencies

---

## 🚀 Getting Started

```bash
pip install -r requirements.txt
```

## Run the notebook:
jupyter notebook chatbotmultipletools.ipynb

## Why LangGraph?

LangGraph makes it easier to:

- Define explicit control flow

- Add conditional logic and thresholds

- Debug stateful conversations

- Build predictable, production-ready agents

- LangChain and LangGraph are used together, not as replacements.
