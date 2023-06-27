import uuid

from sqlmodel import Field, Relationship
from typing_extensions import TYPE_CHECKING

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .schedule import Schedule
    from .team import Team


class LeagueBase(BaseSQLModel):
    name: str
    division: str
    day_of_week: str
    open: bool
    coed: bool
    male_age_over: int | None
    female_age_over: int | None


class League(LeagueBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)

    teams: "Team" = Relationship(back_populates="league")
    season_links: list["Schedule"] = Relationship(back_populates="league")

class LeagueCreate(LeagueBase):
    pass


class LeagueRead(LeagueBase):
    pass


class LeagueUpdate(LeagueBase):
    pass
