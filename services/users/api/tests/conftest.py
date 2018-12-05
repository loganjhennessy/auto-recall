import pytest

from api import app, db


@pytest.fixture()
def client_fixture():
    app.config.from_object('api.config.TestingConfig')
    return app.test_client()


@pytest.fixture()
def database_fixture():
    db.create_all()
    db.session.commit()
    yield
    db.session.remove()
    db.drop_all()
