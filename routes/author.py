from flask import Blueprint, jsonify, make_response

from models.author import Author

author_routes = Blueprint('author_route', __name__)


@author_routes.route('/api/v0/authors/', methods=['GET'])
def get_all_authors():
    authors = Author.query.all()
    return make_response(jsonify(authors))
