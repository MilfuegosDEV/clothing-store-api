from ..db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, LargeBinary as ByteLon


class User(db.Model):
    """
    This model represents a user in the database.

    Attributes:
        id (int): The primary key of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        username (str): The username of the user.
        password (str): The password of the user.
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(ByteLon, nullable=False)

    def __init__(self, first_name: str, last_name: str, username: str, password: str):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def save(self):
        """
        This method saves the user to the database.
        """
        db.session.add(self)
        db.session.commit()
        return self

    def __repr__(self):
        return f"<User {self.username}>"
