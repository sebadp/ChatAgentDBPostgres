from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory


def create_memory(llm, use_summary=True):
    """Create conversation memory system"""
    if use_summary:
        memory = ConversationSummaryMemory(
            llm=llm,
            memory_key="chat_history",
            return_messages=True
        )
    else:
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

    return memory


def save_to_memory_store(memory_store, human_message, ai_message):
    """Save interaction to memory store for search tool"""
    memory_store.append({"role": "human", "content": human_message})
    memory_store.append({"role": "ai", "content": ai_message})
    return memory_store


def update_conversation_memory(memory, human_input, ai_output):
    """Update the conversation memory with new interaction"""
    memory.save_context({"input": human_input}, {"output": ai_output})
    return memory