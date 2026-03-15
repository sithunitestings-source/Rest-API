from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_project():
    response = client.post(
        "/projects", 
        json={"title": "Test Project", "description": "This is a test project", "status": "active"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test Project"
    assert "id" in data

def test_get_projects():
    response = client.get("/projects")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_project_not_found():
    response = client.get("/projects/9999")
    assert response.status_code == 404
