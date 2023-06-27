import uuid
from datetime import datetime

from sqlmodel import Field, Relationship
from typing_extensions import TYPE_CHECKING

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .league import League
    from .season import Season

class ScheduleBase(BaseSQLModel):

    game_date: datetime
    game_time: datetime
    field: str
    ref_1: str | None = None
    ref_2: str | None = None

    season_id: int | None = Field(
        default=None, foreign_key="season.id", primary_key=True
    )
    league_id: int | None = Field(
        default=None, foreign_key="league.id", primary_key=True
    )
    home_team_id: int | None = Field(
        default=None, foreign_key="team.id", primary_key=True
    )
    away_team_id: int | None = Field(
        default=None, foreign_key="team.id", primary_key=True
    )


class Schedule(ScheduleBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)


    season: "Season" = Relationship(back_populates="league_links")
    league: "League" = Relationship(back_populates="season_links")


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleRead(ScheduleBase):
    pass


class ScheduleUpdate(ScheduleBase):
    game_date: datetime
    game_time: datetime
    field: str | None
    ref_1: str | None
    ref_2: str | None
