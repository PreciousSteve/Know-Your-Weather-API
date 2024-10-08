from fastapi import APIRouter


router = APIRouter(tags=["Location Management"])


@router.post("/locations", description="Add a new location.")
