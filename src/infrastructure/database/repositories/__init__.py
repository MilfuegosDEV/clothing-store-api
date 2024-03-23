from ..models import User, UserRole, Role
from domain.entities import UserEntity
from domain.repositories import IUserRepository
import sqlalchemy.exc


class UserRepository(IUserRepository):

    def __init__(self):
        self.userModel = User
        self.userRoleModel = UserRole

    def create(self, user: UserEntity) -> dict | None:
        try:
            if self.userModel.exists(user.username):
                return None
            else:
                new_user: dict[User] | None = self.userModel(user).save().to_dict()
                self.userRoleModel(new_user["id"], 2).save()  # Assign user role
                return new_user

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_by_username(self, username: str) -> dict | None:
        try:
            user: User = self.userModel.query.filter_by(username=username).first()

            if not user:
                return None

            user_dict: dict[User] = user.to_dict()
            role: Role = (
                Role.query.join(UserRole).filter(UserRole.user_id == user.id).first()
            )
            user_dict["role"] = role.name
            return user_dict

        except sqlalchemy.exc.IntegrityError:
            return None
