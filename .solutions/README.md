# Workshop Solutions & Checkpoints

This folder contains step-by-step checkpoints for the VS Code Agent Lab workshop. Each folder represents a completed stage that you can use to:

- **Skip ahead** if you're short on time
- **Compare your work** against the expected outcome  
- **Recover** if something went wrong
- **Learn** by examining the code changes

## Checkpoints Overview

| Step | Description | Key Changes |
|------|-------------|-------------|
| `step-00-baseline` | Starting point | Clean Python app with basic bingo game |
| `step-01-instructions` | Workspace instructions | Added `.github/copilot-instructions.md` |
| `step-02-linting` | Linting rules | Ruff linting configured in `pyproject.toml` |
| `step-03-readme-update` | Enhanced README | Made README more engaging as landing page |
| `step-04-redesign-cyberpunk` | UI Redesign | Cyberpunk Neon theme applied |
| `step-05-quiz-techlife` | Quiz Master | Tech Life Bingo questions |
| `step-06-scavenger-hunt` | Scavenger Hunt mode | New game mode with progress tracking |
| `step-07-card-deck` | Card Deck Shuffle | Random card draw mode |
| `finished` | Complete workshop | All features combined |

## How to Use a Checkpoint

### Option 1: Copy files to your project
```bash
# From repo root, copy a checkpoint's app folder
cp -r .solutions/step-04-redesign-cyberpunk/app ./app
```

### Option 2: Run a checkpoint directly
```bash
cd .solutions/step-04-redesign-cyberpunk
uv sync
uv run uvicorn app.main:app --reload --port 8000
```

### Option 3: Compare your changes
```bash
# See what changed in a step
diff -r app .solutions/step-04-redesign-cyberpunk/app
```

## Workshop Guide Reference

See [`.lab/GUIDE.md`](../.lab/GUIDE.md) for the full workshop instructions.

## Checkpoint Details

### Step 0: Baseline
The starting point — a working Python (FastAPI + Jinja2 + HTMX) bingo game with:
- Start screen with "Start Game" button
- 5x5 bingo board with random questions
- Click to mark squares
- Bingo detection (rows, columns, diagonals)
- Win modal celebration

### Step 1: Workspace Instructions
After running "Generate Workspace Instructions":
- `.github/copilot-instructions.md` — Development checklist and project overview

### Step 2: Linting Rules  
After adding linting for code quality:
- Ruff rules configured in `pyproject.toml` for unused variables, type hints

### Step 3: README Update
After making the README engaging:
- `README.md` — Project landing page with features, screenshots, quick start

### Step 4: Cyberpunk Neon Redesign
Full UI overhaul with Cyberpunk Neon theme:
- Neon color palette (cyan, magenta, purple)
- Glowing effects and animations
- Dark background with grid patterns
- Futuristic typography

### Step 5: Tech Life Bingo
Quiz Master generated questions:
- Developer-focused icebreaker questions
- Coding languages, tools, dev culture themes

### Step 6: Scavenger Hunt Mode
New game mode (TDD-driven):
- List view with checkboxes
- Progress meter
- Mode selection on start screen
- Unit tests for game logic

### Step 7: Card Deck Shuffle
Design-driven card mode:
- Random card draw interface
- Swipe left/right for fail/success
- Card flip animations

### Finished
All features combined and polished:
- Multiple game modes (Bingo, Scavenger Hunt, Card Deck)
- Cyberpunk Neon theme
- Tech Life questions
- Full test coverage
