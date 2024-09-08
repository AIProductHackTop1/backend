import sys
import logging
from dependency_injector.wiring import Provide, inject

from src.containers.container import AppContainer


@inject
def init_logger(name: str, settings: dict = Provide[AppContainer.config]):
    settings = settings['logger_settings']

    logger = logging.getLogger(name)
    logger.setLevel(settings['log_level'])

    file_handler = logging.FileHandler(settings['log_dir'], mode='a')
    std_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')  # noqa: WPS323

    file_handler.setFormatter(formatter)
    std_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(std_handler)

    return logger
