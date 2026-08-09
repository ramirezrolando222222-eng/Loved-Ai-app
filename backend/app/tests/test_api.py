from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Loved AI"
    assert data["status"] == "online"


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_create_profile():
    profile = {
        "id": "demo-user-001",
        "name": "Maya",
        "age": 27,
        "location": "Houston, TX",
        "bio": "Music, travel, and good conversation.",
        "interests": [
            "Music",
            "Travel",
            "Food"
        ]
    }

    response = client.post(
        "/api/profiles",
        json=profile,
    )

    assert response.status_code == 200

    data = response.json()

    assert data["success"] is True
    assert data["profile"]["name"] == "Maya"
