from pydantic import BaseModel
from sqlmodel import Session

from app.db.session import get_session


class QueryMixin(BaseModel):
    def save(self):
        Session.add(self)
        Session.commit()
        Session.refresh(self)
        return self

    def delete(self):
        Session.delete(self)
        Session.commit()
