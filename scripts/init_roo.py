#!/usr/bin/env python3
"""
Roo Code Project Scaffolder

Creates the directory structure and core files for a new project
or migrates an existing project to the "Roo Code Rules" architecture.

Usage:
    python3 scripts/init_roo.py [--dry-run] [--backup]

Options:
    --dry-run    Print actions without executing.
    --backup     Backup existing files before overwriting.
"""

import argparse
import sys
import os
import shutil
from pathlib import Path
from datetime import datetime

# ----------------------------------------------------------------------
# Template strings
# ----------------------------------------------------------------------

AGENTS_MD = """# Roo Code Agent Charter (Agents Charter)

**Effective Date**: {date}
**Authority Level**: **Vital** (Highest) — This file has the highest binding power in this project.

## 1. Charter Purpose

This charter defines the **core behavioral guidelines, workflows, and responsibility boundaries** for the AI agent (Roo Code) working in this project. Its purpose is to translate the advanced architectural theories from `deep research.md` into executable, mandatory protocols, ensuring the agent achieves best practices in **constraint systems, weight distribution, and high‑efficiency orchestration**.

## 2. Hierarchy of Constraints

The agent must resolve and apply instructions in the following priority order (highest to lowest):

1.  **`AGENTS.md` (this file)** — **Vital** — Team‑standardized agent charter.
2.  **`.roo/rules‑{{mode}}/`** — **Critical** — Project‑specific **mode‑specific** fine‑grained rules (e.g., `.roo/rules‑architect/planning.md`).
3.  **`.roo/rules/`** — **High** — Project‑wide **general** rules (e.g., coding standards, security).
4.  **`.clinerules`** — **Supplemental** — Traditional single‑file constraint protocol, mainly used for legacy support or quick adjustments.
5.  Global rules (`~/.roo/rules‑{{mode}}/`, `~/.roo/rules/`, system prompts) — **Medium/Low** — Default rules for all projects.

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
2.  **Load mode rules**: Automatically load the corresponding `.roo/rules‑{{mode}}/` rule files, which are placed at the **end** of the prompt, enjoying the highest recency‑effect weight.
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
*   **Tail weight (Context)**: **`.roo/rules‑{{mode}}/` and this `AGENTS.md` file are placed at the end of the prompt**, enjoying the highest recency‑effect weight. The agent must give these instructions the highest priority of compliance.
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
"""

