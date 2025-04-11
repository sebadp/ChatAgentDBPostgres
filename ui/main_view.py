import streamlit as st
from langchain.memory import ConversationSummaryMemory
from langchain_core.exceptions import OutputParserException
from config.settings import MEMORY_SEARCH_PROMPT, DIRECT_RESPONSE_PROMPT
from core.memory import update_conversation_memory, save_to_memory_store
from utils.json_helpers import parse_dispatch_result


def render_instructions():
    """Render the initial instructions for the app"""
    st.markdown("---")
    st.markdown("""
    **Instructions:**
    1. Configure the model type (local with Ollama or API with OpenAI)
    2. Configure the connection to your PostgreSQL database
    3. Connect to the database using the "Connect" button
    4. Ask questions in natural language about:
       - Your data in the database
       - Previous queries and their results
       - Contextual information from the conversation

    The intelligent agent will decide whether it needs to query the database, search memory, or respond directly.
    """)


def render_chat_history():
    """Render the chat history from session state"""
    for message in st.session_state.messages:
        if message["role"] == "human":
            with st.chat_message("user"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant"):
                st.write(message["content"])


def process_query(prompt, show_reasoning=False):
    """Process user query through the planning system"""
    try:
        dispatch_result = st.session_state.dispatcher_chain.invoke(prompt)
        reasoning, action, explanation = parse_dispatch_result(dispatch_result)

        # If user wants to see reasoning, we'll show it
        if show_reasoning:
            with st.expander("🧠 Planner reasoning", expanded=True):
                st.markdown(f"""
        **🧭 Decided action:** `{action}`

        **📖 Reasoning:**
        {reasoning}
        **🗣 Explanation:**
        {explanation}
        """)

        # Based on the decided action, call the corresponding agent
        if action == "database_query":
            try:
                response = st.session_state.sql_agent.invoke({"input": prompt})
                result = response.get("output", "Agent returned no output.")
            except OutputParserException as e:
                raw = getattr(e, "llm_output", "No raw output")
                result = f"Se encontró un error al interpretar la respuesta. Intentaré extraer la información útil:\n\n{raw}"
            except Exception as e:
                result = f"Error en la consulta: {str(e)}"
        elif action == "memory_lookup":
            # Use the memory tool to search the conversation
            memory_result = st.session_state.memory_tool._run(prompt)

            # Generate a response based on memory
            memory_prompt = MEMORY_SEARCH_PROMPT.format(
                memory_result=memory_result,
                prompt=prompt
            )

            result = st.session_state.llm.invoke(memory_prompt).content
        else:  # direct_response
            # Generate a direct response without querying database or memory
            direct_prompt = DIRECT_RESPONSE_PROMPT.format(prompt=prompt)
            result = st.session_state.llm.invoke(direct_prompt).content

        # Update memory with this interaction
        update_conversation_memory(st.session_state.memory, prompt, result)

        # Save to the memory store for the search tool
        save_to_memory_store(st.session_state.memory_store, prompt, result)

        return result

    except Exception as e:
        error_msg = f"Error al procesar la consulta: {str(e)}"
        return error_msg


def render_chat_interface():
    """Render the chat interface including history and input"""
    # Display message history
    render_chat_history()

    # User input
    if prompt := st.chat_input("Ask about your database or the previous conversation..."):
        # Add user message to history
        st.session_state.messages.append({"role": "human", "content": prompt})

        # Display user message
        with st.chat_message("user"):
            st.write(prompt)

        # Check if agent is initialized
        if not st.session_state.initialized:
            with st.chat_message("assistant"):
                st.write("Please configure and connect to the database first.")
            st.session_state.messages.append(
                {"role": "assistant", "content": "Please configure and connect to the database first."})
        else:
            # Process the query with the planning system
            with st.chat_message("assistant"):
                with st.spinner(f"Thinking with {st.session_state.model_name}..."):
                    result = process_query(prompt, st.session_state.show_reasoning)
                    st.write(result)

                    # Add response to history
                    st.session_state.messages.append({"role": "assistant", "content": result})

    # Visualization of memory (optional)
    if st.session_state.initialized and 'memory' in st.session_state:
        with st.expander("View conversation memory", expanded=False):
            if isinstance(st.session_state.memory, ConversationSummaryMemory) and st.session_state.conversation_summary:
                st.subheader("Conversation summary")
                st.write(st.session_state.conversation_summary)

            st.subheader("Message history")
            for i, msg in enumerate(st.session_state.memory_store):
                role = "🧑" if msg["role"] == "human" else "🤖"
                st.text(
                    f"{role} {msg['content'][:100]}..." if len(msg['content']) > 100 else f"{role} {msg['content']}")