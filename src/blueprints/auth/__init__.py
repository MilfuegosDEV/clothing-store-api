from flask import Blueprint, jsonify, request, Response
from .controller import AuthController


class AuthBlueprint(Blueprint):
    """
    This class represents the blueprint for the authentication routes.
    """

    def __init__(self):
        super().__init__("auth", __name__)
        self.controller = AuthController()
        self.add_url_rule("/signup", view_func=self.sign_up, methods=["POST"])

    def sign_up(self) -> Response:
        """
        This method registers a new user.
        Returns:
                Response: The response of the registration.
        """

        data = request.json
        response = self.controller.register(data)

        if not response.get("user"):
            return jsonify(response), 400

        return jsonify(response), 201
