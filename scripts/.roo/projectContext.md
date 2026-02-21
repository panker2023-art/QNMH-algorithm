# Project Context

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
