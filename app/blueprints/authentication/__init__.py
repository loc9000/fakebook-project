from flask import Blueprint

bp = Blueprint('authentication', __name__, template_folder='main', url_prefix='/')

from .import routes, models
