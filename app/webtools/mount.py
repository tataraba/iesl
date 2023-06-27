from functools import lru_cache

from jinja2_fragments.fastapi import Jinja2Blocks
from starlette.staticfiles import StaticFiles

from app.core.config import get_app_settings

settings = get_app_settings()


@lru_cache
def init_template() -> Jinja2Blocks:
    """Initializes Jinja2 templates."""
    templates = Jinja2Blocks(
        settings.TEMPLATE_DIR,
        autoescape=True,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    return templates


@lru_cache
def incl_static(app) -> None:
    """Mount directory for static files."""
    app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")
