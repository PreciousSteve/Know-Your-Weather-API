from app.models.locations import Location
from sqlalchemy.orm import Session
from app.schemas import location_schema

def create_location(session:Session, location:location_schema.Location, user_id:int):
    new_location = Location(name=location.name, latitude=location.latitude, longitude=location.longitude, description=location.description, user_id=user_id)
    
    session.add(new_location)
    session.commit()
    session.refresh(new_location)
    
    return new_location
    