from fastapi import APIRouter

from .league import router as league_router
from .user import router as user_router

routes = APIRouter()

routes.include_router(user_router, tags=["user"])
routes.include_router(league_router, tags=["league"])
