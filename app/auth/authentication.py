from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from typing import Optional, Annotated
from datetime import datetime, timezone, timedelta
from app.crud import user_crud
from app.core.security import verify_password
from app.core import config
from app.database.db import get_db


security_scheme = OAuth2PasswordBearer(tokenUrl="login")


def authenticate_user(session: Session, email: str, password: str):
    user = user_crud.get_user_by_email(session, email)
    if not user:
        print("user not founds")
        return False
    if not verify_password(password, user.hashed_password):
        print("password mismatch")
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta]):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=20)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


def get_current_user(token: Annotated[str, Depends(security_scheme)], session=Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = user_crud.get_user_by_username(session, username=username)
    if user is None:
        raise credentials_exception
    return user
