# System Architecture and Execution Plan

## 1. Project Directory Structure (Hexagonal/Modular Architecture)

```text
.
├── .roo/                  # Memory Bank (Context, patterns, decisions)
├── scripts/               # Utility scripts & documents
├── src/                   # Source code
│   ├── api/               # [I/O Layer] FastAPI endpoints (`endpoints.py`)
│   ├── core/              # [Domain Layer] Core logic
│   │   ├── models/        # Pydantic schemas (`api_models.py`)
│   │   ├── qnmh/          # QNMH Logic (Algorithm implementation)
│   │   │   ├── solver.py  # Abstract solver interface
│   │   │   └── nx_impl.py # NetworkX implementation prototype
│   │   └── pri/           # PRI scoring logic (`calculator.py`)
│   ├── infrastructure/    # [Data & Compute Layer]
│   │   └── compute/       # Async Task execution (`manager.py`, `tasks.py`)
│   └── tests/             # Pytest suites (`test_api.py`, `test_core.py`)
├── environment.yml        # Mamba/Conda environment definition
├── pyproject.toml         # Build system and tool configurations
├── README.md              # Project documentation and usage guide
└── src/main.py            # FastAPI application entry point
```

## 2. Architectural Refinements (Bioinformatics Context)
1. **Compute Intensive Dispatching**: QNMH calculations are offloaded to independent processes using `ProcessPoolExecutor` managed by `TaskManager` (`src/infrastructure/compute/manager.py`) to avoid blocking the FastAPI event loop.
2. **Data Structure Optimizations**: Pydantic is used for API payload validation. The infrastructure layer prepares to handle large adjacency matrices.
3. **Graph Engine Interchangeability**: The `core/qnmh` module defines an abstract solver interface (`solver.py`). The initial prototype uses `networkx`.

## 3. Execution Plan (Completed)

### Step 1: Environment Setup (✅ Done)
- Created `environment.yml` and `pyproject.toml` with dependencies: Python 3.11, FastAPI, Pydantic, NetworkX, NumPy, Pytest.

### Step 2: Core Domain Implementation (✅ Done)
- Defined Pydantic models for API transmission (`TaskSubmitRequest`, `TaskStatusResponse`).
- Implemented the QNMH abstract solver (`QNMHSolver`) and NetworkX prototype (`NetworkXQNMHSolver`).
- Implemented PRI scoring algorithm (`calculate_pri`).

### Step 3: Data Loaders and Infrastructure (✅ Done)
- Implemented the `TaskManager` class using `ProcessPoolExecutor` for asynchronous, non-blocking CPU-bound task execution.
- Created `run_qnmh_analysis` wrapper task.

### Step 4: API Layer (✅ Done)
- Designed asynchronous API endpoints in `src/api/endpoints.py`:
  - `POST /analysis/qnmh` -> Accepts file paths, returns `task_id` (202 Accepted).
  - `GET /analysis/qnmh/{task_id}` -> Polling endpoint for status/results.

### Step 5: Testing & Validation (✅ Done)
- Wrote pytest suites testing core logic (`test_core.py`) and API endpoints using `TestClient` (`test_api.py`).
