# MVC: Models, views, and controllers

import werkzeug
import uuid
from datetime import datetime as dt
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model, UserMixin):

    id = db.Column(db.String(32), primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, default=dt.utcnow)

    def generate_password(self, password_from_form):
        self.password = generate_password_hash(password_from_form)

    def check_password(self, password_from_form):
        return check_password_hash(self.password, password_from_form)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id = uuid.uuid4().hex

    def __repr__(self):
        return f'<User: {self.first_name} {self.last_name}>'


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)