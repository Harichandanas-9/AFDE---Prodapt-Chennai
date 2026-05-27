from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Simple MCP Server")


@mcp.tool()
def hello(name: str) -> str:
    """
    Say hello to someone
    """
    return f"Hello {name} from FastAPI MCP Server!"


if __name__ == "__main__":
    mcp.run()