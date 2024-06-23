from .user_role_model import UserRoleModel
from .role_model import RoleModel
from infrastructure.extensions import db
from domain.entities import UserEntity
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, LargeBinary

class UserModel(db.Model):
    __tablename__ = "USER"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)  
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    roles = relationship("UserRoleModel", backref="USER", cascade="all, delete-orphan")

    def __init__(self, user: UserEntity):
        self.first_name = user.first_name
        self.last_name = user.last_name
        self.username = user.username
        self.password = user.password

    def save(self) -> "UserModel":
        db.session.add(self)
        db.session.commit()
        return self

    def update(self, user: UserEntity) -> "UserModel":
        self.first_name = user.first_name
        self.last_name = user.last_name
        db.session.commit()
        return self

    def to_dict(
        self, include_password: bool = False, include_role_name: bool = True
    ) -> dict | None:
        response: dict = {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
        }

        if include_password:
            response["password"] = self.password

        if include_role_name:
            role = (
                db.session.query(RoleModel)
                .join(UserRoleModel)
                .filter(UserRoleModel.user_id == self.id)
                .first()
            )
            response["role"] = role.name

        return response

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    @staticmethod
    def exists(username: str) -> bool:
        return True if UserModel.query.filter_by(username=username).first() else False