CLINERULES_MD = """# Roo Code Constitution (Constitution) – High‑Efficiency Edition

**Effective Date**: {date}
**Authority Level**: **Supplemental** (Supplemental) – This file is a guiding constraint for the project; the highest authority belongs to `AGENTS.md`.

---

## 1. Core Identity & Style

- **Role**: Senior Python Architect
- **Language**: zh‑CN (prefer Chinese for communication with developers)
- **Style**: Clean, Modern, 12‑Factor App

## 2. Package & Environment Management (Absolute Prohibition of Violations)

- **Tool**: `mamba` (direct use of `pip` is forbidden)
- **Target Environment**: "jitian-intelligence"
- **Manifest**: `environment.yml` (single source of truth)
- **Rules**:
  1. ❌ **FORBIDDEN**: `pip install <package>` is never allowed under any circumstances.
  2. ✅ **REQUIRED**: Adding/updating dependencies must execute `mamba env update --file environment.yml --prune`.
  3. ⚠️ **VERSIONING**: All dependencies must be pinned to exact versions (e.g., `pandas=2.1.0`).

## 3. Memory Bank Workflow (Mandatory)

The agent must perform the following actions **at the start of each session**:

### 3.1 On Start
1. Read static context:
   - `.roo/projectContext.md` – High‑level project goals & design philosophy
   - `.roo/techContext.md` – Tech stack, database schema, API specifications
   - `.roo/productContext.md` – User stories, business logic, ADRs
   - `.roo/systemPatterns.md` – System architectural patterns & design principles
2. Read dynamic context:
   - `.roo/activeContext.md` – Current task progress, to‑do items (must read first!)
   - (optional) `.roo/progress.md` – Project milestones
   - (optional) `.roo/decisionLog.md` – Recent key decisions

### 3.2 On Finish
1. Update `.roo/activeContext.md`, recording this session’s progress, new to‑do items, encountered problems.
2. If this session made an important technical decision, append it to `.roo/decisionLog.md`.
3. Maintain **Tail Strategy**: If `activeContext.md` contains more than 5 entries, move the oldest completed tasks to `.roo/archive.md`.

## 4. Tech Stack (Non‑Negotiable)

- **Language**: Python 3.11+
- **Framework**: FastAPI
- **Data Validation**: Pydantic v2 (Strict mode)
- **Database**: SQLAlchemy 2.0 (Async) / SQLModel
- **Testing**: pytest + pytest‑asyncio

## 5. Coding Standards

- **Architecture**: Hexagonal / Modular Architecture, strict layering.
- **File Size**: A single source‑code file must not exceed **200 lines**; refactor immediately if exceeded.
- **Type Hints**: All functions, methods must have complete type hints; **the use of `Any` is prohibited**.
- **Security**:
  - Configuration must be loaded via environment variables (use `pydantic‑settings`).
  - **Never hard‑code** secrets, passwords, or other sensitive information.
  - The `.env` file must be excluded by `.gitignore` and never committed.

## 6. Process Control

The agent must work in the following four‑step cycle:

1. **Step 1: Read Context** – Execute all reading operations from `3.1 On Start`.
2. **Step 2: TDD** – Write tests first (Red) → minimal implementation (Green) → Refactor.
3. **Step 3: Refactor & Type Check** – Ensure code complies with `5. Coding Standards`.
4. **Step 4: Update Memory Bank** – Execute the update operations from `3.2 On Finish`.

## 7. Hierarchy of Constraints

The agent must follow the following priority (highest to lowest):

1. **`AGENTS.md`** – Supreme charter (team standard)
2. **`.roo/rules‑{{mode}}/`** – Mode‑specific rules (e.g., `.roo/rules‑architect/planning.md`)
3. **`.roo/rules/`** – Project‑wide general rules (e.g., `.roo/rules/coding‑standards.md`)
4. **`.clinerules`** – This file (supplemental guidance)
5. Global rules (user‑directory rule files)

**Conflict resolution**: higher‑level files override lower‑level files.

## 8. Directory Structure (Key Paths)

- **`.roo/`** – AI memory bank (contains `activeContext.md`, `projectContext.md`, `techContext.md`, `productContext.md`, `systemPatterns.md`, `decisionLog.md`, `progress.md`, `archive.md`, `rules/`, `rules‑{{mode}}/`)
- **`AGENTS.md`** – Supreme charter
- **`.clinerules`** – This file (guidance)
- **`.env.example`**, **`environment.yml`** – Environment configuration
- **`README.md`** – Project entry point
- **`docs/`** – User guides
- **`app/`**, **`tests/`** – Source code & tests (detailed structure see `techContext.md`)

## 9. Critical Bootstrap Instruction

**Before you reply to the user’s first message, you must**:

1. Check whether `.roo/activeContext.md` exists.
2. **If it exists**: Immediately read it together with `projectContext.md`, `techContext.md`, `systemPatterns.md` to restore context.
3. **If it does not exist**: Initialize the `.roo/` directory according to the structure in Section 8 and create the basic memory‑bank files.

## 10. Communication Protocol

- **Conciseness**: Avoid conversational filler (“I will now…”, “Here is the code…”). Just do the work.
- **Error handling**: When encountering an error, first analyze the traceback, then propose a fix—do not simply report failure.
- **Precise mentions**: Use the `@` symbol or exact paths to refer to files; avoid letting the agent blindly scan.

---

**Constitutional Oath**:  
“I, as an AI agent serving this project, have read and understood the entirety of this constitution. I pledge to strictly follow its defined workflows, tech stack, and coding standards in every interaction, and to respect the hierarchy of constraints.”

<!-- This file is pure Markdown, designed to provide high‑weight, distraction‑free instructions for the LLM. -->
"""

