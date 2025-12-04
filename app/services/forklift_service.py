from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.forklift import Forklift
from app.schemas.forklift import ForkliftCreate

def create_new_forklift(db: Session, data: ForkliftCreate):
    # Validar serial repetido
    exists = db.query(Forklift).filter(Forklift.serial_number == data.serial_number).first()
    if exists:
        raise HTTPException(status_code=400, detail="Serial number already exists")

    forklift = Forklift(
        serial_number=data.serial_number,
        brand=data.brand,
        model=data.model,
        is_active=data.is_active,
    )

    db.add(forklift)
    db.commit()
    db.refresh(forklift)
    return forklift


def get_all_forklifts(db: Session):
    return db.query(Forklift).all()