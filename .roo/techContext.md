# Tech Context

## Core Technologies
- **Language**: Python 3.11+
- **Framework**: FastAPI (for any web APIs/services)
- **Data Validation**: Pydantic v2 (Strict mode)
- **Database**: SQLAlchemy 2.0 (Async) / SQLModel
- **Testing**: pytest + pytest-asyncio

## QNMH Algorithm Tech Stack
- Data processing: Pandas, NumPy, SciPy
- Single-cell analysis and Gene Regulatory Network (GRN) construction: SCENIC, CellOracle integration, or equivalent Python bindings (e.g. Scanpy).
- Network Topology: NetworkX, igraph, or custom algorithms for structural isomorphism analysis.
- Machine Learning (optional/future): Scikit-learn (Random Forests), PyTorch/TensorFlow for Neural Network algorithms to extract pathogenic modules.

## Environment Management
- **Tool**: `mamba` (direct use of `pip install <package>` is forbidden)
- **Target Environment**: `jitian-intelligence`
- **Manifest**: `environment.yml`
- All dependencies must be pinned to exact versions. Updates must execute `mamba env update --file environment.yml --prune`.

## Code Quality Standards
- No `Any` type hints.
- Maximum 200 lines per file.
- Strict Pydantic models for data interchange.
