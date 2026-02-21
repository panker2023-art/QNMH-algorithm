# QNMH-algorithm
analyzing cross-species molecular networks for complex diseases like Alzheimer's

This repository contains the backend implementation for the Quantitative Network Motif Homology (QNMH) algorithm and the Precision Risk Index (PRI) evaluation system.

## Architecture

The project follows a Hexagonal/Modular architecture designed for compute-intensive bioinformatics tasks:

*   **`src/api/`**: FastAPI REST endpoints. All endpoints are fully asynchronous.
*   **`src/core/`**: Domain logic.
    *   `models/`: Pydantic schemas for request/response validation.
    *   `qnmh/`: Abstract solver interfaces and implementations (e.g., NetworkX).
    *   `pri/`: Calculation logic for the Precision Risk Index.
*   **`src/infrastructure/`**: Task compute and data management.
    *   `compute/`: `ProcessPoolExecutor` based asynchronous task manager to prevent blocking the web server event loop during large graph computations.
*   **`src/tests/`**: Pytest suites covering domain logic and API integration.

## Installation

### Using Conda/Mamba

1.  Create the environment from the provided file:
    ```bash
    mamba env create -f environment.yml
    ```
2.  Activate the environment:
    ```bash
    conda activate QNMH
    ```

### Using Pip

```bash
pip install -e ".[dev]"
```

## Running the Server

Start the FastAPI server using Uvicorn:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

You can then access the interactive API documentation at:
*   Swagger UI: http://localhost:8000/docs
*   ReDoc: http://localhost:8000/redoc

## Running Tests

Execute the test suite using pytest:

```bash
pytest
```

## Usage Example

### Submit a QNMH Analysis Task

```bash
curl -X 'POST' \
  'http://localhost:8000/analysis/qnmh' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "matrix_file_path": "/path/to/mouse_network.edgelist",
  "reference_network_path": "/path/to/human_network.edgelist",
  "metadata": {
    "genetic_robustness": 0.85,
    "toxicity_penalty": 0.1
  }
}'
```

This returns a `task_id` (HTTP 202 Accepted).

### Poll Task Status

```bash
curl -X 'GET' \
  'http://localhost:8000/analysis/qnmh/<YOUR_TASK_ID>' \
  -H 'accept: application/json'
```
