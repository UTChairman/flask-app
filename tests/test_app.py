import pytest
from app import app

@pytest.fixture
def client():
    # Flask provides a test client for simulating requests
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_about_route(client):
    response = client.get('/about')
    assert response.status_code == 200
    assert b"This is the About page!" in response.data
