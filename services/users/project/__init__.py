# services/users/project/__init__.py
from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

import os

# instantiate the app
app = Flask(__name__)

# enable CORS
CORS(app)

# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


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
