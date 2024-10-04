from app.models.user import User
from sqlalchemy.orm import Session


def get_user_by_username(session:Session, username:str):
    return session.query(User).filter(User.username == username).first()


def get_user_by_email(session:Session, email:str):
    return session.query(User).filter(User.email == email).first()
