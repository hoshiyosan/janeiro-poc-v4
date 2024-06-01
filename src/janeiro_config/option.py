from dataclasses import dataclass
import os
import re
from typing import Generic, Type, TypeVar
from janeiro_config.types import UNDEFINED
from janeiro_log import get_logger


T = TypeVar("T")

LOG = get_logger(__name__)


@dataclass
class ConfigOption(Generic[T]):
    key: str
    type: Type[T]


def parse_option(option: ConfigOption[T], required=False, default=UNDEFINED) -> T:
    variable = re.sub("[^A-z0-9]+", "_", option.key).upper()
    value = os.getenv(variable)
    
    if required and value is None:
        raise LookupError("Missing environment variable required by configuration: %s" % variable)
    
    if value is None and default != UNDEFINED:
        LOG.trace("Using default value for config option %s: %s", variable, value)
        value = default
    else:
        LOG.trace("Parsed config option for variable %s: %s", variable, value)
    
    return value
