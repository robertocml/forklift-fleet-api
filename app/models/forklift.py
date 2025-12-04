from sqlalchemy import Column, Integer, String, Boolean
from app.db.database import Base

class Forklift(Base):
    __tablename__ = "forklifts"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String, unique=True, index=True, nullable=False)
    brand = Column(String, nullable=False)
    model = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)