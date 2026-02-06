<p align="center">
  <h1 align="center">🧠 LangGraph Multi-Tool ReAct Chatbot</h1>
  <p align="center">
    ⚡ A stateful, tool-using AI agent powered by LangGraph & ReAct<br/>
    🛠️ Wikipedia · arXiv · Web Search · Agent Memory
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/LangGraph-Agentic%20AI-blueviolet"/>
  <img src="https://img.shields.io/badge/ReAct-Reason%20%2B%20Act-orange"/>
  <img src="https://img.shields.io/badge/Memory-LangGraph%20Checkpointer-success"/>
  <img src="https://img.shields.io/badge/UI-Streamlit-red"/>
</p>

---

## ✨ What is this?

This project is a **multi-tool conversational AI agent** built using **LangGraph**, following the **ReAct (Reason + Act)** paradigm.

Unlike typical chatbots that fake memory in the UI, this agent:
> 🧠 **Owns its memory internally using LangGraph checkpointers**

It can:
- Decide *when* to use tools
- Choose *which* tool to use
- Reason over tool outputs
- Remember context across turns
- Transparently show which tools were used

---

## 🚀 Why this is interesting

Most chatbots:
- ❌ store memory in the frontend
- ❌ dump raw tool output
- ❌ blur UI and agent logic

This chatbot:
- ✅ uses **agent-side memory**
- ✅ follows **explicit graph-based execution**
- ✅ separates **UI, reasoning, tools, and memory**
- ✅ mirrors **production-grade agent architecture**

---

## 🧠 Agent Architecture (High Level)

<img width="356" height="317" alt="image" src="https://github.com/user-attachments/assets/9dcd86ab-4397-4941-801a-b2ac5a985bfa" />

Clean Answer + Tool Transparency


---

## 🛠️ Tools Used

| Tool | Purpose |
|----|--------|
| 📘 Wikipedia | General knowledge |
| 📄 arXiv | Research papers |
| 🌐 Tavily | Real-time web search |

The agent **decides automatically** whether a tool is required.

---

## 🧩 Tech Stack

- **LangGraph** – agent graph & memory
- **LangChain** – tooling & message abstraction
- **ChatGroq (llama/llama-4-scout-17b-16e-instruct)** – LLM
- **Streamlit** – UI
- **Python**

---


---

## ▶️ Run Locally

```bash
git clone https://github.com/VinAy1223jhf/langgraph-multitool-react-chatbot.git
cd langgraph-multitool-react-chatbot
pip install -r requirements.txt
streamlit run app.py
```

## 🔑 Environment Variables

Create a .env file:
```bash
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

## 🧠 Memory Design (Core Highlight)

- ❌ No Streamlit session memory

- ❌ No manual history passing

- ✅ LangGraph MemorySaver checkpointer

- ✅ Thread-based conversation state

- ✅ Agent resumes context automatically

This is how real agent systems are built.

## 💬 Example Prompts

“What is the current weather in Sangrur?”

“Summarize the latest arXiv paper on diffusion models”

“Explain transformers like I’m new to ML”

The agent:

- Reasons

- Uses tools (if needed)

- Summarizes cleanly

- Shows tool usage

## 🎯 What I Learned

- Designing stateful agents with LangGraph

- ReAct-style tool orchestration

- Why agent memory ≠ UI memory

- Handling noisy tool outputs

- Building clean agent-UI boundaries

# 👤 Author

Vinayak Garg
B.Tech (AI) – NSUT Delhi
Interested in Agentic AI, LLM Systems & Applied ML

<p align="center"> ⭐ If this helped or inspired you, consider starring the repo ⭐ </p> ```
