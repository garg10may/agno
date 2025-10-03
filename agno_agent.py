from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.mcp import MCPTools

# Create the Agent
agno_agent = Agent(
    name="Agno Agent",
    model=OpenAIChat(id="gpt-4o-mini"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno.db"),
    # Add the Agno MCP server to the Agent
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True,
)


# Create the AgentOS
agent_os = AgentOS(agents=[agno_agent])
# Get the FastAPI app for the AgentOS
app = agent_os.get_app()