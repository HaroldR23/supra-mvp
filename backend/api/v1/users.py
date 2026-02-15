from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from adapters.db.session import get_db
from adapters.db.repositories.user_repository import UserRepository
from api.deps import require_admin, get_password_hash
from domain.models.user import User
from schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.get("/users", response_model=list[UserResponse])
def list_users(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    repo = UserRepository(db)
    users = repo.list_all()
    return [
        UserResponse(id=u.id, email=u.email, role=u.role, created_at=u.created_at)
        for u in users
    ]


@router.post("/users", response_model=UserResponse)
def create_user(
    data: UserCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    repo = UserRepository(db)
    existing = repo.get_by_email(data.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    user = User(
        id="",
        email=data.email,
        hashed_password=get_password_hash(data.password),
        role=data.role,
        created_at=datetime.utcnow(),
    )
    created = repo.create(user)
    return UserResponse(
        id=created.id,
        email=created.email,
        role=created.role,
        created_at=created.created_at,
    )
