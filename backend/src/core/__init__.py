from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List
from functools import lru_cache
import os
from dotenv import load_dotenv, find_dotenv

ACCEPTED_ENVS: List[str] = ["local", "test", "production"]


class Settings(BaseSettings):
    origins: List[str]
    api_v1_str: str = "/api/v1"
    aws_secret_access_key: str
    aws_secret_key: str
    aws_db_table_name: str


class SettingsLocal(Settings):
    origins: List[str] = ["http://localhost:8080"]


class SettingsProd(Settings):
    model_config = SettingsConfigDict()


@lru_cache
def build_settings() -> Settings:
    env: str | None = os.getenv("ENV")

    if env is None:
        raise Exception("The 'ENV' environment variable can't be None")

    env = env.strip()

    if env not in ACCEPTED_ENVS:
        raise Exception(
            f"{env} is not an allowed environment for the 'ENV' variable.\n Accepcted values are: {ACCEPTED_ENVS}"
        )

    print(f"api_environment: {env}")

    if env == "local":
        env_file_path: str = find_dotenv(f".env.{env}")
        load_dotenv(dotenv_path=env_file_path)
        return SettingsLocal()  # pyright: ignore reportCallIssue
    else:
        # prod will not have an .env file.
        # environment variables will be defined directly in the node running the api
        # Ignore reportCallIssue because all class prop values get automatically injected by Pydantic
        return SettingsProd()  # pyright: ignore reportCallIssue
