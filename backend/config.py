from pydantic_settings import BaseSettings
from functools import lru_cache
from dotenv import load_dotenv
import os

load_dotenv()

database_url: str = os.environ.get("DATABASE_URL", "sqlite:///./test.db")
secret_key: str = os.environ.get("SECRET_KEY", "your-secret-key-for-jwt")
environment: str = os.environ.get("ENVIRONMENT", "development")
algorithm: str = "HS256"
access_token_expire_minutes: int = 30
