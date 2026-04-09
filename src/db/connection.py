""" Database connector. """

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from contextlib import contextmanager
from typing import Generator, Any

engine = create_engine('sqlite:///ficha_rdsa.db', echo=True)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):...

@contextmanager
def session_scope() -> Generator[Session, Any, None]:
    """
    Creates a temporary session within a scope that can be accessed with a `with`statement.
    
    Automatically performs:
    - Opens the session.
    - Commits at the end of the operation.
    - Rollback in case of error.
    - Closes the temporary session.
    """
    try:
        session = SessionLocal()
        yield session
        session.commit()
    except Exception as e:
        print('Erro de sessão:', e)
        session.rollback()
    finally:
        session.close()

def create_tables() -> None:
    """ Creates all defined tables if it not exists. """
    Base.metadata.create_all(engine)


__all__ = [
    'Base',
    'session_scope'
]