from sqlmodel import Session, create_engine

from app.core.config import get_app_settings

settings = get_app_settings()

settings.DATA_DIR.mkdir(parents=True, exist_ok=True)
SQLITE_DB_URL = f"sqlite:///{settings.DATA_DIR / settings.SQLITE_DB_FILE}"
CONNECT_ARGS = {"check_same_thread": False}

engine = create_engine(
    SQLITE_DB_URL, pool_pre_ping=True, echo=False, connect_args=CONNECT_ARGS
)


def get_session():
    with Session(engine) as session:
        yield session
