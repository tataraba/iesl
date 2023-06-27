from contextlib import asynccontextmanager
from sqlite3 import register_adapter

import pendulum as pnd
from fastapi import FastAPI

from app.db.init_db import init_db

from .config import get_app_settings

settings = get_app_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """A context manager that calls startup/shutdown hooks for the given
    application.

    Anything prior to `yield` will be called before app startup, whereas
    anything after will be called on app shutdown.

    Args:
        app: Cass pass a FastAPI instance, or passed as an attribute.

    Raises:
        RuntimeError: Will generate an error if app fails to startup.
    """

    register_adapter(pnd.DateTime, lambda val: val.isoformat(" "))
    try:
        init_db()
    except Exception as e:
        raise RuntimeError from e
    yield
    print("app is over")
