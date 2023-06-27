from contextlib import asynccontextmanager
from sqlite3 import register_adapter

import pendulum as pnd
from fastapi import FastAPI

from app.db.init_db import init_db

from .config import get_app_settings

settings = get_app_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    register_adapter(pnd.DateTime, lambda val: val.isoformat(" "))
    try:
        init_db()
    except Exception as e:
        raise RuntimeError from e
    yield
    print("app is over")