SYSTEM_PATTERNS_MD = """# System Architectural Patterns (System Patterns)

This document records **architectural patterns, design principles, and core class relationships** that recur in this project (`Roo code rules`) and are worth solidifying. It is the agent’s “design handbook”, ensuring consistency of architectural decisions.

## 1. Constraint Hierarchy Pattern

### Pattern Description
The agent’s behavior is controlled by a multi‑layer set of rule files, with priority from high to low:
1. `AGENTS.md` (Vital)
2. `.roo/rules‑{{mode}}/` (Critical)
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
- **Tail**: Mode‑specific rules (`.roo/rules‑{{mode}}/`) and `AGENTS.md` have the highest recency‑effect weight.

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
"""

PROGRESS_MD = """# Project Milestones (Progress)

This document tracks key milestones and current phases of the project. Uses **Goal‑Outcome‑Status** format.

## Milestone 1: Project Initialization & Rule Definition
- **Goal**: Establish basic project structure, memory bank, and `.clinerules`.
- **Outcome**: Completed creation of directories `.roo/`, `app/`, `tests/`; `.clinerules` contains full workflow definition.
- **Status**: ✅ Completed ({date})

## Milestone 2: Deep Research & Architectural Optimization
- **Goal**: Based on the findings in `deep research.md`, restructure the project to practice “constraint systems, weight distribution, and high‑efficiency orchestration”.
- **Outcome**:
  - Created `AGENTS.md` as the top‑level charter.
  - Established layered rule directories (`.roo/rules/`, `.roo/rules‑{{mode}}/`).
  - Expanded memory bank (added `systemPatterns.md`, `decisionLog.md`, `progress.md`).
  - Archived scattered documentation into `docs/`.
  - Updated `.clinerules` to reflect the expanded memory bank.
  - Updated `README.md` to describe the new structure.
- **Status**: ✅ Completed ({date})

### Completed Subtasks
- [x] Write optimization plan `optimization_plan.md`
- [x] Create `AGENTS.md`
- [x] Create `.roo/rules/coding‑standards.md`
- [x] Create `.roo/rules/security.md`
- [x] Create `.roo/rules‑architect/planning.md`
- [x] Create `.roo/systemPatterns.md`
- [x] Create `.roo/progress.md` (this document)
- [x] Create `.roo/decisionLog.md`
- [x] Update `.clinerules` to reflect the expanded memory bank
- [x] Update `README.md` to describe the new structure
- [x] Run integrity check (directory structure, file links)

## Milestone 3: Example Code Implementation
- **Goal**: Provide a small but complete example (e.g., user‑authentication module) under `app/` to demonstrate the practical application of rules and memory bank.
- **Outcome**: Deliver a runnable FastAPI service containing models, services, API routes, and full test suite.
- **Status**: ⭕ Not Started

## Milestone 4: Documentation & Training Material
- **Goal**: Produce final user guides and training materials, making this project a template for Roo Code best practices.
- **Outcome**: The `docs/` directory contains complete Chinese/English guides, video‑tutorial links.
- **Status**: ⭕ Not Started

---

*This document is updated by the agent each time a milestone advances. Please add new entries using the “Goal‑Outcome‑Status” format.*
"""

