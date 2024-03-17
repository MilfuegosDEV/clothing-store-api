from domain.entities import UserEntity
from domain.interfaces.services import IUserService
from infrastructure.database.repositories import UserRepository
from bcrypt import hashpw, gensalt


class UserService(IUserService):
    def __init__(self, user_repository: UserRepository = None):
        self.user_repository = user_repository or UserRepository()

    def create_user(self, user: UserEntity) -> dict | None:
        user.password = hashpw(user.password.encode(), gensalt())
        return self.user_repository.create(user)
