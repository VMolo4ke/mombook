from pydantic_settings import BaseSettings
from pydantic import computed_field

class Settings(BaseSettings):
    app_name: str = "MomBook"
    debug: bool = True

    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int

    cors_origins: list = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ]
    static_dir: str = "static"
    image_dit: str = "static/image"

    @computed_field
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

settings = Settings()
