<!-- l10n-sync: source-file="workshop/02-design.md" -->
# Parte 2: Frontend Design-First

[🎮 Demo ao Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guia do Lab](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Parte 1](01-setup.md)

---

> ⏱️ **Tempo:** ~15 minutos

Agora que o contexto do seu repositório está engenheirado, vamos ser criativos! Você vai redesenhar toda a UI usando desenvolvimento assistido por IA.

---

## 🎨 Tarefa 1: Deixe do Seu Jeito

Use o **Plan Mode** para começar qualquer item de trabalho maior. Itere no plano (2+ vezes!) com ajustes e esclarecimentos.

### Passos

1. No Chat, mude para **Plan Mode** (botão na parte inferior)
2. Digite sua visão:
   ```
   Let's do a full redesign. Make it [YOUR THEME]
   ```
3. Revise o plano gerado
4. Peça ajustes até ficar satisfeito
5. Clique em **Implement** para executar

### 🎭 Ideias de Temas

Escolha um que combine com você:

| Categoria | Temas |
|-----------|-------|
| **Minimal** | Minimalist Mono, Scandinavian Calm, Desert Sand Minimal |
| **Retro** | Retro Terminal Green, Pixel Arcade Style, Vaporwave Sunset |
| **Dark** | Cyberpunk Neon, Dark Mode Noir, Space Galaxy Glow |
| **Playful** | Playful Candy Pop, Toybox Primary Colors, Anime Bubble |
| **Professional** | Corporate Clean Blue, Gradient Glass UI, Metallic Chrome |
| **Creative** | Brutalist Blocks, Geometric Memphis, Bold Constructivist |
| **Cozy** | Cozy Coffee Shop, Soft Pastel Clouds, Notebook Doodle |
| **Unique** | Skeuomorphic Stickers, Paper Card Cutouts, Chalkboard |

✅ **Resultado:** Instruções de frontend e utilitários CSS se combinam para construir um design bonito.

---

## 📝 Tarefa 2: Mantenha as Instruções Atualizadas

Quando você fizer mudanças grandes de arquitetura, design ou dependências, atualize suas instruções!

### Passos

1. Após o redesign, continue com:
   ```
   Add a design guide section to copilot-instructions.md
   ```
2. Revise as mudanças
3. **Faça commit e push**

> 💡 Verifique se o GitHub Pages está atualizando com seu novo design!

---

## 🚀 Tarefa 3: Escale a Exploração com Agentes na Nuvem

Gere múltiplas variações de design em paralelo usando agentes na nuvem.

### Passos

1. Inicie um **novo Chat** em Plan Mode
2. Digite:
   ```
   Redesign the start screen as a more engaging landing page
   ```
3. Note as variações sugeridas no plano
4. Execute o prompt de exploração:
   ```
   /cloud-explore design variations
   ```
   📄 Veja `.github/prompts/cloud-explore.prompt.md`

5. Verifique as **Agent Sessions** para acompanhar os 3 novos agentes na nuvem
6. Clique em qualquer sessão para acompanhar o progresso ou abrir na web

### O que Está Acontecendo

O prompt inicia **3 agentes na nuvem em paralelo**, cada um explorando uma direção de design diferente. Eles vão:
- Criar branches
- Implementar variações
- Tirar capturas de tela
- Abrir PRs para sua revisão

✅ **Resultado:** 3 variações de design para comparar, todas rodando em paralelo!

> ⏰ Isso leva alguns minutos. Continue para a Parte 3 enquanto eles rodam.

---

## 🖼️ Vitrine de Design

Veja como fica o tema **Cyberpunk Neon**:

```
┌─────────────────────────────────────────────┐
│  ╔═══════════════════════════════════════╗  │
│  ║     🎮 SOC OPS - SOCIAL BINGO 🎮      ║  │
│  ╚═══════════════════════════════════════╝  │
│                                             │
│  ┌─────┬─────┬─────┬─────┬─────┐          │
│  │ ▓▓▓ │ ░░░ │ ▓▓▓ │ ░░░ │ ▓▓▓ │          │
│  ├─────┼─────┼─────┼─────┼─────┤          │
│  │ ░░░ │ ▓▓▓ │ ░░░ │ ▓▓▓ │ ░░░ │  NEON   │
│  ├─────┼─────┼─────┼─────┼─────┤  GLOW   │
│  │ ▓▓▓ │ ░░░ │ ★★★ │ ░░░ │ ▓▓▓ │          │
│  ├─────┼─────┼─────┼─────┼─────┤          │
│  │ ░░░ │ ▓▓▓ │ ░░░ │ ▓▓▓ │ ░░░ │          │
│  ├─────┼─────┼─────┼─────┼─────┤          │
│  │ ▓▓▓ │ ░░░ │ ▓▓▓ │ ░░░ │ ▓▓▓ │          │
│  └─────┴─────┴─────┴─────┴─────┘          │
│                                             │
│         [ 🔄 NEW GAME ]  [ 🎯 BINGO! ]      │
└─────────────────────────────────────────────┘
```

---

## ✅ Parte 2 Completa!

Você aprendeu como:
- Usar Plan Mode para tarefas complexas de design
- Iterar em planos antes de implementar
- Manter instruções atualizadas com as mudanças
- Escalar a exploração com agentes na nuvem em paralelo
