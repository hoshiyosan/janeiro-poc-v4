
import logging
from typing import List
from janeiro_config import ConfigOption, parse_option
from janeiro_log import get_logger

ALLOW_ORIGINS_OPTION = ConfigOption(
    key="cors.allow_origins",
    type=List[str]
)

LOG = get_logger(__name__)

class RestAPI:
    def setup(self):
        self.configure_cors()
    
    def configure_cors(self):
        self.allowed_origins = parse_option(ALLOW_ORIGINS_OPTION, required=False)
        if self.allowed_origins:
            LOG.info("Cors middleware enabled with allowed_origins: %s", self.allowed_origins)
        else:
            LOG.debug("Cors middleware is disabled")
