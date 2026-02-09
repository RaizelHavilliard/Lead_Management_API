from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None

class LeadUpdate(BaseModel):
    status: str

class LeadOut(BaseModel):
    id: int
    name: str
    email: str
    phone: Optional[str]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
