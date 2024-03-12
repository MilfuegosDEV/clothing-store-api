from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, LargeBinary as ByteLon


class User(db.Model):
    '''
    This model represents a user in the database.
    
    Attributes:
        id (int): The primary key of the user.
        username (str): The username of the user.
        password (str): The password of the user.
    '''
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username:Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(ByteLon, nullable=False)

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'