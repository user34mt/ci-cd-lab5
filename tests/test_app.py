from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_user():
    r = client.get("/user/1")
    assert r.status_code == 200