import pytest

from fastapi.testclient import TestClient

from class_social.main import app


valid_user_data = {
    'name': 'Franz',
    'age': 36,
    'email': 'email@example.cum',
    'password': 'fucktypos'
}


def test_given_valid_user_data_the_system_must_register_the_user_and_return_200_ok():
    test_client = TestClient(app=app)
    result = test_client.post('/users', json=valid_user_data)
    assert result.status_code == 200
