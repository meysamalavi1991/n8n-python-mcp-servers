from typing import Annotated
from pydantic import Field
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings


security = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=[
        "127.0.0.1:8000",
        "localhost:8000",
        "mcp-server-python-calculator:8000",
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


@mcp.tool()
def multiply_numbers(
    a: Annotated[float, Field(ge=-1000, le=1000)],
    b: Annotated[float, Field(ge=-1000, le=1000)]
) -> float:
   """
   Multiply two numbers and return their product.
   Both numbers must be between -1000 and 1000.
   """

   return a * b


@mcp.tool()
def divide_numbers(a: float, b: float) -> float:
    """
    Divide the first number by the second number.

    Raises:
       ValueError: If the divisor is zero.
    """

    if b == 0:
        raise ValueError("Division by zero is not allowed.")

    return a / b
   

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
