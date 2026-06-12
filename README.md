# enterprise-ai-ops-copilot

Phase 1 establishes the production foundation for the backend:

- Python 3.12 application scaffold
- FastAPI package layout
- Pydantic settings and environment-based configuration
- Async SQLModel database wiring for PostgreSQL
- Redis and Qdrant client setup
- Alembic migration bootstrap
- Docker-ready local dependency stack

## Local development

1. Copy `.env.example` to `.env`.
2. Start infrastructure with `docker compose up -d`.
3. Install dependencies with `pip install -r requirements.txt`.
4. Run the API with `uvicorn app.main:app --reload`.

## Migrations

- Create a revision: `alembic revision --autogenerate -m "message"`
- Apply migrations: `alembic upgrade head`
