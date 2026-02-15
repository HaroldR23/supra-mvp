from domain.ports.user_repository import UserRepositoryPort
from domain.models.user import User
from api.deps import verify_password, get_password_hash, create_access_token


def authenticate_user(repo: UserRepositoryPort, email: str, password: str) -> User | None:
    user = repo.get_by_email(email)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user


def login_user(repo: UserRepositoryPort, email: str, password: str) -> str | None:
    user = authenticate_user(repo, email, password)
    if not user:
        return None
    return create_access_token(data={"sub": user.id, "email": user.email})
