from pydantic import BaseModel
from typing import Optional


class Location(BaseModel):
    name: str
    latitude: float
    longitude: float
    description: Optional[str] = None

    class Config:
        orm_mode = True


class LocationResponse(Location):
    id: int
