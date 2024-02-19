from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, Engine as SqlEngine
from config import DATABASE_CONNECTION_URI


class Database(DeclarativeBase):
    pass


Engine: SqlEngine = create_engine(
    DATABASE_CONNECTION_URI,
    pool_size=True,
    max_overflow=0,
    pool_recycle=3600,
)
