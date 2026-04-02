<!-- l10n-sync: source-file="workshop/01-setup.md" -->
# Parte 1: Configuración & Ingeniería de Contexto

[🎮 Demo en Vivo](https://madebygps.github.io/vscode-github-copilot-agent-lab/) • [📚 Guía del Lab](https://madebygps.github.io/vscode-github-copilot-agent-lab/docs/) • [← Descripción General](00-overview.md)

---

> ⏱️ **Tiempo:** ~15 minutos

En esta sección, configurarás tu entorno de desarrollo y le enseñarás a GitHub Copilot sobre tu código base.

---

## 🔧 Configuración Inicial

### Paso 1: Crea Tu Repositorio

1. Abre [github.com/copilot-dev-days/agent-lab-python](https://github.com/copilot-dev-days/agent-lab-python)
2. Haz clic en **Use this template** → **Create a new repository**
   - Nombre: `my-soc-ops-python`
   - Visibilidad: **Public**
3. ✅ ¡Tu propio repositorio de Soc Ops está listo!

### Paso 2: Activa GitHub Pages

1. Ve a **Settings** → **Pages** de tu repositorio
2. En "Build and deployment", selecciona **GitHub Actions**
3. ✅ Cada commit ahora se publicará en: `https://{username}.github.io/{repo-name}`

### Paso 3: Clona & Abre en VS Code

1. Abre VS Code
2. Ejecuta el comando: `Git: Clone` → `Clone from GitHub`
3. Selecciona tu nuevo repositorio
4. Cuando se te solicite, instala las **extensiones recomendadas**

### Paso 4: Ejecuta el Agente de Setup

En el panel de Chat:

```
/setup
```

El agente va a:
- Detectar tu entorno
- Instalar las dependencias faltantes
- Iniciar el servidor de desarrollo

✅ **Éxito:** ¡La aplicación está corriendo en tu navegador!

---

## 📚 Entendiendo la Ingeniería de Contexto

La ingeniería de contexto es cómo le enseñas a la IA sobre tu código base específico. Esto hace que las sugerencias de Copilot sean más precisas y relevantes.

### Tarea 1: Generar Instrucciones de Workspace

Las instrucciones guían todas las interacciones agénticas, haciéndolas eficientes y confiables.

**Pasos:**

1. Ejecuta el comando: `Chat: Generate Workspace Instructions File`
2. Espera a que el agente analice tu código base
3. Revisa las instrucciones generadas (¡probablemente demasiado detalladas!)
4. Continúa con:
   ```
   Compress down by half and add a mandatory development checklist 
   (lint, build, test) to the top
   ```
5. **Haz commit** del archivo de instrucciones

✅ **Resultado:** Todas las solicitudes futuras tendrán un mapa básico de tu workspace.

---

### Tarea 2: Agentes en Segundo Plano para Trabajo Paralelo

Los agentes en segundo plano corren en worktrees git aisladas — perfectos para tareas que no necesitan supervisión.

**Pasos:**

1. Haz clic en `+` en Chat → **New background agent**
2. Escribe:
   ```
   Add linting rules with ruff for unused vars and type hints; fix any errors
   ```
3. Déjalo correr, luego **Revisa** y **Aplica** los cambios
4. Haz clic derecho en la sesión para eliminarla cuando termines

**Prueba también un Agente en la Nube:**

1. Haz clic en `+` → **New cloud agent**
2. Escribe:
   ```
   Make the README more engaging as a landing page to the project
   ```

✅ **Resultado:** Reglas de linting agregadas, errores corregidos, README mejorado — ¡todo fusionado de vuelta a main!

---

### Tarea 3: Explora Instrucciones Existentes

Tu repositorio viene con instrucciones preconfiguradas que ayudan a la IA a entender el proyecto.

#### Instrucciones de Utilidades CSS

📄 Consulta `.github/instructions/css-utilities.instructions.md`

Estas documentan las clases utilitarias CSS personalizadas disponibles en este proyecto Python/Jinja2.

> 💡 **Opcional:** Elimina el texto principal y vuelve a ejecutar el prompt para ver cómo lo genera

#### Instrucciones de Diseño Frontend

📄 Consulta `.github/instructions/frontend-design.instructions.md`

Las instrucciones "sin gradientes morados" desafían al agente a pensar como un diseñador.

> 💡 **Piensa en:** ¿Qué otros sesgos de la IA podrías desafiar y redirigir?

---

## ✅ ¡Parte 1 Completa!

Aprendiste cómo:
- Configurar tu entorno de desarrollo
- Generar y refinar instrucciones de workspace
- Usar agentes en segundo plano y en la nube para trabajo paralelo
- Entender archivos de instrucciones existentes
