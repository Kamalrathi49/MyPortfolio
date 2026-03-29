from functools import lru_cache
from pathlib import Path
from typing import List, Set

from pydantic_settings import BaseSettings, SettingsConfigDict

_BACKEND_DIR = Path(__file__).resolve().parents[2]
_ENV_FILE = _BACKEND_DIR / ".env"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(_ENV_FILE),
        env_file_encoding="utf-8",
        extra="ignore",
    )

    database_url: str
    api_key: str
    smtp_host: str
    smtp_port: int = 587
    smtp_user: str
    smtp_password: str
    smtp_from: str = ""
    contact_notify_to: str = ""

    cors_origins: str = "https://kamalrathi.dev,https://www.kamalrathi.dev,http://localhost:5173,http://127.0.0.1:5173"

    cors_strict: bool = False

    def cors_origins_list(self) -> List[str]:
        from_env = [o.strip() for o in self.cors_origins.split(",") if o.strip()]
        if self.cors_strict:
            return from_env
        dev_origins = [
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://localhost:3000",
            "http://127.0.0.1:3000",
        ]
        seen: Set[str] = set()
        merged: List[str] = []
        for o in from_env + dev_origins:
            if o and o not in seen:
                seen.add(o)
                merged.append(o)
        return merged

    def effective_smtp_from(self) -> str:
        return self.smtp_from or self.smtp_user

    def effective_notify_to(self) -> str:
        return self.contact_notify_to or self.smtp_user


@lru_cache
def get_settings() -> Settings:
    return Settings()
