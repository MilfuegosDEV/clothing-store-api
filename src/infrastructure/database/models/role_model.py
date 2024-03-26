from infrastructure.extensions import db
from domain.entities import RoleEntity

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String

class RoleModel(db.Model):
    __tablename__ = "ROLE"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)

    users = relationship("UserRoleModel", backref="ROLE", cascade="all, delete-orphan")

    def __init__(self, name: str):
        self.name = name

    def save(self) -> "RoleModel":
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self) -> dict[RoleEntity] | None:
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self) -> str:
        return f"<Role {self.name}>"

    @staticmethod
    def SeedRoles() -> list["RoleModel"]:
        """Seed roles if they do not exist"""
        if not RoleModel.query.first():
            roles = ["admin", "user"]
            for role in roles:
                if not RoleModel.exists(role):
                    RoleModel(role).save()

        return RoleModel.query.all()

    @staticmethod
    def exists(name: str) -> bool:
        return True if RoleModel.query.filter_by(name=name).first() else False
