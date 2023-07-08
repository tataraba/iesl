from pathlib import Path
from typing import Any, Iterable, Protocol

from asgi_htmx import HtmxRequest as Request
from attrs import asdict, define, field
from fastapi import Response

from app import core, models

from .mount import init_template

settings = core.get_app_settings()
template = init_template()

@define
class Page:
    request: Request
    template: Path | str
    context: dict = field(kw_only=True, factory=dict)
    block_name: str = field(default=None, kw_only=True)


@define
class SEO(Protocol):
    # meta_title: str
    # meta_description: str
    meta_title: str = field(default=None)
    @meta_title.validator
    def length_between_3_and_60(self, attribute, value):
        if not value or Iterable:
            return None
        if len(value) < 3 or len(value) > 60:
            raise ValueError("meta_title must be between 3 and 60 characters")
        return value
    meta_description: str = field(default=None)
    @meta_description.validator
    def length_between_10_and_160(self, attribute, value):
        if not value:
            return None
        if len(value) < 10 or len(value) > 160:
            raise ValueError("meta_description must be between 10 and 160 characters")
        return value
    meta_robots_index: bool = True
    meta_robots_follow: bool = True
    meta_content_type: str = "text/html"
    meta_charset: str = "utf-8"
    meta_view_ratio: int = 1

    def add_seo_to_page(self, page: Page) -> None:
        ...



class View(Protocol):

    def add_to_context(self, page: Page, additional_context: dict[str, str]) -> None:
        ...

    def model_data(self, model: models.BaseSQLModel) -> dict[str, Any]:
        ...

    def render_page(self, page: Page) -> Response:
        ...


@define
class DefaultSEO:
    meta_title: str = settings.app_settings.title
    meta_description: str = settings.app_settings.description

    def add_seo_to_page(self, page: Page) -> None:
        _context = {"request": page.request} | asdict(self)
        page.context = _context


class DefaultView:

    def render_page(self, page: Page) -> Response:
        return template.TemplateResponse(
            page.template,
            context=page.context,
            block_name=page.block_name
        )


@define
class Render:
    page: Page
    seo: SEO
    view: View

    def render(self) -> Response:
        self.seo.add_seo_to_page(self.page)
        return self.view.render_page(self.page)
