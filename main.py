import uvicorn

from settings import api_settings


if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host=api_settings.server_host,
        port=api_settings.server_port,
        reload=api_settings.reload,
    )
