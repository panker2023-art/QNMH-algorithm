# System Patterns

## Architectural Patterns
- **Hexagonal Architecture (Ports and Adapters)**:
  - **Core Domain**: The QNMH algorithm logic, network motive homology calculations, graph matching.
  - **Application Layer**: Services handling data ingestion (snRNA-seq matrix), preprocessing, pipeline orchestration.
  - **Adapters**: HTTP APIs (FastAPI), data loaders (reading from AnnData/CSV), external database connectivity (SQLAlchemy/SQLModel).
- **Modular Monolith**: Separation by functional domains (e.g. `gdi_matrix`, `grn_builder`, `qnmh_engine`, `pri_calculator`).

## Design Principles
- **Dependency Inversion**: Core algorithms must not depend on database or HTTP layers.
- **Pydantic Validation**: All data passing across module boundaries must be validated strictly via Pydantic v2 models. (Note: Pydantic is used strictly for API metadata and task control plane. Large matrices must use NumPy/SciPy/HDF5 data planes).
- **Async Execution**: Any IO-bound operations (API calls, DB queries) must be asynchronous.
- **File Size Constraint**: To ensure modularity, no single `.py` file can exceed 200 lines. Break down complex classes into smaller specialized components.

## Technical Decisions (ADR)
- *To be populated via decisionLog.md*