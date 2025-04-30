from mcp.server.fastmcp import FastMCP
from Tools.Create_file import create_file

mcp=FastMCP("FileFlow")

@mcp.tool()
def create_file(path: str, filename: str) -> str:
    """Wrapper around the imported create_file function."""
    return create_file(path, filename)