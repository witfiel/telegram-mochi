from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
from typing import Optional

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        env_prefix="TELEGRAM_"
    )

    api_id: int = Field(..., description="Telegram API ID")
    api_hash: str = Field(..., description="Telegram API Hash")

    session_path: str = Field("./session")

    database_url: str = Field("sqlite+aiosqlite:///./telegram_client.db")

    proxy_enabled: bool = Field(False)
    proxy_type: Optional[str] = Field(None)
    proxy_host: Optional[str] = Field(None)
    proxy_port: Optional[str] = Field(None)
    theme: str = Field("light")
    language: str = Field("en")

settings = Settings()
