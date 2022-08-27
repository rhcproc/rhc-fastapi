
import os

from pydantic import BaseSettings, Field
from fastapi import FastAPI

__AUTHOR__ = "Rhcproc"
__VERSION__ = "0.1.0"

APP_NAME = "RHCPROC-API"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Settings(BaseSettings):
    # Description settings
    title: str = Field(default=APP_NAME)
    version: str = Field(default=__VERSION__)
    app_name: str = Field(APP_NAME, env='APP_NAME')
    description: str = "Welcome"
    term_of_service: str = ""
    contact_name: str = __AUTHOR__
    contact_url: str = ""
    contact_email: str = "rhcproc@gmail.com"
    docs_url: str = "/docs" # Documentation url
    secret_key: str = "super-secret" # JWT settings
    jwt_algorithm: str = "HS256"
    jwt_access_expires: int = 3600 * 24 * 7
    jwt_refresh_expires: int = 3600 * 24 * 30
    slow_api_time: float = 0.5 # Slow API settings
    dynamodb_access_key: str = Field(None, env='DYNAMODB_ACCESS_KEY')
    dynamodb_secret_key: str = Field(None, env='DYNAMODB_SECRET_KEY')
    dynamodb_state: str = Field(None, env='DYNAMODB_STATE')
    dynamodb_endpoint: str = Field(None, env='DYNAMODB_ENDPOINT')
    dynamodb_region: str = Field("ap-northeast-2", env='DYNAMODB_REGION')
    name: str = Field(None, env='NAME')

    class Config:
        env_file = "./settings.ini"
        env_file_encoding = "utf-8"
        
    def init_app(self, app: FastAPI):
        ...


class TestSettings(Settings):
    """Test settings"""
    slow_api_time: float = 1.0

print(BASE_DIR)
settings = Settings()


if __name__ == '__main__':
    print(settings.dict())
    print(BASE_DIR)
