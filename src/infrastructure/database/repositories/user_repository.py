from infrastructure.database.models import UserModel, UserRoleModel, RoleModel
from domain.repositories import IUserRepository
from sqlalchemy import desc, asc
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
                new_user: UserModel = self.userModel(user).save()
                # assign role to user if the user is not the first user the role will be user by default.
                # otherwise, the role will be admin
                self.userRoleModel(
                    user_id=new_user.id, role_id=1 if new_user.id == 1 else 2
                ).save()

                return new_user.to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def update(self, user):
        try:
            found_user: UserModel = self.userModel.query.filter_by(
                username=user.username
            ).first()

            return found_user.update(user).to_dict()

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_by_username(
        self, username, include_password: bool = False, include_role_name: bool = True
    ):
        try:
            user: UserModel = self.userModel.query.filter_by(username=username).first()
            return user.to_dict(include_password, include_role_name)

        except sqlalchemy.exc.IntegrityError:
            return None

    def find_all(self):
        try:
            users: list[UserModel] | None = self.userModel.query.order_by(
                asc(UserModel.id)
            ).all()

            return [user.to_dict() for user in users] if users else None
        except sqlalchemy.exc.IntegrityError:
            return None
