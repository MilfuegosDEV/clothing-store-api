import os
from datetime import timedelta

class Config:
    """
    Config class to load environment variables from .flaskenv file
    """

    __db_user = os.getenv("DB_USER")
    __db_password = os.getenv("DB_PASSWORD")
    __db_host = os.getenv("DB_HOST")
    __db_port = os.getenv("DB_PORT")
    __db_name = os.getenv("DB_NAME")

    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{__db_user}:{__db_password}@{__db_host}:{__db_port}/{__db_name}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=float(os.getenv("JWT_ACCESS_TOKEN_EXPIRES"))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        days=float(os.getenv("JWT_REFRESH_TOKEN_EXPIRES"))
    )
