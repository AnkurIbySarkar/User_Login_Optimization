from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_check_user_exists():
    response = client.get("/check/brute?email=alice@example.com")
    assert response.status_code == 200
    assert response.json() == {"exists": True}


def test_check_user_not_exists():
    response = client.get("/check/brute?email=nobody@example.com")
    assert response.status_code == 200
    assert response.json() == {"exists": False}
