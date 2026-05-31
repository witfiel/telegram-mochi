from pydantic_settings import BaseSettings
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):

    api_id: int = Field(..., env="TELEGRAM_API_ID")
    api_hash: str = Field(..., env="TELEGRAM_API_HASH")

    session_path: str = Field("./session", env="SESSION_PATH")

    database_url: str = Field("sqlite+aiosqlite:///./telegram_client.db", env="DATABASE_URL")

    proxy_enabled: bool = Field(False, env="PROXY_ENABLED")
    proxy_type: Optional[str] = Field(None, env="PROXY_TYPE")
    proxy_host: Optional[str] = Field(None, env="PROXY_HOST")
    proxy_port: Optional[str] = Field(None, env="PROXY_PORT")
    theme: str = Field("light", env="THEME")
    language: str = Field("en", env="LANGUAGE")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()
