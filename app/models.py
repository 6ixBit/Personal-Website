from . import db

class Contacts(db.Model):
    name_ = db.Column(db.String(), primary_key=True, nullable=False)
    email = db.Column(db.String(), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)

