from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from config import settings
DB_URL = f'postgresql://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}'

sync_engine = create_engine(url  = DB_URL)
session_factory = sessionmaker(bind = sync_engine)
class Base(DeclarativeBase):
    pass