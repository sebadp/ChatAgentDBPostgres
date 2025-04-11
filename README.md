# ChatAgentDB 🗣️🐘

ChatAgentDB is a conversational agent that allows you to interact with PostgreSQL databases using natural language. This tool transforms questions and requests in human language into precise SQL queries, facilitating data exploration and analysis for users without advanced SQL knowledge.

## 🌟 Features

- Conversational interface to interact with PostgreSQL databases
- Automatic translation of natural language questions to SQL queries
- Visualization of results in a user-friendly format
- Conversation memory to maintain context during the session
- Configuration panel to easily connect to any PostgreSQL database
- Schema exploration to understand the database structure

## 🛠️ Technologies

- Backend: Python, LangChain, LangGraph
- Language model: OpenAI GPT-4
- Database: PostgreSQL
- Frontend: Streamlit
- Integration: psycopg2 for PostgreSQL connections

## 📋 Requirements

- Python 3.8+
- An accessible PostgreSQL database
- OpenAI API key
- Python dependencies listed in requirements.txt

## 🚀 Installation

To install ChatAgentDB, follow these steps:

```
# Clone the repository
git clone https://github.com/yourusername/ChatAgentDB.git
cd ChatAgentDB

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

For detailed configuration, check setup.md.

## 🏃‍♀️ Execution

To start the application:

```
streamlit run app.py
```

Navigate to the provided URL (typically http://localhost:8501).

## 💬 Usage

1. In the sidebar, enter your PostgreSQL database connection details.
2. Click "Connect" to establish the connection.
3. You will see a summary of available tables in your database.
4. Start asking questions in natural language, such as:
   - "Show the last 5 orders"
   - "How many users registered last month?"
   - "Find products with stock less than 10"

For more examples and use cases, see usage.md.

## 🤝 Contributions

Contributions are welcome! If you want to contribute to ChatAgentDB:

1. Fork the repository
2. Create a branch for your feature (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'Add amazing feature')
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- LangChain for their framework for LLM-based applications
- Streamlit for their excellent user interface framework
- The PostgreSQL community for their amazing database