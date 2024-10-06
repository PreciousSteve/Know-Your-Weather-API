from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import user_schema
from app.database.db import get_db
from app.crud.user_crud import get_user_by_username, get_user_by_email, create_user


router = APIRouter(tags=["Authentication"], prefix="/auth")


@router.post("/register/", description="Endpoint to create new user")
async def create_new_user(user:user_schema.UserCreate, session:Session = Depends(get_db)):
    existing_user_by_email = get_user_by_email(session, user.email)
    if existing_user_by_email:
        raise HTTPException(status_code=409, detail="User already exists")
    
    existing_user_by_username = get_user_by_username(session, user.username)
    if existing_user_by_username:
        raise HTTPException(status_code=409, detail="Username already exists")
    
    new_user = create_user(session=session, user=user)
    return {"message":"User created successfully"}
    