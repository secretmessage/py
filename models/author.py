from shared import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)

    def __init__(self, author_id, full_name, email):
        self.id = author_id
        self.full_name = full_name
        self.email = email

    @property
    def serialize(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'email': self.email
        }
