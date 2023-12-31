from asgi_htmx import HtmxMiddleware
from fastapi import FastAPI

from app.core import get_app_settings, lifespan, setup_rich_logger
from app.db.init_db import init_db
from app.webtools import mount

from .views import routes

settings = get_app_settings()
setup_rich_logger()

def get_app() -> FastAPI:
    """Create a FastAPI factory that returns an `app` instance. App settings
    are defined in settings with `fastapi_kwargs`.
    """

    app = FastAPI(lifespan=lifespan, **settings.fastapi_kwargs)
    app.add_middleware(HtmxMiddleware)
    mount.incl_static(app)
    app.include_router(routes)

    return app


app = get_app()
