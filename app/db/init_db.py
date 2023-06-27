from sqlmodel import SQLModel

import app.models
from app.core.config import get_app_settings

from .session import engine

settings = get_app_settings()


def init_db():
    if settings.ENV_STATE == "dev":
        SQLModel.metadata.create_all(engine)
    else:
        raise RuntimeError
