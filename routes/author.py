from flask import Blueprint, jsonify, make_response

from models.author import Author

author_routes = Blueprint('author_route', __name__)


@author_routes.route('/api/v0/authors/', methods=['GET'])
def get_all_authors():
    return make_response([i.serialize for i in Author.query.all()])


@author_routes.route('/api/v0/authors/<author_id>', methods=['GET'])
def get_author(author_id):
    author = Author.query.get(author_id)
    if author is None:
        return make_response(jsonify({'error': 'Not found'}))
    else:
        return make_response(jsonify(author.serialize))
