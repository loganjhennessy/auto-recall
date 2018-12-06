# services/users/manage.py
from flask.cli import FlaskGroup

import pytest
import unittest

from api import create_app, db
from api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the pytest tests"""
    return pytest.main(['api/tests'])


if __name__ == '__main__':
    cli()
