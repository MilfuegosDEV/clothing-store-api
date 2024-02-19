import re

from flask import Blueprint, jsonify, request
from ..services import auth


class Router(Blueprint, auth.Service):
    def __init__(self):
        super().__init__("auth", __name__)
        auth.Service.__init__(self)
        self.add_url_rule(
            "/register",
            view_func=self.register_view,
            methods=["POST"],
        )

    def register_view(self):
        try:
            data: dict = request.get_json()

            first_name: str | None = data.get("first_name", None)
            last_name: str | None = data.get("last_name", None)
            username: str | None = data.get("username", None)
            password: str | None = data.get("password", None)

            if not first_name or not last_name or not username or not password:
                return jsonify({"error": "Missing data"}), 400

            if not re.match(r"^(?![.-])(?<!_)[a-zA-Z0-9]{6,20}(?!_)$", username):
                return jsonify({"error": "Invalid username"}), 400

            if len(password) < 8:
                return (
                    jsonify(
                        {
                            "error": "Invalid password: Too short, must be at least 8 char"
                        }
                    ),
                    400,
                )
            if len(password) > 20:
                return (
                    jsonify(
                        {"error": "Invalid password: Too long, must be at most 20 char"}
                    ),
                    400,
                )

            if not re.match(r"^(?![.-])(?<!_)[a-zA-Z0-9]{8,20}(?!_)$", password):
                return jsonify({"error": "Invalid password"}), 400

            self.create_user(first_name, last_name, username, password)

            return jsonify({"message": "User registered"}), 201

        except Exception as e:
            if "users_username_key" in str(e):
                return (
                    jsonify(
                        {
                            "error": f"Username '{username}' already taken. Please choose a different username."
                        }
                    ),
                    409,
                )
            return jsonify({"Error": f"Internal Server Error: {str(e)}"}), 500
