# services/users/api/tests/test_users.py
import json

from api.models import User


def add_user(db, username, email):
    """Helper function to add a single user to the database."""
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return user


class TestUserService(object):
    """Tests for the Users Service."""

    def test_users(self, client):
        """Ensure the /ping route behaves correctly."""
        client = client
        response = client.get('/users/ping')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'pong!' in data['message']
        assert 'success' in data['status']

    def test_add_user(self, client, db):
        """Ensure a new user can be added to the database."""
        response = client.post(
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

    def test_add_user_invalid_json(self, client):
        """Ensure error is thrown if the JSON object is empty."""
        response = client.post(
            '/users',
            data=json.dumps({}),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Invalid payload' in data['message']
        assert 'fail', data['status']

    def test_add_user_invalid_json_keys(self, client):
        """Ensure error is thrown if JSON object doesn't have a username key"""
        response = client.post(
            '/users',
            data=json.dumps({'email': 'loganjhennessy@gmail.com'}),
            content_type='application/json',
        )
        data = json.loads(response.data.decode())
        assert response.status_code == 400
        assert 'Invalid payload.' in data['message']
        assert 'fail', data['status']

    def test_add_user_duplicate_email(self, client, db):
        """Ensure error is thrown if the email already exists.

        Passing in the db recreates the database and instantiates
        the appropriate tables which is required for this test to pass.
        """
        client.post(
            '/users',
            data=json.dumps({
                'username': 'logan',
                'email': 'loganjhennessy@gmail.com'
            }),
            content_type='application/json',
        )
        response = client.post(
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

    def test_single_user(self, client, db):
        """Ensure get single user behaves correctly.

        Passing in the db fixture recreates the database and instantiates
        the appropriate tables which is required for this test to pass.
        """
        user = add_user(db, 'logan', 'loganjhennessy@gmail.com')
        response = client.get(f'/users/{user.id}')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert 'logan' in data['data']['username']
        assert 'loganjhennessy@gmail.com' in data['data']['email']
        assert 'success' in data['status']

    def test_single_user_no_id(self, client):
        """Ensure error is thrown if an id is not provided."""
        response = client.get('/users/blerg')
        data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'User does not exist' in data['message']
        assert 'fail' in data['status']

    def test_single_user_incorrect_id(self, client):
        """Ensure error is thrown if the id does not exist."""
        response = client.get('/users/42')
        data = json.loads(response.data.decode())
        assert response.status_code == 404
        assert 'User does not exist' in data['message']
        assert 'fail' in data['status']

    def test_all_users(self, client, db):
        """Ensure get all users behaves correctly.

        Passing in the db fixture recreates the database and instantiates
        the appropriate tables which is required for this test to pass.
        """
        add_user(db, 'logan', 'loganjhennessy@gmail.com')
        add_user(db, 'rick', 'rick@iamapickle.blorg')
        response = client.get('/users')
        data = json.loads(response.data.decode())
        assert response.status_code == 200
        assert len(data['data']['users']) == 2
        assert 'logan' in data['data']['users'][0]['username']
        assert 'loganjhennessy@gmail.com' in data['data']['users'][0]['email']
        assert 'rick', data['data']['users'][1]['username']
        assert 'rick@iamapickle.blorg' in data['data']['users'][1]['email']
        assert 'success' in data['status']

    def test_main_no_users(self, client):
        """Ensure the main route behaves correctly when no users have been
        added to the database."""
        response = client.get('/')
        assert response.status_code == 200
        assert b'All Users' in response.data
        assert b'<p>No users!</p>' in response.data

    def test_main_with_users(self, client, db):
        """Ensure the main route behaves correctly when users have been
        added to the database."""
        add_user(db, 'michael', 'michael@mherman.org')
        add_user(db, 'fletcher', 'fletcher@notreal.com')
        with client:
            response = client.get('/')
            assert response.status_code == 200
            assert b'All Users' in response.data
            assert b'<p>No users!</p>' not in response.data
            assert b'michael' in response.data
            assert b'fletcher' in response.data
