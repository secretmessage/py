#!flask/bin/python

import os

from flask import Flask, jsonify, make_response
from flask_cors import CORS

import shared
from routes.author import author_routes
from routes.message import message_routes
from routes.other import other_route

application = Flask(__name__)
BASE_URL = os.path.abspath(os.path.dirname(__file__))
dist = os.path.join(BASE_URL, "dist")

CORS(application)

application.config[
    'SQLALCHEMY_DATABASE_URI'] = os.environ["DATABASE_URL"]
shared.db.init_app(application)
application.register_blueprint(other_route)
application.register_blueprint(author_routes)
application.register_blueprint(message_routes)

@application.errorhandler(500)
def internal_server_error(error):
    return_json = jsonify({'error': error})
    return make_response(return_json, 500)


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
