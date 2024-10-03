from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.core import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL, 
                       pool_size=10,   # The number of connections to keep in the pool
                       max_overflow=20, # The number of additional connections to allow if the pool is full
                       pool_timeout=30,  # Timeout in seconds to wait for a connection
                       pool_recycle=1800  # Recycle connections after 30 minutes
)

SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()