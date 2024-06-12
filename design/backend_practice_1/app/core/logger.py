import logging

from backend_practice_1.app.core.settings.app import AppSettings


def init(config: AppSettings) -> None:
    logging.basicConfig(
        level=config.logging_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
