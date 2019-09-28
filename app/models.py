from . import db

class Contacts(db.Model):
    name_ = db.Column(db.String(), primary_key=True, nullable=False)
    email = db.Column(db.String(), nullable=False)
    subject = db.Column(db.String(), nullable=False)
    message = db.Column(db.String(), nullable=False)

class Git(db.Model):
    id = db.Column(db.Integer(),  primary_key=True, nullable=False)
    repo_name = db.Column(db.String(30))
    description = db.Column(db.String())
    created_at = db.Column(db.String(30))
    size = db.Column(db.Integer())
    language = db.Column(db.String(20))
    last_updated = db.Column(db.String(30))
    repo_url = db.Column(db.String(64))


    
