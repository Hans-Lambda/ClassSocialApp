from unittest.mock import patch, Mock

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
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.register_user = Mock(return_value=True)
        test_client = TestClient(app=app)
        result = test_client.post('/users', json=valid_user_data)
        assert result.status_code == 200

def test_given_invalid_email_the_user_must_not_be_registered_and_return_code_is_400():
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.register_user = Mock(return_value=False)
        test_client = TestClient(app=app)
        result = test_client.post('/users', json=valid_user_data)
        assert result.status_code == 400
