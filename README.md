# Hyperskill MCP Server

MCP Server to search and access Hyperskill educational content

Hacked on Sunday, Apr 6th, 2025 at the [MIT-MCP hackathon](https://lu.ma/jl8fttnt?tk=w1kdke) by [MIT Decentralized AI](https://www.media.mit.edu/projects/decentralized-ai/overview/).

## About Hyperskill

[Hyperskill](https://hyperskill.org) is an online educational platform that offers project-based learning for programming and computer science. It provides interactive, hands-on learning experiences through step-by-step projects, theoretical materials, and practical exercises. The platform supports multiple programming languages and technologies, helping students build real-world applications while mastering coding concepts.

## Installation for Claude app:

1. Clone this repo: `git clone https://github.com/vyahhi/hyperskill-mcp-server.git`
2. Install [Claude desktop app](https://claude.ai/desktop), start it.
3. Add the following servers to `claude_desktop_config.json` (Claude > Settings > Developer, then restart Claude app):

```json
{
  "mcpServers": {
    "hyperskill": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/vyahhi/projects/hyperskill-mcp-server", // <-- IMPORTANT: UPDATE THIS ABSOLUTE PATH TO YOUR CLONED REPO PATH
        "run",
        "hyperskill.py"
      ]
    }
  }
}
```

4. Restart Claude, ask Claude chat `What is Hyperskill topic # 4606 about?`

## Development

```bash
uv venv
source .venv/bin/activate
uv add "mcp[cli]" httpx
```

```bash
mcp run hyperskill.py
```

```bash
mcp dev hyperskill.py
```