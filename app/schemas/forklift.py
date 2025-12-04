
from pydantic import BaseModel

class ForkliftBase(BaseModel):
    serial_number: str
    brand: str
    model: str

class ForkliftCreate(ForkliftBase):
    is_active: bool = True

class ForkliftResponse(ForkliftBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True