import streamlit as st
from ui.sidebar import render_sidebar
from ui.main_view import render_chat_interface, render_instructions

# Configuración de la página
st.set_page_config(page_title="PostgresWhisperer", page_icon="🤖", layout="wide")
st.title("🤖 PostgresWhisperer: Conversational Agent for PostgreSQL")

# Inicializar estado de la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.initialized = False
    st.session_state.memory_store = []
    st.session_state.conversation_summary = ""

# Renderizar componentes de UI
render_sidebar()


if not st.session_state.messages:
    render_instructions()
    render_chat_interface()
else:
    render_chat_interface()
