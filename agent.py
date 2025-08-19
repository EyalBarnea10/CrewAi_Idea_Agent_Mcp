import os
from crewai import Agent, Task, Crew,Process
from crewai_tools import MCPServerAdapter
from mcp import StdioServerParameters
 
# Add your OpenAI API key and model name in environment variables
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
os.environ["OPENAI_MODEL_NAME"] ="gpt-3.5-turbo"

server_params = StdioServerParameters(
    command="python",
    args=["./servers/idea_to_doc_mcp.py"],
)

with MCPServerAdapter(server_params) as tools:
    agent = Agent(
        role="idea_to_high_level_design_agent",
        goal="Generate a high level design document for a given idea.",
        backstory="""you are experiance software developer you handle all kind of idea and generate a high level design document for that idea.""",
        verbose=True,
        tools=tools,
        model=os.environ["OPENAI_MODEL_NAME"],
    )

    crew = Crew(
        agents=[agent],
        tasks=[
            Task(
                name="generate_high_level_design_document",
                description="Generate a high level design document for a given idea.",
                input_schema={"idea": "string"},
            )
        ],
    )

    result = crew.kickoff(inputs={"idea": "I want to create a web application that allows users to manage their tasks."})
    print(result)
