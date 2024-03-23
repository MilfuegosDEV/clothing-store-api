from application.services import UserService
from flask import Blueprint, jsonify


class UserController(Blueprint):
    def __init__(self):
        super().__init__("user", __name__)
        self.user_service = UserService()

        self.add_url_rule(
            "/<username>", view_func=self.find_user_by_username, methods=["GET"]
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
