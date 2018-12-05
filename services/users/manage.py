# services/users/manage.py
from flask.cli import FlaskGroup

import pytest
import unittest

from api import app, db

cli = FlaskGroup(app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command()
def test():
    """Runs the pytest tests"""
    return pytest.main(['api/pytests'])


if __name__ == '__main__':
    cli()
