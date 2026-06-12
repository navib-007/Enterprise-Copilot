from fastapi.testclient import TestClient

from app.main import app


def test_openapi_endpoint_is_available() -> None:
    client = TestClient(app)

    response = client.get("/api/v1/openapi.json")

    assert response.status_code == 200


def test_docs_endpoint_is_available() -> None:
    client = TestClient(app)

    response = client.get("/docs")

    assert response.status_code == 200
