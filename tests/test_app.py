import sys
import os
import pytest

# Add the /app directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

from app import app  # ✅ import app.py inside app/ folder

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Register for the Event" in response.data

def test_register_success(client):
    response = client.post('/register', data={
        'name': 'Alice',
        'email': 'alice@example.com',
        'event': 'Tech Talk'
    })
    assert response.status_code == 200
    assert b"Thanks Alice for registering for Tech Talk!" in response.data

def test_register_missing_data(client):
    response = client.post('/register', data={
        'name': 'Bob'
    })
    assert response.status_code == 400
    assert b"Bad Request" in response.data  # Updated for actual Flask error
