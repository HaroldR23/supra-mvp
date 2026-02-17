import datetime
from typing import Optional
from sqlalchemy.orm import Session
from ...db.models.user import UserModel, UserRoleEnum
from domain.ports.user_repository import UserRepositoryPort
from domain.models.user import User, UserRole


def _to_domain(model: UserModel) -> User:
    return User(
        id=str(model.id),
        email=str(model.email),
        hashed_password=str(model.hashed_password),
        role=UserRole(model.role.value),
        created_at=datetime.datetime.fromisoformat(str(model.created_at)),
    )


class UserRepository(UserRepositoryPort):
    def __init__(self, db: Session):
        self._db = db

    def get_by_email(self, email: str) -> Optional[User]:
        model = self._db.query(UserModel).filter(UserModel.email == email).first()
        return _to_domain(model) if model else None

    def get_by_id(self, user_id: str) -> Optional[User]:
        model = self._db.query(UserModel).filter(UserModel.id == user_id).first()
        return _to_domain(model) if model else None

    def create(self, user: User) -> User:
        model = UserModel(
            email=user.email,
            hashed_password=user.hashed_password,
            role=UserRoleEnum(user.role.value),
        )
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        return _to_domain(model)

    def list_all(self) -> list[User]:
        models = self._db.query(UserModel).all()
        return [_to_domain(m) for m in models]