DECISION_LOG_MD = """# Decision Log (Decision Log)

This document records **key technical decisions** and their rationale in this project. Its purpose is to avoid repeated discussion, maintain decision transparency, and provide context for future maintenance.

## Decision Record Format

Each decision entry should contain the following fields:
- **Decision ID**: `DL‑001`
- **Date**: YYYY‑MM‑DD
- **Decision Maker**: Who made this decision (e.g., “Architect‑mode AI”, “Project Lead”)
- **Problem Description**: The specific problem to be solved
- **Option Analysis**: Considered alternatives and their pros/cons
- **Final Decision**: Chosen solution
- **Rationale**: Why this solution was chosen
- **Impact Scope**: Which modules or files this decision will affect
- **Status**: ✅ Implemented / 🟡 In Progress / ⭕ Not Started

---

## DL‑001: Adopt Layered Rule Directory Structure
- **Date**: 2026‑02‑14
- **Decision Maker**: Architect‑mode AI (based on `deep research.md` analysis)
- **Problem Description**: The original single‑file `.clinerules` model cannot achieve fine‑grained constraint layering, causing global and project rules to be confused and making it difficult to tailor behavior for different modes (architect/code/debug).
- **Option Analysis**:
  1. **Keep single‑file `.clinerules`**: Simple, but not extensible, weight management difficult.
  2. **Adopt layered directories `.roo/rules/` and `.roo/rules‑{{mode}}/`**: Aligns with the “Constraint Hierarchy” theory from `deep research.md`, supports path‑awareness, weight optimization, but increases initial setup complexity.
- **Final Decision**: Adopt option 2 (layered rule directory structure).
- **Rationale**:
  - Consistent with the advanced architectural theory in `deep research.md`, making this project a demonstration of best practices.
  - Resolves rule conflicts through layer priority, improving agent‑behavior predictability.
  - Path‑aware rule loading saves tokens and increases focus.
- **Impact Scope**:
  - Project root: need to create `AGENTS.md` as the supreme charter.
  - `.roo/` directory: add sub‑directories `rules/`, `rules‑architect/`, `rules‑code/`, `rules‑debug/`.
  - `.clinerules`: part of its content will be moved to layered rule files, but its role as a bootstrap file is retained.
- **Status**: ✅ Implemented

## DL‑002: Expand Memory‑Bank File Set
- **Date**: 2026‑02‑14
- **Decision Maker**: Architect‑mode AI
- **Problem Description**: The original memory bank only contained `activeContext.md`, `productContext.md`, `projectContext.md`, `techContext.md`, `archive.md`, lacking dedicated records for architectural patterns, project progress, and decision history.
- **Option Analysis**:
  1. **Keep as‑is**: Simple, but cannot achieve the full “long‑term memory” capability described in `deep research.md`.
  2. **Add `systemPatterns.md`, `decisionLog.md`, `progress.md`**: Complete the memory‑bank pattern, but increases file count and maintenance burden.
- **Final Decision**: Adopt option 2 (expand memory‑bank file set).
- **Rationale**:
  - Matches the “structured memory bank” description in `deep research.md`, enhancing the agent’s awareness of project history.
  - `systemPatterns.md` can solidify design experience, speeding up future similar problem solving.
  - `decisionLog.md` avoids decision repetition, improves team‑collaboration efficiency.
  - `progress.md` provides a clear view of project milestones, helping the agent grasp the current phase.
- **Impact Scope**:
  - Three new files under `.roo/` directory.
  - The startup workflow in `AGENTS.md` must be updated to include these new files.
  - The `memory_bank` section in `.clinerules` may need updated references (optional).
- **Status**: ✅ Implemented

## DL‑003: Archive Documentation into `docs/` Directory
- **Date**: 2026‑02‑14
- **Decision Maker**: Architect‑mode AI
- **Problem Description**: Multiple Chinese Markdown guide files (e.g., `干人事.md`, `测试套件使用.md`) were scattered in the project root, cluttering the root and not conforming to the norm that “protocol files” should be in prominent locations (like `AGENTS.md`).
- **Option Analysis**:
  1. **Leave in root**: Easy direct access, but harms clarity of directory structure.
  2. **Move to `docs/` subdirectory**: Keeps root minimal, follows common open‑source practice, but may require updating internal links (if any).
- **Final Decision**: Adopt option 2 (move to `docs/` subdirectory).
- **Rationale**:
  - The root directory should contain only the most critical project‑entry files (`README.md`, `.clinerules`, `AGENTS.md`, `environment.yml`).
  - The `docs/` directory is the standard location for user guides, development manuals.
  - As a best‑practice template, this project should exhibit good documentation‑organization habits.
- **Impact Scope**:
  - Create `docs/` directory.
  - Move `Roo Code 高效使用指南.md`, `干人事.md`, `测试套件使用.md` to `docs/` and rename to English (or keep Chinese) filenames.
  - Update links in `README.md` (if any).
- **Status**: ✅ Implemented

---

*New key decisions should continue to be appended in this format.*
"""

ACTIVE_CONTEXT_MD = """# Active Context

This file holds the current session state, to‑do items, and recent issues. It is the primary dynamic memory for the AI agent.

## Current Session
- **Started**: {date}
- **Agent Mode**: (auto‑detect)
- **User Request**: (to be filled by the agent)

## To‑Do List
- [ ] Read the memory‑bank files (projectContext.md, techContext.md, productContext.md, systemPatterns.md, activeContext.md, progress.md, decisionLog.md) to restore context.
- [ ] Execute the task defined by the user.
- [ ] Update this file with progress and new to‑do items.

## Recent Issues / Blockers
*(none yet)*

## Notes
- Keep this file lightweight. After 5 entries, archive old completed tasks to `archive.md`.
"""

