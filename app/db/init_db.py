from sqlmodel import SQLModel

# Need to import models for SQLModel to build tables
import app.models  # noqa
from app.core.config import get_app_settings

from .session import engine

settings = get_app_settings()


def init_db():
    """Initialize a SQL database.

    Raises:
        RuntimeError: Error if database fails to generate tables.
    """
    # if settings.ENV_STATE == "dev":
    #     SQLModel.metadata.create_all(engine)
    # else:
    #     raise RuntimeError

    try:
        SQLModel.metadata.create_all(engine)
    except Exception as e:
        raise RuntimeError from e
