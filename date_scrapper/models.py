from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

from date_scrapper import settings

DeclarativeBase = declarative_base()


def create_db_connection():
    """Returns sqlalchemy engine instance."""
    return create_engine(URL(**settings.DATABASE))


def create_table(engine):
    """Create all tables stored in this metadata."""
    DeclarativeBase.metadata.create_all(engine)


class Copyrights(DeclarativeBase):
    """Sqlalchemy copyrights model."""
    __tablename__ = 'copyrights'
    id = Column(Integer, primary_key=True)
    url = Column('url', String, nullable=True)
    copy_right = Column('copyright', Integer, nullable=True)
    status_code = Column('status_code', Integer)
