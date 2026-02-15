from enum import Enum
from typing import Optional
from dataclasses import dataclass
from datetime import datetime


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    TECHNICIAN = "TECHNICIAN"


@dataclass
class User:
    id: str
    email: str
    hashed_password: str
    role: UserRole
    created_at: datetime
