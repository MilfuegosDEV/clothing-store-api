from domain.services import IUserService
from infrastructure.database.repositories import UserRepository


class UserService(IUserService):

    def __init__(self):
        self.user_repository = UserRepository()

    def update_user(self, user):
        return self.user_repository.update(user)

    def find_user_by_username(self, username):
        username = username.strip().lower()
        return self.user_repository.find_by_username(username, include_role_name=True)

    def find_all_users(self):
        return self.user_repository.find_all()
