import uuid
from datetime import datetime

import pendulum as pnd
from sqlalchemy import text
from sqlmodel import Field, SQLModel

from .mixins.query import QueryMixin


class BaseSQLModel(SQLModel, QueryMixin):
    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        primary_key=True,
        index=True,
        nullable=False,
        sa_column_args={"server_default": text("gen_random_uuid()"), "unique": True},
    )

    # created_at: datetime = Field(
    #     default_factory=datetime,
    #     nullable=False,
    #     sa_column_kwargs={"server_default": text("current_timestamp(0)")},
    # )
    # updated_at: datetime = Field(
    #     default_factory=datetime,
    #     nullable=False,
    #     sa_column_kwargs={
    #         "server_default": text("current_timestamp(0)"),
    #         "onupdate": text("current_timestamp(0)"),
    #     },
    # )

    @property
    def class_name(self):
        return self.__class__.__name
