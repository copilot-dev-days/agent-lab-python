<!-- l10n-sync: source-file="workshop/04-multi-agent.md" -->
# Parte 4: Desenvolvimento Multi-Agente

[🎮 Demo ao Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guia do Lab](GUIDE.md) • [← Parte 3](03-quiz-master.md)

---

> ⏱️ **Tempo:** ~20 minutos

Construa novas funcionalidades usando agentes especializados: agentes TDD para código confiável e agentes de design para uma UI bonita.

---

## 🧪 Tarefa 1: Modo Caça ao Tesouro (TDD)

Agentes personalizados com handoffs dividem fluxos de trabalho complexos em etapas menores, mantendo você no controle para decisões críticas.

### O que Vamos Construir

Um novo modo **Caça ao Tesouro**:
- Mesmas perguntas do bingo
- Exibidas como uma lista simples com checkboxes
- Medidor de progresso no topo
- Clique para marcar itens como completos

### Passos

#### Fase 1: Planejar

1. Inicie um novo Chat em **Plan Mode**
2. Digite:
   ```
   Add a new Scavenger Hunt mode: same questions, but shown as a 
   simple list with checkboxes and a progress meter
   ```
3. **Itere no plano** — verifique se ele:
   - ✅ Adiciona o modo à tela inicial
   - ✅ Cria um novo componente para a visualização em lista
   - ✅ Inclui um indicador de progresso
   - ❌ Não exagera nas funcionalidades

#### Fase 2: TDD Red (Escrever Testes que Falham)

1. Selecione o agente **TDD Red**
2. Clique em **Start**
3. Observe enquanto ele escreve testes para:
   - Renderização de componentes
   - Interações com checkboxes
   - Cálculo de progresso
   - Gerenciamento de estado

4. Verifique o **Test Explorer** do VS Code para ver os testes falhando

#### Fase 3: TDD Green (Fazer os Testes Passarem)

1. Quando o Red terminar, selecione o agente **TDD Green**
2. Observe enquanto ele:
   - Implementa o código mínimo para passar nos testes
   - Executa testes após cada mudança
   - Itera até todos os testes passarem

#### Fase 4: Refactor (Limpar o Código)

1. Selecione o agente **TDD Refactor**
2. Deixe ele limpar o código mantendo os testes verdes

### Recuperação com Checkpoints

Se algo der errado:
1. Use os **Checkpoints** do Chat para reverter
2. Volte para antes do "TDD Red" começar
3. Tente novamente com prompts ajustados

> 💡 **Bônus:** Experimente o **TDD Supervisor** para um fluxo TDD totalmente automatizado

✅ **Resultado:** Uma funcionalidade de Caça ao Tesouro totalmente testada, construída com TDD disciplinado!

---

## 🎴 Tarefa 2: Modo Baralho de Cartas (Design)

Use o agente **Pixel Jam** para focar na iteração de UI enquanto constrói novas funcionalidades.

### O que Vamos Construir

Um novo modo **Card Deck Shuffle**:
- O jogador abre o jogo
- Toca para receber uma carta aleatória
- A carta vira com animação
- Mostra uma pergunta para discussão

### Passos

1. Inicie um novo Chat
2. Selecione **Pixel Jam** como agente
3. Digite:
   ```
   New mode: Card Deck Shuffle. Every player opens the game, 
   taps, and gets a random card with a question
   ```
4. Observe enquanto ele itera na UI
5. Continue refinando:
   ```
   Add a cool 3D flip animation when revealing the card
   ```
   ```
   Make the card styling match the cyberpunk theme
   ```
6. **Faça commit** quando estiver satisfeito

### O que o Pixel Jam Faz de Diferente

- Foca no **design visual** primeiro
- Itera na **UI/UX** antes da lógica
- Usa as instruções de design frontend
- Cria interfaces polidas e animadas

---

## 🔍 Tarefa 3: Agente de Revisão de UX

Combine ferramentas MCP, fluxos personalizados e isolamento de subagentes para capacidades poderosas de revisão.

### Passos

1. Inicie um novo Chat com **Pixel Jam**
2. Digite:
   ```
   Run review
   ```
3. Quando solicitado, clique em **Allow for this Workspace** para acesso à ferramenta Playwright
4. Observe enquanto ele:
   - Tira capturas de tela de cada página
   - Analisa problemas de usabilidade
   - Verifica acessibilidade
   - Revisa consistência visual

### O que é Revisado

| Categoria | Verificações |
|-----------|-------------|
| **Usabilidade** | Fluxo de navegação, clareza dos botões, feedback |
| **Acessibilidade** | Contraste de cores, navegação por teclado, leitores de tela |
| **Visual** | Consistência, espaçamento, alinhamento |
| **Interação** | Alvos de toque, estados de hover, animações |

### Ações de Acompanhamento

Após a revisão:
```
File the critical findings as GitHub issues
```
```
Fix the accessibility issues you found
```
```
Assign the navigation bug to a background agent
```

✅ **Resultado:** Uma revisão de UX completa com descobertas acionáveis!

---

## 🎯 Desafios Bônus

Se você tiver tempo, tente estes:

| Desafio | Abordagem |
|---------|-----------|
| Corrigir problemas de UX | Delegue para agente em segundo plano ou na nuvem |
| Múltiplos temas | Adicione seletor de temas à tela inicial |
| Compartilhamento social | Adicione botão de compartilhar ao estado de vitória |
| Placar | Acompanhe e exiba pontuações mais altas |
| Efeitos sonoros | Adicione feedback de áudio para interações |

---

## ✅ Parte 4 Completa!

Você aprendeu como:
- Usar agentes TDD para desenvolvimento orientado a testes
- Construir funcionalidades com o ciclo Red-Green-Refactor
- Usar agentes focados em design como Pixel Jam
- Executar revisões de UX abrangentes
- Combinar múltiplos agentes para fluxos de trabalho complexos

---

## 🎉 Workshop Completo!

Parabéns! Você completou o VS Code GitHub Copilot Agent Lab.

### O que Você Construiu

- ✅ Um app de Bingo Social totalmente redesenhado
- ✅ Temas de quiz personalizados
- ✅ Modo Caça ao Tesouro (construído com TDD)
- ✅ Modo Card Deck Shuffle (guiado por design)

### O que Você Aprendeu

1. **Engenharia de Contexto** — Ensinar a IA sobre sua base de código
2. **Primitivas Agênticas** — Agentes em segundo plano, na nuvem e personalizados
3. **Desenvolvimento Design-First** — Iteração de UI com assistência de IA
4. **Desenvolvimento Orientado a Testes** — Código confiável com agentes TDD

### Continue Aprendendo

- 📺 [VS Code no YouTube](https://www.youtube.com/code)
- 📖 [VS Code Copilot Docs](https://code.visualstudio.com/docs/copilot/overview)
- 🌟 [Awesome Copilot](https://github.com/github/awesome-copilot)
