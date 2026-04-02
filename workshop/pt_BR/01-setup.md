<!-- l10n-sync: source-file="workshop/01-setup.md" -->
# Parte 1: Configuração & Engenharia de Contexto

[🎮 Demo ao Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guia do Lab](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Visão Geral](00-overview.md)

---

> ⏱️ **Tempo:** ~15 minutos

Nesta seção, você vai configurar seu ambiente de desenvolvimento e ensinar o GitHub Copilot sobre sua base de código.

---

## 🔧 Configuração Inicial

### Passo 1: Crie Seu Repositório

1. Abra [github.com/copilot-dev-days/agent-lab-python](https://github.com/copilot-dev-days/agent-lab-python)
2. Clique em **Use this template** → **Create a new repository**
   - Nome: `my-soc-ops-python`
   - Visibilidade: **Public**
3. ✅ Seu próprio repositório Soc Ops está pronto!

### Passo 2: Ative o GitHub Pages

1. Vá para **Settings** → **Pages** do seu repositório
2. Em "Build and deployment", selecione **GitHub Actions**
3. ✅ Cada commit agora será publicado em: `https://{username}.github.io/{repo-name}`

### Passo 3: Clone & Abra no VS Code

1. Abra o VS Code
2. Execute o comando: `Git: Clone` → `Clone from GitHub`
3. Selecione seu novo repositório
4. Quando solicitado, instale as **extensões recomendadas**

### Passo 4: Execute o Agente de Setup

No painel de Chat:

```
/setup
```

O agente vai:
- Detectar seu ambiente
- Instalar dependências faltantes
- Iniciar o servidor de desenvolvimento

✅ **Sucesso:** O aplicativo está rodando no seu navegador!

---

## 📚 Entendendo a Engenharia de Contexto

Engenharia de contexto é como você ensina a IA sobre sua base de código específica. Isso torna as sugestões do Copilot mais precisas e relevantes.

### Tarefa 1: Gerar Instruções de Workspace

Instruções guiam todas as interações agênticas, tornando-as eficientes e confiáveis.

**Passos:**

1. Execute o comando: `Chat: Generate Workspace Instructions File`
2. Aguarde o agente analisar sua base de código
3. Revise as instruções geradas (provavelmente detalhadas demais!)
4. Continue com:
   ```
   Compress down by half and add a mandatory development checklist 
   (lint, build, test) to the top
   ```
5. **Faça commit** do arquivo de instruções

✅ **Resultado:** Todas as futuras solicitações terão um mapa básico do seu workspace.

---

### Tarefa 2: Agentes em Segundo Plano para Trabalho Paralelo

Agentes em segundo plano rodam em worktrees git isoladas — perfeitos para tarefas que não precisam de acompanhamento.

**Passos:**

1. Clique em `+` no Chat → **New background agent**
2. Digite:
   ```
   Add linting rules with ruff for unused vars and type hints; fix any errors
   ```
3. Deixe rodar, depois **Revise** e **Aplique** as mudanças
4. Clique com o botão direito na sessão para deletá-la quando terminar

**Experimente um Agente na Nuvem também:**

1. Clique em `+` → **New cloud agent**
2. Digite:
   ```
   Make the README more engaging as a landing page to the project
   ```

✅ **Resultado:** Regras de linting adicionadas, erros corrigidos, README melhorado — tudo mesclado de volta ao main!

---

### Tarefa 3: Explore Instruções Existentes

Seu repositório já vem com instruções pré-configuradas que ajudam a IA a entender o projeto.

#### Instruções de Utilitários CSS

📄 Veja `.github/instructions/css-utilities.instructions.md`

Estas documentam as classes utilitárias CSS customizadas disponíveis neste projeto Python/Jinja2.

> 💡 **Opcional:** Delete o texto principal e re-execute o prompt para ver como ele gera

#### Instruções de Design Frontend

📄 Veja `.github/instructions/frontend-design.instructions.md`

As instruções "sem gradientes roxos" desafiam o agente a pensar como um designer.

> 💡 **Pense sobre:** Quais outros vieses da IA você poderia desafiar e direcionar?

---

## ✅ Parte 1 Completa!

Você aprendeu como:
- Configurar seu ambiente de desenvolvimento
- Gerar e refinar instruções de workspace
- Usar agentes em segundo plano e na nuvem para trabalho paralelo
- Entender arquivos de instruções existentes
