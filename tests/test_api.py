import requests

BASE_URL = "http://127.0.0.1:8000"


def test_health():

    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_chat():

    response = requests.post(f"{BASE_URL}/recommend",
        json={
            "query": "Need Python Developer assessment"
        }
    )

    assert response.status_code == 200
    body = response.json()
    
    assert "reply" in body
    assert "recommendations" in body