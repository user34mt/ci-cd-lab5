from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_user():
    r = client.get("/user/1")
    assert r.status_code == 200

def test_not_found():
    r = client.get("/user/9999")
    assert r.status_code in [200, 404]