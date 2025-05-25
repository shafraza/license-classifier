from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_licenses():
    response = client.get("/licenses")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_summary():
    response = client.get("/summary")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
