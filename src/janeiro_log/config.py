from dataclasses import dataclass
from typing import Union
import yaml
import logging
import logging.config
from janeiro_log.buffer import send_bufferized_logs

@dataclass
class LogConfig:
    default_level: int


def parse_log_level(level: Union[int, str]):
    if isinstance(level, int):
        return level
    elif isinstance(level, str):
        return logging._nameToLevel[level]
    else:
        raise TypeError("Unsupported value for log level: %s" % level)


def setup_logging_from_dict(raw_config: dict):
    if not raw_config:
        raw_config = {}
        
    if not raw_config.get("version"):
        raw_config["version"] = 1
        
    if raw_config.get("disable_existing_loggers") is None:
        raw_config["disable_existing_loggers"] = True
    
    logging.config.dictConfig(raw_config)
    send_bufferized_logs()


def setup_logging_from_file(filepath: str):
    with open(filepath, 'r') as log_config_file:
        raw_config: dict = yaml.safe_load(log_config_file)
    
    setup_logging_from_dict(raw_config)


def setup_logging():
    from janeiro_config import ConfigOption, parse_option
    
    log_config_file = parse_option(ConfigOption(key="log.config_file", type=str))
    log_level = parse_option(ConfigOption(key="log.level", type=str), default="TRACE")
    log_format = parse_option(ConfigOption(key="log.format", type=str), default="%(asctime)s ::: %(levelname)s ::: %(message)s")
    
    if log_config_file:
        setup_logging_from_file(log_config_file)
    else:
        setup_logging_from_dict({
            "formatters": {
                "default": {
                    "format": log_format
                }  
            },
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "level": log_level,
                    "formatter": "default",
                    "stream": "ext://sys.stdout"
                }
            },
            "loggers": {
                "": {
                    "level": log_level,
                    "handlers": ["default"],
                    "propagate": "no"
                }
            }
        })