TECH_CONTEXT_MD = """# Technical Context

This document describes the technical stack, database schema, API specifications, and development environment for the project.

## Technology Stack
- **Language**: Python 3.11+
- **Web Framework**: FastAPI
- **Data Validation**: Pydantic v2 (Strict mode)
- **Database ORM**: SQLAlchemy 2.0 (Async) / SQLModel
- **Testing**: pytest + pytest‑asyncio
- **Package Manager**: Mamba (environment.yml)
- **Environment Isolation**: Conda / Mamba

## Database Schema
*(To be filled with your project’s database models)*

## API Specifications
*(To be filled with your project’s API endpoints, request/response models)*

## Development Environment
1. Create environment from `environment.yml`:
   ```bash
   mamba env create -f environment.yml
   mamba activate <env_name>
   ```
2. Copy `.env.example` to `.env` and fill in secrets.
3. Run tests: `pytest`
4. Start development server: `uvicorn app.main:app --reload`

## Code Structure
```
app/
├── api/          # Route definitions (endpoints)
├── core/         # Core configuration (config, security, logging)
├── models/       # Database models (ORM / SQLModel)
├── schemas/      # Pydantic models (DTOs / interface contracts)
├── services/     # Business logic (service layer)
└── utils/        # Utility functions
tests/            # Test cases (pytest)
```

## Dependencies
See `environment.yml` for exact pinned versions.
"""

PROJECT_CONTEXT_MD = """# Project Context

High‑level goals, design philosophy, and overall vision of the project.

## Vision
*(Describe the ultimate goal of the project. Example: “Build a scalable, maintainable web‑service template that demonstrates best practices for AI‑assisted development with Roo Code.”)*

## Core Principles
1. **12‑Factor App**: Strict adherence to the twelve‑factor methodology.
2. **Clean Architecture**: Separation of concerns, dependency inversion.
3. **AI‑First Development**: Designed to be efficiently driven by AI agents through clear constraints and memory‑bank patterns.
4. **Modularity**: Each component should be replaceable and testable in isolation.

## Success Metrics
- [ ] All automated tests pass.
- [ ] Code follows the defined coding standards (type hints, no `Any`, file size ≤200 lines).
- [ ] Memory‑bank files are kept up‑to‑date and lightweight.
- [ ] The project can serve as a reusable template for new projects.

## Stakeholders
- **Developers**: Use this project as a reference for building AI‑assisted applications.
- **AI Agents (Roo Code)**: Follow the rules and workflows defined in `.clinerules` and `AGENTS.md`.

## Constraints
- Must work with Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0.
- Must use Mamba for dependency management; `pip install` is forbidden.
- Secrets must be stored in environment variables, never committed.

## Related Documents
- `deep research.md` – Theoretical foundation for the architecture.
- `optimization_plan.md` – Detailed plan for implementing the optimized structure.
- `AGENTS.md` – Supreme agent charter.
"""

PRODUCT_CONTEXT_MD = """# Product Context

User stories, business logic, and Architecture Decision Records (ADR) for the project.

## User Stories
*(Example: “As a developer, I want to quickly bootstrap a new project with AI‑friendly constraints, so that I can focus on business logic rather than project setup.”)*

## Business Logic
*(Describe the core business rules and workflows that the project implements.)*

## Architecture Decision Records (ADR)

### ADR‑001: Project Structure
**Status**: Accepted  
**Date**: {date}  
**Decision**: Adopt the layered directory structure defined in `.clinerules` and `AGENTS.md`.  
**Alternatives**: Flat structure, monorepo.  
**Rationale**: Provides clear separation of concerns, enables path‑aware rule loading, and aligns with `deep research.md` best practices.  

### ADR‑002: Technology Stack
**Status**: Accepted  
**Date**: {date}  
**Decision**: Use Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0, pytest.  
**Alternatives**: Django, Flask, Tortoise‑ORM.  
**Rationale**: FastAPI offers modern async support, Pydantic provides strong validation, SQLAlchemy 2.0 is the industry‑standard ORM, pytest is the de‑facto testing framework.  

### ADR‑003: Memory‑Bank Pattern
**Status**: Accepted  
**Date**: {date}  
**Decision**: Implement a structured memory bank with eight Markdown files (projectContext.md, techContext.md, productContext.md, systemPatterns.md, activeContext.md, decisionLog.md, progress.md, archive.md).  
**Alternatives**: Rely solely on LLM context window, use external vector database.  
**Rationale**: Provides persistent, version‑controlled context that survives across sessions, reduces token consumption, and improves agent consistency.  

---

*New ADRs should be added here or in a separate `adr/` directory.*
"""

