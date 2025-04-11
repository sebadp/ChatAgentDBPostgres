from langchain_community.utilities.sql_database import SQLDatabase
from sqlalchemy import inspect
from langchain_core.messages import SystemMessage


def connect_to_database(db_user, db_password, db_host, db_port, db_name):
    """Connect to PostgreSQL database and return SQLDatabase object"""
    connection_string = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    try:
        db = SQLDatabase.from_uri(connection_string)
        return db
    except Exception as e:
        raise ConnectionError(f"Failed to connect to database: {str(e)}")


def build_schema_prompt(db):
    """Extract real tables and columns from PostgreSQL and build schema instruction block."""
    inspector = inspect(db._engine)
    schema_lines = ["The database has the following tables and columns:\n"]

    for table_name in inspector.get_table_names():
        columns = inspector.get_columns(table_name)
        column_list = [f"- {col['name']} ({col['type']})" for col in columns]
        schema_lines.append(f"Table: {table_name}")
        schema_lines.extend(column_list)
        schema_lines.append("")  # Blank line between tables

    return "\n".join(schema_lines)


def inject_db_schema_to_memory(db, memory, debug=False):
    """
    Injects the real database schema as a SystemMessage into the memory context.
    Ensures that the LLM (e.g., Ollama) only uses real tables/columns.
    """
    schema_text = build_schema_prompt(db)

    from config.settings import DB_SCHEMA_PROMPT
    system_msg = SystemMessage(content=DB_SCHEMA_PROMPT.format(schema_text=schema_text))

    # Insert at the beginning of the memory context
    memory.chat_memory.messages.insert(0, system_msg)

    if debug:
        print("--- Injected DB Schema into SystemMessage ---")
        print(system_msg.content)

    return schema_text


def get_table_preview(db, table_name, limit=5):
    """Get a preview of a database table"""
    query = f"SELECT * FROM {table_name} LIMIT {limit};"
    try:
        result = db.run(query)
        return result
    except Exception as e:
        return f"Error querying {table_name}: {str(e)}"