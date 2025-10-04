from agno.agent import Agent
from agno.db.sqlite import SqliteDb
from agno.models.anthropic import Claude
from agno.models.openai import OpenAIChat
from agno.os import AgentOS
from agno.tools.mcp import MCPTools
from agno.agent import RunOutput
from agno.utils.pprint import pprint_run_response


# Create the Agent
agno_agent = Agent(
    name="Agno Agent",
    model=OpenAIChat(id="gpt-4o"),
    # Add a database to the Agent
    db=SqliteDb(db_file="agno1.db"),
    # Add the Agno MCP server to the Agent
    tools=[MCPTools(transport="streamable-http", url="https://docs.agno.com/mcp")],
    # Add the previous session history to the context
    add_history_to_context=True,
    markdown=True,
    debug_mode=True
)


# agent_os = AgentOS(agents=[agno_agent])
# app = agent_os.get_app()

# response: RunOutput =agno_agent.run("what tools do you have access to?")
# pprint_run_response(response, markdown=True)

agno_agent.print_response("What is Agno?")
agno_agent.print_response("What is Agno?", stream=True)
agno_agent.aprint_response("What is Agno?")
agno_agent.aprint_response("What is Agno?", stream=True)




