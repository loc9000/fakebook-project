# MVC: Models, views, and controllers

import uuid
from datetime import datetime as dt
from app import db


class User(db.Model):

    id = db.Column(db.String(32), default=uuid.uuid4().hex, primary_key=True)
    First_name = db.Column(db.Text(50))
    Last_name = db.Column(db.Text(50))
    email = db.Column(db.Text(50), unique=True)
    password = db.Column(db.Text(300))
    date_created = db.Column(db.DateTime, default=dt.utcnow)

    def __repr__(self):
        return f'<User: {self.First_name} {self.Last_name}>'