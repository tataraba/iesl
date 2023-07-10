from typing import Any

from attrs import asdict, define
from fastapi import Response

from ._pagebuilder import Page, PageMeta, View
from .metadata import HTMLMetaData
from .mount import init_template

template = init_template()

class DefaultPageMeta:
    """Interface for creating the HTML page metadata elements,
    which match the defaults set in `HTMLMetaData` class.
    """

    meta_data = asdict(HTMLMetaData())

    def add_meta_tags(self, page: Page) -> None:
        _context = {"request": page.request} | self.meta_data
        page.context = _context


class DefaultView:
    """Interface for creating a "default" page view, sending
    only the most basic request and context. Also contains
    the function that sends response to front end.
    """

    def model_data(self) -> dict[str, Any] | None:
        return None

    def render_page(self, page: Page) -> Response:
        return template.TemplateResponse(
            page.template,
            context=page.context,
            block_name=page.block_name
        )


@define
class Render:
    page: Page
    meta_tags: PageMeta
    view: View

    def render(self) -> Response:
        self.meta_tags.add_meta_tags(self.page)
        _data_for_context = self.view.model_data()
        if _data_for_context:
            self.page.context.update(_data_for_context)
        return self.view.render_page(self.page)
