from database import Database

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, ForeignKey

class UserRole(Database):
    """Model for user roles"""
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    uid: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), unique=True,nullable=False)
    rid: Mapped[int] = mapped_column(Integer, ForeignKey('roles.id'), nullable=False)

    def __init__(self, uid: int, rid:int):
        self.uid = uid
        self.rid = rid

    def __repr__(self) -> str:
        return (
            f"UserRole(uid={self.uid}, "
            f"rid={self.rid})"
        )


