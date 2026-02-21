# Product Context

User stories, business logic, and Architecture Decision Records (ADR) for the project.

## User Stories
*(Example: “As a developer, I want to quickly bootstrap a new project with AI‑friendly constraints, so that I can focus on business logic rather than project setup.”)*

## Business Logic
*(Describe the core business rules and workflows that the project implements.)*

## Architecture Decision Records (ADR)

### ADR‑001: Project Structure
**Status**: Accepted  
**Date**: 2026‑02‑d  
**Decision**: Adopt the layered directory structure defined in `.clinerules` and `AGENTS.md`.  
**Alternatives**: Flat structure, monorepo.  
**Rationale**: Provides clear separation of concerns, enables path‑aware rule loading, and aligns with `deep research.md` best practices.  

### ADR‑002: Technology Stack
**Status**: Accepted  
**Date**: 2026‑02‑d  
**Decision**: Use Python 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0, pytest.  
**Alternatives**: Django, Flask, Tortoise‑ORM.  
**Rationale**: FastAPI offers modern async support, Pydantic provides strong validation, SQLAlchemy 2.0 is the industry‑standard ORM, pytest is the de‑facto testing framework.  

### ADR‑003: Memory‑Bank Pattern
**Status**: Accepted  
**Date**: 2026‑02‑d  
**Decision**: Implement a structured memory bank with eight Markdown files (projectContext.md, techContext.md, productContext.md, systemPatterns.md, activeContext.md, decisionLog.md, progress.md, archive.md).  
**Alternatives**: Rely solely on LLM context window, use external vector database.  
**Rationale**: Provides persistent, version‑controlled context that survives across sessions, reduces token consumption, and improves agent consistency.  

---

*New ADRs should be added here or in a separate `adr/` directory.*
