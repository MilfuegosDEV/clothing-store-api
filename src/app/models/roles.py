from database import Database

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class Role(Database):
    """Model for roles"""

    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True),
    name: Mapped[String] = mapped_column(String(10), nullable= False)

    def __init__(self, name:str) -> None:
        self.name:str = name
    
    def __repr__(self) -> str:
        return f"Role(name={self.name})"


