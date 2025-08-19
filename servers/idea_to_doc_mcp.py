from fastmcp import FastMCP

mcp = FastMCP("IdeaToDoc")

@mcp.tool()
def analyze_idea(idea: str) -> str:
    """Analyze a given idea and generate a high level design document for that idea..
    The document should be in the following format: 
    # Idea
    ## Problem
    ## Solution
    ## Features
    ## Tech Stack
    ## Architecture
    ## Database
    """
    return "Document generated for the idea: " + idea + " and save in markdown file"


if __name__ == "__main__":
    mcp.run()
