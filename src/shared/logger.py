"""
Path: src/shared/logger.py
"""

import logging
import sys

def get_logger():
    " Obtener un logger configurado."
    logger = logging.getLogger("meta_ads")
    if not logger.hasHandlers():
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            '[%(levelname)s] %(filename)s:%(lineno)d - %(message)s',
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger
