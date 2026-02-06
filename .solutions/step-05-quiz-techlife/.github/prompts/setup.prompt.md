---
agent: agent
description: Get my development workspace ready
tools: ['execute/runTask', 'execute/runInTerminal', 'read', 'search', 'todo']
---

Your goal is to successfully build and run the workspace as local development environment.

## Checklist
- [ ] Required dependencies (Python 3.13+, uv) installed and verified
- [ ] Dependencies synced (`uv sync`)
- [ ] Tests passing (`uv run pytest`)
- [ ] Dev server running (`uv run uvicorn app.main:app --reload --port 8000`)
- [ ] Site opened in external browser (use `$BROWSER` or instruct the user to open http://localhost:8000)
- [ ] Short engaging welcome tour for the workspace

## Important
- Do NOT use VS Code Simple Browser to preview the site. HTMX requires a full browser to function correctly.
- Use `"$BROWSER" http://localhost:8000` in the terminal to open the site in the user's default browser.