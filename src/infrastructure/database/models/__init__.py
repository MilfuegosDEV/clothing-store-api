from .. import db
from domain.entities import UserEntity
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, LargeBinary, ForeignKey


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    roles = relationship("UserRole", backref="user", cascade="all, delete-orphan")

    def __init__(self, user: UserEntity):
        self.first_name = user.first_name.title().strip()  # joe -> Joe
        self.last_name = user.last_name.title().strip()
        self.username = user.username.lower().strip()
        self.password = user.password.strip()

    def save(self) -> "User":
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self) -> dict | None:
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
        }

    def __repr__(self) -> str:
        return f"<User {self.username}>"

    @staticmethod
    def exists(username: str) -> bool:
        return True if User.query.filter_by(username=username).first() else False


class Role(db.Model):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(10), nullable=False, unique=True)

    users = relationship("UserRole", backref="role", cascade="all, delete-orphan")

    def __init__(self, name: str):
        self.name = name.title().strip()

    def save(self) -> "Role":
        db.session.add(self)
        db.session.commit()
        return self

    def to_dict(self) -> dict | None:
        return {
            "id": self.id,
            "name": self.name,
        }

    def __repr__(self) -> str:
        return f"<Role {self.name}>"

    @staticmethod
    def SeedRoles():
        """Seed roles if they do not exist"""
        if not Role.query.first():
            roles = ["user", "admin"]
            for role in roles:
                if not Role.exists(role):
                    Role(role).save()

    @staticmethod
    def exists(name: str) -> bool:
        return True if Role.query.filter_by(name=name).first() else False


class UserRole(db.Model):
    __tablename__ = "user_roles"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), primary_key=True
    )
    role_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("roles.id"), primary_key=True
    )

    def __init__(self, user_id: int, role_id: int):
        self.user_id = user_id
        self.role_id = role_id

    def save(self) -> "UserRole":
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
            if UserRole.query.filter_by(user_id=user_id, role_id=role_id).first()
            else False
        )
