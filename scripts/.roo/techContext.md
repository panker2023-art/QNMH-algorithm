# Technical Context

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
