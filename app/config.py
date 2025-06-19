# app/config.py - Pydantic V2 compatible
import os
from functools import lru_cache
from typing import List

from pydantic import Field, ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Use ConfigDict instead of class Config
    model_config = ConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    # App settings - environment variables are auto-detected by field name
    app_name: str = Field(default="FastAPI CI Demo")
    app_version: str = Field(default="1.0.0")
    debug: bool = Field(default=False)

    # Server settings
    host: str = Field(default="0.0.0.0")
    port: int = Field(default=8000)

    # CORS settings
    allowed_origins: List[str] = Field(default=["*"])
    allowed_hosts: List[str] = Field(default=["localhost", "127.0.0.1"])

    # Logging
    log_level: str = Field(default="INFO")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
