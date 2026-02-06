# Part 1: Setup & Context Engineering

[🎮 Live Demo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Lab Guide](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Overview](00-overview.md)

---

> ⏱️ **Time:** ~15 minutes

In this section, you'll set up your development environment and teach GitHub Copilot about your codebase.

---

## 🔧 Initial Setup

### Step 1: Create Your Repository

1. Open [github.com/madebygps/vscode-github-copilot-agent-lab](https://github.com/madebygps/vscode-github-copilot-agent-lab)
2. Click **Use this template** → **Create a new repository**
   - Name: `my-soc-ops-python`
   - Visibility: **Public**
3. ✅ Your own Soc Ops repo is ready!

### Step 2: Enable GitHub Pages

1. Go to your repo's **Settings** → **Pages**
2. Under "Build and deployment", select **GitHub Actions**
3. ✅ Every commit will now publish to: `https://{username}.github.io/{repo-name}`

### Step 3: Clone & Open in VS Code

1. Open VS Code
2. Run command: `Git: Clone` → `Clone from GitHub`
3. Select your new repository
4. When prompted, install **recommended extensions**

### Step 4: Run the Setup Agent

In the Chat panel:

```
/setup
```

The agent will:
- Detect your environment
- Install any missing dependencies
- Start the development server

✅ **Success:** App is running in your browser!

---

## 📚 Understanding Context Engineering

Context engineering is how you teach AI about your specific codebase. This makes Copilot's suggestions more accurate and relevant.

### Task 1: Generate Workspace Instructions

Instructions guide all agentic interactions, making them efficient and reliable.

**Steps:**

1. Run command: `Chat: Generate Workspace Instructions File`
2. Wait for the agent to analyze your codebase
3. Review the generated instructions (probably too detailed!)
4. Follow up with:
   ```
   Compress down by half and add a mandatory development checklist 
   (lint, build, test) to the top
   ```
5. **Commit** the instructions file

✅ **Result:** All future requests have a basic map of your workspace.

---

### Task 2: Background Agents for Parallel Work

Background agents run in isolated git worktrees — perfect for tasks that don't need handholding.

**Steps:**

1. Click `+` in Chat → **New background agent**
2. Enter:
   ```
   Add linting rules with ruff for unused vars and type hints; fix any errors
   ```
3. Let it run, then **Review** and **Apply** the changes
4. Right-click the session to delete it when done

**Try a Cloud Agent too:**

1. Click `+` → **New cloud agent**
2. Enter:
   ```
   Make the README more engaging as a landing page to the project
   ```

✅ **Result:** Linting rules added, errors fixed, README improved — all merged back to main!

---

### Task 3: Explore Existing Instructions

Your repo comes with pre-configured instructions that help the AI understand the project.

#### CSS Utilities Instructions

📄 See `.github/instructions/css-utilities.instructions.md`

These document the custom CSS utility classes available in this Python/Jinja2 project.

> 💡 **Optional:** Delete the main text and re-run the prompt to see how it generates

#### Frontend Design Instructions

📄 See `.github/instructions/frontend-design.instructions.md`

The "no purple gradients" instructions challenge the agent to think like a designer.

> 💡 **Think about:** What other AI biases could you challenge and nudge?

---

## ✅ Part 1 Complete!

You've learned how to:
- Set up your development environment
- Generate and refine workspace instructions
- Use background and cloud agents for parallel work
- Understand existing instruction files

---

[🎮 Live Demo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Lab Guide](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Overview](00-overview.md)

👉 **[Continue to Part 2: Design-First Frontend →](02-design.md)**
