import pytest
from fastapi.testclient import TestClient
from starlette import status

from app.main import app

client = TestClient(app)


class TestMain:
    def test_health_check(self):
        response = client.get("/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {"status": "ok"}
