# get_env.py
import logging


def setup_logger(name=__name__, log_file=None, level=logging.INFO):
    """Create and configure a logger"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    # Console handler
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler (optional)
    if log_file:
        fh = logging.FileHandler(log_file)
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger
