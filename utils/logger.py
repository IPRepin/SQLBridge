import logging
from config import settings


def setup_logger(name='transfer_logger'):
    # Получаем уровень логирования из переменной окружения, по умолчанию INFO
    log_level_str = settings.LOG_LEVEL
    log_level = getattr(logging, log_level_str, logging.INFO)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(log_level)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
