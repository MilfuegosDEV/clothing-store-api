from domain.services import IAuthService
from infrastructure.database.repositories import UserRepository
from bcrypt import checkpw
import jwt


class AuthService(IAuthService):

    def __init__(self):
        self.user_repository = UserRepository()

    def register(self, user):
        return self.user_repository.create(user)

    def authenticate(self, user):
        try:

            data = self.user_repository.find_by_username(
                user.username, include_password=True
            )
            if user is None:
                return None

            if not checkpw(user.password.encode(), data["password"]):
                return False

            return jwt.encode(
                {"user": {"id": data["id"], "username": data["username"]}},
                "secret",
                algorithm="HS256",
            )
        except Exception as e:
            print(e)
            return None
