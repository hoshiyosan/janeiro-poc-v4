import logging
from janeiro_log import level

from gelfformatter.formatter import GelfFormatter, GELF_LEVELS
from ..level import TRACE

GELF_LEVELS[TRACE] = 10
