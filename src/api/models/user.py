from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, LargeBinary, Date
from database import Database


class User(Database):
    """Model for users"""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(30), nullable=False)
    last_name: Mapped[str] = mapped_column(String(30), nullable=False)
    username: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    password_hash: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    profile_photo_url: Mapped[str] = mapped_column(String(255), nullable=True)
    creation_date: Mapped[Date] = mapped_column(
        Date, nullable=False, default=datetime.utcnow()
    )

    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        username: str = None,
        password_hash: bytes = None,
        profile_photo_url: str = None,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password_hash = password_hash
        self.profile_photo_url = profile_photo_url

    def __repr__(self) -> str:
        return (
            f"User(first_name={self.first_name}, "
            f"last_name={self.last_name}, "
            f"username={self.username}, "
            f"password_hash={self.password_hash}, "
            f"profile_photo_url={self.profile_photo_url})"
            f"creation_date={self.creation_date})"
        )
