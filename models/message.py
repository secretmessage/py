from shared import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    message = db.Column(db.Text)

    def __init__(self, message_id, author_id, message):
        self.id = message_id
        self.author_id = author_id
        self.message = message
