import os

from flask import current_app
from flask_testing import TestCase

from api import app


class TestDevelopmentConfig(object):
    def create_app(self):
        app.config.from_object('api.config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.create_app()
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert not (current_app is None)
        assert app.config['SQLALCHEMY_DATABASE_URI'] == \
            os.environ.get('DATABASE_URL')


class TestTestingConfig(object):
    def create_app(self):
        app.config.from_object('api.config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.create_app()
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert app.config['TESTING'] is not None
        assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == \
            os.environ.get('DATABASE_TEST_URL')


class TestProductionConfig(object):
    def create_app(self):
        app.config.from_object('api.config.ProductionConfig')
        return app

    def test_app_is_production(self):
        self.create_app()
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert not app.config['TESTING']
