from application.services import UserService
from flask import Blueprint, jsonify, request
from domain.dtos.user import UpdateUserDto

class UserController(Blueprint):
    def __init__(self):
        super().__init__("user", __name__)
        self.user_service = UserService()

        self.add_url_rule("/", view_func=self.find_all_users, methods=["GET"])
        self.add_url_rule(
            "/<username>", view_func=self.find_user_by_username, methods=["GET"]
        )

        self.add_url_rule("/<int:id>", view_func=self.update_user, methods=["PUT"])

    def update_user(self, id: int) -> dict | None:
        data: dict[str] = request.json
        data["id"] = id

        if not all(key in data for key in ["first_name", "last_name"]):
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

        user = UpdateUserDto(**data)

        response = self.user_service.update_user(user)

        if not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "User not found",
                        "success": False,
                        "data": None,
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )

    def find_user_by_username(self, username: str) -> dict | None:
        response = self.user_service.find_user_by_username(username)

        if not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "User not found",
                        "success": False,
                        "data": None,
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )

    def find_all_users(self) -> list[dict] | None:

        response = self.user_service.find_all_users()

        if len(response) == 0 or not response:
            return (
                jsonify(
                    {
                        "status": 404,
                        "message": "No users found",
                        "success": False,
                        "data": [],
                    }
                ),
                404,
            )

        return jsonify(
            {
                "status": 200,
                "success": True,
                "data": response,
            }
        )
