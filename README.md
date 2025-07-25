# Backend Practice - FastAPI

This repository contains an example FastAPI project located in `design/backend_practice_1`.
It demonstrates a simple modular structure with Dependency Injector and SQLAlchemy.

## Requirements

- Python 3.11+
- [Poetry](https://python-poetry.org/) for dependency management
- Optional: PostgreSQL database (the default connection URL can be modified in the settings)

## Installation

1. Navigate to the project directory:
   ```bash
   cd design/backend_practice_1
   ```
2. Install dependencies with Poetry:
   ```bash
   poetry install
   ```

## Running the Application

A helper script `start.sh` is provided. It sets the environment to `local` and launches the server with `uvicorn`:

```bash
./start.sh
```

This starts the API on `http://localhost:8000` with auto‑reload enabled.
You can also run it manually:

```bash
ENV=local uvicorn app.main:app --reload
```

## API Endpoints

The main application is defined in `app/main.py` and registers the following routes:

- `GET /healthcheck` – simple health check
- `GET /v1/item/{itemId}` – retrieve an item
- `POST /v1/item` – create an item
- `GET /v1/user/user_id/{userId}` – retrieve a user by ID
- `GET /v1/user/user_name/{userName}` – retrieve a user by name

The route mappings are configured in `app/api/route.py`.

## Configuration

Application settings are defined using Pydantic in `app/core/settings`. The environment is selected through the `ENV` variable (`local`, `dev`, `prod`, or `test`). Adjust database connection details in `app/core/settings/app.py` or the corresponding environment settings file.

## Project Structure

```
design/backend_practice_1/
├── app/
│   ├── api/                 # API routers
│   ├── core/                # Core configuration, containers, middleware
│   ├── db/                  # Database session and repositories
│   ├── models/              # ORM models and schemas
│   ├── services/            # Business logic
│   └── main.py              # FastAPI entry point
├── pyproject.toml           # Dependencies
├── poetry.lock              # Lock file
└── start.sh                 # Startup script
```

Visit `http://localhost:8000/docs` after starting the server to explore the automatically generated Swagger UI.
