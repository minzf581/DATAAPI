from pydantic_settings import BaseSettings
from functools import lru_cache
import os
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # 数据库配置
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:password@localhost/db")
    
    # Google Cloud配置
    GOOGLE_CLOUD_PROJECT: str = os.getenv("GOOGLE_CLOUD_PROJECT", "your-project-id")
    GOOGLE_CLOUD_BUCKET: str = os.getenv("GOOGLE_CLOUD_BUCKET", "your-bucket-name")
    
    # 加密配置
    ENCRYPTION_KEY_LENGTH: int = 32  # AES-256
    
    # API配置
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "EON Protocol Data API"

@lru_cache()
def get_settings():
    return Settings() 