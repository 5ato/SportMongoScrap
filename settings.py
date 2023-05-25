from pydantic import BaseSettings


class EnvBaseSettings(BaseSettings):
    class Config:
        env_file = '.env'


class ApiSettings(EnvBaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    reload: bool = True

    class Config:
        env_prefix = 'api_'


class DatabaseSettings(EnvBaseSettings):
    uri: str = "mongodb://127.0.0.1:27017"
    database: str = 'SportPitDB'
    collection: str = 'SportPitColl'

    class Config:
        env_prefix = 'mongo_'


api_settings = ApiSettings()
database_settings = DatabaseSettings()
