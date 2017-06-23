from flask import Blueprint, jsonify, make_response, request

import shared
from models.author import Author

author_routes = Blueprint('author_route', __name__)


@author_routes.route('/api/v0/author/<author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return make_response(jsonify({'error': 'Not found'}))
    else:
        return make_response(jsonify(author.serialize))


@author_routes.route('/api/v0/author', methods=['POST'])
def post_signup():
    author_id = request.json['author_id']
    full_name = request.json['full_name']
    email = request.json['email']
    existing_author_id = Author.query.get(author_id)
    existing_author_email = Author.query.filter_by(email=email)
    if existing_author_id is not None:
        return jsonify({'Status': "Failed", "Message": "Author ID exists."})
    elif existing_author_email is not None:
        return jsonify({'Status': "Failed", "Message": "Author email exists."})
    else:
        new_author = Author(id=author_id, full_name=full_name, email=email)
        shared.db.session.add(new_author)
        shared.db.session.commit()
        return jsonify(new_author)
