from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.forklift import ForkliftCreate, ForkliftResponse
from app.services.forklift_service import create_new_forklift, get_all_forklifts




router = APIRouter(prefix="/forklifts", tags=["Forklifts"])



@router.post("/", response_model=ForkliftResponse)
def create_forklift(data: ForkliftCreate, db: Session = Depends(get_db)):
    return create_new_forklift(db, data)


@router.get("/", response_model=list[ForkliftResponse])
def get_forklifts(db: Session = Depends(get_db)):
    return get_all_forklifts(db)