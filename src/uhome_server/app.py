"""FastAPI application for the standalone uHOME server."""

from fastapi import FastAPI

from uhome_server.routes.containers import router as containers_router
from uhome_server.routes.home_assistant import create_ha_routes
from uhome_server.routes.library import router as library_router
from uhome_server.routes.network import router as network_router
from uhome_server.routes.platform import create_platform_routes


def create_app() -> FastAPI:
    app = FastAPI(title="uHOME Server", version="0.1.0")
    app.include_router(create_ha_routes())
    app.include_router(create_platform_routes())
    app.include_router(library_router)
    app.include_router(containers_router)
    app.include_router(network_router)
    return app


app = create_app()
