# services/users/api/tests/test_users.py
import json


class TestUserService(object):
    """Tests for the Users Service."""

    def test_users(self, client_fixture):
        """Ensure the /ping route behaves correctly."""
        client = client_fixture
        response = client.get('/users/ping')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'pong!' in data['message']
        assert 'success' in data['status']

    def test_add_user(self, client_fixture, database_fixture):
        """Ensure a new user can be added to the database."""
        response = client_fixture.post(
            '/users',
            data=json.dumps({
                'username': 'logan',
                'email': 'loganjhennessy@gmail.com'
            }),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 201
        assert 'loganjhennessy@gmail.com was added!' in data['message']
        assert 'success' in data['status']
