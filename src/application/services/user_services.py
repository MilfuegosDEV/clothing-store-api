from domain.entities import UserEntity
from domain.services import IUserService
from infrastructure.database.repositories import UserRepository
from bcrypt import hashpw, gensalt


class UserService(IUserService):

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user: UserEntity) -> dict | None:
        user.password = hashpw(user.password.encode(), gensalt())
        return self.user_repository.create(user)

    def find_user_by_username(self, username: str) -> dict | None:
        username = username.strip().lower()
        return self.user_repository.find_by_username(username)
