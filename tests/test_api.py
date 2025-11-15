"""Test API routes."""


def test_api_index(client):
    """Test API root endpoint."""
    response = client.get("/api/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Welcome to the API"
    assert "version" in data


def test_api_hello(client):
    """Test hello endpoint."""
    response = client.get("/api/hello/World")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Hello, World!"


def test_health_check(client):
    """Test health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
