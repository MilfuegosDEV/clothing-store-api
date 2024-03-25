from domain.services import IAuthService
from infrastructure.database.repositories import UserRepository
from bcrypt import checkpw
import flask_jwt_extended as jwt


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

            # Create a new access token
            return jwt.create_access_token(identity=user.username)
        except Exception as e:
            print(e)
            return None
