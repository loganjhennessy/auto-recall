# services/users/project/__init__.py
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

import os

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

# instantiate the db
db = SQLAlchemy(app)


# model
class User(db.Model):  # new
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username, email):
        self.username = username
        self.email = email


@app.route('/users', methods=['GET'])
def base():
    return jsonify({
        'name': 'logan',
        'email': 'loganjhennessy@gmail.com'
    })


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })