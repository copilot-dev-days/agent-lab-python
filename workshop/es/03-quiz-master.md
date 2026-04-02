<!-- l10n-sync: source-file="workshop/03-quiz-master.md" -->
# Parte 3: Quiz Master Personalizado

[🎮 Demo en Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guía del Lab](GUIDE.md) • [← Parte 2](02-design.md)

---

> ⏱️ **Tiempo:** ~10 minutos

Crea tus propios temas de quiz especializados usando agentes personalizados — flujos de trabajo que van más allá de prompts genéricos de programación.

---

## 🎲 Entendiendo Agentes Personalizados

Los agentes personalizados se definen en `.github/agents/` y proporcionan:
- **Conocimiento especializado** para tareas específicas
- **Flujos de trabajo consistentes** para procesos repetibles
- **Contexto enfocado** que mejora la calidad de la salida

📄 Revisa: `.github/agents/quiz-master.agent.md`

---

## 🎯 Tarea: Tu Propio Quiz Master

### Pasos

1. Inicia un **nuevo Chat**
2. Selecciona **Quiz Master** como agente personalizado (desde el selector de agentes)
3. Escribe tu tema:
   ```
   Update questions to [YOUR THEME]
   ```
   O simplemente:
   ```
   Update quiz
   ```

4. Revisa las preguntas generadas
5. Continúa pidiendo más creatividad:
   ```
   Make them more chaotic and unexpected!
   ```

### 🎭 Ideas de Temas

| Categoría | Temas |
|-----------|-------|
| **Professional** | Skill Bingo, Team Bingo, Work Culture Bingo |
| **Personal** | Personality Bingo, Lifestyle Bingo, Travel Bingo |
| **Tech** | Tech Life Bingo, Fandom Bingo, Dev Memes Bingo |
| **Interactive** | Secret Challenge Bingo, Micro-Challenge Bingo, Mystery Bingo |
| **Fun** | Office Humor Bingo, Chaos Bingo, Opposites Bingo |
| **Deep** | Deep Chat Bingo, Creative Bingo, Reflective Bingo |

### Descripciones de los Temas

- **Skill Bingo** — Habilidades profesionales o técnicas en lugar de datos personales
- **Personality Bingo** — Preferencias, manías y características divertidas
- **Secret Challenge Bingo** — Micro-tareas rápidas con las personas que conoces
- **Team Bingo** — Categorías por departamento o equipo
- **Tech Life Bingo** — Lenguajes de programación, atajos, frameworks, memes de dev
- **Chaos Bingo** — Prompts sorprendentes, absurdos e impredecibles
- **Opposites Bingo** — Encuentra a alguien que sea tu opuesto en ejes específicos

---

## ☁️ Tarea: Generación de Quiz en la Nube

Ejecuta el quiz master como un agente en la nube para generación asíncrona.

### Pasos

1. Haz clic en `+` → **New cloud agent**
2. Selecciona **Quiz Master**
3. Escribe un tema diferente:
   ```
   Create a Tech Life Bingo with questions about 
   coding habits, IDE preferences, and developer culture
   ```
4. Déjalo correr en segundo plano
5. Revisa el PR cuando esté listo

✅ **Resultado:** El agente personalizado genera preguntas creativas y temáticas mientras tú sigues trabajando.

---

## 📝 Ejemplo de Salida: Tech Life Bingo

Esto es lo que un tema Tech Life podría generar:

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

## 💡 Consejos

1. **Sé específico** — "Haz preguntas sobre cultura de startups" funciona mejor que "hazlo gracioso"
2. **Itera** — Sigue refinando el tono y la creatividad
3. **Mezcla temas** — "Combina Tech Life con Chaos Bingo" para resultados inesperados
4. **Prueba localmente** — Ejecuta la app para ver cómo se ven las preguntas en el grid del bingo

---

## ✅ ¡Parte 3 Completa!

Aprendiste cómo:
- Usar agentes personalizados para flujos de trabajo especializados
- Generar preguntas de quiz temáticas
- Ejecutar agentes personalizados en la nube
- Iterar en la salida del agente para mejores resultados
