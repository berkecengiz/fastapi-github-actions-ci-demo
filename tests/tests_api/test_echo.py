from fastapi.testclient import TestClient
from starlette import status

from app.main import app

client = TestClient(app)

class TestEchoAPI:
    def test_echo_success(self):
        payload = {"message": "Hello, World!"}
        # Note the updated URL prefix
        response = client.post("/v1/echo", json=payload)
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"message": "Hello, World!"}

    def test_echo_missing_message(self):
        payload = {}
        response = client.post("/v1/echo", json=payload)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_echo_whitespace_message(self):
        payload = {"message": "   "}
        response = client.post("/v1/echo", json=payload)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
        response_json = response.json()
        assert (
            "Message cannot be empty or contain only whitespace"
            in response_json["detail"][0]["msg"]
        )

# You can keep the health check test in a separate file like tests/test_main.py

