import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


class TestRootEndpoint:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert "message" in data


class TestHealthEndpoint:
    def test_health_check(self):
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert "timestamp" in data
        assert "version" in data
        assert isinstance(data["timestamp"], float)


class TestEchoEndpoint:
    def test_echo_valid_message(self):
        payload = {"message": "Hello, World!"}
        response = client.post("/echo", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["echo"] == "Hello, World!"
        assert data["length"] == 13
        assert "timestamp" in data

    def test_echo_empty_message(self):
        payload = {"message": ""}
        response = client.post("/echo", json=payload)
        assert response.status_code == 422  # Validation error

    def test_echo_whitespace_message(self):
        payload = {"message": "   "}
        response = client.post("/echo", json=payload)
        assert response.status_code == 400
        assert "cannot be empty" in response.json()["error"]["message"]

    def test_echo_long_message(self):
        long_message = "a" * 501  # Exceeds max_length
        payload = {"message": long_message}
        response = client.post("/echo", json=payload)
        assert response.status_code == 422

    def test_echo_missing_message(self):
        response = client.post("/echo", json={})
        assert response.status_code == 422


class TestVersionEndpoint:
    def test_get_version(self):
        response = client.get("/version")
        assert response.status_code == 200
        data = response.json()
        assert "version" in data
        assert "name" in data
        assert data["version"] == "1.0.0"


class TestErrorHandling:
    def test_simulate_error(self):
        response = client.get("/error")
        assert response.status_code == 500
        data = response.json()
        assert "error" in data
        assert "status_code" in data

    def test_not_found(self):
        response = client.get("/nonexistent")
        assert response.status_code == 404


class TestCORS:
    def test_cors_headers(self):
        response = client.get("/", headers={"Origin": "http://localhost:3000"})
        assert response.status_code == 200
        assert "access-control-allow-origin" in response.headers


class TestMiddleware:
    def test_request_logging_middleware(self):
        # This test verifies the middleware doesn't break requests
        response = client.get("/")
        assert response.status_code == 200


@pytest.mark.asyncio
async def test_lifespan_events():
    # Test that the app can start and stop without errors
    # This is implicitly tested by the test client, but we can be explicit
    with TestClient(app) as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
