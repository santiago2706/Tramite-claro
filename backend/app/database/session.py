from sqlalchemy import create_engine
from app.core.settings import settings
from sqlalchemy.orm import sessionmaker, Session
from collections.abc import Generator

engine = create_engine(
    settings.database_url,
    echo = True,
)

SessionLocal = sessionmaker(
    bind = engine,
    autoflush = False,
    autocommit = False,
)

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

