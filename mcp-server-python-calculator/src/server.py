from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

security = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=[
        "127.0.0.1:8000",
        "localhost:8000",
    ],
    allowed_origins=[
        "http://localhost:6274",
        "http://127.0.0.1:6274",
        "http://192.168.1.15:6274",
    ],
)

mcp = FastMCP(
    "n8n-mcp-python-demo",
    host="0.0.0.0",
    port=8000,
    transport_security=security,
)


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Add two numbers and return their sum."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="streamable-http")