# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings

class Settings(BaseSettings):

    APP_NAME: str = "Log Analytics System"
    API_VERSION: str = "v1"

    # Database configuration
    MYSQL_HOST: str = "localhost"
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = ""
    MYSQL_PORT: str = "3306"
    MYSQL_DATABASE: str = "log_analytics"

    REDIS_URL: str = "redis://localhost:6379/0"
    
    class Config:
        env_file = ".env"
        
settings = Settings()