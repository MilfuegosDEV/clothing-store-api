from .. import db
from domain.entities import UserEntity
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, LargeBinary


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(20), nullable=False)
    last_name: Mapped[str] = mapped_column(String(20), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)

    def __init__(self, user: UserEntity):
        self.first_name = user.first_name.title().strip()
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
