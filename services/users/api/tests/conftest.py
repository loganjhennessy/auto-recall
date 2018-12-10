import pytest

from api import create_app, db


@pytest.fixture()
def client_fixture():
    app = create_app()
    app.config.from_object('api.config.TestingConfig')
    client = app.test_client()
    yield client


@pytest.fixture()
def database_fixture():
    db.create_all()
    db.session.commit()
    yield db
    db.session.remove()
    db.drop_all()
