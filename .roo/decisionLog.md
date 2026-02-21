# Decision Log

| Date | Context | Decision | Rationale | Implications |
|---|---|---|---|---|
| 2026-02-21 | Project Initiation | Memory Bank initialized in root `.roo/` | Follows `.clinerules` and Agent Charter (`AGENTS.md`) for standard workflow. | Ensures AI continuity and context sharing across modes. |
| 2026-02-21 | Architecture | Hexagonal Architecture for Python | Segregates the core QNMH algorithm logic from data adapters (snRNA-seq APIs, database). | Ensures modularity and testability. Max 200 lines per file constraint will drive further fragmentation into micro-components. |
| 2026-02-21 | Architecture | Offload Compute Intensive Tasks | FastAPI route must dispatch calculations via `ProcessPoolExecutor` or Task Queue (e.g., Celery). | Prevents event loop blocking during heavy Motif/Isomorphism computation. API will follow async patterns (202 Accepted & Task ID). |
| 2026-02-21 | Architecture | Large Matrix Handling | Do not use Pydantic for matrices; use NumPy/SciPy sparse arrays and HDF5/AnnData representations. | Drastically reduces JSON serialization overhead. Pydantic is reserved purely for API request metadata. |
| 2026-02-21 | Architecture | Pydantic Boundary Strictness | Pydantic is strictly for API metadata and task control plane. Large matrices must use NumPy/SciPy/HDF5 data planes. | Eliminates ambiguity between "strict Pydantic everywhere" rule and performance needs for matrix computations. |
| 2026-02-21 | Architecture | Graph Library Agnostic | `core/qnmh/solver.py` will abstract the graph math logic. | Ensures we can swap `networkx` out for `igraph` or `rustworkx` when addressing performance bottlenecks for 5000+ node networks. |
