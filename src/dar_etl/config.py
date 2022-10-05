from pydantic import BaseSettings

from dar_etl.version import __version__


class Config(BaseSettings):
    version: str = __version__
    kafka_host: str
    kafka_port: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
