from infrastructure.database.models import UserModel, UserRoleModel, RoleModel
from domain.repositories import IUserRepository
from sqlalchemy import asc
import sqlalchemy.exc


class UserRepository(IUserRepository):
    def __init__(self):
        self.userModel = UserModel
        self.userRoleModel = UserRoleModel
        self.roleModel = RoleModel

    def create(self, user):
        try:
            # to prevent create an user with the same username twice in the database
            if self.userModel.exists(user.username):
                return None
            else:
                new_user: dict[UserModel] | None = self.userModel(user).save().to_dict()
                # assign role to user if the user is not the first user the role will be user by default.
                # otherwise, the role will be admin
                self.userRoleModel(user_id=new_user["id"], role_id=1 if new_user["id"] == 1 else 2).save()
                return new_user

        except sqlalchemy.exc.IntegrityError:
            return None

    def update(self, user):
        try:
            found_user: UserModel = self.userModel.query.filter_by(
                username=user.username
            ).first()
            if not found_user:
                return None

            return found_user.update(user).to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_by_username(self, username, include_password: bool = False):
        try:
            user: UserModel = self.userModel.query.filter_by(username=username).first()

            if not user:
                return None

            user_dict: dict[UserModel] = user.to_dict(include_password)

            # appends role name to response
            role: RoleModel = (
                RoleModel.query.join().filter(self.userRoleModel.user_id == user.id).first()
            )

            user_dict["role"] = role.name

            return user_dict

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_all(self):
        try:
            # get all users
            users: list[UserModel] = self.userModel.query.order_by(
                asc(self.userModel.id)
            ).all()

            if not users:
                return None

            # for user in users:

            #     role: Role = (
            #         Role.query.join(UserRole)
            #         .filter(UserRole.user_id == user.id)
            #         .first()
            #     )

            #     user.role_name = role.name
            #     users_list.append(user.to_dict())

            return [user.to_dict() for user in users]

        except sqlalchemy.exc.IntegrityError:
            return None
