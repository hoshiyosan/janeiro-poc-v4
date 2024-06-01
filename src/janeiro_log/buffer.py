from dataclasses import dataclass, field
import logging
from typing import List

_BUFFER: "BufferHandler" = None

@dataclass
class BufferHandler:
    level = 0
    records: List[logging.LogRecord] = field(default_factory=list)
    
    def handle(self, record):
        self.records.append(record)


def bufferize_logs():
    global _BUFFER
    
    if _BUFFER is None:
        _BUFFER = BufferHandler()
    
    logging.basicConfig(level=0)
    root = logging.getLogger()
    root.handlers = [_BUFFER]

def send_bufferized_logs():
    # TODO: ensure buffer handler is removed...

    if _BUFFER is None:
        raise ValueError("Log buffer has not been initialized!")

    root = logging.getLogger()
    for handler in root.handlers:
        for record in _BUFFER.records:
            handler.handle(record)
