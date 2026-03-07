"""FastAPI application for the standalone uHOME server."""

from fastapi import FastAPI

from uhome_server.routes.home_assistant import create_ha_routes
from uhome_server.routes.platform import create_platform_routes


def create_app() -> FastAPI:
    app = FastAPI(title="uHOME Server", version="0.1.0")
    app.include_router(create_ha_routes())
    app.include_router(create_platform_routes())
    return app


app = create_app()
