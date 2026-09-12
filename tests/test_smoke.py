from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_page_is_available() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "FastAPI is ready" in response.text


def test_health_endpoint_is_ok() -> None:
    assert client.get("/health").json() == {"status": "ok"}
