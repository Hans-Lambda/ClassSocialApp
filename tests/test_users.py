from unittest.mock import patch, Mock
from fastapi.testclient import TestClient
from class_social.main import app
import pytest


# replaced by fixture

# valid_user_data = {
#     'name': 'Franz',
#     'age': 36,
#     'email': 'email@example.cum',
#     'password': 'fucktypos'
# }

# example for another fixture - check connection, return, then close

# yield returns value but doesn't finish function
# @pytest.fixture
# def db_connection():
#     db_conn = DBConnection('mysql://localhost/class_social')
#     yield db_conn
#     db_conn.close()

# pytest offers fixtures to replace certain parts of tests that are repeated frequently

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

# mock simulates register_user function and returns return_value
# so the test is tested
def test_given_valid_user_data_the_system_must_register_the_user_and_return_200_ok(test_client, valid_user_data):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.register_user = Mock(return_value=True)
        # test_client = TestClient(app=app) - replaced by fixture
        result = test_client.post('/users', json=valid_user_data)
        assert result.status_code == 200


def test_given_invalid_email_the_user_must_not_be_registered_and_return_code_is_400(test_client, valid_user_data):
    with patch('class_social.users.user_controller') as controller_mock:
        controller_mock.register_user = Mock(return_value=False)
        # test_client = TestClient(app=app) - replaced by fixture
        result = test_client.post('/users', json=valid_user_data)
        assert result.status_code == 400
