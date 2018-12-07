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

    def test_add_user_invalid_json(self, client_fixture):
        """Ensure error is thrown if the JSON object is empty."""
        response = client_fixture.post(
            '/users',
            data=json.dumps({}),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Invalid payload' in data['message']
        assert 'fail', data['status']

    def test_add_user_invalid_json_keys(self, client_fixture):
        """
        Ensure error is thrown if the JSON object does not have a username keyself.
        """
        response = client_fixture.post(
            '/users',
            data=json.dumps({'email': 'loganjhennessy@gmail.com'}),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Invalid payload.' in data['message']
        assert 'fail', data['status']

    def test_add_user_duplicate_email(self, client_fixture, database_fixture):
        """Ensure error is thrown if the email already exists."""
        client_fixture.post(
            '/users',
            data=json.dumps({
                'username': 'logan',
                'email': 'loganjhennessy@gmail.com'
            }),
            content_type='application/json',
        )
        response = client_fixture.post(
            '/users',
            data=json.dumps({
                'username': 'logan',
                'email': 'loganjhennessy@gmail.com'
            }),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Sorry. That email already exists.' in data['message']
        assert 'fail', data['status']
