from flask import Blueprint
from . import auth

bp = Blueprint('blueprints', __name__)
bp.register_blueprint(blueprint=auth.bp, url_prefix='/auth')
