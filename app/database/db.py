from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL,
                       pool_size=10,
                       max_overflow=20,
                       pool_timeout=30,
                       pool_recycle=1800)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
