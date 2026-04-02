<!-- l10n-sync: source-file="workshop/03-quiz-master.md" -->
# Parte 3: Quiz Master Personalizado

[🎮 Demo ao Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guia do Lab](GUIDE.md) • [← Parte 2](02-design.md)

---

> ⏱️ **Tempo:** ~10 minutos

Crie seus próprios temas de quiz especializados usando agentes personalizados — fluxos de trabalho que vão além de prompts genéricos de programação.

---

## 🎲 Entendendo Agentes Personalizados

Agentes personalizados são definidos em `.github/agents/` e fornecem:
- **Conhecimento especializado** para tarefas específicas
- **Fluxos de trabalho consistentes** para processos repetíveis
- **Contexto focado** que melhora a qualidade da saída

📄 Confira: `.github/agents/quiz-master.agent.md`

---

## 🎯 Tarefa: Seu Próprio Quiz Master

### Passos

1. Inicie um **novo Chat**
2. Selecione **Quiz Master** como agente personalizado (no seletor de agentes)
3. Digite seu tema:
   ```
   Update questions to [YOUR THEME]
   ```
   Ou simplesmente:
   ```
   Update quiz
   ```

4. Revise as perguntas geradas
5. Continue pedindo mais criatividade:
   ```
   Make them more chaotic and unexpected!
   ```

### 🎭 Ideias de Temas

| Categoria | Temas |
|-----------|-------|
| **Professional** | Skill Bingo, Team Bingo, Work Culture Bingo |
| **Personal** | Personality Bingo, Lifestyle Bingo, Travel Bingo |
| **Tech** | Tech Life Bingo, Fandom Bingo, Dev Memes Bingo |
| **Interactive** | Secret Challenge Bingo, Micro-Challenge Bingo, Mystery Bingo |
| **Fun** | Office Humor Bingo, Chaos Bingo, Opposites Bingo |
| **Deep** | Deep Chat Bingo, Creative Bingo, Reflective Bingo |

### Descrições dos Temas

- **Skill Bingo** — Habilidades profissionais ou técnicas em vez de fatos pessoais
- **Personality Bingo** — Preferências, manias e características divertidas
- **Secret Challenge Bingo** — Micro-tarefas rápidas com as pessoas que você conhece
- **Team Bingo** — Categorias por departamento ou equipe
- **Tech Life Bingo** — Linguagens de programação, atalhos, frameworks, memes de dev
- **Chaos Bingo** — Prompts surpreendentes, absurdos e imprevisíveis
- **Opposites Bingo** — Encontre alguém que é o seu oposto em eixos específicos

---

## ☁️ Tarefa: Geração de Quiz na Nuvem

Execute o quiz master como um agente na nuvem para geração assíncrona.

### Passos

1. Clique em `+` → **New cloud agent**
2. Selecione **Quiz Master**
3. Digite um tema diferente:
   ```
   Create a Tech Life Bingo with questions about 
   coding habits, IDE preferences, and developer culture
   ```
4. Deixe rodar em segundo plano
5. Revise o PR quando estiver pronto

✅ **Resultado:** O agente personalizado gera perguntas criativas e temáticas enquanto você continua trabalhando.

---

## 📝 Exemplo de Saída: Tech Life Bingo

Veja o que um tema Tech Life pode gerar:

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

## 💡 Dicas

1. **Seja específico** — "Faça perguntas sobre cultura de startups" funciona melhor do que "deixe engraçado"
2. **Itere** — Continue refinando o tom e a criatividade
3. **Misture temas** — "Combine Tech Life com Chaos Bingo" para resultados inesperados
4. **Teste localmente** — Execute o app para ver como as perguntas ficam no grid do bingo

---

## ✅ Parte 3 Completa!

Você aprendeu como:
- Usar agentes personalizados para fluxos de trabalho especializados
- Gerar perguntas de quiz temáticas
- Executar agentes personalizados na nuvem
- Iterar na saída do agente para melhores resultados
