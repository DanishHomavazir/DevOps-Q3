import pytest 
from app.app import app

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
        'email': 'alice@example.com'
    })
    assert response.status_code == 200
    assert b"Thanks for registering, Alice!" in response.data

def test_register_missing_data(client):
    response = client.post('/register', data={
        'name': 'Bob'
    })
    assert response.status_code == 400
    assert b"Missing data" in response.data
