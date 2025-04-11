# ChatAgentDB Setup Guide

This guide will help you correctly configure ChatAgentDB to interact with your PostgreSQL database.

## Prerequisites

Before starting, make sure you have:

1. **Python 3.8+** installed on your system
2. **Access to a PostgreSQL database** (local or remote)
3. **OpenAI API key** (obtainable from [OpenAI Platform](https://platform.openai.com/account/api-keys))
4. **Read permissions** on the tables you want to query

## Step-by-Step Installation

### 1. Prepare the Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/ChatAgentDB.git
cd ChatAgentDB

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables (optional)

For better security, you can configure environment variables instead of entering credentials directly in the interface:

```bash
# On Windows (PowerShell):
$env:OPENAI_API_KEY="your-api-key"
$env:PG_HOST="localhost"
$env:PG_PORT="5432"
$env:PG_USER="postgres"
$env:PG_PASSWORD="your-password"
$env:PG_DATABASE="database-name"

# On macOS/Linux:
export OPENAI_API_KEY="your-api-key"
export PG_HOST="localhost"
export PG_PORT="5432"
export PG_USER="postgres"
export PG_PASSWORD="your-password"
export PG_DATABASE="database-name"
```

Alternatively, you can create a `.env` file in the root directory:

```
OPENAI_API_KEY=your-api-key
PG_HOST=localhost
PG_PORT=5432
PG_USER=postgres
PG_PASSWORD=your-password
PG_DATABASE=database-name
```

### 3. PostgreSQL Configuration

Make sure your PostgreSQL database:

1. Is accessible from the machine where you're running ChatAgentDB
2. Has password authentication enabled
3. The user has permissions to execute SELECT queries on the necessary tables

For a basic local PostgreSQL configuration:

```bash
# Install PostgreSQL (example on Ubuntu)
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Configure a user and database (optional)
sudo -u postgres psql

CREATE DATABASE mydatabase;
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\q
```

### 4. Run the Application

Once everything is configured:

```bash
streamlit run app.py
```

The application will start and be available in your browser (usually at http://localhost:8501).

### 5. Connect to the Database

In the ChatAgentDB interface:

1. Enter the connection details in the sidebar:
   - Host (default: localhost)
   - Port (default: 5432)
   - Database name
   - Username
   - Password
   - OpenAI API key

2. Click "Connect"

If the connection is successful, you'll see a confirmation message and a summary of the available tables in your database.

## Troubleshooting

### PostgreSQL Connection Error

- Verify that the PostgreSQL server is running
- Confirm that the credentials are correct
- Make sure the machine where you're running the application can access the PostgreSQL server
- Check firewall or VPN configuration that might be blocking the connection

### OpenAI API Error

- Verify that your API key is valid and active
- Make sure you have sufficient balance in your OpenAI account
- Check your internet connection

### Python Dependency Issues

If you encounter errors related to dependencies:

```bash
# Update pip
pip install --upgrade pip

# Install specific dependencies
pip install streamlit langchain langchain-openai langchain-community psycopg2-binary langsmith langraph

# If you're using Windows and having issues with psycopg2:
pip install psycopg2-binary
```

## Advanced Configuration

### Language Model Customization

By default, ChatAgentDB uses OpenAI's GPT-4 model. If you want to use a different model, you can modify the `model` variable in the code:

```python
# Look for this line in app.py
llm = ChatOpenAI(temperature=0, model="gpt-4-turbo")

# And change it to the model you prefer, for example:
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
```

### Conversation Memory Adjustment

To modify how the application handles conversation history, you can adjust the memory configuration:

```python
# To increase or decrease the history size
memory = ConversationBufferMemory(return_messages=True, max_token_limit=2000)
```

## Next Steps

Once you have correctly configured ChatAgentDB, consult [usage.md](usage.md) to learn how to effectively interact with your database using natural language.