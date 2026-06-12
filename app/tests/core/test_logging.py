import logging

from app.core.config import Settings
from app.core.logging import configure_logging, get_logger


def test_configure_logging_sets_root_level() -> None:
    settings = Settings(log_level="WARNING")

    configure_logging(settings)

    assert logging.getLogger().level == logging.WARNING


def test_get_logger_returns_named_logger() -> None:
    logger = get_logger("app.tests")

    assert logger.name == "app.tests"
