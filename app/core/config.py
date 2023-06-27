import logging
import secrets
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel, BaseSettings, Field

logger = logging.getLogger(__name__)
APP_ROOT = Path(__file__).resolve().parent.parent


class AppConfig(BaseModel):
    """Application configuration using pydantic BaseModel ('more_settings').

    Args:
        BaseModel: pydantic BaseModel class.

    Arguments:
        title: Application title.
        version: Application version.
        debug: Debug mode.
        docs_url: Documentation URL.
        redoc_url: Redoc URL.
        openapi_url: OpenAPI URL.
        author: Author.
        description: Application description.

    Note:
        Will be accessed as `app_settings` in the `settings` instance.
    """

    title: str = "IESL"
    version: str = "0.0.1"
    debug: bool = False
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"
    author: str = "Mario Munoz"
    description: str = "Inland Empire Soccer League info and stats."


class GlobalConfig(BaseSettings):
    """Provides configuration elements that can vary between dev, test, stage,
    and production tiers. This class is inherited by each of the tiers. However,
    the `settings` instance is generated from the `ENV_STATE` environment variable
    matching the respective tier.

    See References for more info.

    References:
        [Rednafi's Blog](https://rednafi.github.io/digressions/python/
        2020/06/03/python-configs.html)

    Args:
        BaseSettings: pydantic BaseSettings.
    """

    app_settings: AppConfig = AppConfig()

    ENV_STATE: str = Field(..., env="ENV_STATE")
    DISABLE_DOCS: bool = False

    APP_DIR: Path = APP_ROOT
    PROJECT_DIR: Path = APP_ROOT.parent.resolve()
    DATA_DIR: Path = PROJECT_DIR / "iesl_data"
    STATIC_DIR: Path = APP_DIR / "static"
    TEMPLATE_DIR: Path = APP_DIR / "templates"

    LOG_DIR: Path = Path(APP_ROOT.parent, "iesl_logs")
    LOG_FILENAME: str = "iesl.log"
    LOG_FILE_MODE: str = "w"  # use `a` for append, `w` for overwrite

    SQLITE_DB_FILE: str = None

    SECRET_KEY: str = secrets.token_urlsafe(32)

    @property
    def fastapi_kwargs(self) -> dict[str, str]:
        """Creates dictionary of values to pass to FastAPI app
        as **kwargs. Suppress API documentation when in production.

        Returns:
            dict: Includes properties in `AppConfig` and
            disables docs if `prd` is the `ENV_STATE`.
        """
        fastapi_kwargs = self.app_settings.dict()
        if self.DISABLE_DOCS:
            fastapi_kwargs.update(
                {
                    "docs_url": None,
                    "redoc_url": None,
                    "openapi_url": None,
                    "openapi_prefix": None,
                }
            )
        return fastapi_kwargs

    class Config:
        """Loads .env file."""

        env_file: Path = Path(APP_ROOT).parent / ".env"
        env_file_encoding: str = "utf-8"


class DevConfig(GlobalConfig):
    """Development configurations."""

    PYTHONASYNCIODEBUG = 1
    LOG_LEVEL: int = logging.DEBUG

    class Config:
        env_prefix: str = "DEV_"


class TestConfig(GlobalConfig):
    """Test configurations, using test database."""

    LOG_LEVEL: int = logging.INFO

    class Config:
        env_prefix: str = "TEST_"


class StgConfig(GlobalConfig):
    """Staging configurations."""

    LOG_LEVEL: int = logging.INFO

    class Config:
        env_prefix: str = "STG_"


class PrdConfig(GlobalConfig):
    """Production configurations."""

    LOG_LEVEL: int = logging.WARNING

    class Config:
        env_prefix: str = "PRD_"


class FactoryConfig:
    """Inherits configuration from GlobalConfig. Depending on `ENV_STATE`,
    it will inherit from DevConfig, TestConfig, StgConfig, or PrdConfig.
    For example, the .env values with "DEV_" prefix are loaded when the
    `ENV_STATE` is "dev", and the same for respective `env_prefix` values.
    """

    def __init__(self, env_state: str | None) -> None:
        self.env_state = env_state

    def __call__(self) -> GlobalConfig:
        if self.env_state == "dev" or not self.env_state:
            if not self.env_state:
                logger.warning(
                    "Environment variable not found defining the app state. "
                    "Will default to 'Dev' environment."
                )
            return DevConfig()

        elif self.env_state == "test":
            return TestConfig()

        elif self.env_state == "stg":
            return StgConfig()

        elif self.env_state == "prd":
            return PrdConfig()


settings = FactoryConfig(GlobalConfig().ENV_STATE)()


@lru_cache()
def get_app_settings() -> DevConfig | StgConfig | PrdConfig:
    """Returns a cached instance of the settings (config) object.

    To change env variable and reset cache during testing, use the 'lru_cache'
    instance method 'get_app_settings.cache_clear()'."""

    return settings
