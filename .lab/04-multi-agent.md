# Part 4: Multi-Agent Development

[🎮 Live Demo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Lab Guide](GUIDE.md) • [← Part 3](03-quiz-master.md)

---

> ⏱️ **Time:** ~20 minutes

Build new features using specialized agents: TDD agents for reliable code, and design agents for beautiful UI.

---

## 🧪 Task 1: Scavenger Hunt Mode (TDD-Driven)

Custom agents with handoffs break complex workflows into smaller steps, keeping you in control for critical decisions.

### What We're Building

A new **Scavenger Hunt** mode:
- Same questions as bingo
- Displayed as a simple checklist
- Progress meter at the top
- Click to mark items complete

### Steps

#### Phase 1: Plan

1. Start a new Chat in **Plan Mode**
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

#### Phase 2: TDD Red (Write Failing Tests)

1. Select **TDD Red** agent
2. Click **Start**
3. Watch as it writes tests for:
   - Component rendering
   - Checkbox interactions
   - Progress calculation
   - State management

4. Check VS Code's **Test Explorer** to see the failing tests

#### Phase 3: TDD Green (Make Tests Pass)

1. When Red is done, select **TDD Green** agent
2. Watch as it:
   - Implements the minimum code to pass tests
   - Runs tests after each change
   - Iterates until all tests pass

#### Phase 4: Refactor (Clean Up)

1. Select **TDD Refactor** agent
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

1. Start a new Chat
2. Select **Pixel Jam** as the agent
3. Enter:
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

1. Start a new Chat with **Pixel Jam**
2. Enter:
   ```
   Run review
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
Assign the navigation bug to a background agent
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

---

👉 **[🎉 Celebrate Your Completion! →](05-complete.md)**

---

[🎮 Play Game](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Lab Guide](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Part 3](03-quiz-master.md)

Happy Coding! 👋

*— The VS Code Team*
