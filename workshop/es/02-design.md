<!-- l10n-sync: source-file="workshop/02-design.md" -->
# Parte 2: Frontend Design-First

[🎮 Demo en Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guía del Lab](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Parte 1](01-setup.md)

---

> ⏱️ **Tiempo:** ~15 minutos

Ahora que el contexto de tu repositorio está ingeniado, ¡vamos a ser creativos! Vas a rediseñar toda la UI usando desarrollo asistido por IA.

---

## 🎨 Tarea 1: Hazlo Tuyo

Usa el **Plan Mode** para comenzar cualquier elemento de trabajo más grande. Itera en el plan (¡2+ veces!) con ajustes y aclaraciones.

### Pasos

1. En Chat, cambia a **Plan Mode** (botón en la parte inferior)
2. Escribe tu visión:
   ```
   Let's do a full redesign. Make it [YOUR THEME]
   ```
3. Revisa el plan generado
4. Pide ajustes hasta que estés satisfecho
5. Haz clic en **Implement** para ejecutar

### 🎭 Ideas de Temas

Elige uno que te inspire:

| Categoría | Temas |
|-----------|-------|
| **Minimal** | Minimalist Mono, Scandinavian Calm, Desert Sand Minimal |
| **Retro** | Retro Terminal Green, Pixel Arcade Style, Vaporwave Sunset |
| **Dark** | Cyberpunk Neon, Dark Mode Noir, Space Galaxy Glow |
| **Playful** | Playful Candy Pop, Toybox Primary Colors, Anime Bubble |
| **Professional** | Corporate Clean Blue, Gradient Glass UI, Metallic Chrome |
| **Creative** | Brutalist Blocks, Geometric Memphis, Bold Constructivist |
| **Cozy** | Cozy Coffee Shop, Soft Pastel Clouds, Notebook Doodle |
| **Unique** | Skeuomorphic Stickers, Paper Card Cutouts, Chalkboard |

✅ **Resultado:** Las instrucciones de frontend y utilidades CSS se combinan para construir un diseño hermoso.

---

## 📝 Tarea 2: Mantén las Instrucciones Actualizadas

Cuando hagas cambios importantes de arquitectura, diseño o dependencias, ¡actualiza tus instrucciones!

### Pasos

1. Después del rediseño, continúa con:
   ```
   Add a design guide section to copilot-instructions.md
   ```
2. Revisa los cambios
3. **Haz commit y push**

> 💡 ¡Verifica que GitHub Pages se esté actualizando con tu nuevo diseño!

---

## 🚀 Tarea 3: Escala la Exploración con Agentes en la Nube

Genera múltiples variaciones de diseño en paralelo usando agentes en la nube.

### Pasos

1. Inicia un **nuevo Chat** en Plan Mode
2. Escribe:
   ```
   Redesign the start screen as a more engaging landing page
   ```
3. Observa las variaciones sugeridas en el plan
4. Ejecuta el prompt de exploración:
   ```
   /cloud-explore design variations
   ```
   📄 Consulta `.github/prompts/cloud-explore.prompt.md`

5. Revisa las **Agent Sessions** para seguir los 3 nuevos agentes en la nube
6. Haz clic en cualquier sesión para seguir el progreso o abrir en la web

### Qué Está Pasando

El prompt inicia **3 agentes en la nube en paralelo**, cada uno explorando una dirección de diseño diferente. Ellos van a:
- Crear branches
- Implementar variaciones
- Tomar capturas de pantalla
- Abrir PRs para tu revisión

✅ **Resultado:** ¡3 variaciones de diseño para comparar, todas corriendo en paralelo!

> ⏰ Esto toma unos minutos. Continúa con la Parte 3 mientras se ejecutan.

---

## 🖼️ Vitrina de Diseño

Así se ve el tema **Cyberpunk Neon**:

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

## ✅ ¡Parte 2 Completa!

Aprendiste cómo:
- Usar Plan Mode para tareas complejas de diseño
- Iterar en planes antes de implementar
- Mantener instrucciones actualizadas con los cambios
- Escalar la exploración con agentes en la nube en paralelo
