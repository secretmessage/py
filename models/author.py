from shared import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, input_id, full_name, email):
        self.id = input_id
        self.full_name = full_name
        self.email = email