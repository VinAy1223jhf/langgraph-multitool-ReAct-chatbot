from langchain_community.tools import ArxivQueryRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq 
from typing_extensions import TypedDict
from langchain_core.messages import AnyMessage #can be either human or ai message
from typing import Annotated #labelling
from langgraph.graph.message import add_messages # reducers langgraph 
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import InMemorySaver as MemorySaver


import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
os.environ["TAVILY_API_KEY"]=os.getenv("TAVILY_API_KEY")

api_wrapper_arxiv=ArxivAPIWrapper(top_k_results=2,doc_content_chars_max=500)
arxiv=ArxivQueryRun(api_wrapper=api_wrapper_arxiv,description="query arxiv papers in detail.")

api_wrapper_wikipedia=WikipediaAPIWrapper(top_k_results=2,doc_content_chars_max=500)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper_wikipedia,description="Search wikipedia for required information.")

tavily=TavilySearchResults()

# combime all these tools in a list
tools=[arxiv,wiki,tavily]

# initialize the llm model
llm=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# combine these tools with lllm
llm_with_tools=llm.bind_tools(tools=tools)

class State(TypedDict):
    messages: Annotated[list[AnyMessage],add_messages] # add_messages would be a function which would append messanges in the messages variable instead of overwriting it
    

# node definition
def tool_calling_llm(state:State):
    return {"messages":[llm_with_tools.invoke(state["messages"])]}

def tool_calling_llm(state: State):
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


# ================== GRAPH ==================
def build_graph():
    checkpointer = MemorySaver()
    builder = StateGraph(State)

    builder.add_node("tool_calling_llm", tool_calling_llm)
    builder.add_node("tools", ToolNode(tools))

    builder.add_edge(START, "tool_calling_llm")
    builder.add_conditional_edges(
        "tool_calling_llm",
        tools_condition,
    )
    builder.add_edge("tools", "tool_calling_llm")
    # builder.add_edge("tool_calling_llm", END)

    return builder.compile(checkpointer=checkpointer)

# Build once
graph = build_graph()


from langchain_core.messages import AIMessage

def extract_tools(messages):
    tools_used = set()

    for msg in messages:
        if isinstance(msg, AIMessage) and msg.tool_calls:
            for tool_call in msg.tool_calls:
                tools_used.add(tool_call["name"])

    return list(tools_used)

# ================== CHAT FUNCTION ==================
from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.messages import HumanMessage

def chat(user_input: str, thread_id: str):
    result = graph.invoke(
        {
            "messages": [HumanMessage(content=user_input)]
        },
        config={
            "thread_id": thread_id
        }
    )

    final_answer = result["messages"][-1].content
    tools_used = extract_tools(result["messages"])

    return final_answer, tools_used







