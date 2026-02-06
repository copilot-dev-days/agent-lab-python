# Part 3: Custom Quiz Master

[🎮 Live Demo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Lab Guide](GUIDE.md) • [← Part 2](02-design.md)

---

> ⏱️ **Time:** ~10 minutes

Create your own specialized quiz themes using custom agents — workflows that go beyond generic coding prompts.

---

## 🎲 Understanding Custom Agents

Custom agents are defined in `.github/agents/` and provide:
- **Specialized knowledge** for specific tasks
- **Consistent workflows** for repeatable processes
- **Focused context** that improves output quality

📄 Check out: `.github/agents/quiz-master.agent.md`

---

## 🎯 Task: Your Own Quiz Master

### Steps

1. Start a **new Chat**
2. Select **Quiz Master** as the custom agent (from the agent picker)
3. Enter your theme:
   ```
   Update questions to [YOUR THEME]
   ```
   Or simply:
   ```
   Update quiz
   ```

4. Review the generated questions
5. Follow up for more creativity:
   ```
   Make them more chaotic and unexpected!
   ```

### 🎭 Theme Ideas

| Category | Themes |
|----------|--------|
| **Professional** | Skill Bingo, Team Bingo, Work Culture Bingo |
| **Personal** | Personality Bingo, Lifestyle Bingo, Travel Bingo |
| **Tech** | Tech Life Bingo, Fandom Bingo, Dev Memes Bingo |
| **Interactive** | Secret Challenge Bingo, Micro-Challenge Bingo, Mystery Bingo |
| **Fun** | Office Humor Bingo, Chaos Bingo, Opposites Bingo |
| **Deep** | Deep Chat Bingo, Creative Bingo, Reflective Bingo |

### Theme Descriptions

- **Skill Bingo** — Workplace or technical skills instead of personal facts
- **Personality Bingo** — Preferences, quirks, and fun traits
- **Secret Challenge Bingo** — Quick micro-tasks with people you meet
- **Team Bingo** — Department or team categories
- **Tech Life Bingo** — Coding languages, shortcuts, frameworks, dev memes
- **Chaos Bingo** — Surprising, absurd, unpredictable prompts
- **Opposites Bingo** — Find someone who is your opposite on specific axes

---

## ☁️ Task: Cloud Quiz Generation

Run the quiz master as a cloud agent for async generation.

### Steps

1. Click `+` → **New cloud agent**
2. Select **Quiz Master**
3. Enter a different theme:
   ```
   Create a Tech Life Bingo with questions about 
   coding habits, IDE preferences, and developer culture
   ```
4. Let it run in the background
5. Review the PR when ready

✅ **Result:** Custom agent generates creative, themed questions while you continue working.

---

## 📝 Example Output: Tech Life Bingo

Here's what a Tech Life theme might generate:

```
┌────────────────────────────────────────────────┐
│  Uses dark mode     │  Has 50+ browser tabs   │
│  for everything     │  open right now         │
├────────────────────────────────────────────────┤
│  Knows vim          │  Has a mechanical       │
│  keybindings        │  keyboard               │
├────────────────────────────────────────────────┤
│  Prefers tabs       │  Has strong opinions    │
│  over spaces        │  about semicolons       │
├────────────────────────────────────────────────┤
│  Uses AI to write   │  Has a dotfiles         │
│  commit messages    │  repository             │
└────────────────────────────────────────────────┘
```

---

## 💡 Pro Tips

1. **Be specific** — "Make questions about startup culture" works better than "make it funny"
2. **Iterate** — Follow up to refine the tone and creativity
3. **Mix themes** — "Combine Tech Life with Chaos Bingo" for unexpected results
4. **Test locally** — Run the app to see how questions look on the bingo grid

---

## ✅ Part 3 Complete!

You've learned how to:
- Use custom agents for specialized workflows
- Generate themed quiz questions
- Run custom agents in the cloud
- Iterate on agent output for better results

---

---

[🎮 Live Demo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Lab Guide](GUIDE.md) • [← Part 2](02-design.md)

👉 **[Continue to Part 4: Multi-Agent Development →](04-multi-agent.md)**
