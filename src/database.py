from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from settings import DATABASE_URI
from sqlalchemy.orm import Session
from contextlib import contextmanager

# db engine connects Python to db server
engine = create_engine(DATABASE_URI)


class Base(DeclarativeBase):
    pass


def create_table():
    Base.metadata.create_all(engine)


# a cm is a way to manage the setup and clean up resources such as opening/closing db in a clean and controlled manner
@contextmanager
def get_db_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
