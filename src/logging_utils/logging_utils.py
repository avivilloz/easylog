import os
import logging


def setup_logging(
    level: int = logging.DEBUG,
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    logs_dir: str = None,
    log_file_name: str = None,
):
    if logs_dir and log_file_name:
        os.makedirs(logs_dir, exist_ok=True)
        log_file_path = f"{logs_dir}/{log_file_name}"
        logging.basicConfig(
            filename=log_file_path, filemode="a", level=level, format=log_format
        )
    else:
        logging.basicConfig(level=level, format=log_format)


def get_logger(module_name: str):
    return logging.getLogger(module_name)
