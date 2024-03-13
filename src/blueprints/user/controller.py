from .service import UserService
from core.models import User


class UserController:
    """
    This class represents a controller for the User model.
    Attributes:
        user_service (UserService): The user service.
    """

    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_user(self, username: str, password: str) -> User:
        """
        This method creates a new user in the database.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User: The newly created user.
        """
        return self.user_service.create_user(username, password)

    def get_user(self, username: str) -> User:
        """
        This method retrieves a user from the database

        Args:
            username (str): The username of the user.

        Returns:
            User: The user with the given username.
        """
        return self.user_service.get_user(username)
