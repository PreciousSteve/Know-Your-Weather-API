from sqlalchemy import Column, Integer, String
from app.database.db import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)

    locations = relationship("Location", back_populates="user")
