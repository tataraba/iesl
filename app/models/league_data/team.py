import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .league import League
    # from .player import Player

__all__ = (
    "TeamBase",
    "TeamCreate",
    "TeamRead",
    "TeamUpdate",
    "Team",
)




class TeamBase(BaseSQLModel):
    name: str
    uniform_color: str
    active: bool
    pending: bool
    contact: str  # TODO: Eventually should link to User ID

    league_id: int | None = Field(default=None, foreign_key="league.id")


class Team(TeamBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)

    league: "League" = Relationship(back_populates="teams")
    player_links: list["Team"] = Relationship(back_populates="team")


class TeamCreate(TeamBase):
    name: str
    uniform_color: str | None
    active: bool = False
    pending: bool = False
    contact: str


class TeamRead(TeamBase):
    pass


class TeamUpdate(TeamBase):
    pass






