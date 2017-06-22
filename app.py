#!flask/bin/python

import os

from flask import Flask, jsonify, make_response
from flask_cors import CORS

import secret
import shared
from routes.other import other_route
from routes.message import message_routes

application = Flask(__name__)
BASE_URL = os.path.abspath(os.path.dirname(__file__))
dist = os.path.join(BASE_URL, "dist")

CORS(application)

application.config[
    'SQLALCHEMY_DATABASE_URI'] = secret.SQLALCHEMY_DATABASE_URI
shared.db.init_app(application)
application.register_blueprint(other_route)
application.register_blueprint(message_routes)


@application.route('/', defaults={'path': ''})  # Catch All urls, enabling copy-paste url
@application.route('/<path:path>')  # Catch All urls, enabling copy-paste url
def home(path):
    return 'Easy there cowboy.'


@application.errorhandler(404)
def not_found(error):
    return_json = jsonify({'error': 'Not found'})
    return make_response(return_json, 404)


if __name__ == "__main__":
    application.run(host='0.0.0.0')
