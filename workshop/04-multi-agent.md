# Part 4: Multi-Agent Development

[📚 Lab Guide](GUIDE.md) • [← Part 3](03-quiz-master.md)

---

> ⏱️ **Time:** ~20 minutes

Build new features using specialized agents: TDD agents for reliable code, and design agents for beautiful UI.

---

## 🧪 Task 1: Scavenger Hunt Mode (TDD-Driven)

Custom agents with handoffs break complex workflows into smaller steps, keeping you in control for critical decisions.

### How TDD Red → Green → Refactor Works

Test-Driven Development means writing tests **before** writing code. You describe what the code *should* do, watch the tests fail (because the code doesn't exist yet), then write just enough code to make them pass. This gives you confidence that every line of code exists for a reason.

Each phase has its own agent:

| Phase | Agent | What it does |
|-------|-------|------|
| **Red** | TDD Red | Writes tests for the planned feature — they **fail** because nothing is implemented yet |
| **Green** | TDD Green | Writes the **minimum code** to make those failing tests pass — no extras |
| **Refactor** | TDD Refactor | Cleans up the code (readability, structure) while keeping all tests **passing** |

> **Important for this workshop:** In Phase 1 below, you'll plan the feature but **not implement it**. This way, when TDD Red writes tests, they'll genuinely fail — which is the whole point.

### What We're Building

A new **Scavenger Hunt** mode:
- Same questions as bingo
- Displayed as a simple checklist
- Progress meter at the top
- Click to mark items complete

### Steps

#### Phase 1: Plan

1. In the **chat mode dropdown** (bottom-left of the chat input), select **Plan**
2. Enter:
   ```
   Add a new Scavenger Hunt mode: same questions, but shown as a 
   simple list with checkboxes and a progress meter
   ```
3. **Iterate on the plan** — check that it:
   - ✅ Adds the mode to the start screen
   - ✅ Creates a new component for the list view
   - ✅ Includes a progress indicator
   - ❌ Doesn't go overboard with features
4. Once you're satisfied with the plan, **do NOT click Start Implementation** — we want the TDD agents to drive the implementation instead

#### Phase 2: TDD Red (Write Failing Tests)

1. In the same session, open the **chat mode dropdown** (bottom-left of the chat input) and select the **TDD Red** agent — this hands off the conversation context (including your plan) to the new agent
2. Enter:
   ```
   Write failing tests for the scavenger hunt feature from the plan above
   ```
3. The agent will write tests for:
   - Component rendering
   - Checkbox interactions
   - Progress calculation
   - State management
4. The tests should **all fail** since no implementation exists yet — check VS Code's **Test Explorer** to confirm

#### Phase 3: TDD Green (Make Tests Pass)

1. Switch to the **TDD Green** agent using the **chat mode dropdown**
2. Enter:
   ```
   Make the failing tests pass with minimal implementation
   ```
3. Watch as it:
   - Implements the minimum code to pass tests
   - Runs tests after each change
   - Iterates until all tests pass

#### Phase 4: Refactor (Clean Up)

1. Switch to the **TDD Refactor** agent using the **chat mode dropdown**
2. Let it clean up the code while keeping tests green

### Checkpoint Recovery

If something goes wrong:
1. Use Chat **Checkpoints** to revert
2. Reset to before "TDD Red" started
3. Try again with adjusted prompts

> 💡 **Bonus:** Try **TDD Supervisor** for a fully automated TDD flow

✅ **Result:** A fully tested Scavenger Hunt feature built with disciplined TDD!

---

## 🎴 Task 2: Card Deck Mode (Design-Driven)

Use the **Pixel Jam** agent to focus on UI iteration while building new features.

### What We're Building

A new **Card Deck Shuffle** mode:
- Player opens the game
- Taps to get a random card
- Card flips with animation
- Shows a question to discuss

### Steps

1. In the **chat mode dropdown** (bottom-left of the chat input), select **Pixel Jam**
2. Enter:
   ```
   New mode: Card Deck Shuffle. Every player opens the game, 
   taps, and gets a random card with a question
   ```
4. Watch as it iterates on the UI
5. Follow up to refine:
   ```
   Add a cool 3D flip animation when revealing the card
   ```
   ```
   Make the card styling match the cyberpunk theme
   ```
6. **Commit** when you're happy

### What Pixel Jam Does Differently

- Focuses on **visual design** first
- Iterates on **UI/UX** before logic
- Uses the frontend design instructions
- Creates polished, animated interfaces

---

## 🔍 Task 3: UX Review Agent

Combine MCP tools, custom workflows, and subagent isolation for powerful review capabilities.

### Steps

1. In the **chat mode dropdown** (bottom-left of the chat input), select **UI Review**
2. Enter:
   ```
   start
   ```
3. When prompted, click **Allow for this Workspace** for Playwright tool access
4. Watch as it:
   - Takes screenshots of each page
   - Analyzes usability issues
   - Checks accessibility
   - Reviews visual consistency

### What Gets Reviewed

| Category | Checks |
|----------|--------|
| **Usability** | Navigation flow, button clarity, feedback |
| **Accessibility** | Color contrast, keyboard nav, screen readers |
| **Visual** | Consistency, spacing, alignment |
| **Interaction** | Touch targets, hover states, animations |

### Follow-Up Actions

After the review:
```
File the critical findings as GitHub issues
```
```
Fix the accessibility issues you found
```
```
Assign the navigation bug to a Copilot CLI session
```

✅ **Result:** A comprehensive UX review with actionable findings!

---

## 🎯 Bonus Challenges

If you have time, try these:

| Challenge | Approach |
|-----------|----------|
| Fix UX issues | Delegate to background or cloud agent |
| Multiple themes | Add theme picker to start screen |
| Social sharing | Add share button to win state |
| Leaderboard | Track and display high scores |
| Sound effects | Add audio feedback for interactions |

---

## ✅ Part 4 Complete!

You've learned how to:
- Use TDD agents for test-driven development
- Build features with the Red-Green-Refactor cycle
- Use design-focused agents like Pixel Jam
- Run comprehensive UX reviews
- Combine multiple agents for complex workflows

---

## 🎉 Workshop Complete!

Congratulations! You've completed the VS Code GitHub Copilot Agent Lab.

### What You Built

- ✅ A fully redesigned Social Bingo app
- ✅ Custom quiz themes
- ✅ Scavenger Hunt mode (TDD-built)
- ✅ Card Deck Shuffle mode (design-driven)

### What You Learned

1. **Context Engineering** — Teaching AI about your codebase
2. **Agentic Primitives** — Background, cloud, and custom agents
3. **Design-First Development** — UI iteration with AI assistance
4. **Test-Driven Development** — Reliable code with TDD agents

### Keep Going

- 📺 [VS Code on YouTube](https://www.youtube.com/code)
- 📖 [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot/overview)
- 🌟 [Awesome Copilot](https://github.com/github/awesome-copilot)
