import streamlit as st
from langchain_core.tools import BaseTool
from models.schema import MemorySearchInput


class MemorySearchTool(BaseTool):
    name: str = "memory_search"
    description: str = "Search for information in the conversation memory to answer questions about past interactions"

    def _run(self, query: str) -> str:
        if not st.session_state.memory_store:
            return "No previous conversation memory available."

        conversation_text = ""
        for msg in st.session_state.memory_store:
            role = msg.get("role", "")
            content = msg.get("content", "")
            conversation_text += f"{role}: {content}\n\n"

        if st.session_state.conversation_summary:
            conversation_text += f"Conversation summary: {st.session_state.conversation_summary}\n\n"

        return f"Relevant information from conversation:\n{conversation_text}"

    def __init__(self):
        super().__init__(args_schema=MemorySearchInput)