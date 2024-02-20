import re
from . import validators
from typing import Literal
from flask import Blueprint, jsonify, request, Response
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
        self.add_url_rule(
            "/login",
            view_func=self.login_view,
            methods=["POST"],
        )

    def register_view(
        self,
    ) -> (
        tuple[Response, Literal[400]]
        | tuple[Response, Literal[201]]
        | tuple[Response, Literal[409]]
        | tuple[Response, Literal[500]]
    ):
        """
        Endpoint for registering a new user
        :return: 201 if the user was created successfully, 400 if the user already exists, 409 if the user already exists, 500 if something went wrong
        """
        try:
            data: dict = request.get_json()

            first_name: str | None = data.get("first_name", None)
            last_name: str | None = data.get("last_name", None)
            username: str | None = data.get("username", None)
            password: str | None = data.get("password", None)

            # check required fields and show up whose fields are missed.
            missing_fields_message = validators.checkRequiredFields(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
            )

            if missing_fields_message is not None:
                return jsonify({"errors": [missing_fields_message]}), 400

            # check all fields that must to be alphabetic
            must_be_alpha_message = validators.mustBeAlpha(
                first_name=first_name, last_name=last_name
            )
            if must_be_alpha_message is not None:
                return jsonify({"errors": [must_be_alpha_message]}), 400

            # show another messages.
            errors = validators.handleErrors(
                validators.mustBeBetween(first_name, "first_name", 3, 30),
                validators.mustBeBetween(last_name, "last_name", 3, 30),
                validators.mustBeBetween(password, "password", 8, 20),
                validators.mustBeBetween(username, "username", 6, 20),
            )

            if errors is not None:
                return jsonify({"errors": errors}), 400

            if not re.match(r"^(?![.-])(?<!_)[a-zA-Z0-9]{6,20}(?!_)$", username):
                return jsonify({"errors": ["Invalid username"]}), 400

            if not re.match(r"^(?![.-])(?<!_)[a-zA-Z0-9]{8,20}(?!_)$", password):
                return jsonify({"errors": ["Invalid password"]}), 400

            # if all is well...

            self.create_user(first_name, last_name, username, password)

            return jsonify({"message": "User registered"}), 201

        except Exception as e:
            if "users_username_key" in str(e):
                return (
                    jsonify(
                        {
                            "error": f"Username '{username.lower()}' already taken. Please choose a different username."
                        }
                    ),
                    409,
                )

            return jsonify({"Error": f"Internal Server Error: {str(e)}"}), 500

    def login_view(self):
        """
        Endpoint for logging a user in
        :return: 200 if the user was logged in successfully, 400 if the user doesn't exist, 409 if the user doesn't exist, 500 if something went wrong
        """
        try:
            data: dict = request.get_json()

            username: str | None = data.get("username", None)
            password: str | None = data.get("password", None)

            # check required fields and show up whose fields are missed.
            missing_fields_message = validators.checkRequiredFields(
                username=username,
                password=password,
            )

            if missing_fields_message is not None:
                return jsonify({"errors": [missing_fields_message]}), 400

            token = self.login(username, password)

            if token is None:
                return jsonify({"error": "Invalid username or password"}), 400

            return jsonify({"token": token}), 200

        except Exception as e:
            return jsonify({"Error": f"Internal Server Error: {str(e)}"}), 500
