from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):
    DB_HOST: str
    DB_NAME: str
    DB_PORT: int
    DB_PASS: str
    DB_USER: str

    model_config = SettingsConfigDict(env_file=BASE_DIR/'.env')


settings = Settings()

    