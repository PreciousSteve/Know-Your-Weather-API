from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.authentication import get_current_user
from app.database.db import get_db
from app.schemas.user_schema import UserUpdate
from app.crud.user_crud import update_profile, get_user_by_username, get_user_by_email


router = APIRouter(tags=["User Management"], prefix="/user")


@router.get("/profile", description="Get profile details")
async def get_my_profile(
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    data = {"message": f"Hi, {current_user.username}", "email": current_user.email}
    return data


@router.put("/profile/{username}/", description="Edit profile details")
async def edit_profile(
    username: str,
    profile: UserUpdate,
    session: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    existing_profile = get_user_by_username(session=session, username=username)

    if existing_profile is None:
        raise HTTPException(status_code=404, detail="Incorrect username or Username not found")
    if existing_profile.id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to edit this profile")

    # Check for duplicate email, but allow the same email as the current one
    if profile.email and profile.email != existing_profile.email:
        existing_user_by_email = get_user_by_email(session, profile.email)
        if existing_user_by_email:
            raise HTTPException(status_code=409, detail="Email already exists")

    # Check for duplicate username, but allow the same username as the current one
    if profile.username and profile.username != existing_profile.username:
        existing_user_by_username = get_user_by_username(session, profile.username)
        if existing_user_by_username:
            raise HTTPException(status_code=409, detail="Username already exists")

    updated_profile = update_profile(
        session=session, existing_profile=existing_profile, profile=profile
    )
    response_data = {
        "status_code": 200,
        "message": "Update Successful!",
        "id": updated_profile.id,
        "username": updated_profile.username,
        "email": updated_profile.email
    }
    return response_data
