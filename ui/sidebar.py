import os
import streamlit as st
from core.agent_factory import initialize_agents
from core.database import connect_to_database, inject_db_schema_to_memory, get_table_preview
from core.memory import create_memory
from tools.memory_tool import MemorySearchTool
from config.settings import (
    DEFAULT_TEMPERATURE, DEFAULT_MODEL_TYPE, DEFAULT_OLLAMA_HOST,
    DEFAULT_OLLAMA_MODEL, DEFAULT_OPENAI_MODEL, DEFAULT_DB_HOST,
    DEFAULT_DB_PORT, DEFAULT_DB_NAME, DEFAULT_DB_USER
)


def render_sidebar():
    """Render the sidebar configuration UI"""
    with st.sidebar:
        st.header("Configuration")

        # Model selection
        st.subheader("AI Model")
        model_option = st.radio(
            "Select model type:",
            ("Local (Ollama)", "API (OpenAI)"),
            index=0 if DEFAULT_MODEL_TYPE == "Local (Ollama)" else 1
        )

        if model_option == "Local (Ollama)":
            st.info("Using local model with Ollama - No API key required")
            ollama_host = st.text_input("Ollama Host", DEFAULT_OLLAMA_HOST)
            ollama_model = st.selectbox(
                "Ollama Model",
                ["llama3", "llama3:8b", "llama3:70b", "mistral", "mixtral", "codellama", "phi3", "gemma3"]
            )
            api_key = None
        else:
            st.info("Using OpenAI - API key required")
            api_key = st.text_input("OpenAI API Key", "", type="password")
            openai_model = st.selectbox(
                "OpenAI Model",
                ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"]
            )

        # Advanced options
        with st.expander("Advanced options"):
            use_summary_memory = st.checkbox("Use summary memory", value=True,
                                             help="Generates a conversation summary to handle long histories")
            temperature = st.slider("Temperature", min_value=0.0, max_value=1.0, value=DEFAULT_TEMPERATURE, step=0.1,
                                    help="Higher values generate more creative but less accurate responses")
            show_reasoning = st.checkbox("Show reasoning", value=False,
                                         help="Shows the agent's decision process")

        # Database configuration
        st.subheader("PostgreSQL Database")
        db_host = st.text_input("DB Host", DEFAULT_DB_HOST)
        db_port = st.text_input("Port", DEFAULT_DB_PORT)
        db_name = st.text_input("DB Name", DEFAULT_DB_NAME)
        db_user = st.text_input("User", DEFAULT_DB_USER)
        db_password = st.text_input("Password", "", type="password")

        if st.button("Connect"):
            setup_connection(
                model_option,
                db_host, db_port, db_name, db_user, db_password,
                temperature, use_summary_memory, show_reasoning,
                ollama_host=ollama_host if model_option == "Local (Ollama)" else None,
                ollama_model=ollama_model if model_option == "Local (Ollama)" else None,
                openai_api_key=api_key if model_option == "API (OpenAI)" else None,
                openai_model=openai_model if model_option == "API (OpenAI)" else None
            )

        # Display Ollama instructions
        if 'model_type' in st.session_state and st.session_state.model_type == "ollama":
            st.markdown("---")
            st.subheader("Instructions for Ollama")
            st.markdown("""
            To use Ollama, make sure to:

            1. Have Ollama installed: [ollama.ai](https://ollama.ai)
            2. Run `ollama serve` in your terminal
            3. Install the desired model with:
              ```
              ollama pull llama3
              ```
            """)


def setup_connection(
        model_option, db_host, db_port, db_name, db_user, db_password,
        temperature, use_summary_memory, show_reasoning,
        ollama_host=None, ollama_model=None,
        openai_api_key=None, openai_model=None
):
    """Set up the connection to the database and initialize the agents"""
    try:
        # Connect to the database
        db = connect_to_database(db_user, db_password, db_host, db_port, db_name)

        # Configure LLM based on selected option
        if model_option == "Local (Ollama)":
            # Configure local Ollama model
            from langchain_community.chat_models import ChatOllama

            llm = ChatOllama(
                model=ollama_model,
                base_url=ollama_host,
                temperature=temperature
            )
            # Configure a simpler model for the planner (for better performance)
            planner_llm = ChatOllama(
                model=ollama_model,
                base_url=ollama_host,
                temperature=0.1
            )
            st.session_state.model_type = "ollama"
            st.session_state.model_name = ollama_model
        else:
            # Configure OpenAI model
            if not openai_api_key:
                st.error("Please enter an OpenAI API key")
                return

            os.environ["OPENAI_API_KEY"] = openai_api_key
            from langchain_openai import ChatOpenAI

            llm = ChatOpenAI(temperature=temperature, model=openai_model)
            planner_llm = ChatOpenAI(temperature=0.1, model=openai_model)
            st.session_state.model_type = "openai"
            st.session_state.model_name = openai_model

        # Create memory
        memory = create_memory(llm, use_summary_memory)

        # Create memory tool
        memory_tool = MemorySearchTool()

        # Initialize agents
        agents = initialize_agents(db, llm, planner_llm, st.session_state.model_type)

        # Save to session state
        st.session_state.llm = llm
        st.session_state.sql_agent = agents["sql_agent"]
        st.session_state.dispatcher_chain = agents["dispatcher_chain"]
        st.session_state.memory = memory
        st.session_state.memory_tool = memory_tool
        st.session_state.db = db
        st.session_state.initialized = True
        st.session_state.show_reasoning = show_reasoning

        # Inject schema to memory
        inject_db_schema_to_memory(st.session_state.db, st.session_state.memory, debug=True)

        # Success message and database summary
        st.success(f"Connection successful using {st.session_state.model_name}!")

        # Show available tables
        tables_info = db.get_usable_table_names()
        st.subheader("Available tables:")
        for table in tables_info:
            st.write(f"- {table}")

        # Show a preview of the tables
        st.subheader("Table preview:")
        for table in tables_info[:3]:  # Limit to 3 tables to avoid overloading
            st.write(f"**Table: {table}**")
            preview = get_table_preview(db, table)
            st.code(preview)

    except Exception as e:
        st.error(f"Connection error: {str(e)}")
        st.error("If you're using a local Ollama model, make sure it's running")
        st.info("Run Ollama with: `ollama serve` and make sure you've downloaded the model")