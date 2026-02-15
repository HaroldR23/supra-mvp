"""Create initial users (admin and technician). Run after migrations."""
import datetime

from adapters.db.repositories.user_repository import UserRepository
from adapters.db.models.user import UserModel
from adapters.db.session import SessionLocal
from api.deps import get_password_hash
from domain.models.user import User, UserRole

INITIAL_USERS = [
    ("admin@workshop.local", "admin123", UserRole.ADMIN),
    ("tech@workshop.local", "tech123", UserRole.TECHNICIAN),
] 


def main():
    db = SessionLocal()
    try:
        repo = UserRepository(db)
        for email, password, role in INITIAL_USERS:
            existing = db.query(UserModel).filter(UserModel.email == email).first()
            if existing:
                print(f"User {email} ({role.value}) already exists")
                continue
            user = User(
                id="",
                email=email,
                hashed_password=get_password_hash(password),
                role=role,
                created_at=datetime.datetime.now(datetime.timezone.utc),
            )
            repo.create(user)
            print(f"Created {role.value.lower()} user: {email} / {password}")
    except Exception as e:
        print(f"Error creating user: {e}")
    finally:
        db.close()
