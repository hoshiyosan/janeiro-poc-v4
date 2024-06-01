import logging
from typing import Mapping
from .level import TRACE

class Logger(logging.Logger):
    def trace(self, msg: object, *args: object, extra: Mapping[str, object] = None, **kwargs) -> None:
        return self.log(TRACE, msg, *args, extra=extra, **kwargs)

def get_logger(name: str = None) -> Logger:
    return logging.getLogger(name)
