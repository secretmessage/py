from shared import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    message = db.Column(db.Text)

    def __init__(self, message_id, author_id, message):
        self.id = message_id
        self.author_id = author_id
        self.message = message

    @property
    def serialize(self):
        return {
            'id': self.id,
            'author_id': self.author_id,
            'message': self.message
        }

    @property
    def serialize_many2many(self):
        return [item.serialize for item in self.many2many]
