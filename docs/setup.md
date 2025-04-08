# Guía de Configuración de ChatAgentDB

Esta guía te ayudará a configurar ChatAgentDB correctamente para interactuar con tu base de datos PostgreSQL.

## Requisitos Previos

Antes de comenzar, asegúrate de tener:

1. **Python 3.8+** instalado en tu sistema
2. **Acceso a una base de datos PostgreSQL** (local o remota)
3. **Clave API de OpenAI** (obtenible en [OpenAI Platform](https://platform.openai.com/account/api-keys))
4. **Permisos de lectura** en las tablas que deseas consultar

## Instalación Paso a Paso

### 1. Preparar el Entorno

```bash
# Clonar el repositorio
git clone https://github.com/yourusername/ChatAgentDB.git
cd ChatAgentDB

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar Variables de Entorno (opcional)

Para mayor seguridad, puedes configurar variables de entorno en lugar de ingresar credenciales directamente en la interfaz:

```bash
# En Windows (PowerShell):
$env:OPENAI_API_KEY="tu-clave-api"
$env:PG_HOST="localhost"
$env:PG_PORT="5432"
$env:PG_USER="postgres"
$env:PG_PASSWORD="tu-contraseña"
$env:PG_DATABASE="nombre-base-datos"

# En macOS/Linux:
export OPENAI_API_KEY="tu-clave-api"
export PG_HOST="localhost"
export PG_PORT="5432"
export PG_USER="postgres"
export PG_PASSWORD="tu-contraseña"
export PG_DATABASE="nombre-base-datos"
```

Alternativamente, puedes crear un archivo `.env` en el directorio raíz:

```
OPENAI_API_KEY=tu-clave-api
PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASSWORD=tu-contraseña
PG_DATABASE=nombre-base-datos
```

### 3. Configuración de PostgreSQL

Asegúrate de que tu base de datos PostgreSQL:

1. Sea accesible desde la máquina donde ejecutas ChatAgentDB
2. Tenga habilitada la autenticación por contraseña
3. El usuario tenga permisos para ejecutar consultas SELECT en las tablas necesarias

Para una configuración local básica de PostgreSQL:

```bash
# Instalar PostgreSQL (ejemplo en Ubuntu)
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Configurar un usuario y base de datos (opcional)
sudo -u postgres psql

CREATE DATABASE mydatabase;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\q
```

### 4. Ejecutar la Aplicación

Una vez configurado todo:

```bash
streamlit run app.py
```

La aplicación se iniciará y estará disponible en tu navegador (generalmente en http://localhost:8501).

### 5. Conectar a la Base de Datos

En la interfaz de ChatAgentDB:

1. Ingresa los detalles de conexión en el panel lateral:
   - Host (por defecto: localhost)
   - Puerto (por defecto: 5432)
   - Nombre de la base de datos
   - Usuario
   - Contraseña
   - Clave API de OpenAI

2. Haz clic en "Conectar"

Si la conexión es exitosa, verás un mensaje de confirmación y un resumen de las tablas disponibles en tu base de datos.

## Solución de Problemas

### Error de Conexión a PostgreSQL

- Verifica que el servidor PostgreSQL esté en ejecución
- Confirma que las credenciales sean correctas
- Asegúrate de que la máquina donde ejecutas la aplicación pueda acceder al servidor PostgreSQL
- Revisa la configuración de firewall o VPN que pueda estar bloqueando la conexión

### Error con la API de OpenAI

- Verifica que tu clave API sea válida y esté activa
- Asegúrate de tener saldo suficiente en tu cuenta de OpenAI
- Revisa la conexión a internet

### Problemas con las Dependencias de Python

Si encuentras errores relacionados con las dependencias:

```bash
# Actualiza pip
pip install --upgrade pip

# Instala dependencias específicas
pip install streamlit langchain langchain-openai langchain-community psycopg2-binary langsmith langraph

# Si usas Windows y tienes problemas con psycopg2:
pip install psycopg2-binary
```

## Configuración Avanzada

### Personalización del Modelo de Lenguaje

Por defecto, ChatAgentDB utiliza el modelo GPT-4 de OpenAI. Si deseas utilizar un modelo diferente, puedes modificar la variable `model` en el código:

```python
# Busca esta línea en app.py
llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")

# Y cámbiala por el modelo que prefieras, por ejemplo:
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
```

### Ajuste de Memoria de Conversación

Para modificar cómo la aplicación maneja el historial de conversación, puedes ajustar la configuración de memoria:

```python
# Para aumentar o disminuir el tamaño del historial
memory = ConversationBufferMemory(return_messages=True, max_token_limit=2000)
```

## Siguientes Pasos

Una vez que hayas configurado ChatAgentDB correctamente, consulta [usage.md](usage.md) para aprender a interactuar efectivamente con tu base de datos usando lenguaje natural.