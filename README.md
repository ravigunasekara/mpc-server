# mcp-server
This project aims to integrate the MCP server with internal REST applications to test its interaction with an LLM.

## Initialize Python Environment using UV

```bash
uv init mpc-server
cd mpc-server
```

## Add dependencies

```bash
uv add fastmcp
uv add flask
```

## Run APP servers
These mock services are used to demonstrate real-life scenarios.
```bash
uv run src/apps/communication_preference_app.py
uv run src/apps/cafe_app.py
uv run src/apps/hotel_app.py
```

## Run MCP Server

```bash
uv run src/mcp_client.py
```

## Add MCP server to your LLM
### Using OpenAI 
https://platform.openai.com/docs/mcp#connect-in-chatgpt
### Using Copilot via VSCode
https://code.visualstudio.com/docs/copilot/customization/mcp-servers