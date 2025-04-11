from langchain.agents import create_sql_agent
from langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from config.settings import DISPATCH_PROMPT


def create_sql_toolkit(db, llm):
    """Create SQL toolkit for database operations"""
    return SQLDatabaseToolkit(db=db, llm=llm)


def create_dispatcher_chain(planner_llm):
    """Create the dispatcher chain for deciding which action to take"""
    dispatcher_prompt = PromptTemplate(
        template=DISPATCH_PROMPT,
        input_variables=["input"]
    )

    dispatcher_chain = (
            {"input": RunnablePassthrough()}
            | dispatcher_prompt
            | planner_llm
            | StrOutputParser()
    )

    return dispatcher_chain


def initialize_agents(db, llm, planner_llm=None, model_type="ollama"):
    """Initialize all agent components required for the application"""
    if planner_llm is None:
        planner_llm = llm  # Use same LLM if planner not specified

    # Create SQL toolkit
    toolkit = create_sql_toolkit(db, llm)

    # Create SQL agent with proper error handling
    sql_agent = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        agent_type=AgentType.OPENAI_FUNCTIONS if model_type == "openai" else AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True,
    )

    # Create dispatcher
    dispatcher_chain = create_dispatcher_chain(planner_llm)

    return {
        "sql_agent": sql_agent,
        "dispatcher_chain": dispatcher_chain
    }