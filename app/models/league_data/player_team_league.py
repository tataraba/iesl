import uuid
from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .player import Player
    from .team import Team


class PlayerTeamLeagueLinkBase(BaseSQLModel):
    verified: bool
    paid: bool
    eligible: bool

    player_id: int | None = Field(
        default=None, foreign_key="player.id", primary_key=True
    )
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    league_id: int | None = Field(
        default=None, foreign_key="league.id", primary_key=True
    )


class PlayerTeamLeagueLink(PlayerTeamLeagueLinkBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)

    player: "Player" = Relationship(back_populates="team_links")
    team: "Team" = Relationship(back_populates="player_links")
