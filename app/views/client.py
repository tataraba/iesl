import logging
from typing import Annotated

import pendulum as pnd
from asgi_htmx import HtmxRequest as Request
from fastapi import APIRouter, Form
from jinja2_fragments.fastapi import Jinja2Blocks

from app.core.config import get_app_settings
from app.models.league_data import season
from app.webtools.decorator import form_it
from app.webtools.viewmodel import DefaultPageMeta, DefaultView, Page, Render

logger = logging.getLogger(__name__)
settings = get_app_settings()
router = APIRouter()

templates = Jinja2Blocks(
    settings.TEMPLATE_DIR,
)

logger.info("Loading templates from %s", settings.TEMPLATE_DIR)

season = season.SeasonCreate(
    name="testing season",
    description="test",
    start_date=pnd.now(),
    end_date=pnd.now(),
)


@router.get("/dash")
def homepage(request: Request):
    page = Page(request=request, template="admin/dashboard.html")
    meta = DefaultPageMeta()
    view = DefaultView()

    homepage = Render(page=page, meta_tags=meta, view=view)

    return homepage.render()

# @form_it(model=season)
@router.get("/add")
def add(request: Request):
    page = Page(request=request, template="admin/add.html")
    meta = DefaultPageMeta()
    view = DefaultView()

    homepage = Render(page=page, meta_tags=meta, view=view)

    return homepage.render()

@form_it(model=season)
@router.post("/add")
def add_season(request: Request):
    print(locals())
    print(request.headers.items())
    page = Page(request=request, template="admin/dashboard.html")
    meta = DefaultPageMeta()
    view = DefaultView()

    homepage = Render(page=page, meta_tags=meta, view=view)

    return homepage.render()
