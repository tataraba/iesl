import logging
from pathlib import Path
from typing import Any, Protocol

from asgi_htmx import HtmxRequest as Request
from attrs import define, field

from app.core.config import get_app_settings
from app.models.base import BaseSQLModel

from .mount import init_template

logger = logging.getLogger(__name__)

settings = get_app_settings()
_template = init_template()

@define
class PageBuilder(Protocol):

    request: Request = None
    template: Path | str = None
    context: dict = field(kw_only=True, factory=dict)
    block_name: str = field(default=None, kw_only=True)
    model: BaseSQLModel = field(default=None, kw_only=True)


    @classmethod
    def include_context(cls, **kwargs: dict[str, Any]):
        return cls(context=kwargs)

    def add_seo_metadata(self, seo: SEO) -> None:
        ...

    def update_context(self, **kwargs: dict[str, Any]) -> None:
        self.context.update(kwargs)

    def render(self, block_name: str | None = None) -> str:

        _context = self.context

        return _template.TemplateResponse(
            self.template,
            context=_context,
            block_name=self.block_name
        )


@define
SEO:
