import logging


def get_logger(name="wifi_scanner") -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler("wifi_scanner.log")
    fh.setLevel(logging.DEBUG)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s - %(message)s")
    fh.setFormatter(formatter)

    logger.addHandler(fh)
    return logger
