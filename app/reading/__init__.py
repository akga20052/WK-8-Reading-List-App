from flask import Blueprint

reading_blueprint = Blueprint("reading", __name__, url_prefix="/reading")

from . import routes