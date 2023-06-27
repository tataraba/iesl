import pendulum as pnd
from sqlmodel import Field

from app.models.base import BaseSQLModel


class UserLoginBase(BaseSQLModel):
    email: str
    hashed_password: str
    is_active: bool
    is_superuser: bool
    is_verified: bool


class UserLogin(UserLoginBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class UserLoginCreate(UserLoginBase):
    email: str
    hashed_password: str


class UserLoginRead(UserLoginBase):
    pass


class UserLoginUpdate(UserLoginBase):
    pass
