import uuid
from datetime import datetime

from sqlmodel import Field, Relationship
from typing_extensions import TYPE_CHECKING

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .schedule import Schedule


class SeasonBase(BaseSQLModel):
    name: str
    description: str
    start_date: datetime
    end_date: datetime


class Season(SeasonBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)

    league_links: list["Schedule"] = Relationship(back_populates="season")


class SeasonCreate(SeasonBase):
    pass


class SeasonRead(SeasonBase):
    pass


class SeasonUpdate(SeasonBase):
    pass
