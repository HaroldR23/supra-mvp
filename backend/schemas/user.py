from datetime import datetime
from pydantic import BaseModel

from domain.models.user import UserRole


class UserBase(BaseModel):
    email: str
    role: UserRole


class UserCreate(BaseModel):
    email: str
    password: str
    role: UserRole = UserRole.TECHNICIAN


class UserResponse(BaseModel):
    id: str
    email: str
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True
