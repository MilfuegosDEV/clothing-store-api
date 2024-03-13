from core.models import User


class UserService:
    """
    This class represents a service for the User model.

    Attributes:
        user (User): The user model.
    """

    def __init__(self, user: User):
        self.user = user

    def create_user(self, username: str, password: str):
        """
        This method creates a new user in the database.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User: The newly created user.
        """
        new_user = self.user(username, password)
        self.user.save(new_user)
        return new_user

    def get_user(self, username: str):
        """
        This method retrieves a user from the database
        Args:
            username (str): The username of the user.
        Returns:
            User: The user with the given username.
        """
        return self.user.query.filter_by(username=username).first()
