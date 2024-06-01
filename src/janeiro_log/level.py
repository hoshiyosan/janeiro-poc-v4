"""Defines additional log levels"""
import logging

TRACE = 5
DEBUG = 10
INFO = 20
WARNING = 30
ERROR = 40
CRITICAL = 50

CUSTOM_LEVEL_NAME = {
    TRACE: "TRACE"
}

for level_value, level_name in CUSTOM_LEVEL_NAME.items():
    logging.addLevelName(level_value, level_name)
