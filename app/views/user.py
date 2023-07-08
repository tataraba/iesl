import logging

from asgi_htmx import HtmxRequest as Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2_fragments.fastapi import Jinja2Blocks

from app.core.config import get_app_settings
from app.webtools._pagebuilder import DefaultSEO, DefaultView, Page, Render

logger = logging.getLogger(__name__)
settings = get_app_settings()
router = APIRouter()

templates = Jinja2Blocks(
    settings.TEMPLATE_DIR,
)

logger.info("Loading templates from %s", settings.TEMPLATE_DIR)

@router.get("/")
def homepage(request: Request):
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request
        }
    )

@router.get("/test")
def pagebuilder(request: Request):
    page = Page(request=request, template="main.html")
    seo = DefaultSEO()
    view = DefaultView()

    homepage = Render(page=page, seo=seo, view=view)

    return homepage.render()

# @router.get("/")
# def homey(request: Request):
#     return {"yes": "no"}
