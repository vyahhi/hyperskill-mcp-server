# Hyperskill MCP Server

MCP Server to search and access Hyperskill educational content

## About Hyperskill

[Hyperskill](https://hyperskill.org) is an online educational platform that offers project-based learning for programming and computer science. It provides interactive, hands-on learning experiences through step-by-step projects, theoretical materials, and practical exercises. The platform supports multiple programming languages and technologies, helping students build real-world applications while mastering coding concepts.

## Installation

1. `git clone https://github.com/vyahhi/hyperskill-mcp-server.git`
2. Install [Claude desktop app](https://claude.ai/desktop), start it.
3. Add the following servers to `claude_desktop_config.json` (Claude > Settings > Developer, then restart Claude app):

```json
{
  "mcpServers": {
    "hyperskill": {
      "command": "uv",
      "args": [
        "--directory",
        "/Users/vyahhi/projects/hyperskill-mcp-server",
        "run",
        "hyperskill.py"
      ]
    }
  }
}
```

**DO NOT FORGET TO UPDATE THE ABSOLUTE PATH ABOVE TO YOUR CLONED REPO**

4. Restart Claude, ask Claude chat `What is Hyperskill topic # 4606 about?`.

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