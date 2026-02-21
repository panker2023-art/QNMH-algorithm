# Decision Log (Decision Log)

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
  2. **Adopt layered directories `.roo/rules/` and `.roo/rules‑{mode}/`**: Aligns with the “Constraint Hierarchy” theory from `deep research.md`, supports path‑awareness, weight optimization, but increases initial setup complexity.
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
