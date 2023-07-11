import logging

from asgi_htmx import HtmxRequest as Request
from fastapi import APIRouter
from jinja2_fragments.fastapi import Jinja2Blocks

from app.core.config import get_app_settings
from app.webtools.viewmodel import DefaultPageMeta, DefaultView, Page, Render

logger = logging.getLogger(__name__)
settings = get_app_settings()
router = APIRouter()

templates = Jinja2Blocks(
    settings.TEMPLATE_DIR,
)

@router.get("/")
def homepage(request: Request):
    page = Page(request=request, template="main.html")
    meta = DefaultPageMeta()
    view = DefaultView()

    homepage = Render(page=page, meta_tags=meta, view=view)

    return homepage.render()
