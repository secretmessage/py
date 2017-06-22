from flask import Blueprint, jsonify, make_response

import shared
from models.author import Author
from models.message import Message

message_routes = Blueprint('message_route', __name__)


@message_routes.route('/api/v0/messages/', methods=['GET'])
def get_all_messages():
    messages = Message.query.all()
    return make_response(jsonify(messages))


@message_routes.route('/api/v0/messages/<message_id>', methods=['GET'])
def get_message(message_id):
    message = Message.query.get(message_id)
    if message is None:
        return make_response(jsonify({'error': 'Not found'}))
    else:
        return make_response(jsonify(message))


@message_routes.route('/api/v0/message/<message_id>/<author_id>/<message>', methods=['POST'])
def post_signup(message_id, author_id, message):
    existing_author = Author.query.get(author_id)
    if existing_author is None:
        return jsonify({'Status': "Failed", "Message": "Author with ID does not exist."})
    else:
        existing_message = Message.query.get(message_id)
        if existing_message is not None:
            return jsonify({'Status': "Failed", "Message": "Message with ID exists"})
        else:
            new_message = Message(message_id=message_id, author_id=author_id, message=message)
            shared.db.session.add(new_message)
            shared.db.session.commit()
            return jsonify({'Status': "Sucessful"})
