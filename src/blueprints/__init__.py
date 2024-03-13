from flask import Blueprint
from .user import bp as user_bp

bp: Blueprint = Blueprint("api", __name__)
bp.register_blueprint(user_bp, url_prefix="/user")
