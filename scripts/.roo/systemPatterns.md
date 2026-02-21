# System Architectural Patterns (System Patterns)

This document records **architectural patterns, design principles, and core class relationships** that recur in this project (`Roo code rules`) and are worth solidifying. It is the agent’s “design handbook”, ensuring consistency of architectural decisions.

## 1. Constraint Hierarchy Pattern

### Pattern Description
The agent’s behavior is controlled by a multi‑layer set of rule files, with priority from high to low:
1. `AGENTS.md` (Vital)
2. `.roo/rules‑{mode}/` (Critical)
3. `.roo/rules/` (High)
4. `.clinerules` (Supplemental)
5. Global rules (Medium/Low)

### Usage Scenarios
- When you need to customize rules for a specific project or specific mode, create the corresponding layer‑level file instead of modifying global configuration.
- Conflict resolution: higher‑level overrides lower‑level.

### Example
- This project defines the architect‑mode specific process in `.roo/rules‑architect/planning.md`.

## 2. Memory Bank Workflow Pattern

### Pattern Description
The agent achieves “long‑term memory” through a set of structured Markdown files, with workflow:
1. **On start**: Read static context (`projectContext.md`, `techContext.md`, `productContext.md`, `systemPatterns.md`) and dynamic context (`activeContext.md`, `progress.md`, `decisionLog.md`).
2. **During execution**: Refer to design principles in `systemPatterns.md`.
3. **On finish**: Update dynamic context (`activeContext.md`, and `decisionLog.md` if needed).

### Usage Scenarios
- Any task that needs to maintain context across sessions.
- Complex project development, preventing the agent from “forgetting” earlier decisions.

## 3. Attention Weight Distribution Pattern

### Pattern Description
Leverage the LLM’s “primacy‑recency effect” to optimize prompt weight:
- **Head**: Role definition (Identity) establishes the thinking framework.
- **Tail**: Mode‑specific rules (`.roo/rules‑{mode}/`) and `AGENTS.md` have the highest recency‑effect weight.

### Usage Scenarios
- When writing rule files, place the most critical, most‑wanted‑to‑be‑followed instructions at the end of the file.
- Explicitly declare this pattern in `AGENTS.md` to guide the agent’s self‑optimization.

## 4. Mode Responsibility Separation Pattern

### Pattern Description
Split the agent’s work into separate modes, each with clear input/output boundaries:
- **`architect`** → produces plans, ADRs, directory structures.
- **`code`** → produces implementation code, tests.
- **`debug`** → produces problem diagnosis, fixes.

### Usage Scenarios
- Complex tasks should first be planned in `architect` mode, then split into atomic tasks for `code` mode, finally verified by `debug` mode.

## 5. Path‑Aware Rule Loading Pattern

### Pattern Description
Rule files support a `paths:` field, so that a rule is loaded only when the agent is processing files under a specific path, saving tokens and maintaining focus.

### Usage Scenarios
- Write separate rules for `src/backend/` and `src/frontend/` to isolate front‑end/back‑end conventions.

---

*This document should be continuously augmented as the project evolves. New architectural patterns should be recorded here as soon as they are identified.*
