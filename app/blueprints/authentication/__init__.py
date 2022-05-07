from flask import Blueprint

bp = Blueprint('authentication', __name__, template_folder='users', url_prefix='register')

from .import routes, models
