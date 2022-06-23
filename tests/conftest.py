import pytest
from fastapi.testclient import TestClient
from class_social.main import app


@pytest.fixture
def test_client():
    return TestClient(app=app)

@pytest.fixture
def valid_user_data():
    return {
        'name': 'Franz',
        'age': 36,
        'email': 'email@example.cum',
        'password': 'fucktypos'
    }