"""
Carga de variables de entorno desde .env usando pydantic y dotenv.
"""
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    OPENAI_API_KEY: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()
