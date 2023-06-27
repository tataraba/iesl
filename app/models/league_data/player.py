import uuid

from sqlmodel import Field, Relationship
from typing_extensions import TYPE_CHECKING

from app.models.base import BaseSQLModel

if TYPE_CHECKING:
    from .team import Team

class PlayerBase(BaseSQLModel):
    first_name: str
    last_name: str
    email: str | None
    phone: str | None
    birth_date: str | None = None
    release: bool
    user_id: int | None = None  # TODO: Link to User ID if applicable


class Player(PlayerBase, table=True):
    id: uuid.UUID | None = Field(default=None, primary_key=True)

    team_links: list["Team"] = Relationship(back_populates="player")


class PlayerCreate(PlayerBase):
    pass


class PlayerRead(PlayerBase):
    pass

