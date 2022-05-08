from flask import Blueprint

bp = Blueprint('authentication', __name__, template_folder='users', url_prefix='authentication')

from .import routes, models
