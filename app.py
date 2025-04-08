import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_community.utilities import SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain.chains.conversation.memory import ConversationBufferMemory
from langchain_community.agent_toolkits import SQLDatabaseToolkit


# Configuración de la aplicación
st.set_page_config(page_title="DB Agent", page_icon="🤖", layout="wide")
st.title("🤖 Agente Conversacional para PostgreSQL")

# Inicializar la sesión de Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.initialized = False

# Configuración de la conexión a la base de datos PostgreSQL
with st.sidebar:
    st.header("Configuración de la Base de Datos")
    db_host = st.text_input("Host de la DB", "localhost")
    db_port = st.text_input("Puerto", "5432")
    db_name = st.text_input("Nombre de la DB", "postgres")
    db_user = st.text_input("Usuario", "postgres")
    db_password = st.text_input("Contraseña", "", type="password")
    openai_api_key = st.text_input("OpenAI API Key", "", type="password")

    if st.button("Conectar"):
        try:
            # Conexión a la base de datos
            connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
            db = SQLDatabase.from_uri(connection_string)

            # Establecer la clave API de OpenAI
            os.environ["OPENAI_API_KEY"] = openai_api_key

            # Configuración del LLM
            llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")

            # Crear el toolkit de SQL
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)

            # Crear el agente
            agent = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                agent_type=AgentType.OPENAI_FUNCTIONS,
                verbose=True,
                handle_parsing_errors=True,
            )

            # Memoria de conversación
            memory = ConversationBufferMemory(return_messages=True)

            # Configuración del grafo de langchain
            from langchain.agents import AgentExecutor

            agent_executor = AgentExecutor.from_agent_and_tools(
                agent=agent.agent,
                tools=agent.tools,
                memory=memory,
                verbose=True
            )

            # Guardar en sesión
            st.session_state.agent_executor = agent_executor
            st.session_state.db = db
            st.session_state.initialized = True

            # Mostrar mensaje de éxito y detalles de la base de datos
            st.success("Conexión exitosa a la base de datos!")

            # Mostrar las tablas disponibles
            tables_info = db.get_usable_table_names()
            st.subheader("Tablas disponibles:")
            for table in tables_info:
                st.write(f"- {table}")

            # Mostrar una vista previa de las tablas
            st.subheader("Vista previa de las tablas:")
            for table in tables_info[:3]:  # Limitar a 3 tablas para no sobrecargar
                query = f"SELECT * FROM {table} LIMIT 5;"
                try:
                    result = db.run(query)
                    st.write(f"**Tabla: {table}**")
                    st.code(result)
                except Exception as e:
                    st.write(f"Error al consultar {table}: {str(e)}")

        except Exception as e:
            st.error(f"Error de conexión: {str(e)}")

# Mostrar historial de mensajes
for message in st.session_state.messages:
    if message["role"] == "human":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

# Entrada del usuario
if prompt := st.chat_input("Pregunta sobre tu base de datos..."):
    # Agregar mensaje del usuario al historial
    st.session_state.messages.append({"role": "human", "content": prompt})

    # Mostrar el mensaje del usuario
    with st.chat_message("user"):
        st.write(prompt)

    # Comprobar si el agente está inicializado
    if not st.session_state.initialized:
        with st.chat_message("assistant"):
            st.write("Por favor, configura y conecta la base de datos primero.")
        st.session_state.messages.append(
            {"role": "assistant", "content": "Por favor, configura y conecta la base de datos primero."})
    else:
        # Procesar la consulta con el agente
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    # Ejecutar la consulta a través del agente
                    response = st.session_state.agent_executor.invoke({"input": prompt})
                    result = response["output"]
                    st.write(result)

                    # Agregar respuesta al historial
                    st.session_state.messages.append({"role": "assistant", "content": result})
                except Exception as e:
                    error_msg = f"Error al procesar la consulta: {str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

# Información adicional en el pie de página
st.markdown("---")
st.markdown("""
**Instrucciones:**
1. Configura la conexión a tu base de datos PostgreSQL en el panel lateral
2. Conecta a la base de datos usando el botón "Conectar"
3. Realiza preguntas en lenguaje natural sobre tus datos

El agente traducirá tus preguntas a consultas SQL y te mostrará los resultados.
""")