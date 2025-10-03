from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.hackernews import HackerNewsTools

agent = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    tools=[HackerNewsTools()],
    markdown=True,
)

agent.print_response("Summarize the top 5 stories on hackernews", stream=True)