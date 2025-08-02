import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    """API key Chat GPT"""
    openapi_key: str = os.getenv("OPENAPI_KEY")

    """PostgreSQL connections for db"""
    database_url: str = os.getenv("DATABASE_URL")

    """Debug"""
    debug: bool = True

    """Token bot"""
    token: str = os.getenv("TOKEN")

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        if not self.token:
            raise ValueError("TOKEN environment variable is not set!")


settings = Settings()
