from pydantic_settings import BaseSettings
from pydantic import computed_field
from yookassa import Configuration

class Settings(BaseSettings):
    app_name: str = "MomBook"
    debug: bool = True

    yookassa_shop_id: str
    yookassa_secret_key: str

    admin_username: str
    admin_password: str
    jwt_secret: str

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

    frontend_url: str = "http://localhost:5173" 

    @computed_field
    @property
    def database_url(self) -> str:
        return f"postgresql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"

settings = Settings()

Configuration.account_id = settings.yookassa_shop_id
Configuration.secret_key = settings.yookassa_secret_key