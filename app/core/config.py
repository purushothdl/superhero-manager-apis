from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    FIRST_ADMIN_USERNAME: str
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings() 