import psycopg2

from ..models.user import User
from sqlalchemy.orm import sessionmaker
from database import Engine
from bcrypt import hashpw, gensalt


class Service:
    def create_user(
        self,
        first_name: str = None,
        last_name: str = None,
        username: str = None,
        password: str = None,
    ) -> User | None:
        try:
            Session = sessionmaker(bind=Engine)

            first_name = first_name.upper()
            last_name = last_name.upper()
            username = username.lower()

            salts = gensalt(8)
            hashed_password = hashpw(password.encode("utf8"), salts)

            user = User(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password_hash=hashed_password,
            )

            with Session() as session:
                session.add(user)
                session.commit()

            return user
        except Exception as e:
            raise e
