# services/users/api/tests/test_users.py
import json

from api.models import User


def add_user(database_fixture, username, email):
    """Helper function to add a single user to the database."""
    user = User(username=username, email=email)
    database_fixture.session.add(user)
    database_fixture.session.commit()
    return user


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
        """Ensure error is thrown if JSON object doesn't have a username key."""
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
        """Ensure error is thrown if the email already exists.

        Passing in the database_fixture recreates the database and instantiates
        the appropriate tables which is required for this test to pass.
        """
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

    def test_single_user(self, client_fixture, database_fixture):
        """Ensure get single user behaves correctly.

        Passing in the database_fixture recreates the database and instantiates
        the appropriate tables which is required for this test to pass.
        """
        user = add_user(database_fixture, 'logan', 'loganjhennessy@gmail.com')
        response = client_fixture.get(f'/users/{user.id}')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'logan' in data['data']['username']
        assert 'loganjhennessy@gmail.com' in data['data']['email']
        assert 'success' in data['status']

    def test_single_user_no_id(self, client_fixture):
        """Ensure error is thrown if an id is not provided."""
        response = client_fixture.get('/users/blerg')
        data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'User does not exist' in data['message']
        assert 'fail' in data['status']

    def test_single_user_incorrect_id(self, client_fixture):
        """Ensure error is thrown if the id does not exist."""
        response = client_fixture.get('/users/42')
        data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'User does not exist' in data['message']
        assert 'fail' in data['status']

    def test_all_users(self, client_fixture, database_fixture):
        """Ensure get all users behaves correctly.

        Passing in the database_fixture recreates the database and instantiates
        the appropriate tables which is required for this test to pass.
        """
        add_user(database_fixture, 'logan', 'loganjhennessy@gmail.com')
        add_user(database_fixture, 'rick', 'rick@iamapickle.blorg')
        response = client_fixture.get('/users')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']['users']) == 2
        assert 'logan' in data['data']['users'][0]['username']
        assert 'loganjhennessy@gmail.com' in data['data']['users'][0]['email']
        assert 'rick', data['data']['users'][1]['username']
        assert 'rick@iamapickle.blorg' in data['data']['users'][1]['email']
        assert 'success' in data['status']
