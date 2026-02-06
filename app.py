# app.py
import streamlit as st
from chatbot import chat

st.set_page_config(
    page_title="LangGraph Memory Chatbot",
    page_icon="🧠",
)

st.title("🧠 LangGraph Memory Chatbot")

# One thread per user session
if "thread_id" not in st.session_state:
    st.session_state.thread_id = "user-1"  # later you can make this dynamic

user_input = st.chat_input("Ask anything...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response, tools_used = chat(
                user_input,
                st.session_state.thread_id
            )

            st.markdown(response)

            if tools_used:
                st.caption("🔍 Tools used: " + ", ".join(tools_used))
