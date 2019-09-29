from . import db

class Contacts(db.Model):
    id = db.Column(db.Integer(), primary_key=True, nullable=False)
    name_ = db.Column(db.String(30), nullable=False, unique=False)
    email = db.Column(db.String(55), nullable=False, unique=False)
    subject = db.Column(db.String(30), nullable=False, unique=False)
    message = db.Column(db.String(), nullable=False, unique=False)

class Git(db.Model):
    id = db.Column(db.Integer(),  primary_key=True, nullable=False)
    repo_name = db.Column(db.String(30))
    description = db.Column(db.String())
    created_at = db.Column(db.String(30))
    size = db.Column(db.Integer())
    language = db.Column(db.String(20))
    last_updated = db.Column(db.String(30))
    repo_url = db.Column(db.String(64))


    
