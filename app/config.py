import os
from functools import lru_cache
from typing import List

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings with environment variable support"""
    
    # App settings
    app_name: str = Field(default="FastAPI Demo", env="APP_NAME")
    app_version: str = Field(default="1.0.0", env="APP_VERSION")
    debug: bool = Field(default=False, env="DEBUG")
    
    # Server settings
    host: str = Field(default="0.0.0.0", env="HOST")
    port: int = Field(default=8000, env="PORT")
    workers: int = Field(default=1, env="WORKERS")
    
    # CORS settings
    allowed_origins: List[str] = Field(
        default=["*"], 
        env="ALLOWED_ORIGINS"
    )
    allowed_hosts: List[str] = Field(
        default=["*"], 
        env="ALLOWED_HOSTS"
    )
    
    # Logging
    log_level: str = Field(default="INFO", env="LOG_LEVEL")
    
    # Security
    secret_key: str = Field(
        default="your-secret-key-change-in-production", 
        env="SECRET_KEY"
    )

    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()


# Create settings instance
settings = get_settings()