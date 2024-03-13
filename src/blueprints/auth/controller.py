from .service import AuthService


class AuthController(AuthService):
    """
    This class represents a controller for the User model.
    """

    def __init__(self):
        super().__init__()

    def register(self, data: dict) -> dict:
        """
        This method registers a new user.
        Args:
            data (dict): The data to be used to register the user.
        Returns:
            dict: The response of the registration.
        """

        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        response = self.create_user(first_name, last_name, username, password)

        # The response is a tuple, so we need to check if the second element is a User object or None.
        if response[1]:
            response = {
                "message": response[0],
                "user": {
                    "id": response[1].id,
                    "first_name": response[1].first_name,
                    "last_name": response[1].last_name,
                    "username": response[1].username,
                },
            }
        else:
            response = {"message": response[0]}

        return response
