from flask import Blueprint
from .auth import AuthBlueprint

bp: Blueprint = Blueprint("api", __name__)
bp.register_blueprint(AuthBlueprint(), url_prefix="/auth")
