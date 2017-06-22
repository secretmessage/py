from flask import jsonify, Blueprint

import shared
from models.author import Author
from models.message import Message

other_route = Blueprint('other_route', __name__)


# This should never exist outside of development environment
@other_route.route('/api/v0/drop_and_create/SoCbZlkk8CUljxbPl4OQMTnFjYJdqejMM4uenjba9eeN9RbX8ViJjQnaWMRYEZ4')
def get_drop_all():
    shared.db.drop_all()
    shared.db.create_all()
    populate_author_table()
    populate_message_table()
    return jsonify({'status': 'success'}), 200


def populate_author_table():
    author00 = Author(1, 'John Keats', 'john@keats.london')
    shared.db.session.add(author00)
    shared.db.session.commit()


def populate_message_table():
    message00 = Message(1, 1, 'John Keats was an English Romantic poet.')
    shared.db.session.add(message00)
    shared.db.session.commit()
