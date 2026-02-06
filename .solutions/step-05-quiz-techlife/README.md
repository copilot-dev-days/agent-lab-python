# Soc Ops

Social Bingo game for in-person mixers. Find people who match the questions and get 5 in a row!

🎮 **[Play the Game](https://madebygps.github.io/vscode-github-copilot-agent-lab/)** • 📚 **[View Lab Guide](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/)**

---

## 📚 Lab Guide

| Part | Title |
|------|-------|
| [**00**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=00-overview) | Overview & Checklist |
| [**01**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=01-setup) | Setup & Context Engineering |
| [**02**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=02-design) | Design-First Frontend |
| [**03**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=03-quiz-master) | Custom Quiz Master |
| [**04**](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/step.html?step=04-multi-agent) | Multi-Agent Development |

> 📝 Lab guides are also available in the [`.lab/`](.lab/) folder for offline reading.

---

## Prerequisites

- [Python 3.13](https://www.python.org/downloads/) or higher
- [uv](https://docs.astral.sh/uv/) package manager

## Setup

```bash
uv sync
```

## Run

```bash
uv run uvicorn app.main:app --reload
```

Then open http://localhost:8000 in your browser.

## Test

```bash
uv run pytest
```

## Lint

```bash
uv run ruff check .
uv run ruff format .
```

Deploys automatically to GitHub Pages on push to `main`.
