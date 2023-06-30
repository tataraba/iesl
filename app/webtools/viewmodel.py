import logging
from pathlib import Path

from attrs import asdict, define, field
from fastapi import Request

from app.core.config import get_app_settings
from app.models.base import BaseSQLModel

from .pagebuilder import PageBuilder

logger = logging.getLogger(__name__)
settings = get_app_settings()


@define
class BaseView(PageBuilder):

    request: Request | None = None
