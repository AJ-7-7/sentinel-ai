
from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_home_returns_project_information():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["project"] == "SentinelAI"
    assert data["status"] == "running"
    assert data["version"] == "0.1.0"


def test_health_check_returns_healthy():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_unknown_endpoint_returns_404():
    response = client.get("/does-not-exist")

    assert response.status_code == 404
