import re

from flask import Blueprint, jsonify, make_response, request
from flask_cors import cross_origin

import shared
from models.author import Author

author_routes = Blueprint('author_route', __name__)


@author_routes.route('/api/v0/author/', methods=['GET'])
@cross_origin()
def get_message(message_id):
    return make_response({'Status': "Failed", "Message": "Getting all authors is not available"})


@author_routes.route('/api/v0/author/', methods=['POST'])
@cross_origin()
def post_signup():
    author_id = request.json['author_id']
    full_name = request.json['full_name']
    email = request.json['email']
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({'Status': "Failed", "Message": "Please check email address."})
    existing_author_id = Author.query.get(author_id)
    if existing_author_id is not None:
        return jsonify({'Status': "Failed", "Message": "Author ID exists."})
    else:
        new_author = Author(author_id=author_id, full_name=full_name, email=email)
        shared.db.session.add(new_author)
        shared.db.session.commit()
        return jsonify(new_author.serialize)


@author_routes.route('/api/v0/author/<author_id>', methods=['GET'])
@cross_origin()
def get_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return make_response(jsonify({'error': 'Not found'}))
    else:
        return make_response(jsonify(author.serialize))
