import json
import logging
from functools import lru_cache
from pathlib import Path

from pydantic import BaseModel
from rich.logging import RichHandler

from app.core.config import get_app_settings

logger = logging.getLogger(__name__)

settings = get_app_settings()

# Define the formatting and level of log messages
LOGGER_LEVEL: int = settings.LOG_LEVEL
DATE_FORMAT: str = "%d %b %Y | %H:%M:%S"
MICROSECOND_FORMAT: str = "%s.%03dZ"
SHELL_FORMAT: str = "%(asctime)s | %(message)s"
FILE_FORMAT: str = (
    "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s"
)

# Create directory if none exists
settings.LOG_DIR.mkdir(parents=True, exist_ok=True)
LOGGER_FILE: Path = Path(settings.LOG_DIR / settings.LOG_FILENAME)
LOGGER_FILE_MODE: str = settings.LOG_FILE_MODE


# Create json log handler
class JsonFormatter(logging.Formatter):
    """Formatter for JSON log messages.

    Reference:
    https://stackoverflow.com/questions/50144628/python-logging-into-file-as-a-dictionary-or-json
    """

    def __init__(
        self,
        fmt_dict: dict = None,
        time_format: str = DATE_FORMAT,
        msec_format: str = MICROSECOND_FORMAT,
    ):
        super().__init__(fmt=FILE_FORMAT, datefmt=time_format)
        self.fmt_dict = fmt_dict if fmt_dict is not None else {"message": "message"}
        self.default_time_format = time_format
        self.default_msec_format = msec_format
        self.datefmt = None

    def usesTime(self) -> bool:
        return "asctime" in self.fmt_dict.values()

    def formatMessage(self, record) -> dict:
        """Overwritten to return a dictionary of the relevant LogRecord attributes instead of a string.
        KeyError is raised if an unknown attribute is provided in the fmt_dict.
        """
        return {
            fmt_key: record.__dict__[fmt_val]
            for fmt_key, fmt_val in self.fmt_dict.items()
        }

    def format(self, record: logging.LogRecord) -> str:
        """Format the log message as JSON."""
        record.message = record.getMessage()

        if self.usesTime():
            record.asctime = self.formatTime(record, self.datefmt)

        message_dict = self.formatMessage(record)

        if record.exc_info:
            if not record.exc_text:
                record.exc_text = self.formatException(record.exc_info)

        if record.exc_text:
            message_dict["exc_info"] = record.exc_text

        if record.stack_info:
            message_dict["stack_info"] = self.formatStack(record.stack_info)

        return json.dumps(message_dict)


class LoggerConfig(BaseModel):
    """Provides the pydantic BaseModel as a place to define the various logger
    variables.

    Args:
        BaseModel: pydantic BaseModel class.
    """

    level: int
    handlers: list
    shell_format: str
    file_format: str
    date_format: str
    log_file: Path


@lru_cache()
def get_logger_config() -> LoggerConfig:
    """Configures the logger to use the RichHandler from the Rich library for
    better looking log messages and tracebacks. However, it only does so in the
    Dev and Stg tiers (and not production).

    Returns:
        LoggerConfig: Pydantic BaseModel defined above
    """
    file_handler = logging.FileHandler(LOGGER_FILE, mode=LOGGER_FILE_MODE)
    file_handler_format = JsonFormatter(
        {
            "level": "levelname",
            "message": "message",
            "loggerName": "name",
            "processName": "processName",
            "processID": "process",
            "threadName": "threadName",
            "threadID": "thread",
            "timestamp": "asctime",
            "functionName": "funcName",
        }
    )

    file_handler.setFormatter(file_handler_format)

    shell_handler = RichHandler(
        rich_tracebacks=True, tracebacks_show_locals=True, show_time=False
    )

    return LoggerConfig(
        level=LOGGER_LEVEL,
        handlers=[shell_handler, file_handler],
        shell_format=SHELL_FORMAT,
        file_format=FILE_FORMAT,
        date_format=DATE_FORMAT,
        log_file=LOGGER_FILE,
    )


def setup_rich_logger() -> None:
    """Overrides other handlers/loggers with the configuration defined
    by `get_logger_config()`.
    """
    for name in logging.root.manager.loggerDict.keys():
        logging.getLogger(name).handlers = []
        logging.getLogger(name).propagate = True

    logger_config = get_logger_config()

    logging.basicConfig(
        level=logger_config.level,
        format=logger_config.shell_format,
        datefmt=logger_config.date_format,
        handlers=logger_config.handlers,
    )
