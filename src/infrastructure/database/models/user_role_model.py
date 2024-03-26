from infrastructure.extensions import db
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
class UserRoleModel(db.Model):
    __tablename__ = "USER_ROLE"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("USER.id"), primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("ROLE.id"), primary_key=True
    )

    def __init__(self, user_id: int, role_id: int):
        self.user_id = user_id
        self.role_id = role_id

    def save(self) -> "UserRoleModel":
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self) -> dict | None:
        return {
            "user_id": self.user_id,
            "role_id": self.role_id,
        }

    def __repr__(self) -> str:
        return f"<UserRole {self.user_id} {self.role_id}>"

    @staticmethod
    def exists(user_id: int, role_id: int) -> bool:
        return (
            True
            if UserRoleModel.query.filter_by(user_id=user_id, role_id=role_id).first()
            else False
        )
