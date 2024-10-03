from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from sqlalchemy.orm import Session

security_scheme = OAuth2PasswordBearer(tokenUrl="login")

