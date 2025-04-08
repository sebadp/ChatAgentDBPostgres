# ChatAgentDB 🗣️🐘

ChatAgentDB es un agente conversacional que permite interactuar con bases de datos PostgreSQL utilizando lenguaje natural. Esta herramienta transforma preguntas y solicitudes en lenguaje humano en consultas SQL precisas, facilitando la exploración y análisis de datos para usuarios sin conocimientos avanzados de SQL.

## 🌟 Características

- **Interfaz conversacional** para interactuar con bases de datos PostgreSQL
- **Traducción automática** de preguntas en lenguaje natural a consultas SQL
- **Visualización de resultados** en un formato amigable
- **Memoria de conversación** para mantener el contexto durante la sesión
- **Panel de configuración** para conectarse fácilmente a cualquier base de datos PostgreSQL
- **Exploración de esquemas** para entender la estructura de la base de datos

## 🛠️ Tecnologías

- **Backend**: Python, LangChain, LangGraph
- **Modelo de lenguaje**: OpenAI GPT-4
- **Base de datos**: PostgreSQL
- **Frontend**: Streamlit
- **Integración**: psycopg2 para conexiones a PostgreSQL

## 📋 Requisitos

- Python 3.8+
- Una base de datos PostgreSQL accesible
- Clave API de OpenAI
- Dependencias de Python listadas en `requirements.txt`

## 🚀 Instalación

Para instalar ChatAgentDB, sigue estos pasos:

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/ChatAgentDB.git
cd ChatAgentDB

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

Para configuración detallada, consulta [setup.md](docs/setup.md).

## 🏃‍♀️ Ejecución

Para iniciar la aplicación:

```bash
streamlit run app.py
```

Navega a la URL proporcionada (generalmente http://localhost:8501).

## 💬 Uso

1. En la barra lateral, introduce los detalles de conexión a tu base de datos PostgreSQL.
2. Haz clic en "Conectar" para establecer la conexión.
3. Verás un resumen de las tablas disponibles en tu base de datos.
4. Empieza a hacer preguntas en lenguaje natural, como:
   - "Muestra los últimos 5 pedidos"
   - "¿Cuántos usuarios se registraron el mes pasado?"
   - "Encuentra los productos con stock menor a 10"

Para más ejemplos y casos de uso, consulta [usage.md](docs/usage.md).

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Si deseas contribuir a ChatAgentDB:

1. Haz un fork del repositorio
2. Crea una rama para tu característica (`git checkout -b feature/amazing-feature`)
3. Haz commit de tus cambios (`git commit -m 'Add amazing feature'`)
4. Haz push a la rama (`git push origin feature/amazing-feature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- [LangChain](https://github.com/langchain-ai/langchain) por su framework para aplicaciones basadas en LLM
- [Streamlit](https://streamlit.io/) por su excelente framework para interfaces de usuario
- La comunidad PostgreSQL por su increíble base de datos