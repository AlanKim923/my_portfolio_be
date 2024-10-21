from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

from app.config.database import DatabaseConfig

Base = declarative_base()

engine = create_engine(
    DatabaseConfig.URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


class BaseRepository:
    def __init__(self, db: Session = SessionLocal):
        self.db = db
        self.model = Base
