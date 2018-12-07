import os

from flask import current_app

from api import create_app


class TestDevelopmentConfig(object):

    def test_app_is_development(self):
        app = create_app()
        app.config.from_object('api.config.DevelopmentConfig')
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert not (current_app is None)
        assert app.config['SQLALCHEMY_DATABASE_URI'] == \
            os.environ.get('DATABASE_URL')


class TestTestingConfig(object):

    def test_app_is_testing(self):
        app = create_app()
        app.config.from_object('api.config.TestingConfig')
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert app.config['TESTING'] is not None
        assert not app.config['PRESERVE_CONTEXT_ON_EXCEPTION']
        assert app.config['SQLALCHEMY_DATABASE_URI'] == \
            os.environ.get('DATABASE_TEST_URL')


class TestProductionConfig(object):

    def test_app_is_production(self):
        app = create_app()
        app.config.from_object('api.config.ProductionConfig')
        assert app.config['SECRET_KEY'] == 'my_precious'
        assert not app.config['TESTING']
