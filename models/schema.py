from pydantic import BaseModel, Field


class MemorySearchInput(BaseModel):
    query: str = Field(description="The query to search in the conversation memory")


class AgentResponse(BaseModel):
    reasoning: str = Field(default="", description="Agent's reasoning process")
    action: str = Field(description="Action to take: database_query, memory_lookup, or direct_response")
    explanation: str = Field(default="", description="Explanation for the chosen action")


class DatabaseConfig(BaseModel):
    host: str
    port: str
    name: str
    user: str
    password: str


class ModelConfig(BaseModel):
    model_type: str  # "openai" or "ollama"
    model_name: str
    temperature: float
    host: str = ""  # Only for Ollama
    api_key: str = ""  # Only for OpenAI