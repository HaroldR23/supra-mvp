import os

database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
secret_key: str = os.getenv("SECRET_KEY", "your_secret_key")
environment: str = os.getenv("ENVIRONMENT", "production")
algorithm: str = "HS256"
access_token_expire_minutes: int = 30
