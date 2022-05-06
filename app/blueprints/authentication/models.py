# MVC: Models, views, and controllers

import uuid
from datetime import datetime as dt
from app import db


class User(db.Model):

    id = db.Column(db.String(32), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=dt.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.First_name} {self.Last_name}>'