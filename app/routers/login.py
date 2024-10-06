from fastapi import APIRouter, Depends, status, HTTPException, Form, status
from sqlalchemy.orm import Session
from datetime import timedelta
from app.database.db import get_db
from app.schemas.user_schema import Login
from app.auth.authentication import authenticate_user, create_access_token
from app.core import config
from app.utils.json_response import auth_response


router = APIRouter(tags=["Authentication"], prefix="/auth")

@router.post("/login/", description="Authenticate user with email and password. Returns an access token upon successful login.")
def user_login(form_data:Login, session:Session=Depends(get_db)):
    user = authenticate_user(session, form_data.email, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Incorrect Email or Password",
                            headers ={"WWW-Authenticate":"Bearer"})
        
    access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    
    return auth_response(
        status_code=200,
        message="Login successful",
        access_token=access_token,
        token_type ="Bearer",
        data={"user_id": user.id, "email": user.email, "username": user.username}
    )