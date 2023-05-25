from pydantic import BaseSettings


class EnvBaseSettings(BaseSettings):
    class Config:
        env_file = '.env'


class ApiSettings(EnvBaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = 8000
    reload: bool = True


class DatabaseSettings(EnvBaseSettings):
    uri: str = f"mongodb+srv://Tormato:Voin5aturna@amazoncluster.1pngkd7.mongodb.net/?retryWrites=true&w=majority"
    database: str = 'SportPitDB'
    collection: str = 'SportPitColl'


api_settings = ApiSettings()
database_settings = DatabaseSettings()
