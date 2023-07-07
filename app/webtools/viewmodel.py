import logging

from attrs import define
from fastapi import Request

from app.core.config import get_app_settings
from app.models.base import BaseSQLModel

from .pagebuilder import PageBuilder

logger = logging.getLogger(__name__)
settings = get_app_settings()


@define
class BaseView(PageBuilder):

    request: Request | None = None
    seo: dict | None = None
    model: BaseSQLModel | None = None


    def to_context(self) -> dict:
        return {"request": self.request | self.seo}


@define
class IndexView(BaseView):
    pass

