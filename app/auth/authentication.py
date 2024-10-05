from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.crud import user_crud
from app.core.security import verify_password


security_scheme = OAuth2PasswordBearer(tokenUrl="login")

def authenticate_user(session:Session, email:str, password:str):
    user = user_crud.get_user_by_email(session, email)
    if not user:
        return None
    if not verify_password(password, user.password):
        return None
    return user


