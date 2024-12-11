from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database.config import get_database_url

engine = create_engine(get_database_url(), echo=True)
SessionFactory = sessionmaker(bind=engine)


def init_db():
    from database.models import Base
    Base.metadata.create_all(engine)
