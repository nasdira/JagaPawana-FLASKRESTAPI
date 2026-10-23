import os
from datetime import timedelta
from dotenv import load_dotenv

# Memuat variabel dari file .env
load_dotenv()

# Mengambil URL dari DATABASE_URL atau SQLALCHEMY_DATABASE_URI
_url = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URI") or ""

# SQLAlchemy tidak menerima awalan "postgres://", jadi di-replace dengan "postgresql://"
if _url.startswith("postgres://"):
    _url = _url.replace("postgres://", "postgresql://", 1)

class Config:
    SQLALCHEMY_DATABASE_URI = _url

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "connect_args": {
            "options": f"-c search_path={os.getenv('DB_SCHEMA', 'public')},public"
        },
    }

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "rahasia_jwt_jagapawana_2026s")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.getenv("JWT_EXPIRES_MINUTES", 60)))