# ----------------------------------------------------------------------
# Directory & file mapping
# ----------------------------------------------------------------------

FILE_MAP = {
    "AGENTS.md": AGENTS_MD,
    ".clinerules": CLINERULES_MD,
    ".roo/activeContext.md": ACTIVE_CONTEXT_MD,
    ".roo/projectContext.md": PROJECT_CONTEXT_MD,
    ".roo/techContext.md": TECH_CONTEXT_MD,
    ".roo/productContext.md": PRODUCT_CONTEXT_MD,
    ".roo/systemPatterns.md": SYSTEM_PATTERNS_MD,
    ".roo/decisionLog.md": DECISION_LOG_MD,
    ".roo/progress.md": PROGRESS_MD,
    ".roo/archive.md": "",
    ".roo/rules/coding-standards.md": "",
    ".roo/rules/security.md": "",
    ".roo/rules-architect/planning.md": "",
    ".roo/rules-code/": "",
    ".roo/rules-debug/": "",
    "docs/": "",
    ".env.example": "",
    "environment.yml": "",
    "README.md": "",
    "app/": "",
    "tests/": "",
}

# ----------------------------------------------------------------------
# Helper functions
# ----------------------------------------------------------------------

def log_action(msg, dry_run=False):
    prefix = "[DRY‑RUN] " if dry_run else ""
    print(f"{prefix}{msg}")

def ensure_directory(path, dry_run=False):
    if not path.exists():
        log_action(f"Create directory {path}", dry_run)
        if not dry_run:
            path.mkdir(parents=True, exist_ok=True)

def write_file(path, content, dry_run=False, backup=False):
    if path.exists() and backup:
        backup_path = path.with_suffix(path.suffix + ".bak")
        log_action(f"Backup {path} → {backup_path}", dry_run)
        if not dry_run:
            shutil.copy2(path, backup_path)
    log_action(f"Write {path}", dry_run)
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def create_rule_file(path, dry_run=False):
    """Create empty rule files if they don't exist."""
    if path.suffix == ".md" and not path.exists():
        log_action(f"Create empty rule file {path}", dry_run)
        if not dry_run:
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# {path.stem}\n\n*Define rules here.*")

def process_map(root_path, dry_run=False, backup=False):
    """Create directories and files according to FILE_MAP."""
    root = Path(root_path)
    date_str = datetime.now().strftime("%Y‑%m‑d")
    
    # Process each entry
    for rel_path, template in FILE_MAP.items():
        target = root / rel_path
        if template == "":  # directory or empty file
            if not rel_path.endswith(".md"):
                # It's a directory
                ensure_directory(target, dry_run)
            else:
                # Empty .md file – create placeholder
                if not target.exists():
                    log_action(f"Create empty file {target}", dry_run)
                    if not dry_run:
                        target.parent.mkdir(parents=True, exist_ok=True)
                        with open(target, "w", encoding="utf-8") as f:
                            f.write(f"# {target.stem}\n\n*Define content here.*")
        else:
            # Template content exists – fill with date
            content = template.format(date=date_str)
            write_file(target, content, dry_run, backup)

def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new Roo Code project or migrate existing project"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without executing"
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Backup existing files before overwriting"
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Target directory (default: current directory)"
    )
    args = parser.parse_args()
    
    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Error: Directory '{root}' does not exist.")
        sys.exit(1)
    
    print(f"Initializing Roo Code project in {root}")
    if args.dry_run:
        print("DRY‑RUN mode – no files will be modified.")
    
    try:
        process_map(root, dry_run=args.dry_run, backup=args.backup)
        print("✅ Scaffolding completed.")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()