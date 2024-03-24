import re
from application.services import AuthService
from domain.dtos.auth import RegisterDto, LoginDto
from flask import Blueprint, request, jsonify


class AuthController(Blueprint):
    def __init__(self):
        super().__init__("auth", __name__)
        self.auth_service = AuthService()
        self.add_url_rule("/sign-up", view_func=self.create_user, methods=["POST"])
        self.add_url_rule("/login", view_func=self.login, methods=["POST"])

    def create_user(self) -> dict | None:

        data: dict[str] = request.json

        if not all(
            key in data for key in ["first_name", "last_name", "username", "password"]
        ):
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid input data",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        if not re.search(r"^[a-zA-Z0-9]{3,20}$", data["username"], re.IGNORECASE):
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid username",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", data["password"]):
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid password",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        user = RegisterDto(**data)
        response = self.auth_service.register(user)

        if response:
            return (
                jsonify(
                    {
                        "status": 201,
                        "message": "User created sucessfully",
                        "success": True,
                        "data": response,
                    }
                ),
                201,
            )
        return (
            jsonify(
                {
                    "status": 409,
                    "message": "User already exists",
                    "success": False,
                    "data": None,
                }
            ),
            409,
        )

    def login(self) -> dict | None:
        data = request.json

        if not all(key in data for key in ["username", "password"]):
            return (
                jsonify(
                    {
                        "status": 400,
                        "message": "Invalid input data",
                        "success": False,
                        "data": None,
                    }
                ),
                400,
            )

        user = LoginDto(**data)
        response = self.auth_service.authenticate(user)

        if response is None:
            return (
                jsonify(
                    {
                        "status": 401,
                        "message": "The username doesn't exists",
                        "success": False,
                        "data": None,
                    }
                ),
                401,
            )

        if response == False:
            return (
                jsonify(
                    {
                        "status": 401,
                        "message": "Invalid credentials",
                        "success": False,
                        "data": None,
                    }
                ),
                401,
            )

        return (
            jsonify(
                {
                    "status": 200,
                    "message": "User authenticated sucessfully",
                    "success": True,
                    "data": response,
                }
            ),
            200,
        )
