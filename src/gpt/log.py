import os
import logging


def setup_logging(
    logs_dir: str = "logs",
    log_file_name: str = "log.log",
    level: int = logging.DEBUG,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
):
    os.makedirs(logs_dir, exist_ok=True)
    log_file_path = f"{logs_dir}/{log_file_name}"

    logging.basicConfig(
        filename=log_file_path, filemode="a", level=level, format=log_format
    )


def get_logger(name: str):
    return logging.getLogger(name)
