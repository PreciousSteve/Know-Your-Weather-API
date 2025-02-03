from app.models.user import User
from sqlalchemy.orm import Session
from app.schemas import user_schema
from app.core.security import get_password_hash


def get_user_by_username(session: Session, username: str):
    return session.query(User).filter(User.username == username).first()


def get_user_by_email(session: Session, email: str):
    return session.query(User).filter(User.email == email).first()


def create_user(session: Session, user: user_schema.UserCreate):
    hashed_password = get_password_hash(user.password)
    new_user = User(username=user.username, email=user.email, hashed_password=hashed_password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


def update_profile(session: Session, existing_profile, profile: user_schema.UserUpdate):
    hashed_password = get_password_hash(profile.password)
    existing_profile.username = profile.username
    existing_profile.email = profile.email
    existing_profile.hashed_password = hashed_password
    session.commit()
    session.refresh(existing_profile)
    return existing_profile
