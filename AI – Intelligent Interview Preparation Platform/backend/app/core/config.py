from anyio.functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME:str = Field(default="InterviewGPT")

    APP_VERSION:str=Field(default="1.0")
    API_PREFIX:str=Field(default="/api/v1")

    ENVIRONMENT :str= Field(default="development")

    DEBUG:bool = True

    HOST :str

    PORT :int

    DATABASE_URL :str
    ALEMBIC_DATABASE_URL:str
    SECRET_KEY :str
    ALGORITHM: str

    ACCESS_TOKEN_EXPIRE_MINUTES :int
    REFRESH_TOKEN_EXPIRE_DAYS: int
    REDIS_HOST: str
    REDIS_PORT: int
    EMBEDDING_MODEL :str
    CHROMA_PATH:str
    CHROMA_COLLECTION:str
    CELERY_BROKER_URL: str
    CELERY_RESULT_BACKEND: str
    REDIS_URL :str
    UPLOAD_DIRECTORY:str
    GROQ_API_KEY:str
    GROQ_MODEL:str
    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False,
        extra='ignore'
    )

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()