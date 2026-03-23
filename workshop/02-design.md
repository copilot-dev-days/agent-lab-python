# Part 2: Design-First Frontend

[📚 Lab Guide](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Part 1](01-setup.md)

---

> ⏱️ **Time:** ~15 minutes

Now that your repo context is engineered, let's get creative! You'll redesign the entire UI using AI-assisted development.

---

## 🎨 Task 1: Make It Yours

Use the **Plan agent** to start any bigger work item. Iterate on the plan (2+ times!) with tweaks and clarifications.

### Steps

1. Click the **New Session dropdown** (`+`) and select **Plan**
2. Enter your vision:
   ```
   Let's do a full redesign. Make it [YOUR THEME]
   ```
3. Review the generated plan
4. Ask for adjustments until you're happy
5. Click **Start Implementation** to execute

### 🎭 Theme Ideas

Pick one that speaks to you:

| Category | Themes |
|----------|--------|
| **Minimal** | Minimalist Mono, Scandinavian Calm, Desert Sand Minimal |
| **Retro** | Retro Terminal Green, Pixel Arcade Style, Vaporwave Sunset |
| **Dark** | Cyberpunk Neon, Dark Mode Noir, Space Galaxy Glow |
| **Playful** | Playful Candy Pop, Toybox Primary Colors, Anime Bubble |
| **Professional** | Corporate Clean Blue, Gradient Glass UI, Metallic Chrome |
| **Creative** | Brutalist Blocks, Geometric Memphis, Bold Constructivist |
| **Cozy** | Cozy Coffee Shop, Soft Pastel Clouds, Notebook Doodle |
| **Unique** | Skeuomorphic Stickers, Paper Card Cutouts, Chalkboard |

✅ **Result:** Frontend and CSS utility instructions combine to build a beautiful design.

---

## 📝 Task 2: Keep Instructions Updated

When you make major architecture, design, or dependency changes, update your instructions!

### Steps

1. After your redesign, follow up:
   ```
   Add a design guide section to copilot-instructions.md
   ```
2. Review the changes
3. **Commit and push**

---

## 🚀 Task 3: Scale Exploration with Cloud Agents

Generate multiple design variations in parallel using cloud agents.

### Steps

1. Click the **New Session dropdown** (`+`) and select **Plan**
2. Enter:
   ```
   Redesign the start screen as a more engaging landing page
   ```
3. Note the variations suggested in the plan
4. Run the exploration prompt:
   ```
   /cloud-explore design variations
   ```
   📄 See `.github/prompts/cloud-explore.prompt.md`

5. Check **Agent Sessions** to track the 3 new cloud agents
6. Click any session to follow progress or open in web

### What's Happening

The prompt spins up **3 parallel cloud agents**, each exploring a different design direction. They'll:
- Create branches
- Implement variations
- Take screenshots
- Open PRs for your review

✅ **Result:** 3 design variations to compare, all running in parallel!

> ⏰ These take a few minutes. Continue to Part 3 while they run.

---

## ✅ Part 2 Complete!

You've learned how to:
- Use the Plan agent for complex design tasks
- Iterate on plans before implementing
- Keep instructions updated with changes
- Scale exploration with parallel cloud agents
