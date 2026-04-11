# Voice Brain Dump Workflow (Part 1) | 语音 Brain Dump 工作流 (第一期) | Flujo de Brain Dump por Voz (Parte 1)

> Capture your ideas the moment they hit. No typing, no friction, no lost thoughts.
>
> 想法来了就说出来。不用打字，不怕忘记。
>
> Captura tus ideas en el momento. Sin escribir, sin fricción, sin perder pensamientos.

<!-- Replace with your own Shortcut screenshot for best engagement -->

---

## Table of Contents | 目录 | Índice

- [English](#english)
- [中文](#中文)
- [Español](#español)
- [Series Roadmap](#series-roadmap)

---

<a id="english"></a>

## English

### The Problem

You're at work, on a walk, in the middle of a conversation, and a brilliant idea hits. By the time you can sit down and type it out, it's gone.

Even when you do capture it, it ends up scattered across Apple Notes, sticky notes on your desk, random text files on your desktop. Impossible to consolidate. Impossible to act on.

### The Solution

A voice based brain dump workflow built with the **iPhone Shortcuts app**. Under 5 minutes to set up. One entry point for all your ideas, auto filed and ready for AI agent processing.

### Workflow Steps

#### Step 1: Dictate Text

Open the Shortcuts app and create a new shortcut called **Brain Dump**. Add the **Dictate text** action as your first step. This activates your iPhone's microphone and lets you speak freely. No typing, just talk.

#### Step 2: Current Date

Add the **Current Date** action. This grabs the exact date and time when you triggered the shortcut.

#### Step 3: Format Date

Add the **Format Date** action, taking the Date from Step 2 as input. Configure it to output a consistent timestamp format (e.g., `2026-04-10_1430`). This becomes part of your filename so every brain dump is automatically chronological.

#### Step 4: Text (Dictated Text)

Add a **Text** action and insert the **Dictated Text** variable from Step 1 into it. This converts the dictation output into a clean text block ready to be saved as a file.

#### Step 5: Save Text to journal_inbox

Add the **Save File** action. Set the input to **Text** from Step 4, and the destination to a folder called **journal_inbox** on iCloud Drive. Turn off "Ask Where To Save" so it saves automatically. Turn off "Overwrite If File Exists" so you never lose a previous brain dump.

#### Step 6: Show Notification

Add the **Show Notification** action. Set the message to "Captured" followed by the **Saved File** variable. This gives you instant feedback that it worked, so you can get back to what you were doing without opening any app to check.

#### Step 7: Rename to .md

Add the **Rename** action. Set it to rename **Saved File** to **Formatted Date** + `-brain-dump.md`. For example: `2026-04-10_1430-brain-dump.md`.

Why Markdown? Because this is **Part 1 of a series**. In Part 2, an AI agent will read these `.md` files and process them automatically. Organizing, categorizing, generating action items. Markdown is the universal input format for AI agents.

### The Principle

Reduce friction to zero at the capture layer. Add intelligence at the processing layer.

**Part 2 coming soon:** AI agent integration for automatic brain dump processing.

---

<a id="中文"></a>

## 中文

### 问题

平时工作的时候、在外面玩的时候，脑子里突然冒出一个超棒的想法，然后就忘了。

就算当时存下来了呢？Notes、Sticky Notes 满天飞，东一条西一条，根本没法整理。

### 解决方案

用 iPhone「捷径」App 搭建的语音 Brain Dump 工作流。不到5分钟搞定。所有想法，一个入口，自动归档，为 AI Agent 处理做好准备。

### 工作流步骤

#### 第一步：听写文本

打开「捷径」App，新建一个捷径，命名为 **Brain Dump**。添加「听写文本」操作作为第一步。这会激活 iPhone 麦克风，直接对着手机说就行。不用打字，张嘴就来。

#### 第二步：当前日期

添加「当前日期」操作。这会抓取你触发捷径时的精确日期和时间。

#### 第三步：格式化日期

添加「格式化日期」操作，输入是第二步的 Date。配置成统一的时间戳格式（比如 `2026-04-10_1430`）。这会成为文件名的一部分，让每条 brain dump 自动按时间排列。

#### 第四步：文本（听写文本）

添加一个「文本」操作，把第一步的 **Dictated Text** 变量插入进去。这一步把听写输出转换成一个干净的文本块，可以直接存为文件。

#### 第五步：保存文本到 journal_inbox

添加「储存文件」操作。输入设为第四步的 **Text**，目标路径设为 iCloud Drive 上的 **journal_inbox** 文件夹。关掉「询问储存位置」让它自动保存。关掉「覆盖现有文件」确保你不会丢失之前的 brain dump。

#### 第六步：显示通知

添加「显示通知」操作。消息设为「Captured」加上 **Saved File** 变量。这样你马上就知道成功了，不用打开任何 App 去检查。

#### 第七步：重命名为 .md

添加「重新命名」操作。把 **Saved File** 重命名为 **Formatted Date** + `-brain-dump.md`。例如：`2026-04-10_1430-brain-dump.md`。

为什么用 Markdown？因为这只是**第一期**。第二期会接入 AI Agent 自动读取这些 `.md` 文件并进行处理：整理、分类、生成 action items。Markdown 是 AI Agent 最通用的输入格式。

### 核心理念

在捕捉层把摩擦力降到零，在处理层加入智能。

**第二期即将推出：** AI Agent 自动处理 brain dump。

---

<a id="español"></a>

## Español

### El Problema

Estás trabajando, de paseo, en medio de una conversación, y se te ocurre una idea increíble. Para cuando puedes sentarte a escribirla, ya se fue.

Y cuando sí la capturas, termina perdida entre Apple Notes, sticky notes en tu escritorio, archivos de texto random por todos lados. Imposible consolidar. Imposible actuar.

### La Solución

Un flujo de brain dump por voz construido con la app **Atajos de iPhone**. Menos de 5 minutos para configurar. Un solo punto de entrada para todas tus ideas, archivado automático, listo para procesamiento con AI agent.

### Pasos del Flujo

#### Paso 1: Dictar Texto

Abre la app Atajos y crea un nuevo atajo llamado **Brain Dump**. Agrega la acción **Dictar texto** como primer paso. Esto activa el micrófono de tu iPhone y te permite hablar libremente. Sin escribir, solo habla.

#### Paso 2: Fecha Actual

Agrega la acción **Fecha Actual**. Esto captura la fecha y hora exacta en que activaste el atajo.

#### Paso 3: Formatear Fecha

Agrega la acción **Formatear Fecha**, usando la Date del Paso 2 como input. Configúrala para generar un timestamp consistente (ej., `2026-04-10_1430`). Esto se convierte en parte del nombre del archivo para que cada brain dump quede automáticamente en orden cronológico.

#### Paso 4: Texto (Texto Dictado)

Agrega una acción **Texto** e inserta la variable **Dictated Text** del Paso 1. Esto convierte la salida de dictado en un bloque de texto limpio listo para guardar como archivo.

#### Paso 5: Guardar Texto en journal_inbox

Agrega la acción **Guardar Archivo**. Configura el input como **Text** del Paso 4, y el destino a una carpeta llamada **journal_inbox** en iCloud Drive. Desactiva "Preguntar dónde guardar" para que se guarde automáticamente. Desactiva "Sobrescribir si existe" para no perder brain dumps anteriores.

#### Paso 6: Mostrar Notificación

Agrega la acción **Mostrar Notificación**. Configura el mensaje como "Captured" seguido de la variable **Saved File**. Esto te da feedback instantáneo de que funcionó, para que puedas volver a lo que estabas haciendo sin abrir ninguna app para verificar.

#### Paso 7: Renombrar a .md

Agrega la acción **Renombrar**. Renombra **Saved File** a **Formatted Date** + `-brain-dump.md`. Por ejemplo: `2026-04-10_1430-brain-dump.md`.

¿Por qué Markdown? Porque esto es solo la **Parte 1 de una serie**. En la Parte 2, un AI agent va a leer estos archivos `.md` y procesarlos automáticamente. Organizar, categorizar, generar action items. Markdown es el formato de entrada universal para AI agents.

### El Principio

Reducir la fricción a cero en la capa de captura. Agregar inteligencia en la capa de procesamiento.

**Parte 2 próximamente:** integración con AI agent para procesamiento automático de brain dumps.

---

## Series Roadmap

| Part | Topic | Status |
|---|---|---|
| **Part 1** | Voice capture to .md on iCloud (this post) | ✅ Published |
| **Part 2** | AI Agent reads and processes brain dumps | 🔜 Coming soon |
| **Part 3** | Full automation pipeline | 🔜 Coming soon |

---

## License

MIT
