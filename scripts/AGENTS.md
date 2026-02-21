# Roo Code Agent Charter (Agents Charter)

**Effective Date**: 2026‑02‑d
**Authority Level**: **Vital** (Highest) — This file has the highest binding power in this project.

## 1. Charter Purpose

This charter defines the **core behavioral guidelines, workflows, and responsibility boundaries** for the AI agent (Roo Code) working in this project. Its purpose is to translate the advanced architectural theories from `deep research.md` into executable, mandatory protocols, ensuring the agent achieves best practices in **constraint systems, weight distribution, and high‑efficiency orchestration**.

## 2. Hierarchy of Constraints

The agent must resolve and apply instructions in the following priority order (highest to lowest):

1.  **`AGENTS.md` (this file)** — **Vital** — Team‑standardized agent charter.
2.  **`.roo/rules‑{mode}/`** — **Critical** — Project‑specific **mode‑specific** fine‑grained rules (e.g., `.roo/rules‑architect/planning.md`).
3.  **`.roo/rules/`** — **High** — Project‑wide **general** rules (e.g., coding standards, security).
4.  **`.clinerules`** — **Supplemental** — Traditional single‑file constraint protocol, mainly used for legacy support or quick adjustments.
5.  Global rules (`~/.roo/rules‑{mode}/`, `~/.roo/rules/`, system prompts) — **Medium/Low** — Default rules for all projects.

**Conflict resolution**: higher‑level files override lower‑level files.

## 3. Core Workflow (Prime Directive)

The agent must strictly execute the `memory_bank` workflow **at the start of each session**, as defined in `.clinerules` and reinforced here.

### 3.1 On Start
1.  **Read static context**:
    *   `projectContext.md` — Understand high‑level project goals and design philosophy.
    *   `techContext.md` — Master the tech stack, database schema, API specifications.
    *   `productContext.md` — Understand user stories, business logic, and Architecture Decision Records (ADR).
    *   `systemPatterns.md` — Learn project‑specific architectural patterns and design principles.
2.  **Read dynamic context**:
    *   `activeContext.md` — Restore current task progress, to‑do items, and recent issues.
    *   `progress.md` — View project milestones, clarify current phase.
    *   `decisionLog.md` — Review past key decisions to avoid repeating mistakes.

### 3.2 Execution
1.  **Mode identification**: Based on the user request or task nature, the agent must **self‑identify** which mode (`architect`, `code`, `debug`, `orchestrator`) it should be in.
2.  **Load mode rules**: Automatically load the corresponding `.roo/rules‑{mode}/` rule files, which are placed at the **end** of the prompt, enjoying the highest recency‑effect weight.
3.  **Atomic tasks**: Follow the **TDD cycle** (Red‑Green‑Refactor) and **modularity** principles. No source‑code file may exceed **200 lines**.
4.  **Strong‑type contracts**: All data exchange must be defined through **Pydantic v2 (Strict)** models; the use of `Any` is prohibited.

### 3.3 On Finish
1.  **Update dynamic context**: **Append** this session’s progress, new to‑do items, encountered technical difficulties, etc., to `activeContext.md`.
2.  **Tail‑Strategy maintenance**: If `activeContext.md` contains more than 5 entries, move the oldest completed tasks to `archive.md`.
3.  **Optional updates**: If this task produced new architectural patterns or key decisions, update `systemPatterns.md` or `decisionLog.md` accordingly.

## 4. Mode Responsibility Boundaries

The agent must adjust its behavior and output tendencies according to the following role definitions.

| Mode          | Core Responsibilities                                                                 | Forbidden Actions                                                                               |
| :------------ | :------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------- |
| **`architect`** | Macro design, directory‑structure planning, writing ADRs, creating execution plans, analyzing technology choices. | Writing concrete business‑logic code (except for minimal examples).                              |
| **`code`**      | Implementing concrete features, writing Pydantic models, service‑layer logic, API routes, unit tests.                | Blind refactoring without an explicit plan from `architect` or a clear task in `activeContext.md`. |
| **`debug`**     | Analyzing tracebacks, troubleshooting environment issues, running test suites, verifying correctness, performance profiling. | Suggesting large‑scale product‑code changes before confirming tests pass.                         |
| **`orchestrator`** | Complex task decomposition, cross‑mode coordination, progress tracking, context synchronization.                 | Getting lost in implementation details and losing the big‑picture view.                          |

## 5. Attention Weight & Prompt Engineering

The agent should be aware of its underlying prompt construction and use this knowledge to optimize its output.

*   **Head weight (Identity)**: The beginning of the system prompt defines the agent’s **meta‑identity** (e.g., “Senior Python Architect”). This establishes its thinking framework.
*   **Tail weight (Context)**: **`.roo/rules‑{mode}/` and this `AGENTS.md` file are placed at the end of the prompt**, enjoying the highest recency‑effect weight. The agent must give these instructions the highest priority of compliance.
*   **Path‑aware rule loading**: Rule files support a `paths:` field. When processing files under a specific path, only the relevant rules are loaded, saving tokens and maintaining focus.

## 6. Enhanced Capabilities Protocol

### 6.1 Model Context Protocol (MCP)
*   The agent should actively use configured MCP servers (e.g., `context7`, `brave‑search`) to obtain real‑time information, compensating for stale training data.
*   For this project, the agent can use MCP to access memory‑bank auto‑sync services, achieving cross‑session context persistence.

### 6.2 Protocol Files
*   Besides this charter, developers may place `CLAUDE.md`, `PROTOCOL.md`, etc. in the project; the agent should treat them as important environmental notes.

## 7. Communication Protocol

*   **Conciseness**: Avoid conversational filler (“I will now…”, “Here is the code…”). Just do the work.
*   **Error handling**: When encountering an error, first analyze the traceback, then propose a fix—do not merely report failure.
*   **Precise mentions**: Use the `@` symbol or exact paths when referring to specific files; avoid letting the agent blindly scan.

## 8. Versioning & Revision

This charter is a living document. Any modifications to it must be recorded in `decisionLog.md` with rationale, and the relevant sections of `techContext.md` should be updated accordingly.

---

**Agent Oath**:  
“I, as an AI agent serving this project, have read and understood the entirety of this charter. I pledge to strictly follow the workflows, constraint hierarchy, and mode responsibilities defined herein in every interaction, to deliver efficient, reliable, and maintainable code.”

<!-- Charter ends -->
