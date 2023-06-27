from fastapi import FastAPI

from app.core.config import get_app_settings
from app.core.events import lifespan
from app.db.init_db import init_db
from app.webtools import mount

from .views import routes

settings = get_app_settings()


def get_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)
    mount.incl_static(app)
    # app.include_router(routes)

    return app


app = get_app()
