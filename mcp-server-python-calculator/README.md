# n8n-python-mcp-servers
# Python Calculator MCP Server

A lightweight MCP (Model Context Protocol) server built with Python and FastMCP. It exposes calculator operations as MCP tools and communicates over Streamable HTTP.

This project is part of my hands-on journey into learning and building MCP servers with Python.

## Features

Currently available tools:

| Tool | Description |
|---|---|
| `add_numbers` | Adds two numbers and returns their sum. |
| `multiply_numbers` | Multiplies two numbers and returns their product. |

## Tech Stack

- Python 3.13
- MCP Python SDK
- FastMCP
- Pydantic
- Docker
- Streamable HTTP

## Project Structure

```text
mcp-server-python-calculator/
+-- src/
¦   +-- server.py
+-- Dockerfile
+-- requirements.txt
+-- README.md
```

The project also uses a local `pydantic-core` wheel file during Docker builds.

## Getting Started

### Prerequisites

- Docker
- Docker Compose is not required.
- Python 3.13 (for running outside Docker)

### Build Docker Image

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/mcp-server-python-calculator.git

cd mcp-server-python-calculator
```

Build the Docker image:

```bash
docker build \
  --build-arg PIP_DEFAULT_TIMEOUT=120 \
  --build-arg PIP_RETRIES=10 \
  -t mcp-server-python-calculator:dev .
```

### Run the MCP Server

```bash
docker run -d \
  --name mcp-server-python-calculator \
  -p 127.0.0.1:8000:8000 \
  mcp-server-python-calculator:dev
```

The MCP server will be available at:

```text
http://127.0.0.1:8000/mcp
```

### View Logs

```bash
docker logs -f mcp-server-python-calculator
```

### Stop and Remove Container

```bash
docker stop mcp-server-python-calculator
docker rm mcp-server-python-calculator
```

## Testing with MCP Inspector

You can use [MCP Inspector](https://github.com/modelcontextprotocol/inspector) to connect to and test the server.

Start the Inspector:

```bash
HOST=192.168.1.15 \
ALLOWED_ORIGINS=http://localhost:6274,http://127.0.0.1:6274,http://192.168.1.15:6274 \
MCP_INSPECTOR_SECRET_STORE=file \
npx @modelcontextprotocol/inspector
```

Open the Inspector web interface:

```text
http://localhost:6274
```

Configure the connection:

| Setting | Value |
|---|---|
| Transport Type | Streamable HTTP |
| URL | `http://127.0.0.1:8000/mcp` |

After connecting, navigate to the **Tools** section to discover and execute the available calculator tools.

> Note: The `HOST` and `ALLOWED_ORIGINS` values above are examples for a local development environment. Adjust them to match your Inspector setup.

## Example

Call `add_numbers`:

```json
{
  "a": 10,
  "b": 25
}
```

Expected result:

```json
35
```

Call `multiply_numbers`:

```json
{
  "a": 10,
  "b": 5
}
```

Expected result:

```json
50
```

## Learning Goals

This project is intended to explore:

- Building MCP servers with Python.
- Exposing Python functions as MCP tools.
- Understanding Streamable HTTP transport.
- Testing MCP servers using MCP Inspector.
- Containerizing MCP servers with Docker.
- Integrating MCP servers with AI applications and automation platforms.

## Roadmap

- [x] Set up a Python MCP server.
- [x] Configure Streamable HTTP transport.
- [x] Implement `add_numbers`.
- [x] Implement `multiply_numbers`.
- [ ] Improve input validation and error handling.
- [ ] Add MCP Resources.
- [ ] Add MCP Prompts.
- [ ] Integrate with n8n.

## License

This project is open source and available under the MIT License.
