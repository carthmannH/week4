import pytest
from myapp import app

@pytest.fixture
def client():
    """Create a test client using Flask application."""
    with app.test_client() as client:
        yield client

def test_home_page(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Welcome to My App' in response.data

def test_account_page(client):
    """Test the account page."""
    response = client.post('/account', data={'name': 'John'})
    assert response.status_code == 200
    assert b'Hello, John!' in response.data

def test_invalid_account_page(client):
    """Test the account page with invalid input."""
    response = client.post('/account', data={'name': ''})
    assert response.status_code == 200
    assert b'Hello, User Not Defined!' in response.data

if __name__ == '__main__':
    pytest.main()
