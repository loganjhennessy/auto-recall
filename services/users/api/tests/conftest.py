"""users.api.tests.conftest.py

Fixtures created with the help of a very useful post
by Nelson Batalha https://spotofdata.com/flask-testing/
"""
import pytest

from api import create_app, db as _db


@pytest.yield_fixture(scope='session')
def app():
    _app = create_app()
    _app.config.from_object('api.config.TestingConfig')
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def db(app):
    _db.app = app
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope='function', autouse=True)
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session_ = db.create_scoped_session(options=options)

    db.session = session_

    yield session_

    transaction.rollback()
    connection.close()
    session_.remove()
