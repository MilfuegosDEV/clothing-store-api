from dotenv import load_dotenv
import os


class DBConfig:
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
