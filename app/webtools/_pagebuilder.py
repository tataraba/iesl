from pathlib import Path
from typing import Any, Protocol, runtime_checkable

from asgi_htmx import HtmxRequest as Request
from attrs import define, field
from fastapi import Response

from app import core

from .mount import init_template

settings = core.get_app_settings()
template = init_template()

@define
class Page:
    """Defines the base model for creating a page response."""
    request: Request
    template: Path | str
    context: dict = field(kw_only=True, factory=dict)
    block_name: str = field(default=None, kw_only=True)


@runtime_checkable
class PageMeta(Protocol):

    meta_data: dict[str, Any] = field(factory=dict)

    def add_meta_tags(self, page: Page) -> None:
        ...

@runtime_checkable
class View(Protocol):

    def model_data(self) -> dict[str, Any] | None:
        ...

    def render_page(self, page: Page) -> Response:
        ...

