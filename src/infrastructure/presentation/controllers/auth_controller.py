import re
from application.services import UserService
from domain.entities import UserEntity
from flask import Blueprint, request, jsonify


class AuthController(Blueprint):
    def __init__(self):
        super().__init__("auth", __name__)
        self.user_service = UserService()
        self.add_url_rule("/sign-up", view_func=self.create_user, methods=["POST"])

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

        user = UserEntity(**data)
        response = self.user_service.create_user(user)

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
