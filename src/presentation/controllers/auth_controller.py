from application.services import UserService
from domain.entities import UserEntity

from flask import Blueprint, request, jsonify


class AuthController(Blueprint):
    def __init__(self, user_service: UserService = None):
        super().__init__("user", __name__)
        self.user_service = user_service or UserService()

        self.add_url_rule("/sigup", view_func=self.create_user, methods=["POST"])

    def create_user(self) -> dict | None:

        data = request.json

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
