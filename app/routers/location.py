from fastapi import APIRouter, Depends
from app.crud.location_crud import create_location
from app.database.db import get_db
from sqlalchemy.orm import Session
from app.schemas.location_schema import Location, LocationResponse
from app.auth.authentication import get_current_user

router = APIRouter(tags=["Location Management"])


@router.post("/locations", response_model=LocationResponse, description="Add a new location.")
async def new_location(location:Location, session:Session=Depends(get_db), current_user=Depends(get_current_user)):
    new_location = create_location(session=session, location=location, user_id=current_user.id)
    return new_location