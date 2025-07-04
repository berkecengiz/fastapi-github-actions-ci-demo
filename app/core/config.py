from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )

    app_name: str = Field(default="FastAPI CI Demo")
    app_version: str = Field(default="1.0.0")
    debug: bool = Field(default=False)

    host: str = Field(default="0.0.0.0")  # nosec
    port: int = Field(default=8000)

    allowed_origins: List[str] = Field(default=["*"])
    allowed_hosts: List[str] = Field(default=["localhost", "127.0.0.1"])

    log_level: str = Field(default="INFO")


@lru_cache()
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
