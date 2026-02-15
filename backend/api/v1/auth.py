from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from adapters.db.session import get_db
from adapters.db.repositories.user_repository import UserRepository
from api.deps import get_current_user
from domain.models.user import User
from schemas.auth import LoginRequest, Token
from schemas.user import UserResponse
from use_cases.auth import login_user

router = APIRouter()


@router.post("/login", response_model=Token)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    token = login_user(repo, request.email, request.password)
    if not token:
        from fastapi import HTTPException
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return Token(access_token=token)


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return UserResponse(
        id=current_user.id,
        email=current_user.email,
        role=current_user.role,
        created_at=current_user.created_at,
    )
