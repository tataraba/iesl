import logging

from asgi_htmx import HtmxRequest as Request
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from jinja2_fragments.fastapi import Jinja2Blocks

from app.core.config import get_app_settings

logger = logging.getLogger(__name__)
settings = get_app_settings()
router = APIRouter()

templates = Jinja2Blocks(
    settings.TEMPLATE_DIR,
)

logger.info("Loading templates from %s", settings.TEMPLATE_DIR)

@router.get("/", response_class=HTMLResponse)
def homepage(request: Request):
    return templates.TemplateResponse(
        "main.html",
        {
            "request": request
        }
    )


# @router.get("/")
# def homey(request: Request):
#     return {"yes": "no"}
