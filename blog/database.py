from lib2to3.pytree import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQL_ALCHEMY_DATABASE_URL = 'sqlite:///blog.db'

engine = create_engine(SQL_ALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

Base = declarative_base()
session_local = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()




