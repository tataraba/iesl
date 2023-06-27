from fastapi import APIRouter, Depends
from sqlmodel import Session

from app.db.session import get_session
from app.models.league_data.season import Season, SeasonCreate, SeasonRead

router = APIRouter()


@router.post("/season/", response_model=SeasonRead)
def create_season(*, session: Session = Depends(get_session), season: SeasonCreate):
    db_season = Season.from_orm(season)
    session.add(db_season)
    session.commit()
    session.refresh(db_season)
    return db_season

