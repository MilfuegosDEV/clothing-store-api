from domain.dtos.user import CreateUserDto, UpdateUserDto
from domain.services import IUserService
from infrastructure.database.repositories import UserRepository
from bcrypt import hashpw, gensalt


class UserService(IUserService):

    def __init__(self):
        self.user_repository = UserRepository()

    def create_user(self, user):
        user.password = hashpw(user.password.encode(), gensalt())
        return self.user_repository.create(user)

    def update_user(self, user):
        return self.user_repository.update(user)

    def find_user_by_username(self, username):
        username = username.strip().lower()
        return self.user_repository.find_by_username(username)

    def find_all_users(self):
        return self.user_repository.find_all()
