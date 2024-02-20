import jwt
from datetime import datetime, timedelta
from ..models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from database import Engine
from bcrypt import hashpw, gensalt, checkpw
from config import SECRET_KEY


class Service:
    def create_user(
        self,
        first_name: str = None,
        last_name: str = None,
        username: str = None,
        password: str = None,
    ) -> User | None:
        """
        This method will create a new user in the database.
        :param first_name: The first name of the user
        :param last_name: The last name of the user
        :param username: The username of the user
        :param password: The password of the user
        :return: The newly created user
        """
        try:
            Session = sessionmaker(bind=Engine)

            first_name = first_name.upper().strip()
            last_name = last_name.upper().strip()
            username = username.lower().strip()
            password = password.strip()

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

    def login(self, username: str, password: str) -> str | None:
        """
        This method will return a JWT token for the user if the username and password are correct.
        :param username: The username of the user
        :param password: The password of the user
        :return: A JWT token for the user if the username and password are correct.
        """
        try:
            username = username.lower().strip()
            Session = sessionmaker(bind=Engine)
            with Session() as session:
                user: User = session.execute(
                    select(User.username, User.password_hash).where(
                        User.username == username
                    )
                ).fetchone()

                if not user:
                    return None  # Move this line inside the session scope

                if not checkpw(password.encode("utf8"), user.password_hash):
                    return None

                token = jwt.encode(
                    {
                        "username": user.username,
                        "exp": datetime.utcnow() + timedelta(hours=6),
                    },
                    SECRET_KEY,
                    algorithm="HS256",
                )

                return token

        except Exception as e:
            raise e
