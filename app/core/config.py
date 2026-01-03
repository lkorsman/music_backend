from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    db_host: str = "localhost"
    db_user: str = "root"
    db_password: str = Field(..., env="DB_PASSWORD")
    db_name: str = "music_app"

    class Config:
        env_file = ".env"

settings = Settings()
