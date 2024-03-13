import bcrypt
import jwt

from core.models import User


class AuthService:
    """
    This class represents a service for the User model.
    """

    def __init__(self):
        self.user = User

    def create_user(
        self, first_name: str, last_name: str, username: str, password: str
    ) -> tuple[str, User | None]:
        """
        This method creates a new user in the database.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User: The newly created user. In case of an error, it returns a string indicating the error and
        """

        try:
            first_name = first_name.strip().title()
            last_name = last_name.strip().title()
            password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            username = username.strip().lower()

            new_user = self.user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password,
            ).save()

            return "User created successfully", new_user

        except Exception as e:
            if "unique" in str(e):
                return "Username already exists", None
            return "An error occurred", None
