# test_app.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_docs_available():
    res = client.get("/docs")
    assert res.status_code == 200
