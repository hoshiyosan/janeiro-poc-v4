import logging
from janeiro_log.buffer import bufferize_logs
from typing import List
from .config import setup_logging
from .logger import get_logger, Logger
from . import level
from dataclasses import dataclass, field

logging.setLoggerClass(Logger)

# bufferize logs until setup_logger has been called
bufferize_logs()
