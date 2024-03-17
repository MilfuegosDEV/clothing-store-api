from ..models import User
from domain.entities import UserEntity
from domain.interfaces.repositories import IUserRepository
import sqlalchemy.exc


class UserRepository(IUserRepository):
    def __init__(self, user: User = None):
        self.user = user or User

    def create(self, user: UserEntity) -> dict | None:
        try:
            if self.user.exists(user.username):
                return None
            else:
                user = self.user(user)
                new_user: User = user.save()
                return new_user.to_dict()
        except sqlalchemy.exc.IntegrityError:
            return None
