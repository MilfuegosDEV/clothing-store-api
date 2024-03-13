from flask import Blueprint, request, jsonify
from .controller import UserController

bp: Blueprint = Blueprint("user", __name__)


@bp.route("/", methods=["POST"])
def __create_user():
    """
    This method creates a new user in the database.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    user = UserController.create_user(username, password)
    return jsonify(user)
