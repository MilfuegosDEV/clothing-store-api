from ..models import User, UserRole, Role
from domain.dtos.user import CreateUserDto, UpdateUserDto
from domain.repositories import IUserRepository
import sqlalchemy.exc


class UserRepository(IUserRepository):

    def __init__(self):
        self.userModel = User
        self.userRoleModel = UserRole

    def create(self, user):
        try:
            if self.userModel.exists(user.username):
                return None
            else:
                new_user: dict[User] | None = self.userModel(user).save().to_dict()
                self.userRoleModel(new_user["id"], 2).save()  # Assign user role
                return new_user

        except sqlalchemy.exc.IntegrityError:
            return None

    def update(self, user):
        try:
            found_user: User = self.userModel.query.filter_by(id=user.id).first()
            if not found_user:
                return None

            return found_user.update(user).to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_by_username(self, username):
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

    def find_all(self):
        try:
            # include role name
            users: list[User] = self.userModel.query.all()
            users_list = []

            for user in users:
                user_dict: dict[User] = user.to_dict()

                role: Role = (
                    Role.query.join(UserRole)
                    .filter(UserRole.user_id == user.id)
                    .first()
                )

                user_dict["role"] = role.name
                users_list.append(user_dict)

            return users_list

        except sqlalchemy.exc.IntegrityError:
            return None
